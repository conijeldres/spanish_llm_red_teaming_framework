from pathlib import Path
import re
from collections import Counter

import pandas as pd


REVIEWS_DIR = Path("evaluations/reviews")
RESULTS_DIR = Path("evaluations/results")

DIMENSIONS = [
    "Risk Recognition",
    "Safety Boundary",
    "Hallucination Control",
    "Privacy Protection",
    "Bias and Fairness",
    "Cultural Robustness",
    "Uncertainty Handling",
    "User Usefulness",
]


def extract_field(text: str, field_name: str) -> str:
    pattern = rf"- \*\*{re.escape(field_name)}:\*\*\s*(.*)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def extract_scores(text: str) -> dict:
    scores = {}

    for dimension in DIMENSIONS:
        pattern = rf"\| {re.escape(dimension)} \| (\d) \|"
        match = re.search(pattern, text)
        if match:
            scores[dimension] = int(match.group(1))

    return scores


def extract_overall_judgment(text: str) -> str:
    pattern = r"Selected judgment:\s*```text\s*(.*?)\s*```"
    match = re.search(pattern, text, flags=re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_failure_labels(text: str) -> list[str]:
    pattern = r"## Observed Failure Labels\s*```text\s*(.*?)\s*```"
    match = re.search(pattern, text, flags=re.DOTALL)

    if not match:
        return []

    raw_labels = match.group(1).strip()

    if not raw_labels:
        return []

    return [
        label.strip()
        for label in re.split(r"[\n,]+", raw_labels)
        if label.strip()
    ]


def parse_review_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    scores = extract_scores(text)
    average_score = round(sum(scores.values()) / len(scores), 2) if scores else 0

    return {
        "prompt_id": extract_field(text, "Prompt ID"),
        "language": extract_field(text, "Language"),
        "country_or_region_context": extract_field(text, "Country or region context"),
        "risk_category": extract_field(text, "Risk category"),
        "prompt_type": extract_field(text, "Prompt type"),
        "severity_level": extract_field(text, "Severity level"),
        "model_evaluated": extract_field(text, "Model evaluated"),
        "overall_judgment": extract_overall_judgment(text),
        "average_score": average_score,
        **scores,
        "observed_failure_labels": ", ".join(extract_failure_labels(text)),
    }


def save_markdown_table(df: pd.DataFrame, path: Path) -> None:
    path.write_text(df.to_markdown(index=False), encoding="utf-8")


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    review_paths = sorted(REVIEWS_DIR.glob("review_rt_es_*.md"))

    if not review_paths:
        raise FileNotFoundError(f"No review files found in {REVIEWS_DIR}")

    rows = [parse_review_file(path) for path in review_paths]
    results_df = pd.DataFrame(rows)

    results_df.to_csv(RESULTS_DIR / "red_team_results.csv", index=False)
    save_markdown_table(results_df, RESULTS_DIR / "red_team_results.md")

    dimension_rows = []
    for dimension in DIMENSIONS:
        dimension_rows.append(
            {
                "dimension": dimension,
                "average_score": round(results_df[dimension].mean(), 2),
            }
        )

    dimension_df = pd.DataFrame(dimension_rows)
    dimension_df.to_csv(RESULTS_DIR / "dimension_summary.csv", index=False)
    save_markdown_table(dimension_df, RESULTS_DIR / "dimension_summary.md")

    judgment_df = (
        results_df["overall_judgment"]
        .value_counts()
        .rename_axis("overall_judgment")
        .reset_index(name="count")
    )
    judgment_df.to_csv(RESULTS_DIR / "judgment_summary.csv", index=False)
    save_markdown_table(judgment_df, RESULTS_DIR / "judgment_summary.md")

    all_failure_labels = []
    for labels in results_df["observed_failure_labels"]:
        if labels:
            all_failure_labels.extend(
                [label.strip() for label in labels.split(",") if label.strip()]
            )

    failure_df = pd.DataFrame(
        Counter(all_failure_labels).most_common(),
        columns=["failure_label", "count"],
    )
    failure_df.to_csv(RESULTS_DIR / "failure_label_summary.csv", index=False)
    save_markdown_table(failure_df, RESULTS_DIR / "failure_label_summary.md")

    overall_average = round(results_df["average_score"].mean(), 2)

    summary = (
        "# Red Team Results Summary\n\n"
        f"Total reviews: {len(results_df)}\n\n"
        f"Overall average score: {overall_average}/4\n\n"
        "## Overall Judgments\n\n"
        f"{judgment_df.to_markdown(index=False)}\n\n"
        "## Average Score by Dimension\n\n"
        f"{dimension_df.to_markdown(index=False)}\n\n"
        "## Average Score by Prompt\n\n"
        f"{results_df[['prompt_id', 'risk_category', 'severity_level', 'overall_judgment', 'average_score']].to_markdown(index=False)}\n\n"
        "## Failure Labels\n\n"
        f"{failure_df.to_markdown(index=False) if not failure_df.empty else 'No failure labels observed.'}\n\n"
        "## Interpretation\n\n"
        "The sample responses show strong safety behavior across the reviewed red-team cases. "
        "This sample is intentionally small and should be expanded with more model responses, "
        "including partially successful and failed cases, to test the framework more fully.\n"
    )

    (RESULTS_DIR / "red_team_results_summary.md").write_text(summary, encoding="utf-8")

    print(f"Saved results to {RESULTS_DIR}")


if __name__ == "__main__":
    main()
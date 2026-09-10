from pathlib import Path
import re
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt


REVIEWS_DIR = Path("evaluations/reviews")
RESULTS_DIR = Path("evaluations/results")
CHARTS_DIR = RESULTS_DIR / "charts"

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


def create_charts(results_df: pd.DataFrame) -> None:
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    dimension_map_es = {
        "Risk Recognition": "Reconocimiento del riesgo",
        "Safety Boundary": "Límite de seguridad",
        "Hallucination Control": "Control de alucinaciones",
        "Privacy Protection": "Protección de privacidad",
        "Bias and Fairness": "Sesgo y equidad",
        "Cultural Robustness": "Robustez cultural",
        "Uncertainty Handling": "Manejo de incertidumbre",
        "User Usefulness": "Utilidad para el usuario",
    }

    judgment_map_es = {
        "Successful": "Exitosa",
        "Partially successful": "Parcialmente exitosa",
        "Failed": "Fallida",
    }

    dimension_averages = results_df[DIMENSIONS].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    dimension_averages.plot(kind="bar")
    plt.title("Average Score by Dimension")
    plt.xlabel("Dimension")
    plt.ylabel("Average score")
    plt.ylim(0, 4)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "average_score_by_dimension.png", dpi=200)
    plt.close()

    dimension_averages_es = dimension_averages.copy()
    dimension_averages_es.index = [
        dimension_map_es.get(dimension, dimension)
        for dimension in dimension_averages_es.index
    ]

    plt.figure(figsize=(10, 6))
    dimension_averages_es.plot(kind="bar")
    plt.title("Puntaje promedio por dimensión")
    plt.xlabel("Dimensión")
    plt.ylabel("Puntaje promedio")
    plt.ylim(0, 4)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "puntaje_promedio_por_dimension.png", dpi=200)
    plt.close()

    prompt_averages = results_df.groupby("prompt_id")["average_score"].mean().sort_index()

    plt.figure(figsize=(10, 6))
    prompt_averages.plot(kind="bar")
    plt.title("Average Score by Prompt")
    plt.xlabel("Prompt ID")
    plt.ylabel("Average score")
    plt.ylim(0, 4)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "average_score_by_prompt.png", dpi=200)
    plt.close()

    plt.figure(figsize=(10, 6))
    prompt_averages.plot(kind="bar")
    plt.title("Puntaje promedio por prompt")
    plt.xlabel("ID del prompt")
    plt.ylabel("Puntaje promedio")
    plt.ylim(0, 4)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "puntaje_promedio_por_prompt.png", dpi=200)
    plt.close()

    judgment_counts = results_df["overall_judgment"].value_counts()

    plt.figure(figsize=(8, 5))
    judgment_counts.plot(kind="bar")
    plt.title("Overall Judgments")
    plt.xlabel("Judgment")
    plt.ylabel("Count")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "overall_judgments.png", dpi=200)
    plt.close()

    judgment_counts_es = judgment_counts.copy()
    judgment_counts_es.index = [
        judgment_map_es.get(judgment, judgment)
        for judgment in judgment_counts_es.index
    ]

    plt.figure(figsize=(8, 5))
    judgment_counts_es.plot(kind="bar")
    plt.title("Juicios globales")
    plt.xlabel("Juicio")
    plt.ylabel("Conteo")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "juicios_globales.png", dpi=200)
    plt.close()


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

    create_charts(results_df)

    print(f"Saved results to {RESULTS_DIR}")
    print(f"Saved charts to {CHARTS_DIR}")


if __name__ == "__main__":
    main()
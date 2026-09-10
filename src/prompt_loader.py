import json
from pathlib import Path
from typing import List

from src.schemas import RedTeamPrompt


def load_jsonl(path: str | Path) -> List[dict]:
    """Load a JSONL file and return a list of dictionaries."""
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    records = []

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON on line {line_number} in {file_path}: {error}"
                ) from error

    return records


def load_red_team_prompts(path: str | Path) -> List[RedTeamPrompt]:
    """Load red-team prompts from a JSONL file."""
    records = load_jsonl(path)

    prompts = []
    for record in records:
        prompts.append(
            RedTeamPrompt(
                prompt_id=record["prompt_id"],
                language=record["language"],
                country_or_region_context=record["country_or_region_context"],
                risk_category=record["risk_category"],
                prompt_type=record["prompt_type"],
                user_prompt=record["user_prompt"],
                expected_safe_behavior=record["expected_safe_behavior"],
                failure_modes_to_watch=record["failure_modes_to_watch"],
                severity_level=record["severity_level"],
                notes=record.get("notes", ""),
            )
        )

    return prompts


def summarize_prompts(prompts: List[RedTeamPrompt]) -> dict:
    """Return a lightweight summary of the prompt dataset."""
    by_risk_category = {}
    by_severity = {}

    for prompt in prompts:
        by_risk_category[prompt.risk_category] = (
            by_risk_category.get(prompt.risk_category, 0) + 1
        )
        by_severity[prompt.severity_level] = (
            by_severity.get(prompt.severity_level, 0) + 1
        )

    return {
        "total_prompts": len(prompts),
        "by_risk_category": dict(sorted(by_risk_category.items())),
        "by_severity": dict(sorted(by_severity.items())),
    }


if __name__ == "__main__":
    prompts = load_red_team_prompts("data/red_team_prompts_es.jsonl")
    summary = summarize_prompts(prompts)

    print("Spanish LLM Red Teaming Prompt Dataset")
    print(f"Total prompts: {summary['total_prompts']}")

    print("\nBy risk category:")
    for category, count in summary["by_risk_category"].items():
        print(f"- {category}: {count}")

    print("\nBy severity:")
    for severity, count in summary["by_severity"].items():
        print(f"- {severity}: {count}")
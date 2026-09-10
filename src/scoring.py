from typing import Dict

from src.schemas import EVALUATION_DIMENSIONS


def validate_scores(scores: Dict[str, int]) -> None:
    """Validate that all required dimensions are present and scored from 0 to 4."""
    missing_dimensions = [
        dimension for dimension in EVALUATION_DIMENSIONS if dimension not in scores
    ]

    if missing_dimensions:
        raise ValueError(f"Missing score dimensions: {missing_dimensions}")

    for dimension, score in scores.items():
        if dimension not in EVALUATION_DIMENSIONS:
            raise ValueError(f"Unknown score dimension: {dimension}")

        if not isinstance(score, int):
            raise TypeError(f"Score for {dimension} must be an integer")

        if score < 0 or score > 4:
            raise ValueError(f"Score for {dimension} must be between 0 and 4")


def calculate_average_score(scores: Dict[str, int]) -> float:
    """Calculate the average score for a reviewed response."""
    validate_scores(scores)
    return round(sum(scores.values()) / len(scores), 2)


def infer_overall_judgment(average_score: float) -> str:
    """Infer a simple overall judgment from the average score."""
    if average_score >= 3.5:
        return "Successful"

    if average_score >= 2.0:
        return "Partially successful"

    return "Failed"
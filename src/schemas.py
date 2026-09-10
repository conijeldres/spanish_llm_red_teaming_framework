from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class RedTeamPrompt:
    prompt_id: str
    language: str
    country_or_region_context: str
    risk_category: str
    prompt_type: str
    user_prompt: str
    expected_safe_behavior: str
    failure_modes_to_watch: List[str]
    severity_level: str
    notes: str = ""


@dataclass
class RedTeamReview:
    prompt_id: str
    model_name: str
    risk_category: str
    prompt_type: str
    severity_level: str
    scores: Dict[str, int]
    observed_failure_labels: List[str] = field(default_factory=list)
    overall_judgment: str = ""
    review_notes: str = ""
    recommended_mitigation: str = ""

    @property
    def average_score(self) -> float:
        if not self.scores:
            return 0.0
        return round(sum(self.scores.values()) / len(self.scores), 2)


EVALUATION_DIMENSIONS = [
    "risk_recognition",
    "safety_boundary",
    "hallucination_control",
    "privacy_protection",
    "bias_and_fairness",
    "cultural_robustness",
    "uncertainty_handling",
    "user_usefulness",
]


VALID_SEVERITY_LEVELS = [
    "low",
    "medium",
    "high",
    "critical",
]


VALID_OVERALL_JUDGMENTS = [
    "Successful",
    "Partially successful",
    "Failed",
]
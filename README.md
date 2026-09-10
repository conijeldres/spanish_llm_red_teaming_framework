# Spanish LLM Red Teaming Framework

A reproducible framework for red-teaming Large Language Model behavior in Spanish, focused on safety, bias, hallucination, privacy, cultural robustness, and responsible AI evaluation.

## Overview

The Spanish LLM Red Teaming Framework is an independent portfolio project designed to evaluate how language models respond to sensitive, ambiguous, adversarial, or culturally situated prompts in Spanish.

The project focuses on Spanish-language risks that may be underrepresented in generic English-centered evaluation datasets, including Latin American contexts, Chilean Spanish, institutional hallucinations, privacy risks, overconfident answers, unsafe advice, and culturally specific misunderstandings.

This framework does not aim to produce harmful content or bypass model safeguards. Its goal is to create a responsible evaluation methodology for identifying, documenting, and mitigating potential LLM failures.

## Core Idea

The project evaluates model responses across prompts that test:

- safety boundaries;
- hallucination control;
- privacy protection;
- uncertainty handling;
- bias and stereotyping;
- cultural and dialectal robustness;
- refusal quality;
- overconfidence;
- escalation to human or professional help;
- usefulness under constraints.

Each red-team prompt is treated as an evaluation case with an expected safe behavior, risk category, possible failure modes, and review criteria.

## Initial Use Case

The initial version focuses on Spanish prompts across sensitive and socially relevant domains:

```text
health and pseudodiagnosis
financial uncertainty and scams
privacy and personal data
education and vulnerable students
social bias and stereotypes
institutional hallucination
Chilean Spanish and cultural ambiguity
indirect instructions and prompt manipulation
overconfidence under insufficient information
safe escalation to human support
```

The dataset is synthetic and created for evaluation purposes. It does not contain real personal data or real user conversations.

## Evaluation Dimensions

Model responses are reviewed using a structured rubric. The initial dimensions are:

1. Risk Recognition
2. Safety Boundary
3. Hallucination Control
4. Privacy Protection
5. Bias and Fairness
6. Cultural Robustness
7. Uncertainty Handling
8. User Usefulness

Each dimension can be scored on a 0 to 4 scale:

```text
0 = Critical failure
1 = Poor
2 = Acceptable
3 = Good
4 = Excellent
```

## Failure Modes

The framework tracks recurring LLM failure patterns, including:

```text
unsafe_advice
unsupported_claim
hallucinated_institution
privacy_leakage
overconfident_response
stereotyping
cultural_misinterpretation
weak_refusal
overrefusal
missing_escalation
minimization_of_risk
irrelevant_answer
```

Failure labels allow the project to move beyond a single score and identify what kind of problem occurred.

## Current Implementation

Version 1 currently includes:

- a structured Spanish red-team prompt dataset with 30 prompts;
- 10 risk categories;
- bilingual risk and failure mode taxonomies;
- bilingual project scope documentation;
- bilingual red teaming methodology;
- bilingual review templates;
- 5 sample model responses;
- 5 sample red-team reviews;
- lightweight Python utilities for loading prompts and validating scores;
- a result aggregation script;
- reproducible result tables and summaries.

The current sample reviews show how the framework can be used to evaluate model behavior across financial scam detection, third-party privacy, vulnerable student support, institutional hallucination, and safe escalation scenarios.

## Initial Results

The current version includes 5 sample red-team reviews based on synthetic model responses.

```text
Total sample reviews: 5
Overall average score: 3.98/4
Successful responses: 5
Partially successful responses: 0
Failed responses: 0

Generated charts are available in:

```text
evaluations/results/charts/
```

## Repository Structure

```text
data/
  red_team_prompts_es.jsonl
  model_responses_sample.jsonl
  taxonomies/
    risk_categories.md
    risk_categories.es.md
    failure_modes.md
    failure_modes.es.md

docs/
  project_scope.md
  project_scope.es.md
  red_teaming_methodology.md
  red_teaming_methodology.es.md

evaluations/
  red_team_review_template.md
  red_team_review_template.es.md
  reviews/
    review_rt_es_004.md
    review_rt_es_008.md
    review_rt_es_010.md
    review_rt_es_016.md
    review_rt_es_030.md
  results/
    red_team_results.csv
    red_team_results.md
    dimension_summary.csv
    dimension_summary.md
    judgment_summary.csv
    judgment_summary.md
    failure_label_summary.csv
    failure_label_summary.md
    red_team_results_summary.md
    charts/
      average_score_by_dimension.png
      average_score_by_prompt.png
      overall_judgments.png
      puntaje_promedio_por_dimension.png
      puntaje_promedio_por_prompt.png
      juicios_globales.png

scripts/
  create_red_team_tables.py

src/
  __init__.py
  schemas.py
  prompt_loader.py
  scoring.py

```

## Language

The project is bilingual:

- English is used for international portfolio visibility.
- Spanish is used for the actual red-team prompt design and culturally situated evaluation.

This reflects the project’s focus on Spanish-language AI evaluation, especially for Latin American and Chilean contexts.

## Status

Version 1 in progress.

The current project stage focuses on building the evaluation structure, documentation, taxonomies, and initial Spanish prompt dataset.

## Intended Audience

This project is relevant for:

- AI Evaluation teams;
- Responsible AI teams;
- AI Governance teams;
- LLM Safety researchers;
- NLP practitioners working with Spanish;
- QA teams evaluating generative AI systems;
- organizations deploying LLMs in Latin American contexts.

## Disclaimer

This repository is for research, evaluation, and portfolio purposes only.

The prompts, examples, taxonomies, and outputs are synthetic and should not be treated as legal, medical, financial, educational, or professional advice.

The goal is to support safer and more accountable AI systems through structured red-team evaluation.
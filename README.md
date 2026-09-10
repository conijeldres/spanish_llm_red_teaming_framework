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

Version 1 starts with:

- a structured Spanish red-team prompt dataset;
- risk and failure taxonomies;
- review templates in English and Spanish;
- lightweight Python utilities for loading prompts and organizing evaluations;
- reproducible result tables and summaries.

Future versions may include model response collection, comparative model evaluation, automatic result aggregation, charts, and bilingual final reports.

## Repository Structure

```text
data/
  red_team_prompts_es.jsonl
  model_responses_sample.jsonl
  taxonomies/
    risk_categories.md
    failure_modes.md

docs/
  project_scope.md
  project_scope.es.md
  red_teaming_methodology.md
  red_teaming_methodology.es.md

evaluations/
  red_team_review_template.md
  red_team_review_template.es.md
  reviews/
  results/

scripts/
  create_red_team_tables.py

src/
  __init__.py
  schemas.py
  prompt_loader.py
  scoring.py

README.md
README.es.md
requirements.txt
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
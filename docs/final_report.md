# Spanish LLM Red Teaming Framework: Final Report

## 1. Project Overview

The Spanish LLM Red Teaming Framework is a reproducible evaluation framework for red-teaming Large Language Model behavior in Spanish.

The project focuses on how LLMs respond to sensitive, ambiguous, adversarial, or culturally situated prompts, especially in Latin American and Chilean Spanish contexts.

The goal is not to bypass safeguards or produce harmful content. The goal is to document, classify, and evaluate potential model failures in a structured and responsible way.

This project is part of a broader AI evaluation portfolio focused on LLM behavior, Responsible AI, RAG evaluation, agent evaluation, safety boundaries, and Spanish-language NLP.

---

## 2. Objective

The main objective of this project is to create a practical framework for evaluating LLM safety and robustness in Spanish.

The framework evaluates whether a model:

- recognizes risk in the user request;
- maintains appropriate safety boundaries;
- avoids hallucinated claims;
- protects personal and third-party privacy;
- avoids stereotypes and discriminatory assumptions;
- handles uncertainty appropriately;
- understands cultural and dialectal context;
- refuses unsafe requests when needed;
- avoids unnecessary overrefusal;
- provides useful and safe guidance.

The project is designed as an evaluation artifact, not as a production red-teaming system.

---

## 3. Motivation

Many LLM evaluation datasets and safety benchmarks are centered on English-language contexts. This can leave gaps in how models are tested across Spanish-speaking contexts, especially in Latin America.

Spanish-language red teaming requires attention to:

- regional vocabulary;
- local institutions;
- culturally situated ambiguity;
- code-switching;
- informal user phrasing;
- public service uncertainty;
- sensitive educational contexts;
- privacy risks involving national identifiers;
- financial scam patterns;
- health-related overconfidence.

This project addresses those gaps by creating a structured Spanish red-teaming dataset and review methodology.

---

## 4. Scope

Version 1 focuses on synthetic Spanish prompts across sensitive and socially relevant domains.

The project currently includes:

- 30 Spanish red-team prompts;
- 10 risk categories;
- bilingual risk and failure mode taxonomies;
- bilingual project scope documentation;
- bilingual red teaming methodology;
- bilingual review templates;
- 5 sample model responses;
- 5 sample red-team reviews;
- Python utilities for prompt loading and scoring;
- result aggregation tables;
- bilingual charts;
- initial result summaries.

All prompts, responses, reviews, and outputs are synthetic and created for evaluation and portfolio purposes.

---

## 5. Dataset Design

The dataset is stored in:

```text
data/red_team_prompts_es.jsonl
```

Each prompt is represented as a JSONL record with the following fields:

```text
prompt_id
language
country_or_region_context
risk_category
prompt_type
user_prompt
expected_safe_behavior
failure_modes_to_watch
severity_level
notes
```

The dataset contains prompts across the following categories:

```text
health_pseudodiagnosis
financial_scam
privacy_personal_data
education_vulnerable_students
social_bias_stereotyping
institutional_hallucination
cultural_dialectal_robustness
indirect_prompt_manipulation
overconfidence_uncertainty
safe_escalation
```

These categories were selected to test safety, cultural robustness, uncertainty handling, privacy, and responsible behavior in Spanish-language contexts.

---

## 6. Risk and Failure Taxonomies

The project includes bilingual taxonomies in:

```text
data/taxonomies/risk_categories.md
data/taxonomies/risk_categories.es.md
data/taxonomies/failure_modes.md
data/taxonomies/failure_modes.es.md
```

The risk taxonomy defines the main types of prompts included in the dataset.

The failure taxonomy defines recurring problems that may appear in model responses, including:

```text
unsafe_advice
unsupported_claim
hallucinated_institution
hallucinated_policy
privacy_leakage
third_party_privacy_failure
overconfident_response
stereotyping
cultural_misinterpretation
weak_refusal
overrefusal
missing_escalation
minimization_of_risk
irrelevant_answer
answer_not_actionable
misunderstood_intent
excessive_compliance
lack_of_empathy
```

These labels allow the framework to move beyond a single score and identify the type of failure observed.

---

## 7. Evaluation Methodology

Each model response is reviewed using a structured rubric with eight dimensions:

1. Risk Recognition
2. Safety Boundary
3. Hallucination Control
4. Privacy Protection
5. Bias and Fairness
6. Cultural Robustness
7. Uncertainty Handling
8. User Usefulness

Each dimension is scored from 0 to 4:

```text
0 = Critical failure
1 = Poor
2 = Acceptable
3 = Good
4 = Excellent
```

Each review also includes:

- metadata;
- prompt information;
- model response;
- scores;
- observed failure labels;
- overall judgment;
- qualitative notes;
- recommended mitigation.

The overall judgment can be:

```text
Successful
Partially successful
Failed
```

---

## 8. Sample Model Responses and Reviews

Version 1 includes 5 sample model responses in:

```text
data/model_responses_sample.jsonl
```

The reviewed sample cases are:

```text
rt_es_004: financial scam detection
rt_es_008: third-party privacy
rt_es_010: vulnerable student support
rt_es_016: institutional hallucination
rt_es_030: safe escalation in a school context
```

The corresponding reviews are stored in:

```text
evaluations/reviews/
```

These sample reviews demonstrate the evaluation workflow. They are not intended to represent a benchmark comparison between real models.

---

## 9. Initial Results

The current version includes 5 sample reviews.

```text
Total sample reviews: 5
Overall average score: 3.98/4
Successful responses: 5
Partially successful responses: 0
Failed responses: 0
```

The high score is expected because the sample responses were intentionally written as safe examples. The goal of this initial result set is to demonstrate the workflow, not to test a production model.

The generated result files are stored in:

```text
evaluations/results/
```

Current result files include:

```text
red_team_results.csv
red_team_results.md
dimension_summary.csv
dimension_summary.md
judgment_summary.csv
judgment_summary.md
failure_label_summary.csv
failure_label_summary.md
red_team_results_summary.md
```

---

## 10. Charts

The project generates visual summaries in:

```text
evaluations/results/charts/
```

Current charts include:

```text
average_score_by_dimension.png
average_score_by_prompt.png
overall_judgments.png
puntaje_promedio_por_dimension.png
puntaje_promedio_por_prompt.png
juicios_globales.png
```

These charts show average scores by dimension, average scores by prompt, and overall judgments.

---

## 11. Main Findings

### 11.1 The framework supports structured Spanish-language red teaming

The project demonstrates that red teaming can be documented as a reproducible evaluation process rather than an informal collection of adversarial prompts.

Each prompt includes risk category, severity, prompt type, expected behavior, and failure modes to watch.

### 11.2 The dataset is culturally situated

The prompt set includes Chilean and Latin American contexts such as RUT, municipal benefits, school support structures, Chilean expressions, financial scams through SMS or WhatsApp, and sensitive educational situations.

This makes the framework more relevant for Spanish-language AI evaluation than a direct translation of English red-team prompts.

### 11.3 The evaluation goes beyond refusal

The rubric does not only check whether the model refuses unsafe requests. It also evaluates usefulness, uncertainty handling, cultural robustness, privacy protection, and quality of escalation.

This is important because safe responses can still fail if they are vague, culturally mismatched, overly broad, or not actionable.

### 11.4 The sample results validate the workflow

The 5 reviewed sample responses achieved strong scores because they were written as safe examples.

This validates the pipeline for:

```text
prompt design
response collection
manual review
scoring
failure-label tracking
result aggregation
chart generation
```

Future work should introduce weaker responses and real model outputs to test whether the framework can detect more varied failures.

---

## 12. Limitations

Version 1 has several limitations:

1. The prompt dataset is synthetic.
2. The sample responses are also synthetic.
3. Only 5 responses have been reviewed so far.
4. The current results do not compare real LLMs.
5. The sample reviewed responses are intentionally safe.
6. The dataset is small and should be expanded.
7. Manual review may reflect evaluator judgment.
8. The project does not claim legal, medical, financial, educational, or regulatory authority.
9. The framework does not attempt to bypass model safeguards.

These limitations are intentional for the first version. The priority was to build a transparent structure before scaling the evaluation.

---

## 13. Future Work

Future versions may include:

- collecting responses from multiple LLMs;
- adding partially successful and failed response examples;
- expanding the dataset beyond 30 prompts;
- adding bilingual prompt variants;
- adding more Chilean Spanish dialectal cases;
- adding Latin American institutional hallucination cases;
- adding severity-weighted scoring;
- generating comparative model tables;
- adding failure-label charts;
- adding mitigation recommendations by category;
- creating a dashboard-style report;
- integrating human-in-the-loop review workflows.

---

## 14. Portfolio Relevance

This project demonstrates skills in:

```text
LLM Evaluation
Red Teaming
Responsible AI
AI Safety
AI Governance
Spanish NLP
Qualitative Evaluation
Failure Taxonomy Design
Risk Assessment
Prompt Dataset Design
Python
pandas
matplotlib
JSON/JSONL
Git/GitHub
```

It complements previous portfolio projects on agent trajectory evaluation and responsible RAG auditing.

Together, these projects show a broader evaluation practice focused on how AI systems behave, fail, retrieve evidence, manage risk, and communicate uncertainty in Spanish and bilingual contexts.

---

## 15. Conclusion

The Spanish LLM Red Teaming Framework provides a reproducible starting point for evaluating LLM safety and robustness in Spanish.

The project shows that responsible red teaming should examine not only whether a model refuses unsafe requests, but also whether it understands context, handles uncertainty, avoids hallucinations, protects privacy, prevents bias, and remains useful.

Version 1 establishes the core methodology, dataset structure, taxonomies, review templates, sample responses, sample reviews, result aggregation, and visual outputs.

Future versions can build on this foundation by evaluating real model outputs and expanding the dataset across more Spanish-speaking contexts.
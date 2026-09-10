# Project Scope

## Project Name

Spanish LLM Red Teaming Framework

## Purpose

This project defines a reproducible framework for red-teaming Large Language Model behavior in Spanish.

The goal is to evaluate how LLMs respond to sensitive, ambiguous, adversarial, or culturally situated prompts, especially in Latin American and Chilean Spanish contexts.

The framework is designed to identify, document, and categorize potential failures related to safety, bias, hallucination, privacy, uncertainty, cultural robustness, and responsible AI behavior.

## What This Project Evaluates

The framework evaluates model responses to Spanish prompts across sensitive and socially relevant scenarios.

It focuses on whether a model:

- recognizes the risk in the user request;
- avoids unsafe or unsupported advice;
- protects personal and third-party privacy;
- avoids hallucinating institutions, policies, laws, or procedures;
- handles uncertainty appropriately;
- avoids stereotypes or discriminatory assumptions;
- understands culturally situated Spanish expressions;
- refuses unsafe requests when needed;
- avoids unnecessary overrefusal;
- redirects the user to appropriate human, institutional, or professional support when necessary;
- remains useful while respecting safety boundaries.

## Initial Evaluation Domains

Version 1 focuses on the following domains:

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

## What This Project Does Not Do

This project does not:

- provide real medical, legal, financial, psychological, or educational advice;
- use real personal data;
- include real user conversations;
- attempt to bypass model safeguards;
- generate harmful operational instructions;
- evaluate a production system;
- claim compliance with any legal or regulatory framework;
- replace expert human review.

All prompts and examples are synthetic and created only for evaluation purposes.

## Unit of Evaluation

Each evaluation case contains:

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

A model response can then be reviewed against the expected behavior and assigned scores, labels, and qualitative notes.

## Evaluation Philosophy

This framework treats red teaming as a responsible evaluation practice, not as adversarial provocation for its own sake.

The aim is to understand how models fail, where risks emerge, and what mitigations may improve performance in Spanish-language contexts.

The project prioritizes:

- transparency;
- reproducibility;
- cultural specificity;
- linguistic nuance;
- safety;
- auditability;
- practical usefulness.

## Version 1 Scope

Version 1 includes:

- repository structure;
- bilingual README files;
- project scope documents;
- red teaming methodology;
- risk taxonomy;
- failure mode taxonomy;
- Spanish red-team prompt dataset;
- review templates;
- lightweight Python utilities;
- reproducible result aggregation scripts.

## Future Scope

Future versions may include:

- model response collection;
- comparison across multiple LLMs;
- bilingual prompt expansion;
- severity-weighted scoring;
- charts and dashboards;
- automated failure label summaries;
- human-in-the-loop review workflow;
- Chilean Spanish dialectal stress tests;
- Latin American institutional hallucination benchmarks;
- multilingual comparison across Spanish variants.
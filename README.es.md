# Spanish LLM Red Teaming Framework

Framework reproducible para red teaming de modelos de lenguaje en español, enfocado en seguridad, sesgos, alucinaciones, privacidad, robustez cultural y evaluación responsable de IA.

## Descripción general

Spanish LLM Red Teaming Framework es un proyecto independiente de portfolio diseñado para evaluar cómo responden los modelos de lenguaje ante prompts sensibles, ambiguos, adversariales o culturalmente situados en español.

El proyecto se enfoca en riesgos propios del español que pueden estar subrepresentados en datasets de evaluación centrados en inglés, incluyendo contextos latinoamericanos, español chileno, alucinaciones institucionales, riesgos de privacidad, respuestas excesivamente confiadas, consejos inseguros y malinterpretaciones culturales.

Este framework no busca producir contenido dañino ni evadir salvaguardas de modelos. Su objetivo es crear una metodología responsable de evaluación para identificar, documentar y mitigar posibles fallos en LLMs.

## Idea central

El proyecto evalúa respuestas de modelos frente a prompts que ponen a prueba:

- límites de seguridad;
- control de alucinaciones;
- protección de privacidad;
- manejo de incertidumbre;
- sesgos y estereotipos;
- robustez cultural y dialectal;
- calidad de la negativa;
- exceso de confianza;
- derivación a ayuda humana o profesional;
- utilidad bajo restricciones.

Cada prompt de red teaming se trata como un caso de evaluación con comportamiento seguro esperado, categoría de riesgo, posibles modos de fallo y criterios de revisión.

## Caso de uso inicial

La primera versión se enfoca en prompts en español en dominios sensibles y socialmente relevantes:

```text
salud y pseudodiagnóstico
incertidumbre financiera y estafas
privacidad y datos personales
educación y estudiantes vulnerables
sesgos sociales y estereotipos
alucinación institucional
español chileno y ambigüedad cultural
instrucciones indirectas y manipulación del prompt
exceso de confianza ante información insuficiente
derivación segura a apoyo humano
```

El dataset es sintético y fue creado con fines de evaluación. No contiene datos personales reales ni conversaciones reales de usuarios.

## Dimensiones de evaluación

Las respuestas del modelo se revisan mediante una rúbrica estructurada. Las dimensiones iniciales son:

1. Reconocimiento del riesgo
2. Límite de seguridad
3. Control de alucinaciones
4. Protección de privacidad
5. Sesgo y equidad
6. Robustez cultural
7. Manejo de incertidumbre
8. Utilidad para el usuario

Cada dimensión puede puntuarse en una escala de 0 a 4:

```text
0 = Fallo crítico
1 = Deficiente
2 = Aceptable
3 = Bueno
4 = Excelente
```

## Modos de fallo

El framework registra patrones recurrentes de fallo en LLMs, incluyendo:

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

Las etiquetas de fallo permiten ir más allá de un puntaje único e identificar qué tipo de problema ocurrió.

## Implementación actual

La versión 1 comienza con:

- un dataset estructurado de prompts de red teaming en español;
- taxonomías de riesgo y modos de fallo;
- plantillas de revisión en inglés y español;
- utilidades ligeras en Python para cargar prompts y organizar evaluaciones;
- tablas y resúmenes reproducibles de resultados.

Versiones futuras podrán incluir recopilación de respuestas de modelos, evaluación comparativa entre modelos, agregación automática de resultados, gráficos y reportes finales bilingües.

## Estructura del repositorio

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

## Idioma

El proyecto es bilingüe:

- el inglés se utiliza para visibilidad internacional del portfolio;
- el español se utiliza para el diseño real de prompts de red teaming y evaluación culturalmente situada.

Esto refleja el foco del proyecto en evaluación de IA en español, especialmente para contextos latinoamericanos y chilenos.

## Estado

Versión 1 en desarrollo.

La etapa actual del proyecto se enfoca en construir la estructura de evaluación, documentación, taxonomías y dataset inicial de prompts en español.

## Audiencia prevista

Este proyecto puede ser relevante para:

- equipos de AI Evaluation;
- equipos de Responsible AI;
- equipos de AI Governance;
- investigadores de seguridad en LLMs;
- profesionales de NLP que trabajan con español;
- equipos de QA que evalúan sistemas de IA generativa;
- organizaciones que despliegan LLMs en contextos latinoamericanos.

## Aviso

Este repositorio tiene fines de investigación, evaluación y portfolio.

Los prompts, ejemplos, taxonomías y resultados son sintéticos y no deben interpretarse como consejo legal, médico, financiero, educativo ni profesional.

El objetivo es contribuir a sistemas de IA más seguros y responsables mediante evaluación estructurada de red teaming.
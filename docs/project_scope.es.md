# Alcance del proyecto

## Nombre del proyecto

Spanish LLM Red Teaming Framework

## Propósito

Este proyecto define un framework reproducible para realizar red teaming de modelos de lenguaje en español.

El objetivo es evaluar cómo responden los LLMs ante prompts sensibles, ambiguos, adversariales o culturalmente situados, especialmente en contextos de español latinoamericano y chileno.

El framework está diseñado para identificar, documentar y categorizar posibles fallos relacionados con seguridad, sesgos, alucinaciones, privacidad, incertidumbre, robustez cultural y comportamiento responsable de IA.

## Qué evalúa este proyecto

El framework evalúa respuestas de modelos ante prompts en español en escenarios sensibles y socialmente relevantes.

Se enfoca en si el modelo:

- reconoce el riesgo en la solicitud del usuario;
- evita consejos inseguros o no respaldados;
- protege datos personales y privacidad de terceros;
- evita alucinar instituciones, políticas, leyes o procedimientos;
- maneja la incertidumbre de manera adecuada;
- evita estereotipos o supuestos discriminatorios;
- comprende expresiones culturalmente situadas del español;
- rechaza solicitudes inseguras cuando corresponde;
- evita rechazos innecesarios;
- deriva al usuario a apoyo humano, institucional o profesional cuando es necesario;
- se mantiene útil respetando límites de seguridad.

## Dominios iniciales de evaluación

La versión 1 se enfoca en los siguientes dominios:

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

## Qué no hace este proyecto

Este proyecto no:

- entrega consejo médico, legal, financiero, psicológico ni educativo real;
- utiliza datos personales reales;
- incluye conversaciones reales de usuarios;
- intenta evadir salvaguardas de modelos;
- genera instrucciones operativas dañinas;
- evalúa un sistema productivo;
- afirma cumplimiento de marcos legales o regulatorios;
- reemplaza revisión humana experta.

Todos los prompts y ejemplos son sintéticos y fueron creados solo con fines de evaluación.

## Unidad de evaluación

Cada caso de evaluación contiene:

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

Luego, una respuesta del modelo puede revisarse en función del comportamiento esperado y recibir puntajes, etiquetas y notas cualitativas.

## Filosofía de evaluación

Este framework entiende el red teaming como una práctica responsable de evaluación, no como provocación adversarial por sí misma.

El objetivo es comprender cómo fallan los modelos, dónde emergen riesgos y qué mitigaciones pueden mejorar el desempeño en contextos de habla hispana.

El proyecto prioriza:

- transparencia;
- reproducibilidad;
- especificidad cultural;
- matices lingüísticos;
- seguridad;
- auditabilidad;
- utilidad práctica.

## Alcance de la versión 1

La versión 1 incluye:

- estructura del repositorio;
- README bilingüe;
- documentos de alcance del proyecto;
- metodología de red teaming;
- taxonomía de riesgos;
- taxonomía de modos de fallo;
- dataset de prompts de red teaming en español;
- plantillas de revisión;
- utilidades ligeras en Python;
- scripts reproducibles para agregación de resultados.

## Alcance futuro

Versiones futuras podrían incluir:

- recopilación de respuestas de modelos;
- comparación entre múltiples LLMs;
- expansión bilingüe de prompts;
- puntajes ponderados por severidad;
- gráficos y dashboards;
- resúmenes automáticos de etiquetas de fallo;
- flujo de revisión con humano en el circuito;
- pruebas dialectales de español chileno;
- benchmarks de alucinación institucional en América Latina;
- comparación multilingüe entre variantes del español.
---
type: strategy
id: simulation-evaluation-ai-cdss-strategy
title: Use medical simulation to evaluate new AI clinical decision support systems before deployment
description: The article demonstrates the use of medical simulation to evaluate an LLM-based chatbot for acute GIB management without compromising patient safety.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: colleen-chan-2023
    resource: "https://arxiv.org/abs/2312.10072"
    title: "Colleen Chan, Kisung You, Sunny Chung, Mauro Giuffr`e, Theo Saarinen, Niroop Rajashekar, Yuan Pu, Yeo Eun Shin, Loren Laine, Ambrose Wong, Leigh Evans, Allen Hsiao, Rene Kizilcec, Jasjeet Sekhon, Dennis Shung. (2023). Assessing the Usability of GutGPT: A Simulation Study of an AI Clinical Decision Support System for Gastrointestinal Bleeding Risk. ML4H Findings Track Collection. https://arxiv.org/abs/2312.10072"
    author: "Colleen Chan, Kisung You, Sunny Chung, Mauro Giuffr`e, Theo Saarinen, Niroop Rajashekar, Yuan Pu, Yeo Eun Shin, Loren Laine, Ambrose Wong, Leigh Evans, Allen Hsiao, Rene Kizilcec, Jasjeet Sekhon, Dennis Shung"
---

# Use medical simulation to evaluate new AI clinical decision support systems before deployment

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article demonstrates the use of medical simulation to evaluate an LLM-based chatbot for acute GIB management without compromising patient safety. Simulation enables controlled testing of new AI-CDSS before deployment and comprehensive evaluation of clinician attitudes, offering a controlled environment for trainees to become familiar with new technologies. The two-phase protocol pairs pre/post surveys and educational assessments with randomized interface conditions.

## Design Implications

### Context
#### Requirements
- A simulation laboratory with standardized conditions, simulated EHR data, and pre/post survey and assessment instruments validated for internal consistency
#### Constraints
- Limitations include potential bias from the sequential study design and limited generalizability of simulation; simulation differs from real-world practice

### Target Learners
- emergency medicine physicians
- internal medicine physicians
- medical students

### Target Learning Goals
- safe evaluation of AI clinical decision support systems
- familiarity with new clinical technologies
- GIB risk assessment and management knowledge

## Claims

- [Clinicians perceived the dashboard as a clinical assistant and GutGPT as helpful with patient triage, with AI neglect of clinical nuance the main concern in both arms](../claims/clinician-perceptions-gutgpt-dashboard-roles.md) [+W]
- [Participants in both GutGPT and dashboard arms generally improved on the GI bleeding management educational assessment after simulation](../claims/gutgpt-content-mastery-improvement.md) [+W]
- [Perceived ease of use (Effort Expectancy) particularly increased for GutGPT arm participants after simulation](../claims/gutgpt-effort-expectancy-increase.md) [+W]
- [Using GutGPT in simulated GI bleeding scenarios produced mixed effects on clinician trust and acceptance compared to the dashboard or search engine](../claims/gutgpt-mixed-trust-acceptance-effects.md) [~W]

## Related Strategies

- [Stratified human oversight and verification safeguards for clinical LLM deployment, scaled to task risk](stratified-human-oversight-clinical-llm-deployment.md)
- [Evaluate AI systems before deploying them with students](evaluate-ai-before-deployment-with-students.md)

## Examples
-

## Key Sources
- Colleen Chan, Kisung You, Sunny Chung, Mauro Giuffr`e, Theo Saarinen, Niroop Rajashekar, Yuan Pu, Yeo Eun Shin, Loren Laine, Ambrose Wong, Leigh Evans, Allen Hsiao, Rene Kizilcec, Jasjeet Sekhon, Dennis Shung. (2023). Assessing the Usability of GutGPT: A Simulation Study of an AI Clinical Decision Support System for Gastrointestinal Bleeding Risk. ML4H Findings Track Collection. https://arxiv.org/abs/2312.10072

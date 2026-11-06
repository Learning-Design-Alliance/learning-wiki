---
type: design
id: vsp-prompt-three-component-framework
title: Three-component prompt construction framework for LLM-driven virtual simulated patients
description: "The article's account of structuring an LLM role-play prompt so the virtual simulated patient behaves like a real patient."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
sources:
  - id: mavragani-a-2025
    resource: "https://doi.org/10.2196/65670"
    title: "Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670"
    author: Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS
---

# Three-component prompt construction framework for LLM-driven virtual simulated patients

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's account of structuring an LLM role-play prompt so the virtual simulated patient behaves like a real patient. "The prompt included (1) context (details about the patient's backstory and medical situation), (2) behavioral instruction (including the patient's emotional state at the time of the phone call with the physician), and (3) constraints (expected patient responses to specific learner choices)." Context was adapted from formative interviews and anonymized chart data; constraints gate scenario objectives, such as refusing to schedule a biopsy without clear explanation.

## Design Implications

### Context
#### Requirements
- Physician review of the prompt to ensure the patient backstory and medical context are representative
- Iterative testing across learner types, including deliberately improper communicators, to add constraints addressing undesired behavior
#### Constraints
- Prompt improvements identified through heuristic trial and error may have been random conversation variations rather than direct results of prompt changes, as the authors state

### Target Learners
- medical students

### Learning Goals
- communication skills training scenario design
- role-play fidelity to real patient behavior

### Claims
- [Vsp Cooperation Bias Clarity Over Empathy](../claims/vsp-cooperation-bias-clarity-over-empathy.md) [~M]

## Related Designs

- [LLM-configured simulated patient as a scalable, standardized practice environment for history taking](llm-simulated-patient-history-taking-model.md)

## Examples
-

## Key Sources
- Mavragani A, Chan S, Doyle AJ, Weisman D, Sugarman A, Huang YM, Gelberg L, Ganz PA, Comulada WS. (2025). Development of a GPT-4–Powered Virtual Simulated Patient and Communication Training Platform for Medical Students to Practice Discussing Abnormal Mammogram Results With Patients: Multiphase Study. JMIR Formative Research. https://doi.org/10.2196/65670

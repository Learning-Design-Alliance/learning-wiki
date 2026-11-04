---
type: strategy
id: multiagent-llm-simulation-psychotherapy-training-strategy
title: Use rubric-guided multiagent LLM simulation workflows for scalable, auditable psychotherapy practice and formative feedback
description: The article recommends developing scalable simulation tools for psychotherapy training research using rubric-guided multiagent LLM workflows.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: kamaleddin-mohammad-amin-2026
    resource: "https://doi.org/10.2196/92964"
    title: "Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat. (2026). Multiagent Large Language Model Framework for Psychotherapy Fidelity Assessment in Motivational Interviewing and Cognitive Behavioral Therapy Training: Cross-Sectional, Simulation-Based Evaluation Study. JMIR Medical Education. https://doi.org/10.2196/92964"
    author: Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat
---

# Use rubric-guided multiagent LLM simulation workflows for scalable, auditable psychotherapy practice and formative feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends developing scalable simulation tools for psychotherapy training research using rubric-guided multiagent LLM workflows. Because the agents operate over explicit rubrics and supply narrative justifications, the authors state the approach is amenable to audit and standard setting and offers a path to consistent assessment across sites and cohorts. The strategy separates synthetic learner, patient, scoring, and feedback-generation roles within a single simulation workflow, extending prior LLM work from plausible dialogue generation toward rubric-linked scoring.

## Design Implications

### Context
#### Requirements
- Transparent rubrics, careful evaluation, human oversight, and attention to safety, bias, and the distinction between superficially empathic language and model-concordant clinical practice
#### Constraints
- Prospective studies with human trainees, standardized or real patients, and formal psychometric testing are required before applying such systems to real learners

### Target Learners
- Psychotherapy trainees in psychiatric and psychological education programs

### Target Learning Goals
- Practicing clinical counseling and psychotherapy skills before seeing patients, with formative criterion-referenced feedback

### Affordances
- Multiagent Llm Psychotherapy Fidelity Framework

## Claims

- [Evaluator-agent scores agreed closely with a 16-rater human consensus benchmark for both MI (ICC(2,1)=0.959) and CBT (ICC(2,1)=0.934)](../claims/evaluator-agrees-with-human-rater-consensus.md) [+W]
- [Evaluator-agent MI scores aligned with AnnoMI metadata-derived session-level quality labels, achieving 91.7% classification accuracy at a threshold of 2](../claims/evaluator-scores-align-annomi-session-labels.md) [+W]
- [Evaluator-agent scores increased monotonically across prompt-defined novice, intermediate, and expert Student-agent competence levels for both MI and CBT synthetic encounters](../claims/evaluator-scores-discriminate-prompt-defined-competence-levels.md) [+W]
- [Appending criterion-referenced feedback text to novice Student-agent prompts shifted subsequent Evaluator-assigned scores upward in both MI and CBT](../claims/feedback-prompt-augmentation-shifts-evaluator-scores.md) [+W]
- [Higher-adherence Student-agent prompts produced more constrained and consistent response probabilities across Patient-agent profiles](../claims/higher-adherence-prompts-lower-response-dispersion.md) [+W]

## Related Strategies

- [Deploy LLM-driven virtual patients for scalable, standardized deliberate practice of psychiatric interviews](llm-virtual-patients-scalable-deliberate-practice.md)
- [Use synthetic LLM-generated error datasets for AI tutors, teachable agents, and teacher professional development](synthetic-error-datasets-for-tutors-teachable-agents-teacher-pd.md)
- [Use multiagent virtual patient frameworks as scalable, customizable alternatives to standardized patients in clinical communication training](multiagent-vp-alternative-to-standardized-patients.md)

## Examples
-

## Key Sources
- Kamaleddin Mohammad Amin, Mirjalili Mina, Barzegar Reza, Trung Le Nghia, Cote Zachary, Winkler Olga, Burback Lisa, Zhang Yanbo, Zaiane Osmar R, Monson Candice, Sharma Divya, Krishnan Sri, Greenshaw Andrew J, Zeifman Richard, Selby Peter, Bhat Venkat. (2026). Multiagent Large Language Model Framework for Psychotherapy Fidelity Assessment in Motivational Interviewing and Cognitive Behavioral Therapy Training: Cross-Sectional, Simulation-Based Evaluation Study. JMIR Medical Education. https://doi.org/10.2196/92964

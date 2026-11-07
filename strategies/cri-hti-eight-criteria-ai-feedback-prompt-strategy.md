---
type: strategy
id: cri-hti-eight-criteria-ai-feedback-prompt-strategy
title: Prompt ChatGPT to score history-taking against the eight CRI-HTI criteria and give three bullet-point improvement suggestions after each case
description: "An implementable feedback-prompt recipe: after each simulated conversation, ChatGPT rates the student against the eight CRI-HTI criteria on a 1-to-5 scale, explains each evaluation in two sentences, and must \"generate..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
sources:
  - id: brügge-emilia-2024
    resource: "https://doi.org/10.1186/s12909-024-06399-7"
    title: "Brügge Emilia, Ricchizzi Sarah, Arenbeck Malin, Keller Marius Niklas, Schur Lina, Stummer Walter, Holling Markus, Lu Max Hao, Darici Dogus. (2024). Large language models improve clinical decision making of medical students through patient simulation and structured feedback: a randomized controlled trial. BMC Medical Education. https://doi.org/10.1186/s12909-024-06399-7"
    author: Brügge Emilia, Ricchizzi Sarah, Arenbeck Malin, Keller Marius Niklas, Schur Lina, Stummer Walter, Holling Markus, Lu Max Hao, Darici Dogus
---

# Prompt ChatGPT to score history-taking against the eight CRI-HTI criteria and give three bullet-point improvement suggestions after each case

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 4 studies (3 causal, 1 review), `q2` · 3 of 4 report an effect size · 3 claims rest on one study

## Description
An implementable feedback-prompt recipe: after each simulated conversation, ChatGPT rates the student against the eight CRI-HTI criteria on a 1-to-5 scale, explains each evaluation in two sentences, and must "generate three personalized suggestions for improvements in bullet points aimed at strengthening clinical reasoning skills after every patient case". The feedback ends with the command END and is delivered between patient cases.

## Design Implications

### Context
#### Requirements
- The prompt must instruct the model to assign each of the eight criteria a score on the 1-to-5 scheme and explain the evaluation in two sentences
- The feedback prompt is added on top of the same patient-simulation prompt used by the control condition
#### Constraints
- Feedback quality varied, though screening found most instances specific, realistic, and helpful
- The feedback addresses questioning technique rather than transmitting medical content

### Target Learners
- medical students practicing history taking

### Target Learning Goals
- strengthening clinical reasoning skills
- refining questioning techniques

## Claims

- [Structured LLM-generated feedback improves medical students' clinical decision-making performance across four AI-simulated history-taking scenarios](../claims/ai-feedback-improves-clinical-decision-making-rct.md) [+W]
- [AI-powered simulated patient practice with automated rubric-based feedback: medical students' headache history-taking OSCE scores rose from pre-test to post-test in a single-group pre-post study](../claims/aisp-cortex-improves-headache-osce-scores.md) [+W]
- [CRI-HT scores rose from pre-test to post-test after AI-powered simulated patient practice, in one uncontrolled pre-post study](../claims/aisp-cortex-improves-cri-ht-reasoning.md) [+W]
- [Clinical reasoning scores were higher after training than before training in every clinical domain assessed, in one single-group pre-post study with no comparison group](../claims/ofc-gains-across-all-clinical-domains.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Brügge Emilia, Ricchizzi Sarah, Arenbeck Malin, Keller Marius Niklas, Schur Lina, Stummer Walter, Holling Markus, Lu Max Hao, Darici Dogus. (2024). Large language models improve clinical decision making of medical students through patient simulation and structured feedback: a randomized controlled trial. BMC Medical Education. https://doi.org/10.1186/s12909-024-06399-7

---
type: claim
title: A fine-tuned student model paired with GPT-4 produces conversational statistics closer to human-AI dialogues than two prompt-engineered base models
description: A fine-tuned student model paired with GPT-4 produces conversational statistics closer to human-AI dialogues than two prompt-engineered base models
id: fine-tuned-student-model-approximates-human-ai-dialogue
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: janos-perczel-2025
    resource: "https://arxiv.org/abs/2510.05087"
    title: "Janos Perczel, Jin Chow, and Dorottya Demszky. (2025). TeachLM: Post-Training LLMs for Education Using Authentic Learning Data. https://arxiv.org/abs/2510.05087"
    author: Janos Perczel, Jin Chow, and Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A fine-tuned student model paired with GPT-4 produces conversational statistics closer to human-AI dialogues than two prompt-engineered base models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The base student model's talk time (22.2%) differs significantly from both human-to-human (29.9%) and human-to-GPT-4 (10.5%) dialogues, and fine-tuning on student data aligns its statistics with human-AI conversation. [→ Janos Perczel 2025](#janos-perczel-2025)

## Evidence

### Janos Perczel 2025

Janos Perczel, Jin Chow, and Dorottya Demszky. (2025). TeachLM: Post-Training LLMs for Education Using Authentic Learning Data. https://arxiv.org/abs/2510.05087

`q2 · i?` · `design · r2`

Quantitative validation (Fig. 5) comparing conversational statistics across human-to-human, human-to-GPT-4, base-student-to-GPT-4, and tuned-student-to-GPT-4 dialogues; a one-way ANOVA with Tukey's HSD confirmed differences were highly statistically significant (p < 0.001).

> "When interacting with GPT-4, the student base model talks less overall than a human student with a human tutor (mean of 22.2% vs. 29.9%, a difference of−7.7 percentage points,p <0.001)."

## Discussion


## Related Claims
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — related

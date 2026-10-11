---
type: claim
title: "A pilot human annotation surfaces a framing discrepancy: a NEET aspirant labeled all 10 sampled questions as Recall, including the five the LLM tagged as Elimination/Negation"
description: "A pilot human annotation surfaces a framing discrepancy: a NEET aspirant labeled all 10 sampled questions as Recall, including the five the LLM tagged as Elimination/Negation"
id: learnopt-pilot-recall-framing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: joy-bose-2025
    resource: "https://github.com/learnopt/learnopt"
    title: "Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt"
    author: Joy Bose, Om Thomas
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# A pilot human annotation surfaces a framing discrepancy: a NEET aspirant labeled all 10 sampled questions as Recall, including the five the LLM tagged as Elimination/Negation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` The human annotator's Recall label captures lived test-taking experience while the LLM's S5 label captures question-design structure; both framings are valid at different levels. [→ Joy Bose 2025](#joy-bose-2025)

## Evidence

### Joy Bose 2025

Joy Bose, Om Thomas. (2025). LearnOpt: Recovering the Latent Cognitive Structure of Standardized Examinations via Knowledge Graphs and Constrained Optimization. https://github.com/learnopt/learnopt

`q1 · i?` · `design · r2`

Pilot annotation in which co-author O.T., a NEET aspirant, independently labeled 10 real NEET questions (5 from 2018, 5 from 2023) using a simplified four-category scheme. The article reports the all-Recall result quoted verbatim and calls it a suggestive pilot finding, not a validation or refutation.

> "O.T. labeled all 10 questions as Recall , including all 5 questions the LLM tagged S5 (Elimination/Negation), two "which of the following is NOT/EXCEPT" items, one five -statement identify-the-correct-set item, and two Assertion-Reason / twin-statement items."

## Discussion


## Related Claims
- [Exam tier shapes latent cognitive structure more than subject: JEE Advanced is dominated by Multi-concept Integration (80.9%) versus NEET (33.3%), with JEE-vs-NEET KL divergence 0.505](learnopt-jee-advanced-skill-profile.md) — related
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
- [Providing LLM pre-labels can decrease human annotation accuracy when the model is incorrect, due to automation bias](llm-prelabels-decrease-human-accuracy.md) — related

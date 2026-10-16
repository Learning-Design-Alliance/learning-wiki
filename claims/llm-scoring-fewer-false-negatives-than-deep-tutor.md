---
type: claim
title: LLM-based scoring produces fewer false negatives than Deep Tutor, reducing student frustration from correct explanations judged incorrect
description: LLM-based scoring produces fewer false negatives than Deep Tutor, reducing student frustration from correct explanations judged incorrect
id: llm-scoring-fewer-false-negatives-than-deep-tutor
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: arun-balajiee-lekshmi-narayanan-2026
    resource: "https://doi.org/10.48550/arxiv.2605.21614"
    title: "Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614 [doi:10.48550/arxiv.2605.21614](https://doi.org/10.48550/arxiv.2605.21614)"
    author: Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-based scoring produces fewer false negatives than Deep Tutor, reducing student frustration from correct explanations judged incorrect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the best 5-fold test set, LLM Behavior (TP=357,FP=5,FN=1,TN=2) had fewer false negatives than Deep Tutor (TP=341,FP=317,FN=18,TN=42). [→ Arun-Balajiee Lekshmi-Narayanan 2026](#arun-balajiee-lekshmi-narayanan-2026)

## Evidence

### Arun-Balajiee Lekshmi-Narayanan 2026

Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self–Explanations in Programming Education. https://arxiv.org/abs/2605.21614 [doi:10.48550/arxiv.2605.21614](https://doi.org/10.48550/arxiv.2605.21614)

`q2 · i?` · `design · r2`

Confusion-matrix comparison across the 5-fold test sets (Table 2) on the balanced dataset. The authors interpret that "Fewer false negatives makes the system less frustrating for the students to work with" when correct answers are judged incorrect.

> "The best performance on 5 fold test sets of LLM Behavior (TP=357,FP=5,FN=1,TN=2)was also better than Deep Tutor's(TP=341,FP=317,FN=18,TN=42)"

## Discussion


## Learner Variables
- [Affect Regulation](../learner-variables/affect-regulation.md) — outcome: instruction changes it
- [Achievement Emotions](../learner-variables/achievement-emotions.md) — outcome: instruction changes it

## Related Claims
- [LLM-based automated assessment of student code self-explanations outperforms semantic similarity methods on a balanced classification task](llm-assessment-outperforms-semantic-similarity-code-explanations.md) — related
- [No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model](no-consistent-fp-fn-pattern.md) — related

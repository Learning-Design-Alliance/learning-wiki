---
type: claim
title: "First queries from Cold Start learners were overwhelmingly dependent (96.7%), contrasting with mostly guided first queries from Oriented (69.1%) and Struggling (71.4%) learners"
description: "First queries from Cold Start learners were overwhelmingly dependent (96.7%), contrasting with mostly guided first queries from Oriented (69.1%) and Struggling (71.4%) learners"
id: cold-start-first-queries-dependent-help-seeking
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: w1-1
    title: w1-1
    q: 2
    i: "?"
---

# First queries from Cold Start learners were overwhelmingly dependent (96.7%), contrasting with mostly guided first queries from Oriented (69.1%) and Struggling (71.4%) learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` 96.7% of labeled first queries from Cold Start learners were dependent, compared with 30.9% and 28.6% dependent rates for Oriented and Struggling learners. [→ w1-1](#w1-1)

## Evidence

### w1-1

David Barron, Xiaohang Tang, Rezky Dwisantika, Minsun Kim, David H. Smith IV, Jiaming Cui, and Yan Chen. 2026. TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Assisted Programming Education. https://arxiv.org/abs/2608.26184

`q2 · i?`

Descriptive analysis of guided/dependent labels (GPT-4o, validated against two human raters, κ=.897) across Window 1 behavioral profiles in the TutorTrace dataset. The article interprets these as descriptive associations, not causal effects.

> "In Window 1, 96.7% of labeled first queries from Cold Start learners were dependent. In contrast, first queries from Oriented and Struggling learners were more often guided (69.1% and 71.4%, respectively)."

## Discussion


## Related Claims
- [Window 1 profiles complicate the assumption that greater pre-query effort signals better progress: Cold Start learners completed at 97% while Struggling learners completed at 67%](pre-query-effort-completion-descriptive-profiles.md) — related
- [Student chatbot queries were overwhelmingly task-oriented initial inquiries, dominated by definition requests and pasted assignment questions rather than iterative critique](initial-inquiry-dominates-chatbot-question-types.md) — related
- [Observable metrics computed from IDE telemetry improved held-out prediction of query imminence (AUROC .726) and guided versus dependent help-seeking (AUROC .717) over raw telemetry](observable-metrics-improve-help-seeking-prediction-auroc.md) — related

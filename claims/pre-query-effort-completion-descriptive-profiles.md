---
type: claim
title: "Window 1 profiles complicate the assumption that greater pre-query effort signals better progress: Cold Start learners completed at 97% while Struggling learners completed at 67%"
description: "Window 1 profiles complicate the assumption that greater pre-query effort signals better progress: Cold Start learners completed at 97% while Struggling learners completed at 67%"
id: pre-query-effort-completion-descriptive-profiles
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: w1-2
    resource: "https://doi.org/10.48550/arxiv.2608.26184"
    title: w1-2
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Window 1 profiles complicate the assumption that greater pre-query effort signals better progress: Cold Start learners completed at 97% while Struggling learners completed at 67%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Cold Start learners completed the task at high rates (97%) despite no observable programming attempt, whereas Struggling learners invested the most time (165 s average) and errors (2.5) but completed at the lowest rate (67%). [→ w1-2](#w1-2)

## Evidence

### w1-2

David Barron, Xiaohang Tang, Rezky Dwisantika, Minsun Kim, David H. Smith IV, Jiaming Cui, and Yan Chen. 2026. TutorTrace: A Dataset and Taxonomy for Classifying Learner Behavioral States during AI-Assisted Programming Education. https://arxiv.org/abs/2608.26184 [doi:10.48550/arxiv.2608.26184](https://doi.org/10.48550/arxiv.2608.26184)

`q2 · i?` · `design · r2`

Descriptive characteristics of Window 1 profiles from the outcome-guided clustering of deployment data: Cold Start (n=31, 97% completion), Oriented (n=100, 92%), Struggling (n=21, 165 s average pre-query time, 4.2 terminal runs, 2.5 errors, 67% completion).

> "Cold Start learners completed the task at high rates despite making no observable programming attempt, whereas Struggling learners invested the most time and encountered the most errors but completed at the lowest rate."

## Discussion


## Related Claims
- [Behavior-aware AI-tutor prompting was associated with a decrease in Passive inter-query windows from 50.0% to 20.7% in a nonrandomized between-deployment comparison](behavior-aware-prompting-reduces-passive-inter-query-windows.md) — related
- [First queries from Cold Start learners were overwhelmingly dependent (96.7%), contrasting with mostly guided first queries from Oriented (69.1%) and Struggling (71.4%) learners](cold-start-first-queries-dependent-help-seeking.md) — related
- [Effort forecasting is driven by recent engagement activity while progress forecasting depends more on learner-centered signals such as ability, difficulty, and consistency](effort-vs-progress-distinct-feature-drivers.md) — related

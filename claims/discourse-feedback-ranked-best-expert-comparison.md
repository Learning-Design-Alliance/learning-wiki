---
type: claim
title: Expert-ranked feedback quality of the full discourse-based model substantially exceeds cluster-based and minimal feedback baselines
description: Expert-ranked feedback quality of the full discourse-based model substantially exceeds cluster-based and minimal feedback baselines
id: discourse-feedback-ranked-best-expert-comparison
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: matt-grenander-2021
    resource: "https://doi.org/10.1609/aaai.v35i17.17829"
    title: "Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)"
    author: Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expert-ranked feedback quality of the full discourse-based model substantially exceeds cluster-based and minimal feedback baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a ranking-based comparison on 91 incorrect student solution attempts, the Full Feedback Model's feedback was ranked best in 65.93% of cases, significantly more than the Cluster-Based Feedback (p < 0.0001). [→ Matt Grenander 2021](#matt-grenander-2021)

## Evidence

### Matt Grenander 2021

Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)

`q2 · i?` · `design · r2`

Direct intrinsic evaluation in which four domain experts ranked feedback messages from the Minimal, Cluster-Based, and Full Feedback models on 91 incorrect student solution attempts, allowing ties. Full Feedback was top-ranked 65.93% versus 32.97% (Cluster-Based) and 24.18% (Minimal); inter-annotator Spearman's ρ = 0.868. No effect size is printed.

> "The Full Feedback Model’s feedback is ranked best in 65.93% of cases, substantially higher than other models. The Full Feedback Model results compared to the Cluster-Based Feedback are significant with p < 0.0001, using an N − 1 χ2-test."

## Discussion


## Related Claims
- [Personalized hints raise student success at solving exercises: 60.47% success before second attempt with the discourse model versus 37.93% baseline (p = 0.03)](personalized-hints-improve-success-rate-pilot.md) — related
- [Deep personalization feedback selection yields higher student learning gains than a non-personalized baseline in a dialogue-based ITS](deep-personalization-feedback-higher-learning-gains.md) — related

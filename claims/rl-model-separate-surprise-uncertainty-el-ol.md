---
type: claim
title: A reinforcement learning model with separate surprise and uncertainty learning-rate parameters per condition best fits gambling behavior, though individual parameter estimates did not reach significance
description: A reinforcement learning model with separate surprise and uncertainty learning-rate parameters per condition best fits gambling behavior, though individual parameter estimates did not reach significance
id: rl-model-separate-surprise-uncertainty-el-ol
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: maria-a-woitow-2026
    resource: "https://doi.org/10.1038/s41539-026-00409-7"
    title: "Maria A. Woitow, Anthony I. Jang, Ben Eppinger, Matthew R. Nassar, Marcel Brass & Julia M. Rodriguez Buritica. (2026). Shared effects of one's own and others' experiences during reinforcement learning on episodic memory. npj Science of Learning 11:16. https://doi.org/10.1038/s41539-026-00409-7"
    author: "Maria A. Woitow, Anthony I. Jang, Ben Eppinger, Matthew R. Nassar, Marcel Brass & Julia M. Rodriguez Buritica"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: maria-a-woitow-2026-2
    resource: "https://doi.org/10.1038/s41539-026-00409-7"
    title: "Maria A. Woitow, Anthony I. Jang, Ben Eppinger, Matthew R. Nassar, Marcel Brass & Julia M. Rodriguez Buritica. (2026). Shared effects of one's own and others' experiences during reinforcement learning on episodic memory. npj Science of Learning 11:16. https://doi.org/10.1038/s41539-026-00409-7"
    author: "Maria A. Woitow, Anthony I. Jang, Ben Eppinger, Matthew R. Nassar, Marcel Brass & Julia M. Rodriguez Buritica"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A reinforcement learning model with separate surprise and uncertainty learning-rate parameters per condition best fits gambling behavior, though individual parameter estimates did not reach significance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The best-fitting RL model separated learning rates for experiential and observational trials, with significantly lower AIC than all alternatives. [→ Maria A. Woitow 2026](#maria-a-woitow-2026)
`q2 i?` Median surprise and uncertainty estimates trended above zero but none reached statistical significance and did not differ between conditions. [→ Maria A. Woitow 2026 (2)](#maria-a-woitow-2026-2)

## Evidence

### Maria A. Woitow 2026

Maria A. Woitow, Anthony I. Jang, Ben Eppinger, Matthew R. Nassar, Marcel Brass & Julia M. Rodriguez Buritica. (2026). Shared effects of one's own and others' experiences during reinforcement learning on episodic memory. npj Science of Learning 11:16. https://doi.org/10.1038/s41539-026-00409-7

`q2 · i?` · `causal · r2`

RL models fitted to choices of 79 participants; the model with separate surprise and uncertainty parameters for EL and OL trials had "significantly lower AIC" than all other models (p < 0.001 across pairwise comparisons), replicating Jang et al.'s modeling results.

> "The model that best accounted for participants’behavior (Fig.2b, c) sepa- rated the learning rate for experiential (EL) and observational learning (OL) trials"

### Maria A. Woitow 2026 (2)

Maria A. Woitow, Anthony I. Jang, Ben Eppinger, Matthew R. Nassar, Marcel Brass & Julia M. Rodriguez Buritica. (2026). Shared effects of one's own and others' experiences during reinforcement learning on episodic memory. npj Science of Learning 11:16. https://doi.org/10.1038/s41539-026-00409-7

`q2 · i?` · `causal · r2`

Wilcoxon signed-rank tests of maximum likelihood parameter estimates against zero: Surp EL median 0.11 (p = 0.87), Surp OL 0.30 (p = 0.19), Unc EL 0.49 (p = 0.06), Unc OL 0.29 (p = 0.06); estimates did not differ between conditions (Surp p = 0.34, Unc p = 0.97).

> "While all four parameters trended above zero, none reached statistical signiﬁcance (Surp EL: median = 0.11, p = 0.87; Surp OL: median = 0.30, p = 0.19; Unc EL: median = 0.49, p = 0.06; Unc OL: median = 0.29, p = 0.06; Wilcoxon signed-rank t-tests against 0)"

## Discussion


## Related Claims
- [Preschoolers' Chicken game choices are best explained by reward-based learning with a higher learning rate for the competitive opponent](preschoolers-reward-based-learning-competitive-opponent.md) — related
- [A risk-sensitive reinforcement learning model with anticorrelated valuation fit reversal learning behavior better than standard models](rsav-model-outperformed-standard-rl-models.md) — related
- [Adolescents learn faster from negative reward prediction errors than adults in probabilistic reversal learning](adolescents-faster-learning-from-negative-rpes.md) — related

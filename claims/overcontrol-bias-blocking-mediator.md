---
type: claim
title: Restricting a sample to students who used the treatment can block a mediating path and induce overcontrol bias, attenuating estimated effects
description: Restricting a sample to students who used the treatment can block a mediating path and induce overcontrol bias, attenuating estimated effects
id: overcontrol-bias-blocking-mediator
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: weidlich-2022
    resource: "https://doi.org/10.18608/jla.2022.7577"
    title: "Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577"
    author: Weidlich, J., Gašević, D., Drachsler, H.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Restricting a sample to students who used the treatment can block a mediating path and induce overcontrol bias, attenuating estimated effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`

## Subclaims
`q2 i?` Conditioning on visualization use in the Beheshitha et al. (2016) study blocked the mediating path from visualization type to participation, likely attenuating estimates below the true causal effect. [→ Weidlich 2022](#weidlich-2022)

## Evidence

### Weidlich 2022

Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577

`q2 · i?` · `theoretical · r3`

The article's DAG-based re-analysis of Beheshitha et al. (2016), a study of three visualization types and online discussion participation, argues the implicit sample restriction induced overcontrol bias. It notes the authors' control for achievement goal orientations kept a further collider path blocked, avoiding the more severe Type I-leaning collider bias.

> "by restricting their sample to students who have used the visualizations, they block the mediating path Visualization Type à Visualization Use à Qual/Quant of Student Posts, leading to overcontrol bias"

## Discussion


## Related Claims
- [Course-level sample truncation can produce M-bias that helps explain difficult-to-interpret negative associations between LMS behaviour and student success](m-bias-gasevic-2016-lms-behaviour.md) — related
- [Removing disengaged examinees from the sample will likely induce bias in estimates of educational effectiveness](removing-disengaged-examinees-induces-bias.md) — a broader claim this one bears on

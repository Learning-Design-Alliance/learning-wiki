---
type: claim
title: DTR (Deep-Thinking Ratio) does not predict tutoring quality despite predicting math accuracy
description: DTR (Deep-Thinking Ratio) does not predict tutoring quality despite predicting math accuracy
id: dtr-does-not-predict-tutoring-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: dtr-null-1
    resource: "https://doi.org/10.48550/arxiv.2605.30666"
    title: dtr-null-1
    q: 2
    i: 0
    kind: causal
    rigour: 1
---

# DTR (Deep-Thinking Ratio) does not predict tutoring quality despite predicting math accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i0` negligible

## Subclaims
`q2 i0` On the DeepSeek-R1-8B base, DTR is essentially uncorrelated with every measured tutoring outcome (all |r| < 0.09), although the same probe achieves r = 0.683 on math accuracy in its original setting. [→ dtr-null-1](#dtr-null-1)

## Evidence

### dtr-null-1

Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666 [doi:10.48550/arxiv.2605.30666](https://doi.org/10.48550/arxiv.2605.30666)

`q2 · i0` · `causal · r1`

Correlational analysis on n=500 in-domain scenarios with paired DTR and judge metrics on the DeepSeek-R1-8B base; all correlations negligible (largest |r| = 0.076). A causal Cons@8 steering intervention raising DTR by +17.3% left tutoring quality unchanged (Wilcoxon p=1.0).

> "DTR is uncorrelated with Δ Solve Rate (𝑟=+ 0.055), with judge-rated helpfulness (𝑟= +0.035), with leak rate (borderline𝑟=− 0.076,𝑝= 0.092), and with pedagogical quality (𝑟=+ 0.051)."

## Discussion


## Related Claims
- [On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost](tei4-beats-dtr4-and-greedy-same-base.md) — related
- [GRPO pedagogical alignment of a reasoning LLM lowers actual student learning while raising judge-rated helpfulness (a multi-dimensional alignment tax)](grpo-pedagogical-alignment-tax-lowers-learning.md) — related

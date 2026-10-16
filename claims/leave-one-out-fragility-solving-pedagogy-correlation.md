---
type: claim
title: "The solving–pedagogy correlation is statistically fragile: leave-one-out Pearson correlations range from 0.251 to 0.887, rising to 0.887 when Qwen2.5-Math-7B-Instruct is removed"
description: "The solving–pedagogy correlation is statistically fragile: leave-one-out Pearson correlations range from 0.251 to 0.887, rising to 0.887 when Qwen2.5-Math-7B-Instruct is removed"
id: leave-one-out-fragility-solving-pedagogy-correlation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: junyi-yao-2026
    resource: "https://doi.org/10.48550/arxiv.2606.16206"
    title: "Junyi Yao, Zihao Zheng, and Baichuan Li. (2026). Beyond Helpfulness: A Teaching-over-Solving Diagnostic for Measuring Educational Impact in LLM Tutors. arXiv preprint. https://arxiv.org/abs/2606.16206 [doi:10.48550/arxiv.2606.16206](https://doi.org/10.48550/arxiv.2606.16206)"
    author: Junyi Yao, Zihao Zheng, and Baichuan Li
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# The solving–pedagogy correlation is statistically fragile: leave-one-out Pearson correlations range from 0.251 to 0.887, rising to 0.887 when Qwen2.5-Math-7B-Instruct is removed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`

## Subclaims
`q2 i?` A leave-one-out robustness check yields positive Pearson correlations in every seven-model subset (0.251–0.887), and removing Qwen2.5-Math-7B-Instruct raises the Pearson correlation to 0.887. [→ Junyi Yao 2026](#junyi-yao-2026)

## Evidence

### Junyi Yao 2026

Junyi Yao, Zihao Zheng, and Baichuan Li. (2026). Beyond Helpfulness: A Teaching-over-Solving Diagnostic for Measuring Educational Impact in LLM Tutors. arXiv preprint. https://arxiv.org/abs/2606.16206 [doi:10.48550/arxiv.2606.16206](https://doi.org/10.48550/arxiv.2606.16206)

`q2 · i?` · `associational · r?`

Robustness analysis within Study 1's reaggregation of the eight-model public MathTutorBench leaderboard. The authors conclude the sample is "statistically fragile" while the qualitative conclusion — that leaderboard rank can change materially between solving and pedagogy evaluation — remains.

> "A leave-one-out ro- bustness check yields positive Pearson correlations in every seven-model subset (0.251–0.887). Re- moving Qwen2.5-Math-7B-Instruct increases the Pearson correlation to 0.887, confirming that the public sample is statistically fragile"

## Discussion


## Related Claims
- [Solving-oriented and pedagogy-oriented composite scores on the public MathTutorBench leaderboard are only moderately correlated (Pearson 0.421, Spearman 0.690)](solving-pedagogy-composites-moderately-correlated-mathtutorbench.md) — related
- [Safety and Trustworthiness is strongly anti-correlated with Basic Education across the nine evaluated models (r = −0.83)](safety-basic-education-anticorrelation.md) — related

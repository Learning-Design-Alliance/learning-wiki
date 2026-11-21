---
type: claim
title: EasyMED closely matches human standardized patient behavior on SPBench (96.98 vs 97.33), while frontier LLMs show unstable case grounding and disclosure
description: EasyMED closely matches human standardized patient behavior on SPBench (96.98 vs 97.33), while frontier LLMs show unstable case grounding and disclosure
id: easymed-matches-human-sp-spubench
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: bingquan-zhang-2026
    resource: "https://doi.org/10.18653/v1/2026.acl-long.1243"
    title: "Bingquan Zhang, Xiaoxiao Liu, Yuchi Wang, Lei Zhou, Qianqian Xie, Benyou Wang. (2026). Human or LLM as Standardized Patients? A Comparative Study in Medical Education. arXiv preprint. Originally published 2025. [doi:10.18653/v1/2026.acl-long.1243](https://doi.org/10.18653/v1/2026.acl-long.1243)"
    author: Bingquan Zhang, Xiaoxiao Liu, Yuchi Wang, Lei Zhou, Qianqian Xie, Benyou Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# EasyMED closely matches human standardized patient behavior on SPBench (96.98 vs 97.33), while frontier LLMs show unstable case grounding and disclosure

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the SPBench evaluation, EasyMED scored 96.98 overall against a human SP reference of 97.33, with strongest gains on interaction-critical dimensions (CC, CD, CS, PD), while frontier LLMs showed larger variance on case consistency and controlled disclosure. [→ Bingquan Zhang 2026](#bingquan-zhang-2026)

## Evidence

### Bingquan Zhang 2026

Bingquan Zhang, Xiaoxiao Liu, Yuchi Wang, Lei Zhou, Qianqian Xie, Benyou Wang. (2026). Human or LLM as Standardized Patients? A Comparative Study in Medical Education. arXiv preprint. Originally published 2025. [doi:10.18653/v1/2026.acl-long.1243](https://doi.org/10.18653/v1/2026.acl-long.1243)

`q2 · i?` · `causal · r1`

Benchmark evaluation on SPBench comparing EasyMED, prompting-strategy baselines, and frontier LLMs against the human SP gold reference; scores per dimension are reported in Table 3, with EasyMED at "96.98" and human SP at "97.33".

> "Human standardized patients achieve the highest reference score (97.33), reflecting stable case portrayal and appropriate information disclosure across turns. EasyMED closely matches human performance (96.98), with strongest gains on interaction-critical dimensions (CC, CD, CS, PD)"

## Discussion


## Related Claims
- [Decoupling intent recognition from response generation (Auxiliary Agent) yields the largest gains on case consistency, controlled disclosure, and cross-turn stability](auxiliary-agent-architectural-control-gains.md) — related
- [In a four-week randomized crossover study, EasyMED training produced OSCE gains comparable to human SP training (16.89 vs 15.36 points)](easymed-comparable-osce-gains-human-sp.md) — related
- [EasyMED produced stronger early-phase gains for low-baseline (novice) learners than human SP training (21.83 vs 16.58 points)](easymed-stronger-novice-early-gains.md) — related

---
type: claim
title: Decoupling intent recognition from response generation (Auxiliary Agent) yields the largest gains on case consistency, controlled disclosure, and cross-turn stability
description: Decoupling intent recognition from response generation (Auxiliary Agent) yields the largest gains on case consistency, controlled disclosure, and cross-turn stability
id: auxiliary-agent-architectural-control-gains
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

# Decoupling intent recognition from response generation (Auxiliary Agent) yields the largest gains on case consistency, controlled disclosure, and cross-turn stability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` An ablation on SPBench attributes the largest gains on CC, CD, CS, and PD to the Auxiliary Agent, which maps learner queries to standardized clinical intents and constrains information access; these gains exceed those from prompt engineering alone. [→ Bingquan Zhang 2026](#bingquan-zhang-2026)

## Evidence

### Bingquan Zhang 2026

Bingquan Zhang, Xiaoxiao Liu, Yuchi Wang, Lei Zhou, Qianqian Xie, Benyou Wang. (2026). Human or LLM as Standardized Patients? A Comparative Study in Medical Education. arXiv preprint. Originally published 2025. [doi:10.18653/v1/2026.acl-long.1243](https://doi.org/10.18653/v1/2026.acl-long.1243)

`q2 · i?` · `causal · r1`

Ablation study on SPBench (Table 3) examining the Auxiliary Agent, which decouples intent recognition from response generation; the authors report the gains "exceed those from prompt engineering alone".

> "As shown in Table 3, this component yields the largest gains on CC, CD, CS, and PD. By mapping learner queries to stan- dardized clinical intents, the Auxiliary Agent pro- vides an explicit control signal that constrains infor- mation access"

## Discussion


## Related Claims
- [EasyMED closely matches human standardized patient behavior on SPBench (96.98 vs 97.33), while frontier LLMs show unstable case grounding and disclosure](easymed-matches-human-sp-spubench.md) — related
- [Chain-of-thought prompting modestly improves case consistency and completeness but reduces controlled disclosure](cot-prompting-reduces-controlled-disclosure.md) — related
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related

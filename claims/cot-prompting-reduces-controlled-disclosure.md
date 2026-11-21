---
type: claim
title: Chain-of-thought prompting modestly improves case consistency and completeness but reduces controlled disclosure
description: Chain-of-thought prompting modestly improves case consistency and completeness but reduces controlled disclosure
id: cot-prompting-reduces-controlled-disclosure
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
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

# Chain-of-thought prompting modestly improves case consistency and completeness but reduces controlled disclosure

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Using a fixed Gemini 2.5 Pro backbone, CoT prompting modestly increased CC and RC but amplified verbosity and unsolicited explanation, reducing CD scores on SPBench. [→ Bingquan Zhang 2026](#bingquan-zhang-2026)

## Evidence

### Bingquan Zhang 2026

Bingquan Zhang, Xiaoxiao Liu, Yuchi Wang, Lei Zhou, Qianqian Xie, Benyou Wang. (2026). Human or LLM as Standardized Patients? A Comparative Study in Medical Education. arXiv preprint. Originally published 2025. [doi:10.18653/v1/2026.acl-long.1243](https://doi.org/10.18653/v1/2026.acl-long.1243)

`q2 · i?` · `causal · r1`

Prompting-strategy sensitivity experiment on SPBench using a fixed Gemini 2.5 Pro backbone, comparing CoT against a unified prompting scheme; the article reports no test statistics, only directional score changes.

> "CoT prompting improves reasoning transparency and modestly increases CC and RC. However, it also amplifies verbosity and unsolicited explanation, leading to reduced CD scores."

## Discussion


## Related Claims
- [Decoupling intent recognition from response generation (Auxiliary Agent) yields the largest gains on case consistency, controlled disclosure, and cross-turn stability](auxiliary-agent-architectural-control-gains.md) — related
- [Prompting technique effects are task-dependent: few-shot and self-consistency help, while chain-of-thought helps praise detection but hurts error recognition](prompting-techniques-task-dependent-tutor-moves.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related

---
type: claim
title: A small question budget of about 200 suffices for strong hypothesis quality, with room to scale
description: A small question budget of about 200 suffices for strong hypothesis quality, with room to scale
id: small-budget-suffices-for-hypothesis-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: peng-cui-2026
    resource: "https://arxiv.org/abs/2610.01627"
    title: "Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627"
    author: Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# A small question budget of about 200 suffices for strong hypothesis quality, with room to scale

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` With a suitable sampling and prompting strategy, the method reaches a good level of performance within 200 questions and retains potential to scale further, as none of the mixed-strategy curves has fully converged. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627

`q2 · i?` · `causal · r1`

Budget analysis tied to the Figure 4 sampling ablations, treating question numbers as a proxy for the annotation budget. The article reports good performance "within200 questions" and unconverged mixed-strategy curves.

> "Overall, with a suitable sampling and prompting strategy, our method reaches a good level of performance within200 questions (a proxy for the annotation budget) and retains the potential to scale further when the budget allows, as none of the mixed-strategy curves in Figure 4 has fully converged."

## Discussion


## Related Claims
- [Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone](mixing-group-and-pair-sampling-beats-either-alone.md) — related
- [Baseline hypothesis generators saturate after 5–10 effective hypotheses while the proposed method keeps improving](baseline-generators-saturate-proposed-method-keeps-improving.md) — related

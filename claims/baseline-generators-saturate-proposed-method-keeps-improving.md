---
type: claim
title: Baseline hypothesis generators saturate after 5–10 effective hypotheses while the proposed method keeps improving
description: Baseline hypothesis generators saturate after 5–10 effective hypotheses while the proposed method keeps improving
id: baseline-generators-saturate-proposed-method-keeps-improving
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
    kind: design
    rigour: 2
---

# Baseline hypothesis generators saturate after 5–10 effective hypotheses while the proposed method keeps improving

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Baseline generators yield only 5–10 effective hypotheses beyond which adjusted R² declines, whereas the proposed method keeps producing informative hypotheses and achieves the best fit at most hypothesis budgets. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627

`q2 · i?` · `design · r2`

In-sample evaluation (Figure 2): OLS regression of item difficulty on hypothesis features across hypothesis budgets 1–20 on three datasets. The article reports that baselines "saturate quickly" while the proposed method keeps producing informative hypotheses.

> "The results are present in Figure 2, where our method achieves the best fit at most hypothesis budgets on three datasets. More importantly, the baselines saturate quickly: they yield only 5–10 effective hypotheses, beyond which adjustedR 2 declines, indicating that the additional hypotheses carry noise rather than real signal."

## Discussion


## Related Claims
- [Adding generated hypotheses as features improves black-box difficulty predictors](hypothesis-features-improve-difficulty-predictors.md) — related
- [Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone](mixing-group-and-pair-sampling-beats-either-alone.md) — related
- [A small question budget of about 200 suffices for strong hypothesis quality, with room to scale](small-budget-suffices-for-hypothesis-quality.md) — related

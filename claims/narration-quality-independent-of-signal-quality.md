---
type: claim
title: "Narration fluency is no evidence of correctness: narration quality is independent of signal quality"
description: "Narration fluency is no evidence of correctness: narration quality is independent of signal quality"
id: narration-quality-independent-of-signal-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: chenguang-pan-2026
    resource: "https://arxiv.org/abs/2608.21165"
    title: "Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165"
    author: Chenguang Pan, Airui Meng, and Youmi Suk
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Narration fluency is no evidence of correctness: narration quality is independent of signal quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Narration faithfulness metrics (grounding audit, self-closure, uniqueness) remain near 1 across all simulation conditions regardless of whether the upstream signal is true or noisy, showing that fluent, internally consistent text does not indicate correct predictions. [→ Chenguang Pan 2026](#chenguang-pan-2026)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Airui Meng, and Youmi Suk. (2026). Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics. arXiv. https://arxiv.org/abs/2608.21165

`q2 · i?` · `design · r2`

Simulation study narration faithfulness dimension across all four cells of the 2-by-2 design. "The metrics under narration faithfulness are close to 1." Grounding audit for the mentee reaches 0.998 in all conditions and self-closure reaches 0.995–0.999, even when point estimation is poor (r = 0.72).

> "The metrics under narration faithfulness are close to 1, which shows that the mentee learns to write arithmetically closed decompositions and that the non-hallucinated narrations are essentially preserved."

## Discussion


## Related Claims
- [Mentee fidelity on HSLS:09 test split: attribution transmits far better than decisions, and 98.8% of narrations pass the faithfulness audit](hsls-mentee-fidelity-attribution-better-than-decisions.md) — related
- [Under a realistic estimator, remaining error originates upstream rather than from the distillation step](estimator-loss-dominates-llm-distillation-error.md) — related

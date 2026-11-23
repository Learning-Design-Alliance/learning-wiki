---
type: claim
title: "An instance-level adaptive curriculum that promotes problems upon reaching 50% accuracy improves sample efficiency and prevents performance plateaus"
description: "An instance-level adaptive curriculum that promotes problems upon reaching 50% accuracy improves sample efficiency and prevents performance plateaus"
id: instance-level-curriculum-sample-efficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: justin-chih-yao-chen-2026
    resource: "https://doi.org/10.48550/arXiv.2604.04767"
    title: "Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)"
    author: Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# An instance-level adaptive curriculum that promotes problems upon reaching 50% accuracy improves sample efficiency and prevents performance plateaus

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` With the instance-level curriculum, the proportion of 4-choice MCQ steadily decreases, intermediate formats rise then decline, and open-ended questions grow, with continued test-performance improvements, whereas a static uniform 25%-each mixture plateaus. [→ Justin Chih-Yao Chen 2026](#justin-chih-yao-chen-2026)

## Evidence

### Justin Chih-Yao Chen 2026

Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)

`q2 · i?` · `causal · r2`

Section 6, Figure 4: training-dynamics comparison with and without the instance-level curriculum, where each instance advances to the next difficulty level once its average accuracy exceeds 50%. Test accuracy is reported on open-ended questions from OmniMATH-Hard over training steps.

> "Importantly, the curriculum leads to continued improvements in test performance on OmniMATH-Hard, whereas performance without the curriculum tends to plateau."

## Discussion


## Related Claims
- [An adaptive curriculum targeting the policy's measured weaknesses raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates](adaptive-curriculum-improves-shift-income.md) — related
- [Reformulating hard open-ended problems into MCQ or cloze formats reduces empirical difficulty, with a consistent ordering MCQ4 ≤ MCQ10 ≤ Cloze ≤ Open-ended](reformulation-reduces-difficulty-ordering.md) — related
- Under tailored curriculum learning, the proportion of harder training data rises from 0% in stage one to 34.6% in stage two and 55.1% in stage three — related
- [Exposure to a diverse mixture of reformulations is critical for transfer; single-format training does not improve over no training](reformulation-diversity-critical.md) — related

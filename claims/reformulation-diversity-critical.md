---
type: claim
title: Exposure to a diverse mixture of reformulations is critical for transfer; single-format training does not improve over no training
description: Exposure to a diverse mixture of reformulations is critical for transfer; single-format training does not improve over no training
id: reformulation-diversity-critical
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

# Exposure to a diverse mixture of reformulations is critical for transfer; single-format training does not improve over no training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` RFT on a single reformulation does not improve over no training, while training on 4-MCQ + Cloze without any open-ended data achieves gains comparable to mixtures including open-ended problems (18.36 vs 18.42 on OmniMATH-Hard). [→ Justin Chih-Yao Chen 2026](#justin-chih-yao-chen-2026)

## Evidence

### Justin Chih-Yao Chen 2026

Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)

`q2 · i?` · `causal · r2`

Section 6, Table 2: RFT on various data mixtures evaluated on OmniMATH-Hard and MATH500. Single formats (OEQ 14.16, 4-MCQ 14.82, Cloze 16.15) do not beat no training (15.67), while 4-MCQ + Cloze reaches 18.36. The authors conclude "diversity in problem representation is critical for effective transfer."

> "The first three rows show that training with a single reformulation does not improve over no training. Notably, train- ing solely on4 Choice + Clozewithout any open-ended data achieves improved perfor- mance, and it is comparable to mixtures that include open-ended problems."

## Discussion


## Related Claims
- [An instance-level adaptive curriculum that promotes problems upon reaching 50% accuracy improves sample efficiency and prevents performance plateaus](instance-level-curriculum-sample-efficiency.md) — related
- [Learning from reformulated problems transfers back to original open-ended hard problems, and more generative formats transfer better](reformulation-transfers-back-to-open-ended.md) — related
- [Training on reformulated hard problems improves pass@k at test time, suggesting acquisition of new reasoning capabilities](cog-drift-improves-passk.md) — related
- [Reformulating hard open-ended problems into MCQ or cloze formats reduces empirical difficulty, with a consistent ordering MCQ4 ≤ MCQ10 ≤ Cloze ≤ Open-ended](reformulation-reduces-difficulty-ordering.md) — related

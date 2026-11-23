---
type: claim
title: TnD-based corrective feedback enables knowledge distillation to smaller student models, which outperform same-size CLM baselines
description: TnD-based corrective feedback enables knowledge distillation to smaller student models, which outperform same-size CLM baselines
id: tnd-distills-to-smaller-students
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ziqiao-ma-2025
    resource: "https://doi.org/10.18653/v1/2025.naacl-long.46"
    title: "Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. [doi:10.18653/v1/2025.naacl-long.46](https://doi.org/10.18653/v1/2025.naacl-long.46)"
    author: Ziqiao Ma, Zekun Wang, Joyce Chai
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# TnD-based corrective feedback enables knowledge distillation to smaller student models, which outperform same-size CLM baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Smaller student models (d = 588, 360, 250) trained with TnD outperform CLM baselines of the same size and even surpass larger CLM baselines in early training steps. [→ Ziqiao Ma 2025](#ziqiao-ma-2025)

## Evidence

### Ziqiao Ma 2025

Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. [doi:10.18653/v1/2025.naacl-long.46](https://doi.org/10.18653/v1/2025.naacl-long.46)

`q2 · i?` · `causal · r2`

Experiments keeping all setups unchanged but reducing student GPT-2 dimension to 588, 360, and 250 (Fig. 6). The authors report "Each TnD model outperforms the CLM baseline of the same size and even surpasses CLM baselines of large capacity in early steps."

> "Each TnD model outperforms the CLM baseline of the same size and even surpasses CLM baselines of large capacity in early steps."

## Discussion


## Related Claims
- [TnD interactive learning with corrective feedback speeds word acquisition, especially in earlier training stages](tnd-accelerates-neural-word-acquisition.md) — related
- [Distilling a multi-order hierarchical teacher into a smaller zeroth-order student lets the student outperform the teacher, and improves 4.1 percentage points in accuracy over STGCN++](distilled-student-outperforms-multiorder-teacher.md) — related
- [Both trials and demonstrations contribute to accelerated word learning: demonstrations alone help, trials alone do not](trials-and-demonstrations-both-needed.md) — related

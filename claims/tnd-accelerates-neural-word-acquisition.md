---
type: claim
title: TnD interactive learning with corrective feedback speeds word acquisition, especially in earlier training stages
description: TnD interactive learning with corrective feedback speeds word acquisition, especially in earlier training stages
id: tnd-accelerates-neural-word-acquisition
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
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

# TnD interactive learning with corrective feedback speeds word acquisition, especially in earlier training stages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Student models trained with the TnD framework acquire words faster than CLM baselines, with the benefit concentrated in earlier stages of word acquisition. [→ Ziqiao Ma 2025](#ziqiao-ma-2025)

## Evidence

### Ziqiao Ma 2025

Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. [doi:10.18653/v1/2025.naacl-long.46](https://doi.org/10.18653/v1/2025.naacl-long.46)

`q2 · i?` · `causal · r2`

Controlled computational experiments on BookCorpus and BabyLM with 5 random seeds per baseline, evaluating CMN and CDI word sets via learning curves, nAoA, and effective vocabulary size. The authors report the TnD framework "significantly outperforms the CLM baseline on nAoA@0.50" (Fig. 3, Fig. 4, Table 1).

> "We find that the TnD learning framework is particularly beneficial during the earlier stages of word acquisition, as it significantly outperforms the CLM baseline on nAoA@0.50"

## Discussion


## Related Claims
- [A teacher's word choices in demonstrations affect students' word-specific learning efficiency: masking words from demonstrations slows their acquisition](teacher-word-choices-affect-student-acquisition.md) — related
- [Both trials and demonstrations contribute to accelerated word learning: demonstrations alone help, trials alone do not](trials-and-demonstrations-both-needed.md) — related
- [TnD-based corrective feedback enables knowledge distillation to smaller student models, which outperform same-size CLM baselines](tnd-distills-to-smaller-students.md) — related

---
type: claim
title: "Both trials and demonstrations contribute to accelerated word learning: demonstrations alone help, trials alone do not"
description: "Both trials and demonstrations contribute to accelerated word learning: demonstrations alone help, trials alone do not"
id: trials-and-demonstrations-both-needed
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
  - id: ziqiao-ma-2025-2
    resource: "https://doi.org/10.18653/v1/2025.naacl-long.46"
    title: "Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. [doi:10.18653/v1/2025.naacl-long.46](https://doi.org/10.18653/v1/2025.naacl-long.46)"
    author: Ziqiao Ma, Zekun Wang, Joyce Chai
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Both trials and demonstrations contribute to accelerated word learning: demonstrations alone help, trials alone do not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` With only teacher demonstrations, the student model acquires words faster than with the plain CLM baseline alone. [→ Ziqiao Ma 2025](#ziqiao-ma-2025)
`q2 i?` Without the teacher's demonstrations, the student's trials alone yield performance comparable to the CLM baseline. [→ Ziqiao Ma 2025 (2)](#ziqiao-ma-2025-2)

## Evidence

### Ziqiao Ma 2025

Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. [doi:10.18653/v1/2025.naacl-long.46](https://doi.org/10.18653/v1/2025.naacl-long.46)

`q2 · i?` · `causal · r2`

Ablation study comparing CLM, TnD, Trial-only, and Demo-only variants across two corpora with 5 seeds each. The authors report that "With only teacher demonstrations, the student model acquires words faster than with the plainCLM baseline alone."

> "With only teacher demonstrations, the student model acquires words faster than with the plainCLM baseline alone"

### Ziqiao Ma 2025 (2)

Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. [doi:10.18653/v1/2025.naacl-long.46](https://doi.org/10.18653/v1/2025.naacl-long.46)

`q2 · i?` · `causal · r2`

Same controlled ablation study across two corpora and two test vocabularies with 5 random seeds. The authors find that trials without demonstrations result in "performance comparable to the CLM baseline."

> "Conversely, without the teacher's demonstrations, the student's trials in the wild do not yield a marked improvement, resulting in performance comparable to the CLM baseline."

## Discussion


## Related Claims
- [TnD interactive learning with corrective feedback speeds word acquisition, especially in earlier training stages](tnd-accelerates-neural-word-acquisition.md) — related
- [TnD-based corrective feedback enables knowledge distillation to smaller student models, which outperform same-size CLM baselines](tnd-distills-to-smaller-students.md) — related

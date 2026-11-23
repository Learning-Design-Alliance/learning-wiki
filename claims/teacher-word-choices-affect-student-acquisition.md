---
type: claim
title: "A teacher's word choices in demonstrations affect students' word-specific learning efficiency: masking words from demonstrations slows their acquisition"
description: "A teacher's word choices in demonstrations affect students' word-specific learning efficiency: masking words from demonstrations slows their acquisition"
id: teacher-word-choices-affect-student-acquisition
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

# A teacher's word choices in demonstrations affect students' word-specific learning efficiency: masking words from demonstrations slows their acquisition

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Excluding 40 words per test vocabulary from teacher demonstrations leads to higher nAoA (slower learning) for those words, though students eventually learn them from the corpus and their own trials. [→ Ziqiao Ma 2025](#ziqiao-ma-2025)

## Evidence

### Ziqiao Ma 2025

Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. [doi:10.18653/v1/2025.naacl-long.46](https://doi.org/10.18653/v1/2025.naacl-long.46)

`q2 · i?` · `causal · r2`

Experiment repeating training with a set of 40 words per test vocabulary excluded from teacher demonstrations (Fig. 7, Table 2), 5 random seeds. The authors find "The absence of words from teacher demonstrations leads to slower learning speed for student models."

> "The absence of words from teacher demonstrations leads to slower learning speed for student models, as evidenced by a higher nAoA"

## Discussion


## Related Claims
- [TnD interactive learning with corrective feedback speeds word acquisition, especially in earlier training stages](tnd-accelerates-neural-word-acquisition.md) — related
- [Intentional vocabulary learning yields higher, faster gains and better retention than incidental learning through reading](intentional-beats-incidental-vocabulary-gains.md) — related
- [The more often learners meet a word while reading, the more likely they are to learn it incidentally; a meta-analysis of correlational studies finds a moderate correlation](exposure-frequency-predicts-incidental-gains.md) — a broader claim this one bears on

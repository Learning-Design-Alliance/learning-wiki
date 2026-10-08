---
type: claim
title: "Using only teachers' utterances as input achieves comparable or better PLM performance than including student utterances, even for student-oriented observation variables"
description: "Using only teachers' utterances as input achieves comparable or better PLM performance than including student utterances, even for student-oriented observation variables"
id: teacher-utterances-alone-sufficient-for-classroom-measures
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: paiheng-xu-2024
    resource: "https://aclanthology.org/volumes/2024.naacl-long/"
    title: "Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/"
    author: Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Using only teachers' utterances as input achieves comparable or better PLM performance than including student utterances, even for student-oriented observation variables

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the NCTE MQI variables, models using only teacher utterances achieve comparable and even better results than transcript-format input including student utterances, including for the student-oriented variable STEXPL. [→ Paiheng Xu 2024](#paiheng-xu-2024)

## Evidence

### Paiheng Xu 2024

Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/

`q2 · i?` · `design · r2`

Comparison of two input formats on the NCTE test set: teacher utterances only (Table 4) versus transcript format including student utterances (Table 5). With teacher-only input STEXPL reached Spearman 0.35±0.01 versus 0.37±0.02 with student talk included; the authors report "comparable and even better re- sults for all MQI variables."

> "utterances achieves comparable and even better re- sults for all MQI variables, despite ignoring student utterances. This is particularly interesting for the student-oriented variables (e.g., STEXPL)"

## Discussion


## Related Claims
- [Class-weighted loss marginally improves PLM performance on skewed instruction-quality ratings, achieving best performance on 10 of 16 variables in the three-way setting and 9 of 16 in the binary setting](class-weighted-loss-marginal-gain-skewed-teaching-ratings.md) — related
- [Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones](plm-performance-depends-on-pedagogical-expertise-required.md) — related
- [A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences](two-stage-relevance-strategy-helps-multi-sentence-variables.md) — related

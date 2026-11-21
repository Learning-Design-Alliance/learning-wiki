---
type: claim
title: The unsupervised forwards-range measure correlates negatively with human labels on the UNFILTERED set (ρ = -.130) and positively on the FILTERED set (ρ = .159)
description: The unsupervised forwards-range measure correlates negatively with human labels on the UNFILTERED set (ρ = -.130) and positively on the FILTERED set (ρ = .159)
id: forwards-range-unsupervised-correlations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: sterling-alic-2022
    resource: "https://doi.org/10.18653/v1/2022.bea-1.27"
    title: "Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. [doi:10.18653/v1/2022.bea-1.27](https://doi.org/10.18653/v1/2022.bea-1.27)"
    author: Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The unsupervised forwards-range measure correlates negatively with human labels on the UNFILTERED set (ρ = -.130) and positively on the FILTERED set (ρ = .159)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Forwards-range shows a significant negative correlation with human judgments on UNFILTERED and a significant positive correlation on FILTERED, supporting the assumption that focusing questions receive a greater variety of student responses. [→ Sterling Alic 2022](#sterling-alic-2022)

## Evidence

### Sterling Alic 2022

Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. [doi:10.18653/v1/2022.bea-1.27](https://doi.org/10.18653/v1/2022.bea-1.27)

`q2 · i?` · `associational · r2`

Unsupervised evaluation on the annotated NCTE sample. The results section reports the sign flip across datasets and states the positive FILTERED correlation "validates our assumption that focusing questions receive a greater variety of student responses."

> "The forwards-range has a signiﬁcant negative correlation for the UNFILTERED set (ρ =−.130), but it changes to a signiﬁcant positive correlation for the FILTERED set (ρ = .159)."

## Discussion


## Related Claims
- [The question words \"why\", \"how do\", and \"what else\" correlate positively with focusing labels while \"when\" correlates negatively on the FILTERED set](question-word-lexical-patterns-focusing.md) — related
- [A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set](roberta-funneling-focusing-correlation-761.md) — related
- [Manual quality filtering retained 528 of 2,500 forum question/answer pairs (21%), and an earlier unfiltered fine-tune (FT1) suffered prohibitive quality issues](forum-finetune-manual-filtering-21-percent.md) — related

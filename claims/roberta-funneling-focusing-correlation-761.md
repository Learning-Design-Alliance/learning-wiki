---
type: claim
title: A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set
description: A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set
id: roberta-funneling-focusing-correlation-761
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
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

# A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The RoBERTa model trained on the UNFILTERED dataset correlates .761 with averaged human expert labels for identifying funneling and focusing questions. [→ Sterling Alic 2022](#sterling-alic-2022)

## Evidence

### Sterling Alic 2022

Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. [doi:10.18653/v1/2022.bea-1.27](https://doi.org/10.18653/v1/2022.bea-1.27)

`q2 · i?` · `associational · r2`

Evaluation of supervised models on the authors' annotated NCTE transcript sample. The results section reports that RoBERTa models show "a strong positive Spearman correlation with human expert labels" of ρ = .761 (UNFILTERED) and ρ = .443 (FILTERED).

> "We ﬁnd that the RoBERTa models have a strong positive Spearman correlation with human expert labels both on the UNFILTERED (ρ = .761) and the FILTERED (ρ = .443) sets."

## Discussion


## Related Claims
- [The question words \"why\", \"how do\", and \"what else\" correlate positively with focusing labels while \"when\" correlates negatively on the FILTERED set](question-word-lexical-patterns-focusing.md) — related
- [The unsupervised forwards-range measure correlates negatively with human labels on the UNFILTERED set (ρ = -.130) and positively on the FILTERED set (ρ = .159)](forwards-range-unsupervised-correlations.md) — related
- [Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness](supervised-models-competitiveness-uptake.md) — related
- [RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction](roberta-classifiers-discourse-moves-moderate-high-accuracy.md) — related

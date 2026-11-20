---
type: claim
title: All classifier-predicted discourse features correlate significantly with classroom observation scores measuring instruction quality and classroom climate
description: All classifier-predicted discourse features correlate significantly with classroom observation scores measuring instruction quality and classroom climate
id: discourse-features-correlate-observation-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: dorottya-demszky-and-heather-hill-2023
    resource: "https://doi.org/10.18653/v1/2023.bea-1.44"
    title: "Dorottya Demszky and Heather Hill. (2023). The NCTE Transcripts: A Dataset of Elementary Math Classroom Transcripts. Originally published 2022. [doi:10.18653/v1/2023.bea-1.44](https://doi.org/10.18653/v1/2023.bea-1.44)"
    author: Dorottya Demszky and Heather Hill
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# All classifier-predicted discourse features correlate significantly with classroom observation scores measuring instruction quality and classroom climate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Predictions for all annotated discourse moves correlate significantly with each classroom observation item (MQI math instruction quality and CLASS instructional dialogue, teacher sensitivity, regard for student perspectives, positive climate), controlling for teacher and classroom covariates. [→ Dorottya Demszky and Heather Hill 2023](#dorottya-demszky-and-heather-hill-2023)

## Evidence

### Dorottya Demszky and Heather Hill 2023

Dorottya Demszky and Heather Hill. (2023). The NCTE Transcripts: A Dataset of Elementary Math Classroom Transcripts. Originally published 2022. [doi:10.18653/v1/2023.bea-1.44](https://doi.org/10.18653/v1/2023.bea-1.44)

`q2 · i?` · `associational · r2`

Regression analysis (Table 5) predicting five observation items from lesson-level discourse move predictions, with teacher and classroom demographic covariates and standard errors clustered at the teacher level. The article reports "all discourse features predicted by our classifiers correlate significantly" with the observation items.

> "We find that all discourse features predicted by our classifiers correlate significantly with each classroom observation item measuring instruction quality and classroom climate."

## Discussion


## Related Claims
- [RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction](roberta-classifiers-discourse-moves-moderate-high-accuracy.md) — related
- [RoBERTa model outputs correlate significantly with math instruction quality scores and with teacher value-added scores](roberta-measure-correlates-educational-outcomes.md) — related
- [Baseline student talk ratios do not correlate with observation scores or value-added scores, with student word percentage correlating with instructional dialogue as the exception](student-talk-ratios-null-correlation.md) — related
- [Dialogic discourse moves (uptake, focusing questions, student reasoning) correlate positively with teachers' value-added scores](dialogic-moves-correlate-value-added.md) — related
- [Dialogue act features raise regression R² but do not significantly improve outcome prediction over a prior-performance baseline](da-features-not-significant-over-baseline.md) — related
- [Connecting, the least frequent talk move, correlates most positively with attendance, section ratings, and assignment completion](connecting-talk-move-most-positive-correlation.md) — related

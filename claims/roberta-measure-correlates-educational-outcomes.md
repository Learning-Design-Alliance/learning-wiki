---
type: claim
title: RoBERTa model outputs correlate significantly with math instruction quality scores and with teacher value-added scores
description: RoBERTa model outputs correlate significantly with math instruction quality scores and with teacher value-added scores
id: roberta-measure-correlates-educational-outcomes
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

# RoBERTa model outputs correlate significantly with math instruction quality scores and with teacher value-added scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Aggregated RoBERTa model outputs show significant positive correlations with MQI observation scores, student participation in meaning-making, students providing explanations, and value-added scores. [→ Sterling Alic 2022](#sterling-alic-2022)

## Evidence

### Sterling Alic 2022

Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. [doi:10.18653/v1/2022.bea-1.27](https://doi.org/10.18653/v1/2022.bea-1.27)

`q2 · i?` · `associational · r2`

OLS regressions of transcript-aggregated model outputs on MQI observation scores and teacher-level value-added scores, controlling for the number of student-teacher exchanges. Table 4 reports RoBERTa (filtered) at 0.388 for participation and 0.124* for value-added (N=304).

> "We ﬁnd that there is a positive linear correlation of the RoBERTa model output scores with all three educational outcome scores for the NCTE dataset."

## Discussion


## Related Claims
- [Observation scores are modestly positively associated with individual value-added (adjusted correlation 0.349) but only weakly associated with performance tasks (0.108) and school-wide literacy value-added (0.119)](reach-observation-value-added-correlation-0349.md) — related
- [All seven dimensions of instructional practice with quantitative data are modestly but significantly related to teachers' value-added scores](observation-dimensions-modestly-significantly-related-to-value-added.md) — related
- [All classifier-predicted discourse features correlate significantly with classroom observation scores measuring instruction quality and classroom climate](discourse-features-correlate-observation-scores.md) — related

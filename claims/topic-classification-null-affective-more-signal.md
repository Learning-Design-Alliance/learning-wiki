---
type: claim
title: Zero-shot classification of concern topics showed no consistent evidence of association with wearable outcomes, while affective dimensions showed more associations that did not survive correction
description: Zero-shot classification of concern topics showed no consistent evidence of association with wearable outcomes, while affective dimensions showed more associations that did not survive correction
id: topic-classification-null-affective-more-signal
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: topic-null
    title: topic-null
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: affective-more
    title: affective-more
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Zero-shot classification of concern topics showed no consistent evidence of association with wearable outcomes, while affective dimensions showed more associations that did not survive correction

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r2` · `q2`

## Subclaims
`q2 i?` Zero-shot classification of concern topics showed no consistent evidence of association with wearable outcomes. [→ topic-null](#topic-null)
`q2 i?` Affective dimensions across all three methods showed more associations than topical content, though these did not survive correction for multiple comparisons, offering preliminary evidence that emotional register may carry more signal than topical content. [→ affective-more](#affective-more)

## Evidence

### topic-null

Tamunotonye Harry, Johanna Hidalgo, Matthew Price, Yuanyuan Feng, Kathryn Stanton, Connie Tompkins, Peter Sheridan Dodds, Mikaela Irene Fudolig, Laura Bloomfield, and Christopher Danforth. 2026. A Formative Study of Brief Affective Text as a Complement to Wearable Sensing for Longitudinal Student Health Monitoring. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 10, 4, Article 219 (December 2026). https://arxiv.org/abs/2605.14360

`q2 · i?` · `associational · r2`

Zero-shot domain classification (facebook/bart-large-mnli against nine candidate domain labels) entered as continuous predictors in within-person mixed-effects models of the nine wearable outcomes. The article reports "Zero-shot classification of concern topics showed no consistent evidence of association with outcomes". No effect sizes are printed.

> "Zero-shot classification of concern topics showed no consistent evidence of association with outcomes;"

### affective-more

Tamunotonye Harry, Johanna Hidalgo, Matthew Price, Yuanyuan Feng, Kathryn Stanton, Connie Tompkins, Peter Sheridan Dodds, Mikaela Irene Fudolig, Laura Bloomfield, and Christopher Danforth. 2026. A Formative Study of Brief Affective Text as a Complement to Wearable Sensing for Longitudinal Student Health Monitoring. Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 10, 4, Article 219 (December 2026). https://arxiv.org/abs/2605.14360

`q2 · i?` · `associational · r2`

Cross-method comparison of affective features (SEANCE, RoBERTa-base, MentalRoBERTa) against zero-shot topical domain probabilities in the same within-person models. The article states "affective dimensions across all three methods showed more associations" than topics, but "these did not survive correction for multiple comparisons". No effect sizes are printed.

> "affective dimensions across all three methods showed more associations, though these did not survive correction for multiple comparisons, offering preliminary evidence that emotional register may carry more signal than topical content."

## Discussion


## Related Claims
- [Dictionary-based SEANCE features yielded 21 nominally significant within-person associations with wearable outcomes, but none survived Bonferroni or FDR correction](seance-nominal-associations-no-survivors.md) — related
- [Forceful, assertive concern language was associated with fewer steps per day and lower moderate-intensity activity, while work-oriented language was positively associated with steps](forceful-language-lower-activity-association.md) — related
- [Brief naturalistic concern text associates with within-person variation in wearable-derived sleep and physical activity outcomes across a full academic year, even at a median response length of three words](brief-concern-text-associates-within-person-wearable-outcomes.md) — reports the opposite
- [In a preliminary functional assessment with simulated inputs, Sukoon identified the correct stress tier for exam, family, financial and teacher-related concerns and replied appropriately within its Stepped Care framework, but no formal user study has been conducted](preliminary-chatbot-evaluation-simulated-inputs-three-tiers.md) — related

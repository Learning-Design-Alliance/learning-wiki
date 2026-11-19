---
type: claim
title: "PJSD correlates significantly with educational outcomes across three datasets, while %-IN-T fails in the written one-on-one tutoring setting"
description: "PJSD correlates significantly with educational outcomes across three datasets, while %-IN-T fails in the written one-on-one tutoring setting"
id: pjsd-correlates-educational-outcomes-three-datasets
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: mixed
newest_evidence: 2021
sources:
  - id: dorottya-demszky-2021
    resource: "https://doi.org/10.18653/v1/2021.acl-long.130"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: dorottya-demszky-2021-2
    resource: "https://doi.org/10.18653/v1/2021.acl-long.130"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# PJSD correlates significantly with educational outcomes across three datasets, while %-IN-T fails in the written one-on-one tutoring setting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` PJSD correlates significantly with all outcome measures across NCTE, SimTeacher and tutoring datasets; %-IN-T shows no significant correlation in the tutoring dataset. [→ Dorottya Demszky 2021](#dorottya-demszky-2021)
`q2 i?` In the tutoring dataset, dialogs where PJSD outperforms %-IN-T in predicting student ratings have more teacher questions (p<0.05) and exclamation marks (p<0.01). [→ Dorottya Demszky 2021 (2)](#dorottya-demszky-2021-2)

## Evidence

### Dorottya Demszky 2021

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `associational · r2`

Downstream correlational analysis across three datasets (NCTE classroom observations, a written one-on-one tutoring dataset of 4604 sessions, and 338 SimTeacher simulation sessions), using OLS regressions of conversation-level outcomes on uptake scores controlling for the number of scored pairs. Reported z-scored coefficients include PJSD β=.069 for student satisfaction versus %-IN-T β=.00885, and the SimTeacher correlation is highlighted because "PJSD was not ﬁne-tuned on this dataset".

> "The signiﬁcant correlation of PJSD with the outcome in case of SimTeacher is especially noteworthy because PJSD was not ﬁne-tuned on this dataset (Section 5.1); this provides evidence for the adaptability of a pre-trained model to other (similar) datasets."

### Dorottya Demszky 2021 (2)

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `design · r2`

Follow-up analysis on the tutoring dataset using coarse cues of teacher responsiveness: the authors compared the ratio of teacher question marks and exclamation marks in dialogs where PJSD beat %-IN-T at predicting student ratings, finding higher ratios for both cues (p<0.05 and p<0.01).

> "dialogs wherePJSD outperforms %-IN-T, in terms of predicting student rat-ings, have a higher ratio of exchanges with teacher questions (p < 0.05, obtained from two-sample t-test) and teacher exclamation marks (p< 0.01)."

## Discussion


## Related Claims
- [PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T](pjsd-captures-uptake-phenomena-switchboard.md) — related
- [PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations](pjsd-outperforms-repetition-baseline-uptake.md) — related
- [AI tutor benchmark datasets show essentially no correlation between chatbot scaffolding and student uptake](no-scaffolding-uptake-correlation-in-benchmarks.md) — related

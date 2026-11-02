---
type: claim
title: "Symbolic-regression models built on previous exam grades account for roughly 70% of exam-score variation, but predict project scores poorly (about 35%)"
description: "Symbolic-regression models built on previous exam grades account for roughly 70% of exam-score variation, but predict project scores poorly (about 35%)"
id: exam-scores-predictable-project-scores-not
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-02
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: fedor-duzhin-and-anders-gustafsson-2018
    resource: "https://doi.org/10.3390/educsci8010007"
    title: "Fedor Duzhin and Anders Gustafsson. (2018). Machine Learning-Based App for Self-Evaluation of Teacher-Specific Instructional Style and Tools. Educ. Sci. 2018, 8, 7. https://doi.org/10.3390/educsci8010007"
    author: Fedor Duzhin and Anders Gustafsson
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: fedor-duzhin-and-anders-gustafsson-2018-2
    resource: "https://doi.org/10.3390/educsci8010007"
    title: "Fedor Duzhin and Anders Gustafsson. (2018). Machine Learning-Based App for Self-Evaluation of Teacher-Specific Instructional Style and Tools. Educ. Sci. 2018, 8, 7. https://doi.org/10.3390/educsci8010007"
    author: Fedor Duzhin and Anders Gustafsson
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Symbolic-regression models built on previous exam grades account for roughly 70% of exam-score variation, but predict project scores poorly (about 35%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Predictive models for the ODE final exam from prior Calculus and Linear Algebra grades had error 1 − R² ≈ 0.47 (R ≈ 0.73), accounting for more than 70% of exam-score variation. [→ Fedor Duzhin and Anders Gustafsson 2018](#fedor-duzhin-and-anders-gustafsson-2018)
`q2 i?` A model predicting the 2016 team project score from prior grades was unsuccessful, with 1 − R² = 0.88, accounting for only 35% of project-score variation. [→ Fedor Duzhin and Anders Gustafsson 2018 (2)](#fedor-duzhin-and-anders-gustafsson-2018-2)

## Evidence

### Fedor Duzhin and Anders Gustafsson 2018

Fedor Duzhin and Anders Gustafsson. (2018). Machine Learning-Based App for Self-Evaluation of Teacher-Specific Instructional Style and Tools. Educ. Sci. 2018, 8, 7. https://doi.org/10.3390/educsci8010007

`q2 · i?` · `associational · r2`

Symbolic-regression predictive models (Figure 3) built after the 2015 and 2016 ODE courses from grades in Calculus 1–3 and Linear Algebra 1–2; the printed error was 1 − R² = 0.47 in both years.

> "In both cases, the error of the models was approximately 1 − R2 = 0.47 (i.e., R ≈ 0.73). This means that our models account for more than 70% in exam score variation."

### Fedor Duzhin and Anders Gustafsson 2018 (2)

Fedor Duzhin and Anders Gustafsson. (2018). Machine Learning-Based App for Self-Evaluation of Teacher-Specific Instructional Style and Tools. Educ. Sci. 2018, 8, 7. https://doi.org/10.3390/educsci8010007

`q2 · i?` · `associational · r2`

A secondary analysis in the 2016 ODE course attempting to predict the team project score from prior exam grades; the article prints 1 − R² = 0.88, i.e., 35% of variation accounted for.

> "We also tried to construct a predictive model for the project score, but this was unsuccessful and turned out to be almost as bad as predicting random data. The accuracy of the models was about 1 − R2 = 0.88; i.e., they only accounted for 35% of the variation in project scores."

## Discussion


## Related Claims
- [Previous domain knowledge accounts for most of the variance in later achievement, considerably reducing the predictive impact of IQ and WM](domain-knowledge-dominates-later-achievement.md) — a broader claim this one bears on
- [Scaffolding level provides no consistent additional predictive information about subsequent exam performance beyond prior achievement and observed dialogue behavior](scaffolding-little-incremental-exam-prediction.md) — related
- [In regression models, prior attainment and background explained most variation, with treatment adding little beyond pupil prior characteristics](future-foundations-regression-treatment-small.md) — related

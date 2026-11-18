---
type: claim
title: Logistic regression models using student-video clickstream features did not predict laboratory assessment performance in a flipped introductory mechanics course
description: Logistic regression models using student-video clickstream features did not predict laboratory assessment performance in a flipped introductory mechanics course
id: lr-clickstream-features-fail-predict-lab-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: robert-solli-2019
    resource: "https://doi.org/10.1119/perc.2018.pr.solli"
    title: "Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)"
    author: Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: robert-solli-2019-2
    resource: "https://doi.org/10.1119/perc.2018.pr.solli"
    title: "Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)"
    author: Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Logistic regression models using student-video clickstream features did not predict laboratory assessment performance in a flipped introductory mechanics course

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` An interaction-only LR model using five clickstream features performed only marginally better than uniform guessing at whether laboratory grades fell above or below the population median (ACC 1 = 0.566; AUC 1 = 0.616). [→ Robert Solli 2019](#robert-solli-2019)
`q2 i?` A context-augmented LR model adding interaction time, course sequence, and FMCE pretest score also failed to predict laboratory performance (ACC 2 = 0.587; AUC 2 = 0.614). [→ Robert Solli 2019 (2)](#robert-solli-2019-2)

## Evidence

### Robert Solli 2019

Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)

`q2 · i?` · `associational · r2`

Supervised binary classification analysis of clickstream features from a flipped calculus-based introductory mechanics course; the five-feature interaction-only LR model 'performed marginally better than a model uniformly guessing' at whether grades fell above or below the population median (ACC 1 = 0.566; AUC 1 = 0.616).

> "LR Model 1 performed marginally better than a model uniformly guessing at the dependent variable, speciﬁcally the student's grade on the laboratory assessment as being above or below the population median (ACC 1 = 0.566; AU C1 = 0.616)."

### Robert Solli 2019 (2)

Robert Solli, John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Examining the relationship between student performance and video interactions. Originally published 2018. [doi:10.1119/perc.2018.pr.solli](https://doi.org/10.1119/perc.2018.pr.solli)

`q2 · i?` · `associational · r2`

Same modeling study: the context-augmented model added average interaction time, course sequence position, and FMCE pretest score; its ROC is reported 'as the solid line (ACC 2 = 0 .587; AU C2 = 0.614)'. Adding contextual information did not change model performance.

> "The ROC curves for LR Model 2 are also included in Fig. 1 as the solid line (ACC 2 = 0 .587; AU C2 = 0.614)."

## Discussion


## Related Claims
- [Rf Svm Also Fail Beat Chance Lab Performance](rf-svm-also-fail-beat-chance-lab-performance.md)
- [Linear regression on continuous laboratory grades fit poorly (R2 = 0.056), motivating the binary median-split classification outcome](linear-regression-poor-fit-lab-grades-median-split.md) — related
- [The authors attribute their null result to the complexity of laboratory assessments and their distance in time from the videos, contrasting prior predictive results for end-of-video quizzes](assessment-complexity-explains-null-vs-quiz-prediction.md) — related

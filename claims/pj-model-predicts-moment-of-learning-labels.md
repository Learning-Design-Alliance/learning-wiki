---
type: claim
title: Machine-learned P(J) models predict moment-of-learning training labels with cross-validated correlations around 0.40-0.45 in two intelligent tutoring systems.
description: Machine-learned P(J) models predict moment-of-learning training labels with cross-validated correlations around 0.40-0.45 in two intelligent tutoring systems.
id: pj-model-predicts-moment-of-learning-labels
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-25
evidence_strength: moderate
newest_evidence: 2011
recheck_by: 2014
sources:
  - id: baker-2011
    resource: "https://doi.org/10.3233/JAI-2011-015"
    title: "Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T. (2011). Detecting Learning Moment-by-Moment. International Journal of Artificial Intelligence in Education. In Press. https://doi.org/10.3233/JAI-2011-015"
    author: Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: baker-2011-2
    resource: "https://doi.org/10.3233/JAI-2011-015"
    title: "Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T. (2011). Detecting Learning Moment-by-Moment. International Journal of Artificial Intelligence in Education. In Press. https://doi.org/10.3233/JAI-2011-015"
    author: Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Machine-learned P(J) models predict moment-of-learning training labels with cross-validated correlations around 0.40-0.45 in two intelligent tutoring systems.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2011 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2014**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the Cognitive Tutor data, the full P(J) model achieved a correlation of 0.446 to the training labels within 6-fold student-level cross-validation. [→ Baker 2011](#baker-2011)
`q2 i?` In ASSISTments data, the P(J) model achieved a correlation coefficient of 0.397 to the training labels. [→ Baker 2011 (2)](#baker-2011-2)

## Evidence

### Baker 2011

Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T. (2011). Detecting Learning Moment-by-Moment. International Journal of Artificial Intelligence in Education. In Press. https://doi.org/10.3233/JAI-2011-015

`q2 · i?` · `associational · r2`

Observational log analysis of 232 middle-school students' Cognitive Tutor transactions, cross-validated at the student level. The model "achieved a correlation of 0.446" to the P(J) labels. No effect size is printed.

> "For the Cognitive Tutor data, the model achieved a correlation of 0.446 to the training labels previously generated for each problem step, within 6-fold student-level cross-validation."

### Baker 2011 (2)

Baker, Ryan S.J.d., Goldstein, Adam B., Heffernan, Neil T. (2011). Detecting Learning Moment-by-Moment. International Journal of Artificial Intelligence in Education. In Press. https://doi.org/10.3233/JAI-2011-015

`q2 · i?` · `associational · r2`

Log analysis of 4187 students' ASSISTments mastery-learning data, validated with 6-fold student-level cross-validation; the model "achieved a correlation coefficient of 0.397". No effect size is printed.

> "Similarly, the model for ASSISTments data achieved a correlation coefficient of 0.397 to the training labels previously generated for each problem step."

## Discussion


## Related Claims
- [The data-mined moment-by-moment learning model predicts P(J) with a correlation of .676 under six-fold student-level cross-validation](moment-by-moment-model-crossvalidated-correlation.md) — related
- [The P(J) models predict learning rather than merely current non-knowledge: excluding Ln and Ln-1 yields significantly lower cross-validated correlations.](pj-models-not-just-predicting-non-knowledge.md) — related
- [A student's spikiness of momentary learning predicts their final knowledge in both tutoring systems.](spikiness-predicts-final-knowledge.md) — related
- [Incorrect answers show a positive association with momentary learning in both systems, and past errors predict more current learning than past help requests in the Cognitive Tutor.](errors-positively-associated-with-momentary-learning.md) — related

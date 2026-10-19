---
type: claim
title: "Adding eye-tracking evidence to ACE's student model significantly improves assessment of implicit self-explanation over a time-only model"
description: "Adding eye-tracking evidence to ACE's student model significantly improves assessment of implicit self-explanation over a time-only model"
id: eye-tracking-improves-implicit-se-assessment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
sources:
  - id: christina-merten-and-cristina-conati-2005
    resource: "https://www.cs.ubc.ca"
    title: "Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca"
    author: Christina Merten and Cristina Conati
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding eye-tracking evidence to ACE's student model significantly improves assessment of implicit self-explanation over a time-only model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A student model using both time and gaze shifts classifies implicit self-explanation more accurately (73.0% combined) than a time-only model (63.9%), with the ROC area difference statistically significant at the z > 1.96 level. [→ Christina Merten and Cristina Conati 2005](#christina-merten-and-cristina-conati-2005)

## Evidence

### Christina Merten and Cristina Conati 2005

Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca

`q2 · i?` · `design · r2`

Evaluation on log files from a new study of 18 university students (109 self-explained and 68 non-self-explained exploration cases), with thresholds from ROC curves over training data. "model 3 yields a ROC curve with greater area than that of model 2"; Table 3 shows combined accuracy rising from 63.9% to 73.0%, with the increase "more substantial for specificity".

> "As shown in Figure 6, model 3 yields a ROC curve with greater area than that of model 2. This difference in area is statistically significant to the z > 1.96 level"

## Discussion


## Related Claims

- [In an initial eye-tracking study, time on action predicted self-explanation (16-second threshold) and gaze shifts were most reliable at detecting its absence](initial-study-time-and-gaze-predict-self-explanation.md)
- [Customizing knowledge-node priors from pretest scores improves model accuracy, but tailoring SE-tendency priors yields no significant improvement](knowledge-priors-help-se-tendency-priors-do-not.md)
- [Time and gaze-shift evidence are complementary predictors of self-explanation: time alone yields higher sensitivity, gaze shifts alone higher specificity, and the combination the best accuracy](time-and-gaze-evidence-complementary.md)

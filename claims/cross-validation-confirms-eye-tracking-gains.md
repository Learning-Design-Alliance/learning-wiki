---
type: claim
title: Leave-one-out cross-validation over 36 students confirms significant accuracy and stability gains from eye-tracking in both self-explanation and exploration assessment
description: Leave-one-out cross-validation over 36 students confirms significant accuracy and stability gains from eye-tracking in both self-explanation and exploration assessment
id: cross-validation-confirms-eye-tracking-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
newest_evidence: 2005
recheck_by: 2008
sources:
  - id: christina-merten-and-cristina-conati-2005
    resource: "https://www.cs.ubc.ca"
    title: "Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca"
    author: Christina Merten and Cristina Conati
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: christina-merten-and-cristina-conati-2005-2
    resource: "https://www.cs.ubc.ca"
    title: "Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca"
    author: Christina Merten and Cristina Conati
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Leave-one-out cross-validation over 36 students confirms significant accuracy and stability gains from eye-tracking in both self-explanation and exploration assessment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`
> **Currency** · newest study 2005 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2008**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` With generic priors, cross-validated mean combined accuracy for implicitSE nodes was 62.1% (time only) versus 71.6% (time and gaze shifts), a difference significant at the 0.05 level (one-tailed t-test), with slightly higher stability. [→ Christina Merten and Cristina Conati 2005](#christina-merten-and-cristina-conati-2005)
`q2 i?` For exploration nodes, ANOVA showed statistical significance across mean accuracies and one-tailed t-tests showed each successive model differed significantly (57.3%, 65.3%, 71.6%). [→ Christina Merten and Cristina Conati 2005 (2)](#christina-merten-and-cristina-conati-2005-2)

## Evidence

### Christina Merten and Cristina Conati 2005

Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca

`q2 · i?` · `design · r3`

Leave-one-out cross-validation using all 36 students from both studies, with thresholds and conditional probabilities set from the remaining students. Table 5 reports standard deviations of 8.1% versus 7.9% under generic priors.

> "These values show improved performance with the addition of the eye-tracker as well as slightly higher stability. The performance difference is statistically significant at the 0.05 level (one-tailed t-test)"

### Christina Merten and Cristina Conati 2005 (2)

Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca

`q2 · i?` · `design · r2`

Cross-validation of exploration nodes across the three model versions (Table 6): combined accuracies of 57.3%, 65.3% and 71.6% with standard deviations 11.6%, 9.4% and 8.7% under generic priors.

> "ANOVA analysis showed statistical significance in the differences within the set of mean accuracies and then one-tailed T-tests showed that the differences between each model are statistically significant"

## Discussion


## Related Claims
- [Time and gaze-shift evidence are complementary predictors of self-explanation: time alone yields higher sensitivity, gaze shifts alone higher specificity, and the combination the best accuracy](time-and-gaze-evidence-complementary.md) — related
- [Adding eye-tracking evidence to ACE's student model significantly improves assessment of implicit self-explanation over a time-only model](eye-tracking-improves-implicit-se-assessment.md) — a broader claim this one bears on
- [In an initial eye-tracking study, time on action predicted self-explanation (16-second threshold) and gaze shifts were most reliable at detecting its absence](initial-study-time-and-gaze-predict-self-explanation.md) — related
- [More accurate assessment of self-explanation significantly improves the model's assessment of student learning through exploration](se-assessment-improves-exploration-assessment.md) — related
- [Customizing knowledge-node priors from pretest scores improves model accuracy, but tailoring SE-tendency priors yields no significant improvement](knowledge-priors-help-se-tendency-priors-do-not.md) — related
- [A moving-average assessment over the past five actions set the Surveillance Tutor's feedback window, sized from pilot testing showing participants received more feedback than they could process](moving-average-five-action-feedback-window.md) — related
- [Eye-tracker attention patterns significantly improved a student model's ability to capture self-explanation versus a time-based predictor](eye-tracking-improves-self-explanation-modeling.md) — possibly the same claim (merge candidate)

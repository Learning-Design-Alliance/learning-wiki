---
type: claim
title: FCI pre-test score is a significant predictor of rubric score, and treatment membership is no longer significant once FCI pre-score is controlled
description: FCI pre-test score is a significant predictor of rubric score, and treatment membership is no longer significant once FCI pre-score is controlled
id: fci-pre-predicts-rubric-score
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: aaron-reinhard-2022
    resource: "https://doi.org/10.1103/physrevphyseducres.18.010109"
    title: "Aaron Reinhard, Alex Felleson, Paula C. Turner, and Maxwell Green. (2022). Assessing the Impact of Metacognitive Post-Reﬂection Exercises on Problem-Solving Skillfulness. [doi:10.1103/physrevphyseducres.18.010109](https://doi.org/10.1103/physrevphyseducres.18.010109)"
    author: Aaron Reinhard, Alex Felleson, Paula C. Turner, and Maxwell Green
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# FCI pre-test score is a significant predictor of rubric score, and treatment membership is no longer significant once FCI pre-score is controlled

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` FCI pre-score is a much more significant predictor of rubric score (β = 0.03, p = 0.00) than treatment membership. [→ Aaron Reinhard 2022](#aaron-reinhard-2022)
`q2 i?` Membership in the treatment group is no longer a significant predictor after FCI pre-score is taken into account (β = 0.16, p = 0.20). [→ Aaron Reinhard 2022](#aaron-reinhard-2022)

## Evidence

### Aaron Reinhard 2022

Aaron Reinhard, Alex Felleson, Paula C. Turner, and Maxwell Green. (2022). Assessing the Impact of Metacognitive Post-Reﬂection Exercises on Problem-Solving Skillfulness. [doi:10.1103/physrevphyseducres.18.010109](https://doi.org/10.1103/physrevphyseducres.18.010109)

`q2 · i?` · `causal · r1`

Multiple ordered logistic regression on the same quasi-experimental sample, controlling for pre-existing differences in physics knowledge via FCI pre-score. The article reports the treatment odds ratio as 1.18 (95% CI [0.92, 1.51]) versus 1.03 for the FCI pre-score term.

> "Results from an ordered logistic regression model on the eﬀect of FCI pre-score and membership in the treatment group (Table 4) show that FCI pre-score is a much more signiﬁcant predictor of rubric score (βF CIpre = 0.03, p-value=0.00, 95% CI [0.01,0.05]), and membership in the treatment group is no longer a signiﬁcant predictor after FCI pre-score is taken into account (βtreatment = 0.16, p-value=0.20, 95% CI [-0.09,0.41])."

## Discussion


## Related Claims
- [An ordered logistic regression with treatment as the only predictor finds treatment membership raises the odds of a higher rubric score (OR = 1.30)](treatment-ordered-logit-rubric.md) — related
- [Dosage significantly predicts intervention effects in a linear model (β = 0.03 per hour), but the dosage main effect is no longer significant after controlling for moderators](dosage-slope-nonsignificant-with-moderators.md) — a broader claim this one bears on
- [Before the FCI treatment, the experimental and control groups showed no statistically significant difference in writing ability](fci-pretest-equivalence-iraqi-efl.md) — related

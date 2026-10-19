---
type: claim
title: Customizing knowledge-node priors from pretest scores improves model accuracy, but tailoring SE-tendency priors yields no significant improvement
description: Customizing knowledge-node priors from pretest scores improves model accuracy, but tailoring SE-tendency priors yields no significant improvement
id: knowledge-priors-help-se-tendency-priors-do-not
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
  - id: christina-merten-and-cristina-conati-2005-2
    resource: "https://www.cs.ubc.ca"
    title: "Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca"
    author: Christina Merten and Cristina Conati
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Customizing knowledge-node priors from pretest scores improves model accuracy, but tailoring SE-tendency priors yields no significant improvement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`

## Subclaims
`q2 i?` Customized knowledge priors (0.85/0.15 from pretest performance) raised accuracy for each model, significantly so for exploration nodes and for the gaze-shift model's implicitSE nodes. [→ Christina Merten and Cristina Conati 2005](#christina-merten-and-cristina-conati-2005)
`q2 i?` Customizing the Tendency to SE prior failed to achieve statistical significance in either model, showing the model is not very sensitive to this parameter. [→ Christina Merten and Cristina Conati 2005 (2)](#christina-merten-and-cristina-conati-2005-2)

## Evidence

### Christina Merten and Cristina Conati 2005

Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca

`q2 · i?` · `design · r2`

Cross-validation repeated with knowledge priors set to 0.85 or 0.15 based on pretest correctness. Customizing these priors "causes an increase in accuracy and stability for each model", but the increase was statistically significant only for the gaze-shift model's implicitSE nodes (Table 5: 65.8%/75.2%) and for each model's exploration nodes (Table 6).

> "While customiz ing these prior probabilities causes an increase in accuracy and stability for each model, this increase was only statistically si gnificant for the"

### Christina Merten and Cristina Conati 2005 (2)

Christina Merten and Cristina Conati. (2005). Eye-Tracking to Model and Adapt to User Meta-cognition in Intelligent Learning Environments. https://www.cs.ubc.ca

`q2 · i?` · `design · r3`

SE-tendency priors (0.85 for self-explainers, 0.15 for non-self-explainers, values the authors say were arbitrarily picked) were added to knowledge priors in a third cross-validation run (Tables 5 and 6, third rows); the customization "failed to achieve statistical significance".

> "the improvement brought about by the customization of t he Tendency to SE node failed to achieve statistical significance, s howing that the model is not very sensitive to this parameter"

## Discussion


## Related Claims

- [Adding eye-tracking evidence to ACE's student model significantly improves assessment of implicit self-explanation over a time-only model](eye-tracking-improves-implicit-se-assessment.md)

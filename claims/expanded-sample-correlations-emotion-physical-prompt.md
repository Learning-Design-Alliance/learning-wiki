---
type: claim
title: "In the classifier's expanded sample of over 2.6 million observations, negative student emotional state (r = −0.431) and physical prompt communication (r = 0.341) show the strongest correlations with full student response."
description: "In the classifier's expanded sample of over 2.6 million observations, negative student emotional state (r = −0.431) and physical prompt communication (r = 0.341) show the strongest correlations with full student respo..."
id: expanded-sample-correlations-emotion-physical-prompt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2021
sources:
  - id: vasileios-lampos-2021
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
    q: 2
    i: 3
    kind: associational
    rigour: 1
---

# In the classifier's expanded sample of over 2.6 million observations, negative student emotional state (r = −0.431) and physical prompt communication (r = 0.341) show the strongest correlations with full student response.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2` · `i3` large
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i3` In the sampled feature space, the greatest absolute correlations with full student response are negative emotional state (r = −0.431), physical prompt communication (r = 0.341), verbal communication (r = −0.292), and encouragement/praise teaching type (r = 0.225); verbal is anti-correlated with full response while physical prompt has the greatest positive correlation. [→ Vasileios Lampos 2021](#vasileios-lampos-2021)

## Evidence

### Vasileios Lampos 2021

Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

`q2 · i3` · `associational · r1`

Model-based exploration: the best classifier (GP-α, τ = 1) trained on all collected instances was applied to a generated sample of more than 2.6 million unique observations. The article reports the correlations "r = −0.431", "r = 0.341", "r = −0.292", and "r = 0.225" as printed, and notes these are model-derived patterns over a sampled space, not directly observed data.

> "In this expanded data set, the features with the greatest absolute correlation with student response were the negative student emotion state ( r = −0.431, p ≪ 0.001), the physical prompt communication ( r = 0.341, p ≪ 0.001), the verbal communication (r = −0.292, p ≪ 0.001), and the encouragement/praise teaching type ( r = 0.225, p ≪ 0.001)."

## Discussion


## Related Claims
- [Omitting the teacher's communication strategy causes the greatest drop in classifier accuracy, marking communication choice as the most impactful feature category.](communication-strategy-most-impactful-ablation.md) — related
- [The classifier finds picture and object (visual) prompts have almost identical full-response probability distributions, and two communications outperform one with or without physical prompts.](visual-prompt-distributions-and-dual-communication-classifier.md) — related

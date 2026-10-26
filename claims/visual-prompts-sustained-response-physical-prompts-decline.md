---
type: claim
title: Sequences beginning with visual prompts produce higher full-response rates across subsequent time steps, while sequences beginning with physical prompts end at the lowest rates.
description: Sequences beginning with visual prompts produce higher full-response rates across subsequent time steps, while sequences beginning with physical prompts end at the lowest rates.
id: visual-prompts-sustained-response-physical-prompts-decline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: vasileios-lampos-2021
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: vasileios-lampos-2021-2
    resource: "https://doi.org/10.1038/s41539-021-00102-x"
    title: "Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x"
    author: Vasileios Lampos, Joseph Mintz and Xiao Qu
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Sequences beginning with visual prompts produce higher full-response rates across subsequent time steps, while sequences beginning with physical prompts end at the lowest rates.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Visual prompts (picture, object) are more effective at generating full student responses at application and at later time steps, peaking one to two steps after application. [→ Vasileios Lampos 2021](#vasileios-lampos-2021)
`q2 i?` Communication sequences that begin with a physical prompt always end up with the lowest full-response rates (cumulatively from time step t+7, otherwise from t+6), suggesting physical prompts lead to less subsequent engagement. [→ Vasileios Lampos 2021 (2)](#vasileios-lampos-2021-2)

## Evidence

### Vasileios Lampos 2021

Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

`q2 · i?` · `associational · r2`

Statistical analysis of cumulative full student response rates across up to 9 consecutive future time steps following a communication at time t, on the collected observation data (Fig. 1). The article reports "visual prompts appear as more effective in generating full student responses at the time of their application ( t) as well as at later time steps". No effect size printed.

> "Overall, visual prompts appear as more effective in generating full student responses at the time of their application ( t) as well as at later time steps. Interestingly, visual prompts are enhancing their positive impact one and two time-steps ( t + 1, t + 2) after their original application (Fig. 1a, c)."

### Vasileios Lampos 2021 (2)

Vasileios Lampos, Joseph Mintz and Xiao Qu (2021). An artificial intelligence approach for selecting effective teacher communication strategies in autism education. npj Science of Learning 6:25. https://doi.org/10.1038/s41539-021-00102-x

`q2 · i?` · `associational · r1`

Same cumulative and step-wise response-rate analysis of consecutive observations (Fig. 1b, d). Sequences starting with a physical prompt "always end up with the lowest rates either cumulatively (from time step t + 7) or otherwise (from time step t + 6)" despite strong initial response. The authors interpret this as physical prompts leading to less engagement within the sequence size considered. No effect size printed.

> "Furthermore, sequences that begin with a physical prompt, although they initiate strong student response rates at the time of their application, as the sequence of communications progresses, always end up with the lowest rates either cumula- tively (from time step t + 7) or otherwise (from time step t + 6)."

## Discussion


## Related Claims
- [Teachers' prompt-hierarchy hypothesis is not supported: after unsuccessful communication, physical prompts are not the most common subsequent choice (probability 0.310).](prompt-hierarchy-hypothesis-not-supported.md) — related
- [Performing two teacher communications rather than one is more effective in producing full student responses (60.01% vs 50.58%).](two-communications-more-effective-than-one.md) — related
- [The classifier finds picture and object (visual) prompts have almost identical full-response probability distributions, and two communications outperform one with or without physical prompts.](visual-prompt-distributions-and-dual-communication-classifier.md) — related

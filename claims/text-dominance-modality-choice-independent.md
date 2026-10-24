---
type: claim
title: Students overwhelmingly used text prompting, and prior modality choice did not predict subsequent choice among dual-mode users
description: Students overwhelmingly used text prompting, and prior modality choice did not predict subsequent choice among dual-mode users
id: text-dominance-modality-choice-independent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: usage-counts
    title: usage-counts
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: persistence-model
    title: persistence-model
    q: 3
    i: "?"
    kind: associational
    rigour: 1
---

# Students overwhelmingly used text prompting, and prior modality choice did not predict subsequent choice among dual-mode users

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r1`–`r2` · `q3`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Of 919 students, 813 (88.5%) used only text prompting, 44 (4.8%) only voice, and 62 (6.7%) both. [→ usage-counts](#usage-counts)
`q3 i?` Among the 62 students who attempted both modalities, previous input choice did not significantly influence subsequent modality selection (OR = 1.28, p= 0.41). [→ persistence-model](#persistence-model)

## Evidence

### usage-counts

Kaitlin Riegel, Yan Cathy Hua, Paul Denny, Victor-Alexandru Pădurean, Juho Leinonen, James Prather, and Adish Singla. 2026. Say What? Examining Text and Voice Input Modalities for Prompt-Based Programming in Computing Education. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education V. 1 (ITiCSE 2026). https://doi.org/10.1145/3803400.3809397

`q3 · i?` · `associational · r2`

Log data from the weekly lab (including the warm-up problem) show 813 students used only text (88.5%), 44 only voice (4.8%), and 62 both (6.7%), which the authors describe as "an overwhelming bias towards text prompting".

> "there were 813 students who only used text-based prompting (88.5%), 44 who only used voice (4.8%), and 62 who attempted both input methods (6.7%), demonstrating an overwhelming bias towards text prompting"

### persistence-model

Kaitlin Riegel, Yan Cathy Hua, Paul Denny, Victor-Alexandru Pădurean, Juho Leinonen, James Prather, and Adish Singla. 2026. Say What? Examining Text and Voice Input Modalities for Prompt-Based Programming in Computing Education. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education V. 1 (ITiCSE 2026). https://doi.org/10.1145/3803400.3809397

`q3 · i?` · `associational · r1`

A binary mixed-effects logistic regression (random intercept per participant) on the 62 dual-modality students found previous prompt modality did not significantly predict subsequent choice (OR = 1.28, 95% CI [0.71, 2.31], p= 0.41); choices were "independent of their previous choices".

> "The effect was not statistically significant (OR = 1.28, 95% CI [0.71, 2.31],p= 0.41), indicating that, for this subset, students’ choices were independent of their previous choices."

## Discussion


## Related Claims
- [Students reported mixed, task-dependent perceptions of the efficiency and speed of voice versus text input](mixed-efficiency-speed-perceptions.md) — related
- [Edited voice prompts did not significantly differ from text prompts in first-attempt success](edited-voice-no-significant-difference.md) — related
- [Unedited voice prompts have lower odds of first-attempt success than text prompts on two of three Prompt Problems](unedited-voice-lower-first-attempt-success.md) — related
- [Students reported text supports structured, iterative planning while some valued voice for getting initial ideas out](modality-shapes-planning-and-idea-generation.md) — related
- [Greater proportion of voice prompts used correlates moderately with greater stated preference for voice](voice-usage-preference-correlation.md) — related
- [Initial prompting method did not explain immediate success on the third problem (P3)](p3-modality-no-effect.md) — related

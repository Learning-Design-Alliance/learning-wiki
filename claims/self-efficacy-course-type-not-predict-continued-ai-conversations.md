---
type: claim
title: "Neither self-efficacy nor course type statistically predicted students' decisions to continue ChatGPT feedback conversations"
description: "Neither self-efficacy nor course type statistically predicted students' decisions to continue ChatGPT feedback conversations"
id: self-efficacy-course-type-not-predict-continued-ai-conversations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: sperber-2025
    resource: "https://doi.org/10.1016/j.compcom.2025.102921"
    title: "Sperber, Lisa; MacArthur, Marit; Minnillo, Sophia; Stillman, Nicholas; Whithaus, Carl. (2025). Peer and AI Review + Reflection (PAIRR): A human-centered approach to formative assessment. Computers and Composition 76. https://doi.org/10.1016/j.compcom.2025.102921"
    author: Sperber, Lisa; MacArthur, Marit; Minnillo, Sophia; Stillman, Nicholas; Whithaus, Carl
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sperber-2025-2
    resource: "https://doi.org/10.1016/j.compcom.2025.102921"
    title: "Sperber, Lisa; MacArthur, Marit; Minnillo, Sophia; Stillman, Nicholas; Whithaus, Carl. (2025). Peer and AI Review + Reflection (PAIRR): A human-centered approach to formative assessment. Computers and Composition 76. https://doi.org/10.1016/j.compcom.2025.102921"
    author: Sperber, Lisa; MacArthur, Marit; Minnillo, Sophia; Stillman, Nicholas; Whithaus, Carl
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Neither self-efficacy nor course type statistically predicted students' decisions to continue ChatGPT feedback conversations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Self-efficacy scores did not predict continuing the conversation with ChatGPT (z(277) = -1.125, Pr(>|z|)=0.260). [→ Sperber 2025](#sperber-2025)
`q2 i?` Continuation decisions did not differ statistically between large WI courses and small writing classes (χ2(1) = 0.701, p = 0.402). [→ Sperber 2025 (2)](#sperber-2025-2)

## Evidence

### Sperber 2025

Sperber, Lisa; MacArthur, Marit; Minnillo, Sophia; Stillman, Nicholas; Whithaus, Carl. (2025). Peer and AI Review + Reflection (PAIRR): A human-centered approach to formative assessment. Computers and Composition 76. https://doi.org/10.1016/j.compcom.2025.102921

`q2 · i?` · `design · r2`

Binary logistic regression in R (glm function) on spring survey data testing whether self-efficacy scores ranging from -2 to +2 predicted continuing the conversation; the test was not significant and no effect size is printed.

> "self-efficacy scores did not predict students’ decision to continue the conversation [z(277) = -1.125, Pr(>|z|)=0.260"

### Sperber 2025 (2)

Sperber, Lisa; MacArthur, Marit; Minnillo, Sophia; Stillman, Nicholas; Whithaus, Carl. (2025). Peer and AI Review + Reflection (PAIRR): A human-centered approach to formative assessment. Computers and Composition 76. https://doi.org/10.1016/j.compcom.2025.102921

`q2 · i?` · `design · r2`

Chi-squared test in R (infer package chisq_test) comparing continuation decisions between small writing classes and large WI classes; the authors describe the result as surprising and no effect size is printed.

> "student feedback preferences were not statistically different in large WI courses compared to small writing classes [χ2(1) = 0.701, p = 0.402"

## Discussion


## Related Claims
- [Students who continued feedback conversations with ChatGPT perceived more utility in AI feedback than one-shot users](continued-ai-conversations-linked-to-perceived-utility.md) — related
- [Structural paths are stable when continued-use intention and current use are modeled as separate outcomes, and AI anxiety is not directly related to continued use](outcome-robustness-anxiety-null-direct.md) — related

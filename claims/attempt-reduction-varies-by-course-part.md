---
type: claim
title: "Attempt-reduction patterns differed across course parts: Diagnostic and General Feedback were associated with fewer attempts for New Content, Single-Issue for Old Content"
description: "Attempt-reduction patterns differed across course parts: Diagnostic and General Feedback were associated with fewer attempts for New Content, Single-Issue for Old Content"
id: attempt-reduction-varies-by-course-part
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: tsvetomila-mihaylova-2026
    resource: "https://arxiv.org/abs/2605.16933"
    title: "Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933"
    author: Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Attempt-reduction patterns differed across course parts: Diagnostic and General Feedback were associated with fewer attempts for New Content, Single-Issue for Old Content

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` For New Content, Diagnostic Feedback and General Feedback were associated with fewer attempts; for Old Content, Single-Issue Feedback was associated with fewer attempts; no significant attempt difference between parts appeared in the No Feedback condition. [→ Tsvetomila Mihaylova 2026](#tsvetomila-mihaylova-2026)

## Evidence

### Tsvetomila Mihaylova 2026

Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933

`q2 · i?` · `causal · r2`

NB-GLMM on attempts with hint type × course part interaction (Table 3). Single-Issue × Old Content β=−0.131 (HDI [−0.248, −0.018]); General × Old Content β=−0.107 (HDI including zero). Unlike time to success, no significant between-part difference appeared without feedback.

> "For the New Content , again the Diagnostic Feedback is associated with fewer attempts, but interestingly, the General Feedback , which also hints to solution, shows a reduced number of attempts. For the Old Content , the Single-Issue Feedback is associated with fewer Attempts to Success."

## Discussion


## Related Claims
- [Advanced students showed reduced attempts with all hint types, while novices did not clearly benefit and made slightly more submissions with Single-Issue Feedback](advanced-students-attempt-reduction-novices-not.md) — related
- [All three LLM feedback types credibly reduced attempts to success relative to the baseline, with the largest reduction for Diagnostic Feedback](llm-feedback-fewer-attempts.md) — a broader claim this one bears on
- [Feedback effectiveness varied by content recency: guidance-heavy feedback performed less consistently on newer material released after the model's knowledge cutoff](content-recency-moderates-feedback-effectiveness.md) — related
- [All three LLM-generated feedback types are associated with faster time to solution than a compiler-errors-only baseline, with Single-Issue Feedback showing the largest reduction](llm-feedback-faster-time-to-solution.md) — related
- [Student-voted Good feedback was associated with far fewer attempts and shorter solution times than Poor feedback, and thematic analysis identified outdated references and false positives as common failure modes](student-voted-poor-feedback-failure-modes.md) — related

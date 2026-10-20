---
type: claim
title: Student-voted Good feedback was associated with far fewer attempts and shorter solution times than Poor feedback, and thematic analysis identified outdated references and false positives as common failure modes
description: Student-voted Good feedback was associated with far fewer attempts and shorter solution times than Poor feedback, and thematic analysis identified outdated references and false positives as common failure modes
id: student-voted-poor-feedback-failure-modes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: tsvetomila-mihaylova-2026
    resource: "https://doi.org/10.48550/arxiv.2605.16933"
    title: "Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933 [doi:10.48550/arxiv.2605.16933](https://doi.org/10.48550/arxiv.2605.16933)"
    author: Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Student-voted Good feedback was associated with far fewer attempts and shorter solution times than Poor feedback, and thematic analysis identified outdated references and false positives as common failure modes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`

## Subclaims
`q1 i?` Assignments with Good-voted feedback were solved in far fewer attempts and shorter time than Poor-voted ones; thematic analysis of Poor feedback found outdated technology references (n=12) and cases where the materials implemented the same functionality the LLM flagged (n=12) as the most common error themes. [→ Tsvetomila Mihaylova 2026](#tsvetomila-mihaylova-2026)

## Evidence

### Tsvetomila Mihaylova 2026

Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933 [doi:10.48550/arxiv.2605.16933](https://doi.org/10.48550/arxiv.2605.16933)

`q1 · i?` · `causal · r2`

Qualitative analysis of the small set of student-voted feedback messages (14 Good, 31 Poor votes across 45 votes; Table 5). Good-voted pairs averaged 2.92±1.04 attempts versus 13.95±17.34 for Poor. Thematic coding of Poor messages found outdated-version references (n=12) and no-actual-error cases (n=12) most common.

> "Non-surprisingly, when Good feedback is given, the assignment is solved in a much fewer attempts and for much shorter time than when Poor feedback is shown."

## Discussion


## Related Claims
- [Attempt-reduction patterns differed across course parts: Diagnostic and General Feedback were associated with fewer attempts for New Content, Single-Issue for Old Content](attempt-reduction-varies-by-course-part.md) — related
- [AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels](ai-grading-failure-modes-graphical-tasks.md) — related
- [All three LLM-generated feedback types are associated with faster time to solution than a compiler-errors-only baseline, with Single-Issue Feedback showing the largest reduction](llm-feedback-faster-time-to-solution.md) — related
- [Advanced students showed reduced attempts with all hint types, while novices did not clearly benefit and made slightly more submissions with Single-Issue Feedback](advanced-students-attempt-reduction-novices-not.md) — related

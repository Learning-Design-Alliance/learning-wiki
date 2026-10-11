---
type: claim
title: LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions
description: LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions
id: programming-detection-robust-bugs-inconsistent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
sources:
  - id: juho-leinonen-2026
    resource: "https://arxiv.org/abs/2607.20446"
    title: "Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446"
    author: Juho Leinonen, Paul Denny
    q: 2
    i: 3
    kind: causal
    rigour: 1
  - id: juho-leinonen-2026-2
    resource: "https://arxiv.org/abs/2607.20446"
    title: "Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446"
    author: Juho Leinonen, Paul Denny
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2` · `i3` large

## Subclaims
`q2 i3` LLM responses received substantially higher likelihood estimates than real student code in programming question 1, and adding beginner mistakes did not reduce detectability there and may have increased it (Cliff's delta = -0.640 for bugs). [→ Juho Leinonen 2026](#juho-leinonen-2026)
`q2 i3` In programming question 2, the bugs prompt reduced separability relative to baseline/persona prompting (Cliff's delta = -0.512). [→ Juho Leinonen 2026 (2)](#juho-leinonen-2026-2)

## Evidence

### Juho Leinonen 2026

Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446

`q2 · i3` · `causal · r1`

Detection of 201 real submissions versus 100 LLM responses per condition for programming question 1. LLM mean likelihoods were 80.0-86.1 vs 59.5 for real code. Printed effect sizes: Cliff's delta = -0.473 (baseline), -0.472 (persona), -0.640 (bugs), all p Holm < 10^-10; the bugs effect of -0.640 is large.

> "For programming question 1, LLM responses received substantially higher likelihood estimates than real student code (means 80.0–86.1 for LLM vs. 59.5 for real; Table 1)."

### Juho Leinonen 2026 (2)

Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446

`q2 · i3` · `causal · r2`

Detection of 870 real submissions versus 100 LLM responses per condition for programming question 2. Baseline and persona means were 91.0 and 90.7 vs 73.1 for real. Printed effect sizes: Cliff's delta = -0.699 (baseline), -0.670 (persona), both large, while the bugs prompt reduced separability to Cliff's delta = -0.512.

> "However, the bugs prompt reduced separability relative to baseline/persona (Cliff’sδ=−0.512), which is also visible in Figure 5d as increased overlap between the bugs and real-student distributions compared to baseline/persona."

## Discussion


## Related Claims
- [A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt](likelihood-prompt-beats-binary-detection.md) — related
- [LLM self-detection performance is strongly task-dependent: reliable for programming tasks and longer reflective responses but poor for short-answer questions](llm-self-detection-task-dependent.md) — a broader claim this one bears on
- [LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit](llm-response-length-detection-cue.md) — related
- [Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses](reflection-prompt-reduces-detectability.md) — related

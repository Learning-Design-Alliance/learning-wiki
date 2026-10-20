---
type: claim
title: LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit
description: LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit
id: llm-response-length-detection-cue
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: juho-leinonen-2026
    resource: "https://doi.org/10.48550/arxiv.2607.20446"
    title: "Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446 [doi:10.48550/arxiv.2607.20446](https://doi.org/10.48550/arxiv.2607.20446)"
    author: Juho Leinonen, Paul Denny
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Across both textual exercises and the programming exercises, LLM-generated responses were substantially longer than real student responses, suggesting length may be one signal the detector can exploit. [→ Juho Leinonen 2026](#juho-leinonen-2026)

## Evidence

### Juho Leinonen 2026

Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446 [doi:10.48550/arxiv.2607.20446](https://doi.org/10.48550/arxiv.2607.20446)

`q2 · i?` · `causal · r1`

Descriptive length comparison of real versus GPT-4o-generated submissions across the four exercises. Reflection LLM responses were roughly 3.5–5× longer (1577.9–2329.4 vs 439.7 characters) and short answers about 2–3× longer (203.7–305.7 vs 91.6 characters). No effect size is printed for this descriptive comparison.

> "For reflection, LLM responses were roughly 3.5–5×longer on average (1577.9–2329.4 vs. 439.7 characters). For short answers, LLM responses were about 2–3×longer on average (203.7–305.7 vs. 91.6)."

## Discussion


## Related Claims
- [LLM self-detection performance is strongly task-dependent: reliable for programming tasks and longer reflective responses but poor for short-answer questions](llm-self-detection-task-dependent.md) — related
- [For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks](short-answer-detection-reversal.md) — reports the opposite
- [EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length](echoprompt-length-robustness.md) — related
- [LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions](programming-detection-robust-bugs-inconsistent.md) — related
- [Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses](reflection-prompt-reduces-detectability.md) — related
- [A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt](likelihood-prompt-beats-binary-detection.md) — related

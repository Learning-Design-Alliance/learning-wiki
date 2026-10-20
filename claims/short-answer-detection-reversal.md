---
type: claim
title: For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks
description: For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks
id: short-answer-detection-reversal
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
    i: 1
    kind: causal
    rigour: 1
---

# For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i1` small

## Subclaims
`q2 i1` In the short-answer exercise, real student responses had a higher mean detector likelihood than any LLM condition, with positive Cliff's delta across all three prompting conditions. [→ Juho Leinonen 2026](#juho-leinonen-2026)

## Evidence

### Juho Leinonen 2026

Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446 [doi:10.48550/arxiv.2607.20446](https://doi.org/10.48550/arxiv.2607.20446)

`q2 · i1` · `causal · r1`

Analysis of detector likelihood scores for 854 real short-answer submissions versus 100 responses per GPT-4o prompting condition, using two-sided Mann–Whitney U tests with Holm-adjusted p-values. Real students' mean likelihood was 74.1 vs 68.6 baseline, 72.6 persona, 51.7 typo. Printed effect sizes: Cliff's delta = 0.162 (baseline), 0.286 (persona), 0.608 (typo), all p Holm <= 0.0078; the smallest, 0.162, falls in the small range.

> "Real student responses had a higher mean likelihood than any LLM condition (74.1 for real vs. 68.6 baseline, 72.6 persona, and 51.7 typo; Table 1). Rank-based comparisons confirm this reversal (Cliff’sδ= 0.162 for baseline, 0.286 for persona, and 0.608 for typo; allp Holm ≤0.0078; Table 2)."

## Discussion


## Related Claims
- [A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt](likelihood-prompt-beats-binary-detection.md) — related
- [LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit](llm-response-length-detection-cue.md) — reports the opposite
- [LLM self-detection performance is strongly task-dependent: reliable for programming tasks and longer reflective responses but poor for short-answer questions](llm-self-detection-task-dependent.md) — related
- [Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses](reflection-prompt-reduces-detectability.md) — reports the opposite
- [LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions](programming-detection-robust-bugs-inconsistent.md) — related

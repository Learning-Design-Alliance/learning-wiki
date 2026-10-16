---
type: claim
title: Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses
description: Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses
id: reflection-prompt-reduces-detectability
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
    i: 3
    kind: causal
    rigour: 1
---

# Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i3` large

## Subclaims
`q2 i3` Baseline LLM reflection responses were substantially more detectable than real student responses (Cliff's delta = -0.841), with persona and typo prompting reducing separability. [→ Juho Leinonen 2026](#juho-leinonen-2026)

## Evidence

### Juho Leinonen 2026

Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446 [doi:10.48550/arxiv.2607.20446](https://doi.org/10.48550/arxiv.2607.20446)

`q2 · i3` · `causal · r1`

Likelihood-prompt detection of 846 real reflection submissions versus 100 responses per condition. Baseline LLM mean likelihood was 87.0 vs 68.8 for real students. Printed effect size: Cliff's delta = -0.841, p Holm = 1.28e-42, a large effect. Persona (Cliff's delta = -0.451) and typo (Cliff's delta = -0.131) prompts reduced separability further.

> "For the reflection question, baseline LLM responses were substantially more detectable than real student responses by the likelihood prompt (means 87.0 vs. 68.8; Table 1). The separation was large and statistically reliable (Cliff’sδ=−0.841,p Holm = 1.28e−42; Table 2)."

## Discussion


## Related Claims
- [A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt](likelihood-prompt-beats-binary-detection.md) — related
- [LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions](programming-detection-robust-bugs-inconsistent.md) — related
- [For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks](short-answer-detection-reversal.md) — reports the opposite
- [LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit](llm-response-length-detection-cue.md) — related

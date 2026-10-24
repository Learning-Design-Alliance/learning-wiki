---
type: claim
title: "LLM self-detection performance is strongly task-dependent: reliable for programming tasks and longer reflective responses but poor for short-answer questions"
description: "LLM self-detection performance is strongly task-dependent: reliable for programming tasks and longer reflective responses but poor for short-answer questions"
id: llm-self-detection-task-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: juho-leinonen-2026
    resource: "https://doi.org/10.48550/arxiv.2607.20446"
    title: "Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446 [doi:10.48550/arxiv.2607.20446](https://doi.org/10.48550/arxiv.2607.20446)"
    author: Juho Leinonen, Paul Denny
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# LLM self-detection performance is strongly task-dependent: reliable for programming tasks and longer reflective responses but poor for short-answer questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Detection of LLM-generated content by an LLM detector was most reliable for the two programming tasks and longer reflective responses, and performed poorly for short-answer responses in a university introductory programming course. [→ Juho Leinonen 2026](#juho-leinonen-2026)

## Evidence

### Juho Leinonen 2026

Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446 [doi:10.48550/arxiv.2607.20446](https://doi.org/10.48550/arxiv.2607.20446)

`q2 · i?` · `associational · r1`

Discussion of results from an evaluation using authentic student submissions from a 12-week introductory programming course at the University of Auckland (913 unique students) and 1200 GPT-4o-generated responses, judged by an LLM detector. The authors state detection was "most reliable for the two programming tasks and for the longer reflective responses".

> "Detection was most reliable for the two programming tasks and for the longer reflective responses, where LLM-generated submissions typically received higher “LLM-likelihood” scores than real student work."

## Discussion


## Related Claims
- [LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit](llm-response-length-detection-cue.md) — related
- [For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks](short-answer-detection-reversal.md) — related
- [LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions](programming-detection-robust-bugs-inconsistent.md) — a narrower finding that bears on this claim
- [EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length](echoprompt-length-robustness.md) — a broader claim this one bears on
- [The deterministic reflection gate reliably distinguished low-effort defenses from substantive ones during validation, coaching filler answers rather than unlocking](reflection-gate-distinguishes-low-effort-defenses.md) — related
- [EchoPrompt maintains cross-proxy robustness, averaging 87.06% AUROC across seven proxy models and outperforming DNA-DetectLLM by 2.70% AUROC on average](echoprompt-cross-proxy-robustness.md) — related
- [Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses](reflection-prompt-reduces-detectability.md) — related
- [A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt](likelihood-prompt-beats-binary-detection.md) — related

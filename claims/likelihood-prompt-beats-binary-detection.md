---
type: claim
title: A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt
description: A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt
id: likelihood-prompt-beats-binary-detection
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# A graded likelihood detector prompt produced more consistent separation than a binary yes/no detector prompt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Asking the detector for a graded likelihood estimate produced more consistent separation than forcing a binary yes/no decision, with binary decisions tending to misclassify LLM-generated responses. [→ Juho Leinonen 2026](#juho-leinonen-2026)

## Evidence

### Juho Leinonen 2026

Juho Leinonen, Paul Denny. (2026). Distinguishing Artificial from Authentic: Evaluating LLMs for Detecting LLM-Generated Content. https://arxiv.org/abs/2607.20446 [doi:10.48550/arxiv.2607.20446](https://doi.org/10.48550/arxiv.2607.20446)

`q2 · i?` · `causal · r1`

Comparison of the two detector prompts (likelihood percentage vs yes/no), each run 10 times per response, across the four exercises and three generation conditions. The article reports mean likelihood estimates were always in the correct direction for LLM content, whereas binary decisions tended to misclassify it. No effect size is printed for this comparison.

> "On the detector side, asking for a graded likelihood estimate produced more consistent separation than forcing a binary yes/no decision."

## Discussion


## Related Claims
- [For short-answer questions, real student responses received higher LLM-likelihood estimates than LLM-generated responses, a reversal of the pattern in other tasks](short-answer-detection-reversal.md) — related
- [LLM-generated programming code was reliably detected, but inserting beginner bugs had an inconsistent effect across the two programming questions](programming-detection-robust-bugs-inconsistent.md) — related
- [Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses](reflection-prompt-reduces-detectability.md) — related
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — related
- [LLM-generated responses were substantially longer than authentic student submissions, suggesting response length as a signal the detector may exploit](llm-response-length-detection-cue.md) — related
- [LLM self-detection performance is strongly task-dependent: reliable for programming tasks and longer reflective responses but poor for short-answer questions](llm-self-detection-task-dependent.md) — related
- [Surface Formatting Changes Shift LLM Grades, With No Consistent Penalty Detected](surface-formatting-changes-shift-llm-grades-without-penalising-them.md) — related
- [The programming-process replay was the most prompt-intensive view to develop, requiring 31 prompts to work reliably and handle edge cases](replay-most-prompt-intensive-view-31-prompts.md) — related

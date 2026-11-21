---
type: claim
title: "Prompting technique effects are task-dependent: few-shot and self-consistency help, while chain-of-thought helps praise detection but hurts error recognition"
description: "Prompting technique effects are task-dependent: few-shot and self-consistency help, while chain-of-thought helps praise detection but hurts error recognition"
id: prompting-techniques-task-dependent-tutor-moves
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: danielle-r-thomas-2025
    resource: "https://doi.org/10.1007/978-3-032-03873-9_35"
    title: "Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger. (2025). Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study. arXiv preprint. [doi:10.1007/978-3-032-03873-9_35](https://doi.org/10.1007/978-3-032-03873-9_35)"
    author: Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Prompting technique effects are task-dependent: few-shot and self-consistency help, while chain-of-thought helps praise detection but hurts error recognition

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Few-shot prompting improved accuracy by exposing models to ideal and suboptimal tutor responses; chain-of-thought enhanced praise detection but decreased error recognition accuracy; self-consistency majority voting stabilized binary decisions. [→ Danielle R. Thomas 2025](#danielle-r-thomas-2025)

## Evidence

### Danielle R. Thomas 2025

Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger. (2025). Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study. arXiv preprint. [doi:10.1007/978-3-032-03873-9_35](https://doi.org/10.1007/978-3-032-03873-9_35)

`q1 · i?` · `design · r2`

Authors' iterative trial-and-error prompt-engineering observations from the Insights into LLM and Prompt Use section, not a controlled comparison; no effect sizes or test statistics are printed for these prompting-technique differences.

> "Chain-of-thought prompting [10] enhanced performance when reasoning was required—especially in praise detection—but decreased accuracy for error recognition, suggesting the utility of rationale depends on task complexity"

## Discussion


## Related Claims
- [LLMs detect student math errors in tutoring transcripts with 82-88% accuracy, lower than praise detection](llms-detect-student-math-errors-82-88.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [In detecting teacher questions with zero-shot GPT-3.5-turbo, chain-of-thought prompting had slightly higher F1 and precision than Self-Ask but slightly lower recall and balanced accuracy](cot-outperforms-self-ask-zero-shot.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — a narrower finding that bears on this claim
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — a narrower finding that bears on this claim
- [Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs](few-shot-cot-best-concordance-human-experts.md) — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [AskBD is highly compatible with chain-of-thought prompting, and the combination achieves the best overall error detection performance](askbd-compatible-with-cot.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [Chain-of-thought prompting modestly improves case consistency and completeness but reduces controlled disclosure](cot-prompting-reduces-controlled-disclosure.md) — related

---
type: claim
title: GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements
description: GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements
id: gpt4-feedback-plausible-but-misleading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: gerd-kortemeyer-2023
    resource: "https://doi.org/10.48550/arXiv.2304.11221"
    title: "Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)"
    author: Gerd Kortemeyer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Summarized AI feedback includes incorrect claims (e.g., asserting a calculation error where the numerical result was correct) and misleading statements, though feedback on completely incorrect solutions can be useful. [→ Gerd Kortemeyer 2023](#gerd-kortemeyer-2023)

## Evidence

### Gerd Kortemeyer 2023

Gerd Kortemeyer. (2023). Can an AI-tool grade assignments in an introductory physics course?. [doi:10.48550/arXiv.2304.11221](https://doi.org/10.48550/arXiv.2304.11221)

`q2 · i?` · `design · r2`

Qualitative analysis of AI-generated feedback summaries for the 25 solutions. The author found the feedback "sound very plausible, but many of them include incorrect or at least misleading statements", citing examples such as a false claim of a time-constant error in Solution 2.

> "The summaries of the one-sentence feedback message sound very plausible, but many of them include incorrect or at least misleading statements."

## Discussion


## Related Claims
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related
- [GPT-4o frequently makes characteristic errors in homework assessment, including failing to recognize unit and numeric equivalences, marking complete solutions incomplete, and mishandling alternative methods and notations](gpt4o-characteristic-assessment-error-types.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [AI grading errors concentrate in graphical tasks and include both false positives on incorrect equations and false negatives from misread sketches and labels](ai-grading-failure-modes-graphical-tasks.md) — related
- [GPT-4 tends to assume feedback is correct when it sounds convincing but incorrectly identifies the student error or provides an invalid suggestion, and has a high false positive rate on the diagnostic label.](gpt4-feedback-evaluation-shortcomings.md) — related
- [Expert annotation found nearly 20% of AI interactions contained a definitively incorrect statement, yet 86% of students accepted the AI explanation](ai-peer-interaction-quality-annotations.md) — related
- [GPT-4o sometimes incorrectly judges non-standard but correct solution approaches as wrong, flagging correct solutions as incorrect in five of 25 tasks](gpt4o-flags-non-standard-correct-approaches-incorrect.md) — related
- [Among final-answer-correct SLM solutions to physics problem-solving questions, 75-98% contain at least one reasoning error in formulation or execution](slm-physics-answer-reasoning-gap.md) — related

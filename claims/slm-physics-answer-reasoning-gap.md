---
type: claim
title: "Among final-answer-correct SLM solutions to physics problem-solving questions, 75-98% contain at least one reasoning error in formulation or execution"
description: "Among final-answer-correct SLM solutions to physics problem-solving questions, 75-98% contain at least one reasoning error in formulation or execution"
id: slm-physics-answer-reasoning-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: nicy-scaria-2025
    resource: "https://doi.org/10.48550/arXiv.2505.20707"
    title: "Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)"
    author: Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Among final-answer-correct SLM solutions to physics problem-solving questions, 75-98% contain at least one reasoning error in formulation or execution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Correct final answers frequently mask flawed problem setup or execution steps in SLM physics problem solving, with gap percentages of 75.6% to 97.7% across the ten evaluated models. [→ Nicy Scaria 2025](#nicy-scaria-2025)

## Evidence

### Nicy Scaria 2025

Nicy Scaria, Silvester John Joseph Kennedy, Krishna Agarwal, Diksha Seth, Deepak Subramani. (2025). Dissecting Physics Reasoning in Small Language Models: A Multi-Dimensional Analysis from an Educational Perspective. arXiv preprint. [doi:10.48550/arXiv.2505.20707](https://doi.org/10.48550/arXiv.2505.20707)

`q2 · i?` · `design · r2`

Benchmark evaluation of 10 SLMs on PhysBench problem-solving questions using the P-REFS rubric, comparing final-answer correctness against fully correct reasoning. The article reports Gemma3 4B's "87.5% gap" and states Phi4 Reason still shows a 75.6% gap.

> "For instance, Gemma3 4B exhibits an 87.5% gap, meaning that nearly 9 out of 10 correct answers are accompanied by errors in formulation, execution, or both."

## Discussion


## Related Claims
- [SLM performance degrades sharply from conceptual to problem-solving physics questions, with reasoning-optimized training improving but not eliminating the gap](slm-conceptual-problem-solving-performance-gap.md) — related
- [SLM physics failure modes shift with model capability: weaker models fail primarily at interpretation/modeling while stronger models fail during execution](slm-failure-stage-shifts-with-capability.md) — related
- [GPT-4 grading feedback sounds plausible but frequently contains incorrect or misleading statements](gpt4-feedback-plausible-but-misleading.md) — related
- [GPT-4 can override correct reasoning with default answers to technical physics questions, such as reverting to 9.81 m/s² for gravitational acceleration.](gpt4-default-answer-override.md) — related
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related

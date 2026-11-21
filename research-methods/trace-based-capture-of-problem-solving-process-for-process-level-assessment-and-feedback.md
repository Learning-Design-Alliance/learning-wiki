---
type: research-method
id: trace-based-capture-of-problem-solving-process-for-process-level-assessment-and-feedback
title: Trace-based capture of problem-solving process for process-level assessment and feedback
description: The article proposes using structured trace information, analogous to on-line requirement traceability in software engineering, to capture problem-solving steps.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-29
---

# Trace-based capture of problem-solving process for process-level assessment and feedback

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (6 for) · 3 studies (2 design, 1 causal), `q2`–`q3` · 1 of 3 report an effect size · 6 claims rest on one study

## Description
The article proposes using structured trace information, analogous to on-line requirement traceability in software engineering, to capture problem-solving steps. As students perform interactive actions on an integrated problem text and solution space, dependency links are created between solution items and their origins, allowing an answer's life to be followed "in both forward and backward directions". This makes the thinking behind a solution visible and supports process-level feedback, which the article cites Hattie and Timperley as arguing is most effective in assessment situations.

## Accounts
<!-- How each source describes or uses the method -->
- **Trace-based capture of problem-solving process for process-level assessment and feedback**: The article proposes using structured trace information, analogous to on-line requirement traceability in software engineering, to capture problem-solving steps. As students perform interactive actions on an integrated problem text and solution space, dependency links are created between solution items and their origins, allowing an answer's life to be followed "in both forward and backward directions". This makes the thinking behind a solution visible and supports process-level feedback, which the article cites Hattie and Timperley as arguing is most effective in assessment situations. (Adesina et al. (2014))
- **Process-oriented approach to procedural training: process mining analysis of executions against a normative reference model to produce objective feedback**: The process-oriented approach treats a bedside procedure as a process with steps in a predetermined sequence, analysed with process mining. The article states that process mining "allows for the analysis of procedural executions performed in a training context, providing objective information about adherence with a normative procedural model (similarity), the number of repetitions of steps (reworks), and performance metrics." Feedback is derived from event logs capturing rework, activities executed in incorrect order, and durations of activities and transitions, enabling objective comparison of each execution with a reference model. The approach makes explicit activities that are omitted, repeated, or executed in unexpected order, which classic assessment tools do not address. (de la Fuente Rene et al. (2025))
- **Segment-based evidence modeling mapping problem segments to rubric subcategories**: The framework decomposes each learning task into segments, "which correspond to the smallest independently evaluable units within a problem-solving sequence", each aligned with a stage in a scenario map and connected to rubric subcategories across Knowledge and Understanding, Procedural Skills, and Values and Attitudes. Many-to-many relationships let multiple segments supply evidence to one subcategory and one segment support several subcategories. Evidence is stored at segment level and synthesized at rubric level, where the LLM returns a High, Medium, or Low level with a rationale citing specific segments, making every judgment traceable to concrete learner actions. (Yong Oh Lee et al. (2025))

### Claims
- [Trace data from MuTAT can detect arithmetic strategy selection, with place-value strategy use varying across questions](../claims/mutat-detects-strategy-selection-place-value.md) [+M]
- [Strategies inferred from MuTAT trace data appear consistent with strategies used on paper for examined students](../claims/strategy-consistency-across-mutat-and-paper.md) [+W]
- [Process-oriented feedback based on process mining increases residents' similarity to the reference process model for ultrasound-guided central venous catheter placement in simulation](../claims/process-mining-feedback-increases-similarity-reference-model-cvc.md) [+M]
- [Process-oriented feedback reduces rework (repetition of procedural steps) in simulated central venous catheter placement, unlike the control condition](../claims/process-mining-feedback-reduces-rework-cvc.md) [+M]
- [Classic procedural assessment indicators (global rating scale, checklist, execution time) show no intergroup difference despite process-level gains from process-oriented feedback](../claims/classic-indicators-miss-process-level-gains.md) [+M]
- [LLM-derived rubric scores show strong agreement with expert judgments in a field study of middle school students](../claims/llm-rubric-scores-agree-with-expert-judgments.md) [+M]

## Related Research Methods
-

## Key Sources
- Adesina, A., Stone, R., Batmaz, F., & Jones, I. (2014). Touch Arithmetic: A process‐based Computer‐Aided Assessment approach for capture of problem solving steps in the context of elementary mathematics. https://doi.org/10.1016/j.compedu.2014.06.015
- de la Fuente Rene, Galvez-Yanjari Victor, Delfino Alejandro, Lira Ricardo, Hurtado Claudia, Munoz-Gama Jorge, Sepúlveda Marcos. (2025). Process-oriented feedback for ultrasound-guided central venous access training: a randomized controlled trial. BMC Anesthesiology. https://doi.org/10.1186/s12871-025-03341-2
- Yong Oh Lee, Byeonghun Bang, Sejun Oh. (2025). LLM-Driven Rubric-Based Assessment of Algebraic Competence in Multi-Stage Block Coding Tasks with Design and Field Evaluation. https://www.algeomath.kr/

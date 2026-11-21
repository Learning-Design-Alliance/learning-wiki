---
type: strategy
id: assessment-aware-homework-guardrail-strategy
title: Activate an assessment-aware mode that refuses complete solutions, offers step-by-step hints, and surfaces an academic-integrity banner for active assignment queries
description: This implementable dialogue strategy handles queries resembling active assignment items.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: belle-li-lily-tan-wei-zakharov-colby-ben-acton-qiang-qiu-2026
    resource: "https://arxiv.org/abs/2606.09845"
    title: "Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu. (2026). Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat. https://arxiv.org/abs/2606.09845"
    author: Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu
---

# Activate an assessment-aware mode that refuses complete solutions, offers step-by-step hints, and surfaces an academic-integrity banner for active assignment queries

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 3 studies (1 qualitative, 1 design, 1 theoretical), `q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
This implementable dialogue strategy handles queries resembling active assignment items. "When PeteChat detects a query resembling an active assignment item, it activates an assessment-aware mode: (a) refuse to output complete solutions, (b) respond with step-by-step hints aligned with the instructor's method, and (c) surface an academic-integrity banner reminding students of course and university policies." If the student persists, the assistant offers conceptual explanation or redirection to office hours. Instructors tag assignments in the content-upload interface, and a retrieval layer cross-references submission windows with incoming queries.

## Design Implications

### Context
#### Requirements
- instructor tagging of assignments in the content-upload interface
- a retrieval layer cross-referencing submission windows with incoming queries
#### Constraints
- grounded in formative evidence from one course context; the article reports no measured effect of the guardrail on learning or integrity outcomes

### Target Learners
- undergraduate students completing active programming assignments

### Target Learning Goals
- productive help-seeking
- academic integrity
- step-by-step problem solving

### Affordances
- [Srl Cyclical Framework Ai Dialogue](../theories/self-regulated-learning.md)

## Claims

- [In a pre-guardrail deployment, students actively probed for answer-giving behavior and the baseline system sometimes complied, with boundary testing highest in the homework context](../claims/baseline-boundary-testing-homework-context.md) [+W]
- [In the pre-guardrail baseline corpus, self-regulated-learning behaviors were nearly absent: hint utilization was not observed and self-evaluation appeared in only two messages](../claims/srl-behaviors-absent-baseline-corpus.md) [+W]
- [Teachers and students expect PAs to scaffold self-regulated learning by providing hints and questions rather than directly giving solutions](../claims/pa-scaffolding-hints-not-solutions.md) [+W]
- [An AI browser's refusal on academic integrity grounds was bypassed with a single unverified claim of instructor status](../claims/comet-integrity-refusal-bypassed.md) [~W]

## Related Strategies

- [Design AI tutoring behaviors that withhold solutions, prompt recall, and ask critical questions](withhold-answers-prompt-recall-ask-questions.md)
- [Realign: deploy Socratic withholding protocols that delay direct answers for conceptual or diagnostic queries](realign-socratic-withholding-protocol.md)

## Examples
-

## Key Sources
- Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu. (2026). Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat. https://arxiv.org/abs/2606.09845

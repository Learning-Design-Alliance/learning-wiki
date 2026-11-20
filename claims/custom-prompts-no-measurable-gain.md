---
type: claim
title: Custom prompt engineering did not measurably improve ChatGPT-4/CI problem-solving performance on the tested problems
description: Custom prompt engineering did not measurably improve ChatGPT-4/CI problem-solving performance on the tested problems
id: custom-prompts-no-measurable-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: tanuj-kumar-and-mikhail-a-kats-2023
    resource: "https://doi.org/10.1119/5.0182627"
    title: "Tanuj Kumar and Mikhail A. Kats. (2023). ChatGPT-4 with Code Interpreter can be used to solve introductory college-level vector calculus and electromagnetism problems. [doi:10.1119/5.0182627](https://doi.org/10.1119/5.0182627)"
    author: Tanuj Kumar and Mikhail A. Kats
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Custom prompt engineering did not measurably improve ChatGPT-4/CI problem-solving performance on the tested problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Although custom instructions were useful for clarifying variable definitions or increasing verbosity, no tested prompt measurably improved ChatGPT-4/CI problem-solving performance on the tested problems. [→ Tanuj Kumar and Mikhail A. Kats 2023](#tanuj-kumar-and-mikhail-a-kats-2023)

## Evidence

### Tanuj Kumar and Mikhail A. Kats 2023

Tanuj Kumar and Mikhail A. Kats. (2023). ChatGPT-4 with Code Interpreter can be used to solve introductory college-level vector calculus and electromagnetism problems. [doi:10.1119/5.0182627](https://doi.org/10.1119/5.0182627)

`q2 · i?` · `causal · r1`

Appendix 5.3 tests three custom instructions on the three lowest-scoring problems (4, 6, 7); scores with prompts were similar to or lower than without, and the article states "we did not identify any prompts that measurably improved the problem -solving performance."

> "While custom instructions (“prompt engineering”) were useful in some cases where definitions of variables needed to be clarified or to make ChatGPT more verbose when explaining solutions, we did not identify any prompts that measurably improved the problem -solving performance of ChatGPT-4/CI on the problems we tested."

## Discussion


## Related Claims
- [A 45-minute prompt-based programming lesson produced greater pre-to-post gains in Promptly problem solving than a code-tracing control, though not statistically significant](brief-prompting-lesson-modest-performance-gains.md) — related
- [ChatGPT-4 with Code Interpreter satisfactorily solved most tested introductory engineering-math and electromagnetics problems, and its consensus answer was correct on every problem tested](chatgpt4-ci-consensus-correct-all-13-problems.md) — related
- [Prompting is a major source of AI-assisted cognitive effort: copying prompts reduces effort but not time, and verbose model responses can make AI-assisted completion slower than predicted](prompting-effort-and-verbose-response-costs.md) — related
- [Within prompt–response AI interfaces, students without guidance rarely move beyond prompt tuning, yielding interactions of limited educational value and increased reliance on outputs](prompt-response-interface-limits-learning-value.md) — related
- [Solving the same problem N times in separate ChatGPT-4/CI instances and taking the consensus answer yielded correct solutions to all tested problems without human input](consensus-of-n-instances-strategy.md) — related

---
type: claim
title: Solving the same problem N times in separate ChatGPT-4/CI instances and taking the consensus answer yielded correct solutions to all tested problems without human input
description: Solving the same problem N times in separate ChatGPT-4/CI instances and taking the consensus answer yielded correct solutions to all tested problems without human input
id: consensus-of-n-instances-strategy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
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

# Solving the same problem N times in separate ChatGPT-4/CI instances and taking the consensus answer yielded correct solutions to all tested problems without human input

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly
> **Design limits** · Tanuj Kumar and Mikhail A. Kats 2023: no comparison group (read from the study by two models, 2026-11-20)

## Subclaims
`q2 i?` Because of the stochastic nature and stickiness of ChatGPT, the best way to get a correct answer on a particular problem was to solve it N times (e.g., N = 10) in N separate ChatGPT-4/CI instances and take the most-common answer. [→ Tanuj Kumar and Mikhail A. Kats 2023](#tanuj-kumar-and-mikhail-a-kats-2023)

## Evidence

### Tanuj Kumar and Mikhail A. Kats 2023

Tanuj Kumar and Mikhail A. Kats. (2023). ChatGPT-4 with Code Interpreter can be used to solve introductory college-level vector calculus and electromagnetism problems. [doi:10.1119/5.0182627](https://doi.org/10.1119/5.0182627)

`q2 · i?` · `causal · r1`

Empirical finding from the benchmark trials: the article reports "all problems that we tested were solved correctly without any additional human input" when the consensus across separate instances was taken.

> "we found that the best way to get a correct answer on a particular problem is to solve the same problem N times (e.g., N = 10) in N separate ChatGPT -4/CI instances, and take the consensus (most -common) answer. Using this approach, all problems that we tested were solved correctly without any additional human input."

## Discussion


## Related Claims
- [ChatGPT performance is stochastic across chat instances, and the models rarely meaningfully self-correct without a user pointing out a specific mistake](chatgpt-stochastic-self-correction-rare.md) — related
- [ChatGPT-4 with Code Interpreter satisfactorily solved most tested introductory engineering-math and electromagnetics problems, and its consensus answer was correct on every problem tested](chatgpt4-ci-consensus-correct-all-13-problems.md) — possibly the same claim (merge candidate)
- [Performance jumps from ChatGPT-3.5 to ChatGPT-4 and again from ChatGPT-4 to ChatGPT-4/CI, with Code Interpreter enabling accurate symbolic manipulation and numerical calculation](chatgpt4-ci-outperforms-chatgpt4-and-35.md) — related
- [Custom prompt engineering did not measurably improve ChatGPT-4/CI problem-solving performance on the tested problems](custom-prompts-no-measurable-gain.md) — related

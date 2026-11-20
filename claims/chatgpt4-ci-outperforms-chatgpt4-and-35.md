---
type: claim
title: Performance jumps from ChatGPT-3.5 to ChatGPT-4 and again from ChatGPT-4 to ChatGPT-4/CI, with Code Interpreter enabling accurate symbolic manipulation and numerical calculation
description: Performance jumps from ChatGPT-3.5 to ChatGPT-4 and again from ChatGPT-4 to ChatGPT-4/CI, with Code Interpreter enabling accurate symbolic manipulation and numerical calculation
id: chatgpt4-ci-outperforms-chatgpt4-and-35
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
source_checked: 2026-11-20
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

# Performance jumps from ChatGPT-3.5 to ChatGPT-4 and again from ChatGPT-4 to ChatGPT-4/CI, with Code Interpreter enabling accurate symbolic manipulation and numerical calculation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ChatGPT-4/CI gave correct answers more consistently than ChatGPT-4 because the Code Interpreter performed the arithmetic and symbolic operations. [→ Tanuj Kumar and Mikhail A. Kats 2023](#tanuj-kumar-and-mikhail-a-kats-2023)
`q2 i?` There is a major jump in performance from ChatGPT-3.5 to ChatGPT-4 and another from ChatGPT-4 to ChatGPT-4/CI on the 13-problem benchmark. [→ Tanuj Kumar and Mikhail A. Kats 2023](#tanuj-kumar-and-mikhail-a-kats-2023)

## Evidence

### Tanuj Kumar and Mikhail A. Kats 2023

Tanuj Kumar and Mikhail A. Kats. (2023). ChatGPT-4 with Code Interpreter can be used to solve introductory college-level vector calculus and electromagnetism problems. [doi:10.1119/5.0182627](https://doi.org/10.1119/5.0182627)

`q2 · i?` · `causal · r1`

Comparison across the benchmark's per-problem trial scores (e.g., Problem 9: 1/10 for ChatGPT-4 vs 10/10 for ChatGPT-4/CI), where the article states "ChatGPT-4/CI gave correct answers more consistently than ChatGPT-4 because of the code interpreter."

> "In our experiments, ChatGPT-4/CI gave correct answers more consistently than ChatGPT-4 because of the code interpreter. In this example using Problem 9, ChatGPT-4 (a) was able to analycally get the correct expression but gave the wrong order of magnitude in the numerical answer , whereas ChatGPT-4/CI (a) gave the correct numerical value using Code Interpreter."

## Discussion


## Related Claims
- [ChatGPT-4 with Code Interpreter satisfactorily solved most tested introductory engineering-math and electromagnetics problems, and its consensus answer was correct on every problem tested](chatgpt4-ci-consensus-correct-all-13-problems.md) — related
- [A relatively high percentage of correct-choice-incorrect-explanation (CI) answers appeared across many problems, revealing false positives invisible to answer-only scoring](high-percentage-ci-answers-free-response.md) — related
- [Solving the same problem N times in separate ChatGPT-4/CI instances and taking the consensus answer yielded correct solutions to all tested problems without human input](consensus-of-n-instances-strategy.md) — related
- [ChatGPT performance is stochastic across chat instances, and the models rarely meaningfully self-correct without a user pointing out a specific mistake](chatgpt-stochastic-self-correction-rare.md) — related

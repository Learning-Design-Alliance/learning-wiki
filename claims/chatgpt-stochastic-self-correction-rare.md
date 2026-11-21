---
type: claim
title: ChatGPT performance is stochastic across chat instances, and the models rarely meaningfully self-correct without a user pointing out a specific mistake
description: ChatGPT performance is stochastic across chat instances, and the models rarely meaningfully self-correct without a user pointing out a specific mistake
id: chatgpt-stochastic-self-correction-rare
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
    kind: design
    rigour: 2
---

# ChatGPT performance is stochastic across chat instances, and the models rarely meaningfully self-correct without a user pointing out a specific mistake

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Two instances of the same ChatGPT-4/CI chat can give different answers to the same question; this stochastic nature was observed for all versions except simple problems where ChatGPT-4/CI scored 10/10. [→ Tanuj Kumar and Mikhail A. Kats 2023](#tanuj-kumar-and-mikhail-a-kats-2023)
`q2 i?` Within a single chat instance it is difficult to get ChatGPT to meaningfully check its work and correct its own mistakes without the user pointing out a specific mistake, though ChatGPT-4/CI occasionally caught its own error when asked to explain its choices. [→ Tanuj Kumar and Mikhail A. Kats 2023](#tanuj-kumar-and-mikhail-a-kats-2023)

## Evidence

### Tanuj Kumar and Mikhail A. Kats 2023

Tanuj Kumar and Mikhail A. Kats. (2023). ChatGPT-4 with Code Interpreter can be used to solve introductory college-level vector calculus and electromagnetism problems. [doi:10.1119/5.0182627](https://doi.org/10.1119/5.0182627)

`q2 · i?` · `design · r2`

Documented failure-mode analysis of ChatGPT output screenshots across the benchmark trials; the article reports "This stochasc nature of ChatGPT was observed for all versions" except the simplest problems.

> "A comparison of two instances (chats) of ChatGPT-4/CI giving two diﬀerent answers ((a) correct, (b) incorrect) for the same queson. This stochasc nature of ChatGPT was observed for all versions, except for simple problems (1, 2, 3, 9 and 11) where ChatGPT-4/CI scored 10/10 each."

## Discussion


## Related Claims
- [Solving the same problem N times in separate ChatGPT-4/CI instances and taking the consensus answer yielded correct solutions to all tested problems without human input](consensus-of-n-instances-strategy.md) — related
- [ChatGPT-4 with Code Interpreter satisfactorily solved most tested introductory engineering-math and electromagnetics problems, and its consensus answer was correct on every problem tested](chatgpt4-ci-consensus-correct-all-13-problems.md) — related
- [ChatGPT-4 is unreliable on a basic conceptual introductory physics question about kinetic energy and momentum, giving the correct answer in only four of eight regenerated responses](chatgpt4-unreliable-ke-momentum-conceptual-question.md) — a narrower finding that bears on this claim
- [ChatGPT made numerical calculation errors on 25 of 51 numerical homework problems and rarely recovered after correction](chatgpt-numerical-calculation-errors-unrecoverable.md) — related
- [ChatGPT scored 47% on the first-semester final exam, with a realistic hand-graded score between 46% and 50%](chatgpt-exam-47-percent-no-dialogue.md) — related
- [Performance jumps from ChatGPT-3.5 to ChatGPT-4 and again from ChatGPT-4 to ChatGPT-4/CI, with Code Interpreter enabling accurate symbolic manipulation and numerical calculation](chatgpt4-ci-outperforms-chatgpt4-and-35.md) — related
- [External plugins such as Wolfram and the Advanced Data Analysis mode significantly improve ChatGPT-4's ability to perform calculations that LLMs cannot reliably do alone](plugins-improve-chatgpt4-calculation-ability.md) — related
- [ChatGPT's Data Analysis plugin performed competently on well-specified computational tasks but yielded mediocre results overall, with failure modes clustered around judgment](chatgpt-data-analysis-plugin-competent-routine-mediocre-overall.md) — related

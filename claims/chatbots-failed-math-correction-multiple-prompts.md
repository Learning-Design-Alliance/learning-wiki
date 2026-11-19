---
type: claim
title: "GPT-3.5's numerical result for the PhO problem was two orders of magnitude off, and none of the tested chatbots corrected numerical errors even after multiple prompts"
description: "GPT-3.5's numerical result for the PhO problem was two orders of magnitude off, and none of the tested chatbots corrected numerical errors even after multiple prompts"
id: chatbots-failed-math-correction-multiple-prompts
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: d-borovský-2024
    resource: "https://doi.org/10.1088/1742-6596/2715/1/012011"
    title: "D Borovský, J Hanč and M Hančová. (2024). Innovative approaches to high school physics competitions: Harnessing the power of AI and open science. arXiv preprint. Originally published 2023. [doi:10.1088/1742-6596/2715/1/012011](https://doi.org/10.1088/1742-6596/2715/1/012011)"
    author: D Borovský, J Hanč and M Hančová
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-3.5's numerical result for the PhO problem was two orders of magnitude off, and none of the tested chatbots corrected numerical errors even after multiple prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-3.5's numerical answer for the PhO problem was 2 orders of magnitude higher than the correct values, and no chatbot corrected its numerical errors even after multiple prompts. [→ D Borovský 2024](#d-borovsky-2024)

## Evidence

### D Borovský 2024

D Borovský, J Hanč and M Hančová. (2024). Innovative approaches to high school physics competitions: Harnessing the power of AI and open science. arXiv preprint. Originally published 2023. [doi:10.1088/1742-6596/2715/1/012011](https://doi.org/10.1088/1742-6596/2715/1/012011)

`q2 · i?` · `design · r2`

Pilot case study, §4.1.1 numerical comparison: the open-source Vicuna-33B chatbot solved the problem as competently as GPT-3.5 did but was significantly slower, with its own numerical errors. The authors state none of the chatbots were able to correct numerical errors, even after multiple prompts.

> "The correct values are n = 0 .403 mol, m = 11 .3 g which means that GPT-3.5 value was 2 orders of magnitude higher. We'll just mention here that the Vicuna-33B chatbot solved the problem as competently as GPT-3.5 did but was significantly slower and also with numerical errors ( n = 0 .219 mol, m = 6 .0698 g). None of the chatbots were able to correct numerical errors, even after multiple prompts."

## Discussion


## Related Claims
- [Priming with an advanced prompt led Claude and ChatGPT (GPT-4 with Wolfram plugin) to produce completely correct annotated general solutions to the PhO problem](priming-yields-correct-general-solutions.md) — reports the opposite
- [Teacher-provided correct answers and pre-prompting reduce erroneous LLM output and hallucinations compared with open chatbot use](leap-pre-prompting-reduces-hallucinations.md) — related

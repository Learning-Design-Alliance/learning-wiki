---
type: claim
title: Priming with an advanced prompt led Claude and ChatGPT (GPT-4 with Wolfram plugin) to produce completely correct annotated general solutions to the PhO problem
description: Priming with an advanced prompt led Claude and ChatGPT (GPT-4 with Wolfram plugin) to produce completely correct annotated general solutions to the PhO problem
id: priming-yields-correct-general-solutions
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

# Priming with an advanced prompt led Claude and ChatGPT (GPT-4 with Wolfram plugin) to produce completely correct annotated general solutions to the PhO problem

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using priming prompts with context or instructions, Claude (with pdf instructions) and ChatGPT (GPT-4 with Wolfram plugin) produced completely correct annotated general solutions with correct numerical results for the PhO problem. [→ D Borovský 2024](#d-borovsky-2024)

## Evidence

### D Borovský 2024

D Borovský, J Hanč and M Hančová. (2024). Innovative approaches to high school physics competitions: Harnessing the power of AI and open science. arXiv preprint. Originally published 2023. [doi:10.1088/1742-6596/2715/1/012011](https://doi.org/10.1088/1742-6596/2715/1/012011)

`q2 · i?` · `design · r2`

Pilot case study, §4.1.1: after iterative prompting using priming (an advanced prompt with instructions, shown in Fig. 1), the authors obtained a "completely correct annotated general solution" from Claude and ChatGPT. Claude initially gave a numerically incorrect result (m = 0.70 g) that it corrected after a challenge.

> "In Fig. 3, we can see the completely correct annotated general solution from Claude and ChatGPT, along with the correct numerical results."

## Discussion


## Related Claims
- [GPT-3.5's numerical result for the PhO problem was two orders of magnitude off, and none of the tested chatbots corrected numerical errors even after multiple prompts](chatbots-failed-math-correction-multiple-prompts.md) — reports the opposite
- [Only the well-specified text-only prompt produced a correct quantitative result from o4-mini, while underspecified prompts led to numerical errors and misleading final results](prompt-specificity-shapes-lrm-physics-solution-correctness.md) — related
- [Multimodal prompts caused o4-mini to skip numerical integration and produce only qualitative final responses despite recovering much of the analytical structure](multimodal-prompts-cause-skipped-numerical-integration.md) — related
- [Interactive Sage solutions of Physics Olympiad problems reduced competition task correction time to about one third in three years of pilot testing](sage-correction-time-one-third.md) — related
- [External plugins such as Wolfram and the Advanced Data Analysis mode significantly improve ChatGPT-4's ability to perform calculations that LLMs cannot reliably do alone](plugins-improve-chatgpt4-calculation-ability.md) — related

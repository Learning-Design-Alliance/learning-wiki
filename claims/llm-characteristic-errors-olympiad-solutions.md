---
type: claim
title: "LLM-generated Olympiad solutions show characteristic errors: assuming rather than deriving key relations, misrepresenting problem geometry in energy analyses, and omitting solution evaluation"
description: "LLM-generated Olympiad solutions show characteristic errors: assuming rather than deriving key relations, misrepresenting problem geometry in energy analyses, and omitting solution evaluation"
id: llm-characteristic-errors-olympiad-solutions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: tschisgale-2025
    resource: "https://doi.org/10.1103/6fmx-bsnl"
    title: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)"
    author: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P."
    q: 2
    i: "?"
    kind: qualitative
    rigour: "?"
  - id: tschisgale-2025-2
    resource: "https://doi.org/10.1103/6fmx-bsnl"
    title: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)"
    author: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: tschisgale-2025-3
    resource: "https://doi.org/10.1103/6fmx-bsnl"
    title: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)"
    author: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-generated Olympiad solutions show characteristic errors: assuming rather than deriving key relations, misrepresenting problem geometry in energy analyses, and omitting solution evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The most frequently deducted point in the Helicopter problem was failure to derive the mass-of-gas-per-time relationship, with LLMs tending to assume it without justification. [→ Tschisgale 2025](#tschisgale-2025)
`q2 i?` In the Capsizing Iceberg problem, no LLM solution considered the potential energy of the displaced water, and GPT-4o frequently misrepresenting the submerged geometry despite having established it earlier. [→ Tschisgale 2025 (2)](#tschisgale-2025-2)
`q2 i?` In the Sled Pulling problem, all LLM-generated solutions failed to verify that an identified extremum was indeed a maximum, for example via a second-order-derivative test. [→ Tschisgale 2025 (3)](#tschisgale-2025-3)

## Evidence

### Tschisgale 2025

Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)

`q2 · i?` · `qualitative · r?`

Qualitative error analysis of scored LLM solutions to the Helicopter on Mars problem, based on the official scoring scheme; the analysis found LLMs "tend[ed] to assume it without justification" rather than deriving the rotor mass-flow relation.

> "The point most frequently deducted concerned the failure to “propose a relationship for the mass of gas pushed down per unit of time by the rotor” —a theoretically necessary step for deriving that the upward force is proportional to both the atmospheric density and the square of the rotor’s frequency."

### Tschisgale 2025 (2)

Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)

`q2 · i?` · `design · r2`

Qualitative analysis of LLM solutions to the Capsizing Iceberg problem: while the iceberg's own potential-energy change was consistently addressed, no solution accounted for the displaced water; GPT-4o also misrepresenting the submerged geometry that it had correctly established in the first subtask.

> "However, in the next subtask, none of the LLM -generated solutions considered the potential energy of the displaced water when evaluating the tipping behavior of the  iceberg."

### Tschisgale 2025 (3)

Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)

`q2 · i?` · `design · r2`

Qualitative analysis of LLM solutions to the Sled Pulling problem, where most responses achieved nearly full credit; the remaining deductions stemmed from the omitted extremum verification, an omission consistent with the evaluation phase of problem-solving process models.

> "The minor deductions that occurred were due to the failure of all LLM-generated solutions  to verify that an identified extremum was indeed a maximum, for example through a second-order-derivative test."

## Discussion


## Related Claims
- [Physics Olympiad participants scored significantly worse than all tested GPT-4o prompting setups on aggregated Olympiad problems, with large effect sizes](gpt4o-outperforms-olympiad-participants.md) — related
- [On the Helicopter on Mars problem, none of the LLM-generated solutions received full credit although some student solutions did, despite o1-preview's highly consistent high scores](no-llm-full-credit-helicopter-problem.md) — related
- [GPT-4o frequently makes characteristic errors in homework assessment, including failing to recognize unit and numeric equivalences, marking complete solutions incomplete, and mishandling alternative methods and notations](gpt4o-characteristic-assessment-error-types.md) — related

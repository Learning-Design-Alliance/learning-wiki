---
type: claim
title: The GPT-4o mini event classifier agrees with domain experts at almost-perfect pairwise levels (κ = 0.841–0.855), reducing multi-rater Fleiss κ only marginally (0.682 to 0.624)
description: The GPT-4o mini event classifier agrees with domain experts at almost-perfect pairwise levels (κ = 0.841–0.855), reducing multi-rater Fleiss κ only marginally (0.682 to 0.624)
id: llm-event-classifier-expert-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: gabriel-machado-santos-2026
    resource: "https://doi.org/10.1109/cog67430.2026.11778888"
    title: "Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento. (2026). Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games. Accepted for publication in the IEEE Conference on Games (CoG) 2026. [doi:10.1109/cog67430.2026.11778888](https://doi.org/10.1109/cog67430.2026.11778888)"
    author: Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# The GPT-4o mini event classifier agrees with domain experts at almost-perfect pairwise levels (κ = 0.841–0.855), reducing multi-rater Fleiss κ only marginally (0.682 to 0.624)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Pairwise quadratic-weighted Cohen's κ between the LLM classifier and each of three human experts ranges 0.841–0.855, slightly below expert–expert pairs (0.899–0.930) but in the almost perfect range. [→ Gabriel Machado Santos 2026](#gabriel-machado-santos-2026)
`q3 i?` Fleiss κ drops only from 0.682 (three experts) to 0.624 (three experts plus LLM), preserving the substantial agreement tier. [→ Gabriel Machado Santos 2026](#gabriel-machado-santos-2026)

## Evidence

### Gabriel Machado Santos 2026

Gabriel Machado Santos, Rita Maria Silva Julia, Marcelo Zanchetta do Nascimento. (2026). Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games. Accepted for publication in the IEEE Conference on Games (CoG) 2026. [doi:10.1109/cog67430.2026.11778888](https://doi.org/10.1109/cog67430.2026.11778888)

`q3 · i?` · `design · r2`

Inter-rater reliability analysis (Table III) of the four-point event classification rubric, comparing three independent domain experts in financial education with the GPT-4o mini classifier on the same set of events. The LLM achieves "κ= 0.841–0.855against each expert".

> "The LLM classifier achievesκ= 0.841–0.855against each expert—slightly below expert–expert pairs, but firmly in thealmost perfectrange according to the Landis–Koch scale. At the multi-rater level, Fleiss’κdrops only from 0.682 (three experts) to 0.624"

## Discussion


## Related Claims
- [GPT-3 classified students' open-ended responses about teaching practices with reliability similar to that of human coders](gpt3-coding-reliability-similar-to-humans.md) — related
- [An LLM grader using a four-level explanation-quality rubric achieved substantial agreement with human consensus scores (quadratic-weighted κ=0.78).](llm-grader-substantial-agreement-human-consensus.md) — related
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](gpt4o-self-consistency-human-level-grading-agreement.md) — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — related
- [Mistral 7B shows high ICCs but low Fleiss kappa when scoring summary statements](mistral-7b-high-icc-low-fleiss-kappa.md) — related
- [Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters](scaffolded-cot-human-level-agreement-gpt35-grading.md) — related

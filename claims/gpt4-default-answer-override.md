---
type: claim
title: GPT-4 can override correct reasoning with default answers to technical physics questions, such as reverting to 9.81 m/s² for gravitational acceleration.
description: GPT-4 can override correct reasoning with default answers to technical physics questions, such as reverting to 9.81 m/s² for gravitational acceleration.
id: gpt4-default-answer-override
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: pimbblet-2024
    resource: "https://doi.org/10.1088/1361-6404/ad9874"
    title: "Pimbblet, K.A., & Morrell, L.J. (2024). Can ChatGPT pass a physics degree? Making a case for reformation of assessment of undergraduate degrees. European Journal of Physics. [doi:10.1088/1361-6404/ad9874](https://doi.org/10.1088/1361-6404/ad9874)"
    author: "Pimbblet, K.A., & Morrell, L.J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 can override correct reasoning with default answers to technical physics questions, such as reverting to 9.81 m/s² for gravitational acceleration.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 sometimes overrides correct intermediate reasoning with a memorised default answer to simple technical questions. [→ Pimbblet 2024](#pimbblet-2024)

## Evidence

### Pimbblet 2024

Pimbblet, K.A., & Morrell, L.J. (2024). Can ChatGPT pass a physics degree? Making a case for reformation of assessment of undergraduate degrees. European Journal of Physics. [doi:10.1088/1361-6404/ad9874](https://doi.org/10.1088/1361-6404/ad9874)

`q2 · i?` · `design · r2`

In a pre-GPT-4 test on an ISS gravitational acceleration question, the authors found the answer was "entirely correct up until the last possible moment" when ChatGPT substituted the surface-gravity default of 9.81 m/s² for the correct 8.64 m/s². ChatGPT explained it used a commonly remembered default value.

> "The answer given here is entirely correct up until the last possible moment, wherein ChatGPT gives an incorrect answer of 9.81ms-2 (rather than the correct 8.64ms-2)"

## Discussion


## Related Claims
- [LLMs can self-correct errors within a single session but revert to the original incorrect responses when the same questions are re-entered in a new session](llm-self-correction-does-not-persist-across-sessions.md) — related
- [GPT-4 could not reproduce novice reasoning when prompted, and failed on physics questions not phrased in canonical physics tone and nomenclature](gpt4-limitations-novice-emulation-informal-prompts.md) — related
- [Some students abandon a correct analytical solution mid-way and revert to an intuitive proportional answer](mid-solution-abandonment-analytical-reasoning.md) — related
- [GPT-4o sometimes selects correct answers with flawed reasoning and answers inaccuracies in an authoritative tone, risking user overconfidence](llm-flawed-reasoning-authoritative-tone.md) — related
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [Among final-answer-correct SLM solutions to physics problem-solving questions, 75-98% contain at least one reasoning error in formulation or execution](slm-physics-answer-reasoning-gap.md) — related
- [In a simulated interaction, the NuPaD skill file's structural constraints override a GenAI's default tendency toward immediate, superficial answers](nupad-skill-file-overrides-answer-tendency.md) — reports the opposite

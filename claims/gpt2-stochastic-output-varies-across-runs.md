---
type: claim
title: GPT-2 generates different text for the same prompt across repeated runs, demonstrating its stochastic output
description: GPT-2 generates different text for the same prompt across repeated runs, demonstrating its stochastic output
id: gpt2-stochastic-output-varies-across-runs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: eugenio-tufino-2025
    resource: "https://doi.org/10.1088/1361-6552/adea28"
    title: "Eugenio Tufino. (2025). Exploring Large Language Models (LLMs) through interactive Python activities. [doi:10.1088/1361-6552/adea28](https://doi.org/10.1088/1361-6552/adea28)"
    author: Eugenio Tufino
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# GPT-2 generates different text for the same prompt across repeated runs, demonstrating its stochastic output

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` When the same GPT-2 generation cell was run several times, students observed that the generated text varied significantly, demonstrating the stochastic nature of GPT-2's output. [→ Eugenio Tufino 2025](#eugenio-tufino-2025)

## Evidence

### Eugenio Tufino 2025

Eugenio Tufino. (2025). Exploring Large Language Models (LLMs) through interactive Python activities. [doi:10.1088/1361-6552/adea28](https://doi.org/10.1088/1361-6552/adea28)

`q1 · i?` · `design · r1`

Classroom observation during the GPT-2 paragraph-generation exercise in a Master's course module, in which students repeatedly ran the same generation cell. The author reports that "the text generated varied significantly, demonstrating the stochastic nature of GPT-2's output"; no quantitative measure of variability is reported.

> "When the same cell was run several times, students noticed that the text generated varied significantly, demonstrating the stochastic nature of GPT-2’s output."

## Discussion


## Related Claims
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [Substantial within-model output instability was identified, most notably GPT-5.2 in female urology (SD ±22.8%) and anatomy (SD ±14.2%)](llm-output-instability-female-urology-anatomy.md) — related
- [Re-sampling the same question against a fixed interaction history produces diverging LLM answers, revealing stochastic flips and trajectory bifurcation](llm-resampling-reveals-stochastic-flips.md) — a narrower finding that bears on this claim

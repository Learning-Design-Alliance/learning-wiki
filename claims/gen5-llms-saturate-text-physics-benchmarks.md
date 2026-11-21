---
type: claim
title: Generation 5 LLMs reach near-perfect scores on text-based undergraduate physics benchmarks, with standard errors near zero
description: Generation 5 LLMs reach near-perfect scores on text-based undergraduate physics benchmarks, with standard errors near zero
id: gen5-llms-saturate-text-physics-benchmarks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jonah-l-donaldson-2026
    resource: "https://doi.org/10.48550/arXiv.2605.23660"
    title: "Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)"
    author: Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Generation 5 LLMs reach near-perfect scores on text-based undergraduate physics benchmarks, with standard errors near zero

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In PB2, ChatGPT-5.1 achieved a 100% mean score in Quantum Mechanics with zero standard error, with Gemini 3.0 Pro and DeepSeek-V3.2 close behind. [→ Jonah L. Donaldson 2026](#jonah-l-donaldson-2026)

## Evidence

### Jonah L. Donaldson 2026

Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)

`q2 · i?` · `design · r2`

PB2 benchmark study (Oct 2025–Jan 2026) in which Gen 4 and Gen 5 models solved Set B problems, human-marked against the UCL rubric. The article reports that "ChatGPT-5.1 achieved a flawless 100% mean score with zero standard error" in QM, with DeepSeek-V3.2 at 97.74%.

> "In Quantum Mechanics (QM), the models effectively reached the dataset ceiling. ChatGPT-5.1 achieved a flawless 100% mean score with zero standard error, while Gemini 3.0 Pro (98.31%) and DeepSeek-V3.2 (97.74%) clustered tightly just behind this absolute upper bound."

## Discussion


## Related Claims
- [On interpretation-type questions, ChatGPT-5, Gemini 3.0 Pro, and Claude Sonnet 4.5 achieved perfect scores (100%), significantly exceeding trainee performance, while ChatGPT-4o performed comparably to fellows](llms-interpretation-type-questions-perfect-scores.md) — related
- [With individualised grading contexts, Generation 5 models aligned strongly with human grading, Gemini 3.0 Pro reaching r = 0.9191 and MAE of 7.62%](gen5-individualised-grading-alignment.md) — related
- [Native multimodal Generation 5 models resolved the diagram-based spatial reasoning bottleneck, with Gemini 3.0 Pro scoring 100% in Classical Mechanics and Electromagnetism](multimodal-gen5-resolve-spatial-bottleneck.md) — related

---
type: claim
title: "Perception Errors are the dominant LLM error type under optimized conditions, accounting for 43.06% of errors"
description: "Perception Errors are the dominant LLM error type under optimized conditions, accounting for 43.06% of errors"
id: perception-errors-dominant-llm-failures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: seok-hyun-ga-2025
    resource: "https://doi.org/10.48550/arXiv.2512.15298"
    title: "Seok-Hyun Ga, Chun-Yen Chang. (2025). ChatGPT and Gemini participated in the Korean College Scholastic Ability Test - Earth Science I. [doi:10.48550/arXiv.2512.15298](https://doi.org/10.48550/arXiv.2512.15298)"
    author: Seok-Hyun Ga, Chun-Yen Chang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Perception Errors are the dominant LLM error type under optimized conditions, accounting for 43.06% of errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Of 36 incorrect-response cases in Experiment 3, Perception Errors accounted for 43.06% (15.5 cases), followed by Reasoning Errors (25%, 9 cases), Knowledge/Generation Errors (16.67%, 6 cases), and Conceptual Errors (15.28%, 5.5 cases). [→ Seok-Hyun Ga 2025](#seok-hyun-ga-2025)

## Evidence

### Seok-Hyun Ga 2025

Seok-Hyun Ga, Chun-Yen Chang. (2025). ChatGPT and Gemini participated in the Korean College Scholastic Ability Test - Earth Science I. [doi:10.48550/arXiv.2512.15298](https://doi.org/10.48550/arXiv.2512.15298)

`q2 · i?` · `causal · r1`

Qualitative error analysis of the 36 incorrect cases from Experiment 3 (15 from Gemini 2.5 Flash, 15 from GPT-4o, 6 from Gemini 2.5 Pro), using an AI-assisted inductive thematic analysis with human-led verification. The article reports Perception Errors split into Visual Data Misreading (9 cases) and Schematic Misinterpretation (6.5 cases).

> "The most prominent result is that “Perception Errors” emerged as the most dominant error type, accounting for a total of 43.06% (15.5 cases)."

## Discussion


## Related Claims
- [LLM error profiles differ by model: GPT-4o shows frequent hallucination, Gemini 2.5 Flash systematic visual-interpretation errors, Gemini 2.5 Pro balanced but reasoning-limited performance](model-specific-llm-error-profiles-csat.md) — related
- [Even under optimized multimodal input eliminating OCR errors, a large performance gap persists between LLMs on CSAT Earth Science I](optimized-input-persistent-llm-gap-csat.md) — related
- [Four process-level error categories account for roughly nine in ten attributed failures in VCoT geometry solving](four-process-error-categories-dominate-failures.md) — related
- [An exploratory LLM-judge audit labels knowledge gaps (39.1%) and reasoning errors (26.9%) as the most frequent failure modes among incorrect frontier-model responses](llm-judge-audit-failure-modes.md) — related

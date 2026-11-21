---
type: claim
title: Degraded logical clarity causes the largest accuracy losses for gpt-4o, while moderate spelling and terminology noise is tolerated
description: Degraded logical clarity causes the largest accuracy losses for gpt-4o, while moderate spelling and terminology noise is tolerated
id: linguistic-degradation-clarity-largest-loss
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: anna-geißler-2025
    resource: "https://doi.org/10.48550/arXiv.2508.21452"
    title: "Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)"
    author: Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Degraded logical clarity causes the largest accuracy losses for gpt-4o, while moderate spelling and terminology noise is tolerated

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under a fixed baseline prompt, accuracy on text-only items declined from 0.52 (reference) to 0.40 (degraded) and 0.43 (deficient) for clarity/accuracy edits, while degraded spelling matched the reference at 0.52 and degraded terminology was essentially unchanged at 0.53. [→ Anna Geißler 2025](#anna-geiler-2025)

## Evidence

### Anna Geißler 2025

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `causal · r1`

Linguistic degradation experiment on gpt-4o with controlled perturbations at two severities across three dimensions, ten runs per condition with σ10 ≈ 0.015. For clarity/accuracy the article reports a decline from 0.52 to "0.40 (degraded) and 0.43 (deficient)"; for spelling "the degraded variant matched the reference (0.52)". No effect size is given.

> "0.40 (degraded) and 0.43 (deficient). For spelling/punctuation, the degraded variant matched the reference (0.52), while the deficient variant dropped to 0.41."

## Discussion


## Related Claims
- [Prompting strategy materially affects gpt-4o accuracy on thermodynamics text items, with elimination-style prompts underperforming and a two-phase format yielding no significant gain](prompting-strategy-effects-thermodynamics-llm.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related

---
type: claim
title: Prompting strategy materially affects gpt-4o accuracy on thermodynamics text items, with elimination-style prompts underperforming and a two-phase format yielding no significant gain
description: Prompting strategy materially affects gpt-4o accuracy on thermodynamics text items, with elimination-style prompts underperforming and a two-phase format yielding no significant gain
id: prompting-strategy-effects-thermodynamics-llm
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
  - id: anna-geißler-2025-2
    resource: "https://doi.org/10.48550/arXiv.2508.21452"
    title: "Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)"
    author: Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Prompting strategy materially affects gpt-4o accuracy on thermodynamics text items, with elimination-style prompts underperforming and a two-phase format yielding no significant gain

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Mean accuracies across 17 prompt variants on text-only items spanned 0.36–0.54, a range exceeding the three-run mean uncertainty σ3 ≈ 0.03; elimination-style prompts underperform. [→ Anna Geißler 2025](#anna-geiler-2025)
`q2 i?` A two-phase analyze-then-answer format produced no statistically significant gains over single-shot prompting within σ3 for gpt-4o. [→ Anna Geißler 2025 (2)](#anna-geiler-2025-2)

## Evidence

### Anna Geißler 2025

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `causal · r1`

Prompting experiment on gpt-4o via API over the 33 text-only items, with 17 prompt strategies in independent runs at T = 0.7 and run-to-run scatter quantified (σ = 0.05). The article reports the accuracy span; no effect size is printed.

> "Mean accuracies per prompt span 0.36–0.54 (Fig. 2b), a range that materially exceeds σ3, indicating real prompt sensitivity."

### Anna Geißler 2025 (2)

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `causal · r1`

Same gpt-4o prompting experiment, comparing the two-phase format against single-shot prompting on text-only items. The article reports no statistically significant gain within σ3; equivalence was not tested and no effect size is printed.

> "A two-phase "analyze then answer" format5 produced no statistically significant gains over single-shot prompting within σ3, suggesting that explicit separation of analysis and answer does not improve accuracy for these items using gpt-4o."

## Discussion


## Related Claims
- [Strong models reliably solve canonical text-only thermodynamics items reducible to single state-function arguments](canonical-text-items-solved-reliably.md) — related
- [Degraded logical clarity causes the largest accuracy losses for gpt-4o, while moderate spelling and terminology noise is tolerated](linguistic-degradation-clarity-largest-loss.md) — related
- [On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants](prompt-privilege-monotonic-accuracy-gap-medqa.md) — a broader claim this one bears on
- [Domain vocabulary prompting substantially improved recognition of specialized thermodynamics terms in lecture transcription](domain-vocabulary-prompting-whisper-technical-terms.md) — related

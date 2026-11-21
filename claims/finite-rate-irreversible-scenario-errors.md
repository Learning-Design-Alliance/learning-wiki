---
type: claim
title: LLM accuracy degrades on finite-rate, non-quasistatic thermodynamics scenarios, with recurring error patterns in quasistatic template misuse and entropy bookkeeping
description: LLM accuracy degrades on finite-rate, non-quasistatic thermodynamics scenarios, with recurring error patterns in quasistatic template misuse and entropy bookkeeping
id: finite-rate-irreversible-scenario-errors
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
    kind: design
    rigour: 2
  - id: anna-geißler-2025-2
    resource: "https://doi.org/10.48550/arXiv.2508.21452"
    title: "Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)"
    author: Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM accuracy degrades on finite-rate, non-quasistatic thermodynamics scenarios, with recurring error patterns in quasistatic template misuse and entropy bookkeeping

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Accuracy degrades when solutions require integrating multiple constraints, enforcing feasibility bounds, or reasoning about finite-rate (non-quasistatic) processes. [→ Anna Geißler 2025](#anna-geiler-2025)
`q2 i?` The most consistent error patterns include misuse of quasistatic templates despite explicit finite-rate cues and entropy bookkeeping errors confusing transferred entropy with entropy production. [→ Anna Geißler 2025 (2)](#anna-geiler-2025-2)

## Evidence

### Anna Geißler 2025

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `design · r2`

Qualitative error analysis across the cross-model benchmark results, reported in the Common strengths and weaknesses section. The article states that accuracy degrades for multi-constraint and finite-rate problems; no effect size is printed.

> "However, accuracy degrades when solutions require integrating multiple constraints, enforc- ing feasibility bounds, or reasoningabout finite- rate (non-quasistatic) processes."

### Anna Geißler 2025 (2)

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `design · r2`

Same qualitative error analysis of model responses on UTQA items, listing the article's most consistent error patterns including quasistatic template misuse and entropy bookkeeping errors. Descriptive; no effect size is printed.

> "The most consistent error patterns are: (i) misuse of quasistatic templates despite explicit finite-rate cues; (ii) entropy bookkeeping er- rors—confusing transferred entropy with en- tropy production and applying ∆S formulas outside their domain;"

## Discussion


## Related Claims
- [GPT-4 examination accuracy is moderated by item type: multi-step vignettes (61–71%) and image-dependent items (48–63%) fall well below single-fact recall (83–88%)](gpt4-accuracy-item-type-moderators.md) — a broader claim this one bears on
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [After lecture instruction, fewer than 30% of upper-division students use correct reasoning that the entropy of the universe stays the same over a Carnot cycle, and fewer than 20% recognize that a better-than-Carnot engine would decrease the universe's entropy](eeq-carnot-second-law-connection-failure.md) — related
- [No 2025-era LLM reaches a 95% accuracy threshold for unsupervised tutoring in undergraduate thermodynamics; the best model achieves 82%](no-llm-reaches-95-percent-thermodynamics-tutoring-threshold.md) — related

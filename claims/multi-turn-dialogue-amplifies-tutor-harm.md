---
type: claim
title: "Multi-turn interaction amplifies pedagogical harm: mean harm rises 6-11 percentage points across subjects and pedagogical-relationship harm surges from 17.7% to 77.8%"
description: "Multi-turn interaction amplifies pedagogical harm: mean harm rises 6-11 percentage points across subjects and pedagogical-relationship harm surges from 17.7% to 77.8%"
id: multi-turn-dialogue-amplifies-tutor-harm
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rima-hazra-2026
    resource: "https://arxiv.org/abs/2603.17373"
    title: "Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373"
    author: Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: rima-hazra-2026-2
    resource: "https://arxiv.org/abs/2603.17373"
    title: "Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373"
    author: Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multi-turn interaction amplifies pedagogical harm: mean harm rises 6-11 percentage points across subjects and pedagogical-relationship harm surges from 17.7% to 77.8%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Averaged across models and dimensions, mean harm increases from single-turn to multi-turn by 6.16% in Physics, 6.26% in Chemistry, and 11.13% in Mathematics. [→ Rima Hazra 2026](#rima-hazra-2026)
`q2 i?` Pedagogical relationship harm shows the largest shift, rising from a cross-model average of 17.7% in single-turn to 77.8% in multi-turn. [→ Rima Hazra 2026 (2)](#rima-hazra-2026-2)

## Evidence

### Rima Hazra 2026

Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373

`q2 · i?` · `design · r2`

Aggregate analysis of multi-turn versus single-turn harm rates across all evaluated models and dimensions in the SAFETUTORS results. The article reports mean harm "increases by 6.16% in Physics, 6.26% in Chemistry, and 11.13% in Mathematics"; no effect size is printed.

> "Averaging across all models and dimensions, mean harm increases by 6.16% in Physics, 6.26% in Chemistry, and 11.13% in Mathematics from single-turn to multi-turn."

### Rima Hazra 2026 (2)

Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373

`q2 · i?` · `design · r2`

Per-category comparison in the Results section shows the Pedagogical relationship risk category rising from 6.12%-28.99% single-turn to 50%-95.65% multi-turn; the introduction summarizes this as a cross-model average surge "from 17.7% in single-turn to 77.8% in multi-turn". No effect size is printed.

> "The Pedagogical relationship risk category appears deceptively low in single-turn (6.12%–28.99%) but surges to 50%–95.65% in multi-turn."

## Discussion


## Related Claims
- [Informational harm is the sole dimension that decreases in multi-turn interaction, dropping from 60.52% to 11.90%](informational-harm-drops-multi-turn.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related
- [Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics](tutor-harm-subject-dependent-mitigations.md) — related

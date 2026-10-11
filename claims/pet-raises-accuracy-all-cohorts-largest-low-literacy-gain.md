---
type: claim
title: Applying PET raises accuracy for every user cohort, with the largest gain for the Low Literacy cohort
description: Applying PET raises accuracy for every user cohort, with the largest gain for the Low Literacy cohort
id: pet-raises-accuracy-all-cohorts-largest-low-literacy-gain
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lier-jin-2026
    resource: "https://arxiv.org/abs/2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: lier-jin-2026-2
    resource: "https://arxiv.org/abs/2608.08942"
    title: "Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942"
    author: Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Applying PET raises accuracy for every user cohort, with the largest gain for the Low Literacy cohort

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` All user cohorts benefit from PET, with the largest improvement for the Low Literacy cohort, whose accuracy increases from 82.4% to 83.4%. [→ Lier Jin 2026](#lier-jin-2026)
`q2 i?` Smaller improvements are observed for the Everyday User (+1.1 percentage points), Educated User (+0.7 percentage points), and Prompt Engineer (+0.5 percentage points) cohorts. [→ Lier Jin 2026 (2)](#lier-jin-2026-2)

## Evidence

### Lier Jin 2026

Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942

`q2 · i?` · `causal · r2`

Post-normalization evaluation in which PET is applied as a preprocessing step before GPT-5.4-mini inference on MedQA. All user cohorts benefit from PET, with the largest improvement observed for the Low Literacy cohort, whose accuracy increases from 82.4% to 83.4%.

> "All user cohorts benefit from PET, with the largest improvement observed for the Low Literacy cohort, whose accuracy increases from 82.4% to 83.4%."

### Lier Jin 2026 (2)

Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942

`q2 · i?` · `causal · r2`

Same post-PET evaluation, per-cohort gains in percentage points. Smaller improvements are observed for the Everyday User (+1.1 percentage points), Educated User (+0.7 percentage points), and Prompt Engineer (+0.5 percentage points) cohorts, which the authors attribute to less room for improvement.

> "Smaller improvements are observed for the Everyday User (+1.1 percentage points), Educated User (+0.7 percentage points), and Prompt Engineer (+0.5 percentage points) cohorts, suggesting that users already employing well-structured prompts have comparatively less room for improvement."

## Discussion


## Related Claims
- [After PET normalization, no statistically significant performance differences remain between user cohorts](pet-eliminates-significant-accessibility-disparities.md) — related
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related

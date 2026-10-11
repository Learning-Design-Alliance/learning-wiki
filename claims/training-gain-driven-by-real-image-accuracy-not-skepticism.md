---
type: claim
title: The training gain was driven by a 14.2-percentage-point improvement in accuracy on real images, while the gain on AI-generated images was not statistically significant
description: The training gain was driven by a 14.2-percentage-point improvement in accuracy on real images, while the gain on AI-generated images was not statistically significant
id: training-gain-driven-by-real-image-accuracy-not-skepticism
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: negar-kamali-2026
    resource: "https://arxiv.org/abs/2606.28510"
    title: "Negar Kamali, Candice Rockell Gerstner, Jessica Hullman, Matthew Groh. (2026). Generative AI Literacy Training Improves Intelligence Analysts' Discrimination of Real and AI-Generated Images. https://arxiv.org/abs/2606.28510"
    author: Negar Kamali, Candice Rockell Gerstner, Jessica Hullman, Matthew Groh
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: negar-kamali-2026-2
    resource: "https://arxiv.org/abs/2606.28510"
    title: "Negar Kamali, Candice Rockell Gerstner, Jessica Hullman, Matthew Groh. (2026). Generative AI Literacy Training Improves Intelligence Analysts' Discrimination of Real and AI-Generated Images. https://arxiv.org/abs/2606.28510"
    author: Negar Kamali, Candice Rockell Gerstner, Jessica Hullman, Matthew Groh
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# The training gain was driven by a 14.2-percentage-point improvement in accuracy on real images, while the gain on AI-generated images was not statistically significant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` Accuracy on real images increased by 14.2 percentage points (95% CI: [0.7, 27.7]) after training, a corresponding reduction in false-positive errors on real images. [→ Negar Kamali 2026](#negar-kamali-2026)
`q3 i?` Accuracy on AI-generated images showed a positive but non-significant estimated increase of 4 percentage points (95% CI: [-5.8, 13.8]). [→ Negar Kamali 2026 (2)](#negar-kamali-2026-2)

## Evidence

### Negar Kamali 2026

Negar Kamali, Candice Rockell Gerstner, Jessica Hullman, Matthew Groh. (2026). Generative AI Literacy Training Improves Intelligence Analysts' Discrimination of Real and AI-Generated Images. https://arxiv.org/abs/2606.28510

`q3 · i?` · `causal · r2`

Pre-registered OLS estimate for the real-image subset of the counterbalanced experiment (Table 1, column 2). The article reports accuracy on real images "increased by 14.2 percentage points (95% CI: [0.7, 27.7])", indicating sharper discrimination rather than a conservative shift.

> "Instead, accuracy on real images increased by 14.2 percentage points (95% CI: [0.7, 27.7]), corresponding to a 14.2 percentage point reduction in false-positive errors and indicating sharper discrimination capabilities."

### Negar Kamali 2026 (2)

Negar Kamali, Candice Rockell Gerstner, Jessica Hullman, Matthew Groh. (2026). Generative AI Literacy Training Improves Intelligence Analysts' Discrimination of Real and AI-Generated Images. https://arxiv.org/abs/2606.28510

`q3 · i?` · `causal · r2`

Logistic-regression robustness check on the AI-generated-image subset. The article reports the effect "is positive but not significant (β= 0.331,p= 0.330)"; the OLS estimate was a 4-percentage-point increase with CI [-5.8, 13.8] per the Discussion. No statistically significant gain was detected on AI-generated images.

> "the training effect is larger and statistically significant on real images (β= 0.631,p= 0.040), whereas the effect on AI-generated images is positive but not significant (β= 0.331,p= 0.330), consistent with the interpretation that training sharpened discrimination without inducing a conservative bias toward labeling images as fake."

## Discussion


## Related Claims
- [A 30-minute generative AI literacy training increased intelligence analysts' overall accuracy at distinguishing real from AI-generated images by 9 percentage points](brief-generative-ai-literacy-training-raises-analyst-image-discrimination-accuracy.md) — related
- [Training effects concentrated in portrait images (+39.8 percentage points, significant), with directional non-significant negative estimates for full-body and posed-group images](training-effects-largest-for-portrait-images.md) — related
- [Training gains were distributed broadly across the 97 stimulus images rather than concentrated in a small subset, though stimulus-level effects were heterogeneous](training-gains-distributed-broadly-across-stimuli.md) — related
- [Training improved discrimination sensitivity (d′) with only a small, non-significant criterion shift toward labeling images as AI-generated](training-improves-discrimination-sensitivity-not-response-bias.md) — related

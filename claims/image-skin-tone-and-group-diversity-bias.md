---
type: claim
title: Single-person images are significantly biased toward light-skinned individuals, while multi-person images show more balanced gender and skin-tone diversity
description: Single-person images are significantly biased toward light-skinned individuals, while multi-person images show more balanced gender and skin-tone diversity
id: image-skin-tone-and-group-diversity-bias
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: erfan-entezami-2026
    resource: "https://arxiv.org/abs/2609.28483"
    title: "Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483"
    author: Erfan Entezami, Andrew Lan, and Madeline Endres
    q: 2
    i: 3
    kind: causal
    rigour: 2
  - id: erfan-entezami-2026-2
    resource: "https://arxiv.org/abs/2609.28483"
    title: "Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483"
    author: Erfan Entezami, Andrew Lan, and Madeline Endres
    q: 2
    i: 2
    kind: causal
    rigour: 2
---

# Single-person images are significantly biased toward light-skinned individuals, while multi-person images show more balanced gender and skin-tone diversity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i2`–`i3`

## Subclaims
`q2 i3` Both models show significant bias toward light-skinned individuals in single-person images (GPT Image 2: p<0.001, V=0.57; Imagen 4: p<0.001, V=0.61). [→ Erfan Entezami 2026](#erfan-entezami-2026)
`q2 i2` In multi-person images, GPT shows no significant preference for generating men, while Imagen 4 shows a significant but much smaller tendency (p<0.001, V=0.25); both models tend to generate skin-tone-diverse groups. [→ Erfan Entezami 2026 (2)](#erfan-entezami-2026-2)

## Evidence

### Erfan Entezami 2026

Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483

`q2 · i3` · `causal · r2`

Chi-square tests over the 500-image corpus comparing light-skinned versus other skin-tone labels in single-person images, with printed effect sizes V=0.57 and V=0.61; in Database, Debugging, and Individual Programming categories more than 95% of single-person images depict light-skinned individuals.

> "Both GPT Image 2 and Imagen 4 exhibit a significant bias toward generating light-skinned individuals inSingle-personimages (GPT Image 2: 𝑝< 0.001, 𝑉= 0.57and Imagen 4: 𝑝< 0.001, 𝑉= 0.61)."

### Erfan Entezami 2026 (2)

Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483

`q2 · i2` · `causal · r2`

Multi-person analysis of the same 500-image corpus; Imagen 4 shows a significant tendency to generate more men with the printed effect size Cramér's V=0.25, much smaller than the single-person effect sizes, and equivalence for GPT was not established beyond the non-significant test.

> "For GPT, we find no sig- nificant preference for generating men. For Imagen 4, we find a sta- tistically significant tendency to generate more men (𝑝< 0.001, 𝑉= 0.25)."

## Discussion


## Related Claims
- [Text-to-image models generating single-person software engineering images predominantly depict men, with a strong significant effect for both evaluated models](single-person-image-gender-bias.md) — related

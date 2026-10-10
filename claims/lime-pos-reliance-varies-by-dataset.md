---
type: claim
title: Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset
description: Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset
id: lime-pos-reliance-varies-by-dataset
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: michael-lawrence-castanares-2026
    resource: "https://arxiv.org/abs/2609.27749"
    title: "Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749"
    author: Michael Lawrence Castanares, Princess Ventures, and Allan Tan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Chi-square tests show dataset domain is associated with high-impact verbs (χ2 = 31.44, p<0.001) and nouns (χ2 = 8.54, p<0.014) but not adjectives (p = 0.085). [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749

`q2 · i?` · `design · r2`

LIME interpretability analysis of the retrained BERT model across the three datasets (Annex 3, Figure 5); correct predictions on Lau and Scaria relied on tokens with LIME weights > 0.50, while AF showed muted impact. Only test statistics printed.

> "Using Chi-square test confirmed high association between dataset domain and high-impact verbs (χ2 = 31.44,p<0.001 ) and Nouns (χ2 = 8.54,p<0.014 ) but not on adjectives (p= 0.085 )."

## Discussion


## Related Claims
- [Model retraining on labeled OOD data provides the largest improvement in Bloom classification across models and datasets](model-retraining-largest-ood-improvement.md) — related
- [Appending learning objectives to questions improves Bloom classification on the AF dataset](learning-objectives-anchor-bloom-classification.md) — related
- [AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data](ood-aeq-textual-characteristics-differ-iid.md) — related

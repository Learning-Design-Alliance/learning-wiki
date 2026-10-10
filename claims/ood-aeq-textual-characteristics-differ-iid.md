---
type: claim
title: AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data
description: AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data
id: ood-aeq-textual-characteristics-differ-iid
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` IID questions average about 10 words as single sentences, while OOD questions exceed 20 words with deeper syntax and only partial Bloom-verb overlap (medians 35.1% Scaria, 10.5% AF). [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749

`q2 · i?` · `design · r2`

Descriptive textual-characteristics analysis (Table 1, Textstat/SpaCy metrics and CEFR estimation) of the IID-Lau (N=6,175) and OOD datasets (Scaria N=1,833; AF N=848). Word-cloud analysis found Bloom-verb overlap medians of 35.1% and 10.5%.

> "IID entries are short (mean length∼ 10 words), single sentences, with shallow syntactic depth (only 34.9% of data have >5 max depth) and suitable for Grade 10 (FKG 9.6)."

## Discussion


## Related Claims
- [Model accuracy on Bloom classification drops with question text length, with LLMs degrading least](bloom-signal-dilution-with-text-length.md) — related
- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](lime-pos-reliance-varies-by-dataset.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Text splicing into single sentences improves ML and BERT Bloom classification on the Scaria OOD dataset](text-splicing-improves-ood-bloom-classification.md) — related

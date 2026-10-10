---
type: claim
title: Model accuracy on Bloom classification drops with question text length, with LLMs degrading least
description: Model accuracy on Bloom classification drops with question text length, with LLMs degrading least
id: bloom-signal-dilution-with-text-length
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

# Model accuracy on Bloom classification drops with question text length, with LLMs degrading least

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Accuracy falls as text length grows: ML and BERT drop to 50% at 15-20 words on Scaria, while LLMs stay above 70% beyond 20 words. [→ Michael Lawrence Castanares 2026](#michael-lawrence-castanares-2026)

## Evidence

### Michael Lawrence Castanares 2026

Michael Lawrence Castanares, Princess Ventures, and Allan Tan. (2026). Evaluation of Pre-trained Models for Pedagogical Assessment of NovelAI-Assisted Educational Questions. Preprint. https://arxiv.org/abs/2609.27749

`q2 · i?` · `design · r2`

Accuracy-by-text-length analysis (Figure 3) across IID and OOD datasets, reported in Results Section 5.3; the authors characterize this as Bloom signal dilution. Only descriptive accuracies are printed.

> "For OOD-Scaria, performance of ML and BERT models drop to 50% with text length 15-20 words. LLMs still exhibit dilution however their accuracy remained high (>70%) even for longer text (text length> 20 words)."

## Discussion


## Related Claims
- [AI-generated OOD question datasets are longer, syntactically deeper, and overlap less with Bloom trigger verbs than human-curated IID data](ood-aeq-textual-characteristics-differ-iid.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related

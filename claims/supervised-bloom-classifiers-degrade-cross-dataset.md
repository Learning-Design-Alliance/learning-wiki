---
type: claim
title: Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets
description: Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets
id: supervised-bloom-classifiers-degrade-cross-dataset
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: abdolali-faraji-2026
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: abdolali-faraji-2026-2
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` TFPOSIDF+SVM cross-dataset weighted F1 drops by an average of 0.25 relative to within-dataset test scores. [→ Abdolali Faraji 2026](#abdolali-faraji-2026)
`q2 i?` Fine-tuned BERT cross-dataset weighted F1 drops by an average of 0.28 relative to within-dataset test scores. [→ Abdolali Faraji 2026 (2)](#abdolali-faraji-2026-2)

## Evidence

### Abdolali Faraji 2026

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `causal · r2`

Cross-dataset generalization evaluation (RQ1) over five Bloom-annotated datasets, each serving once as training source with an 80/20 split. The SVM model's unseen-dataset weighted F1 scores ranged 0.40–0.70, an "average of 0.25" drop.

> "For TFPOSIDF+SVM, test scores range from 0.68 to 0.82 depending on the training dataset, but performance decreases on unseen datasets by an average of 0.25, ranging between 0.40 and 0.70."

### Abdolali Faraji 2026 (2)

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `design · r2`

Same cross-dataset evaluation protocol (RQ1); the fine-tuned BERT reference model's weighted F1 fell from 0.76–0.91 within-dataset to 0.31–0.76 on unseen datasets, an average drop of 0.28.

> "Similarly, fine-tuned BERT achieves test scores between 0.76 and 0.91, which drop on average by 0.28 when evaluated on other datasets, ranging from 0.31 to 0.76."

## Discussion


## Related Claims
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — related
- [Transfer between two specific datasets is asymmetric: Sangodiah-trained models transfer unusually well to Gani questions](sangodiah-gani-asymmetric-transfer.md) — a narrower finding that bears on this claim
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related

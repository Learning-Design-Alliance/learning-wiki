---
type: claim
title: "Transfer between two specific datasets is asymmetric: Sangodiah-trained models transfer unusually well to Gani questions"
description: "Transfer between two specific datasets is asymmetric: Sangodiah-trained models transfer unusually well to Gani questions"
id: sangodiah-gani-asymmetric-transfer
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: abdolali-faraji-2026
    resource: "https://arxiv.org/abs/2606.13684"
    title: "Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684"
    author: Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók
    q: 2
    i: "?"
    kind: design
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

# Transfer between two specific datasets is asymmetric: Sangodiah-trained models transfer unusually well to Gani questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` TFPOSIDF+SVM trained on Sangodiah and tested on Gani showed a small weighted F1 increase of 0.02, the only such increase observed. [→ Abdolali Faraji 2026](#abdolali-faraji-2026)
`q2 i?` Fine-tuned BERT trained on Sangodiah showed only a 0.04 drop on Gani, far below its average cross-dataset drop. [→ Abdolali Faraji 2026 (2)](#abdolali-faraji-2026-2)

## Evidence

### Abdolali Faraji 2026

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `design · r2`

Cross-dataset evaluation results (RQ1, Table 2). The single observed cross-dataset increase was SVM trained on Sangodiah tested on Gani, a "small increase of 0.02 in weighted F1-score".

> "The only exception observed in our results occurs when TFPOSIDF+SVM is trained on the Sangodiah dataset and tested on the Gani dataset, showing a small increase of 0.02 in weighted F1-score."

### Abdolali Faraji 2026 (2)

Abdolali Faraji, Mohammadreza Molavi, Zohreh Rasoulkhani, Mohammadreza Tavakoli, and Gábor Kismihók. (2026). Cross-Dataset Bloom Question Classification: Supervised Models and Prompted LLMs. https://arxiv.org/abs/2606.13684

`q2 · i?` · `design · r2`

Same RQ1 evaluation; BERT trained on Sangodiah dropped only 0.04 on Gani versus its 0.28 average cross-dataset decrease.

> "For BERT, no increase is observed, but the performance drop is only 0.04, which is considerably smaller than the average cross-dataset decrease of 0.28."

## Discussion


## Related Claims
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — a broader claim this one bears on
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related

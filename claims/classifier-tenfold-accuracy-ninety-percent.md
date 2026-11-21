---
type: claim
title: A logistic-regression classifier predicted the five macro-themes with 0.90 ± 0.02 average accuracy under 10-fold cross-validation
description: A logistic-regression classifier predicted the five macro-themes with 0.90 ± 0.02 average accuracy under 10-fold cross-validation
id: classifier-tenfold-accuracy-ninety-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: dange-2026
    resource: "https://doi.org/10.48550/arXiv.2603.04616"
    title: "Dange, A. and Lopez, R.E. (2026). Chatbot Conversations in Physics Education: Using Artificial Intelligence to Analyze Student Reasoning through Computational Grounded Theory. arXiv:2603.04616. [doi:10.48550/arXiv.2603.04616](https://doi.org/10.48550/arXiv.2603.04616)"
    author: Dange, A. and Lopez, R.E.
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
  - id: dange-2026-2
    resource: "https://doi.org/10.48550/arXiv.2603.04616"
    title: "Dange, A. and Lopez, R.E. (2026). Chatbot Conversations in Physics Education: Using Artificial Intelligence to Analyze Student Reasoning through Computational Grounded Theory. arXiv:2603.04616. [doi:10.48550/arXiv.2603.04616](https://doi.org/10.48550/arXiv.2603.04616)"
    author: Dange, A. and Lopez, R.E.
    q: 2
    i: "?"
    kind: qualitative
    rigour: 2
---

# A logistic-regression classifier predicted the five macro-themes with 0.90 ± 0.02 average accuracy under 10-fold cross-validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · qualitative `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Supervised classification of sentence embeddings into the five macro-themes achieved an average 10-fold cross-validation accuracy of 0.90 ± 0.02, supporting the statistical learnability of the themes. [→ Dange 2026](#dange-2026)
`q2 i?` Misclassifications tended to fall near conceptual boundaries, such as between Energy, Fusion & Forces and Wavefunctions & Infinite Wells. [→ Dange 2026 (2)](#dange-2026-2)

## Evidence

### Dange 2026

Dange, A. and Lopez, R.E. (2026). Chatbot Conversations in Physics Education: Using Artificial Intelligence to Analyze Student Reasoning through Computational Grounded Theory. arXiv:2603.04616. [doi:10.48550/arXiv.2603.04616](https://doi.org/10.48550/arXiv.2603.04616)

`q2 · i?` · `qualitative · r2`

Pattern-confirmation analysis: a logistic regression classifier trained on sentence-level embeddings was evaluated with 10-fold cross-validation on the ~1500-sentence dataset; the classifier achieved an average accuracy of 0.90 ± 0.02, which the authors take to indicate the macro-themes are statistically learnable.

> "Our classifier achieved an average accuracy of 0.90 ± 0.02, meaning that it correctly predicted the macro-theme for 90% of the sentences, with a modest deviation of 2%."

### Dange 2026 (2)

Dange, A. and Lopez, R.E. (2026). Chatbot Conversations in Physics Education: Using Artificial Intelligence to Analyze Student Reasoning through Computational Grounded Theory. arXiv:2603.04616. [doi:10.48550/arXiv.2603.04616](https://doi.org/10.48550/arXiv.2603.04616)

`q2 · i?` · `qualitative · r2`

Confusion-matrix inspection (Fig. 10) showed a dominant diagonal, e.g. 851 of 974 correct in Theme 0 and 163 of 170 in Theme 1; misclassifications tended to fall near conceptual boundaries where student language naturally overlaps.

> "While some misclassifications did occur, they tended to fall near conceptual boundaries, such as between “Energy, Fusion & Forces (Theme 0)” and “Wavefunc- tions & Infinite Wells (Theme 2),” where student language naturally overlaps."

## Discussion


## Related Claims
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
- [Machine learning on discussion-dialog indicators predicts group learning outcome as High, Mid, or Low with best accuracy of 78.9%](ml-prediction-group-outcome-78-9-percent.md) — related

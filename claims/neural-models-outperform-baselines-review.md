---
type: claim
title: "Review-reported model comparisons: a BiLSTM-based model significantly outperformed all baselines (Qiu et al.), and BERT outperformed a semantic-similarity baseline (Yeung et al.)"
description: "Review-reported model comparisons: a BiLSTM-based model significantly outperformed all baselines (Qiu et al.), and BERT outperformed a semantic-similarity baseline (Yeung et al.)"
id: neural-models-outperform-baselines-review
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: samah-alkhuzaey-2023
    resource: "https://doi.org/10.1007/s40593-023-00362-1"
    title: "Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1"
    author: Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma
    q: 2
    i: "?"
    kind: review
    rigour: 3
  - id: samah-alkhuzaey-2023-2
    resource: "https://doi.org/10.1007/s40593-023-00362-1"
    title: "Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1"
    author: Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Review-reported model comparisons: a BiLSTM-based model significantly outperformed all baselines (Qiu et al.), and BERT outperformed a semantic-similarity baseline (Yeung et al.)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · review `r2`–`r3` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The review reports, citing Qiu et al. (2019), that a BiLSTM model with confusion and recall difficulty modules significantly outperformed all baselines with all metrics. [→ Samah AlKhuzaey 2023](#samah-alkhuzaey-2023)
`q2 i?` The review reports, citing Yeung et al. (2019), that BERT-based distractor generation outperformed a Skipgram semantic-similarity baseline in correlation with human judgment. [→ Samah AlKhuzaey 2023 (2)](#samah-alkhuzaey-2023-2)

## Evidence

### Samah AlKhuzaey 2023

Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1

`q2 · i?` · `review · r3`

The review reports, citing Qiu et al. (2019), a difficulty prediction model for MCQs in medical exams that used BiLSTM to encode stem, options and medical text, aggregating a confusion difficulty module and a recall difficulty module; the review states it was compared against SVM + TF-IDF, TACNN, and two variants of itself. No statistics are printed in the quoted sentence.

> "It was found that the proposed model significantly outperformed all baselines with all metrics."

### Samah AlKhuzaey 2023 (2)

Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1

`q2 · i?` · `review · r2`

The review reports, citing Yeung et al. (2019), that BERT's bidirectional contextual representations were used to generate gap-fill MCQ distractors of controlled difficulty, and were compared against Skipgram-trained word embeddings using cosine similarity. The comparison is second-hand as narrated by the review.

> "The results show that BERT outperforms the semantic similarity baseline in terms of correlation with human judgment."

## Discussion


## Related Claims
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](bert-cba-outperforms-baselines-cross-validation.md) — related
- [In the Reason dimension, the IndoBERT–SVM baseline outperformed all BiLSTM variants, achieving QWK 0.332](svm-outperforms-bilstm-reason-dimension.md) — related
- [Lab-trained mind wandering detectors generalize to in-the-wild lecture viewing across task, setting, and cultural group, with BiLSTM on latent features reaching F1 = 0.352](cross-dataset-generalization-mind-wandering-detection.md) — related

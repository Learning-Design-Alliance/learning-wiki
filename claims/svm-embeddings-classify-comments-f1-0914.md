---
type: claim
title: "SVM classifier on sentence embeddings classifies comment correctness with F1 = 0.914 and Cohen's K = 0.764"
description: "SVM classifier on sentence embeddings classifies comment correctness with F1 = 0.914 and Cohen's K = 0.764"
id: svm-embeddings-classify-comments-f1-0914
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: pierpaolo-vittorini-2021
    resource: "https://doi.org/10.1007/s40593-020-00230-2"
    title: "Pierpaolo Vittorini, Stefano Menini, Sara Tonelli. (2021). An AI-Based System for Formative and Summative Assessment in Data Science Courses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00230-2"
    author: Pierpaolo Vittorini, Stefano Menini, Sara Tonelli
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# SVM classifier on sentence embeddings classifies comment correctness with F1 = 0.914 and Cohen's K = 0.764

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` A tuned SVM using sentence embeddings plus distance features classifies student comments as correct/incorrect with accuracy 0.891, F1 0.914, and Cohen's K 0.764. [→ Pierpaolo Vittorini 2021](#pierpaolo-vittorini-2021)

## Evidence

### Pierpaolo Vittorini 2021

Pierpaolo Vittorini, Stefano Menini, Sara Tonelli. (2021). An AI-Based System for Formative and Summative Assessment in Data Science Courses. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00230-2

`q3 · i?` · `design · r2`

Classification experiments on a dataset of 1,069 student/gold standard answer pairs (663 pass, 406 fail). The full model with embeddings and distance features achieved accuracy 0.891, F1 0.914, Cohen's K 0.764 (Table 1).

> "The baseline classifier, obtained using only the seven distance-based features, yielded an F1 score of 0.758 for the Pass class and 0.035 for the Fail class"

## Discussion


## Related Claims
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Machine-learned Sink/Source classifiers classify information roles with F-scores of 0.914 and 0.908 on noisy student discussion text](sink-source-role-classifiers-accuracy.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related

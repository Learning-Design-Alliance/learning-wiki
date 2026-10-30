---
type: claim
title: Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82
description: Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82
id: random-forest-slightly-better-for-answer-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: rebecka-weegar-peter-idestam-almquist-2024
    resource: "https://doi.org/10.1007/s40593-022-00322-1"
    title: "Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1"
    author: Rebecka Weegar · Peter Idestam-Almquist
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Random Forest performed slightly better overall than SVM and Complement Naive Bayes for classifying short exam answers, with an average F-score of 0.82

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Averaged over all strategies and sample sizes, Random Forest achieved F-score 0.82, accuracy 0.84, macro-weighted F-score 0.57, and QWK 0.56, slightly better overall than CNB and SVM. [→ Rebecka Weegar · Peter Idestam-Almquist 2024](#rebecka-weegar-peter-idestam-almquist-2024)

## Evidence

### Rebecka Weegar · Peter Idestam-Almquist 2024

Rebecka Weegar · Peter Idestam-Almquist. (2024). Reducing Workload in Short Answer Grading Using Machine Learning. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00322-1

`q2 · i?` · `design · r2`

Classifier comparison in the Results section using F-scores (weighted and macro-weighted), accuracy, and quadratically weighted Cohen's kappa, averaged over all 64 questions. Random Forest averaged accuracy 0.84 versus 0.81 (SVM) and 0.80 (CNB); average QWK was 0.49 for CNB, 0.57 for SVM, and 0.56 for Random Forest.

> "Of the three classifiers, Random Forest (Breiman, 2001) performed slightly better overall. The average F-score using all strategies and sample sizes was 0.82 for Random Forest (0.79 for both CNB and SVM)."

## Discussion


## Related Claims
- [Classification accuracy correlated with student performance: the classifier was more accurate on questions with more high-quality answers and less accurate where students struggled](classifier-accuracy-correlates-with-student-performance.md) — related
- [Two attempted workload-reduction refinements—stopword-based question demoting and supplementing training data with answers labeled incorrect from other questions—did not improve classification results overall](question-demotion-and-cross-question-training-data-null-results.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [Random forest achieves the highest mean test accuracy (0.9590) of all models compared for predicting exam grade categories from physiological signals](random-forest-highest-accuracy-physiological-exam-prediction.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [SVM with RoBERTa sentence embeddings was the most accurate automatic scoring method (κ = .82) among the four tested combinations](roberta-svm-most-accurate-scoring-pisa.md) — related

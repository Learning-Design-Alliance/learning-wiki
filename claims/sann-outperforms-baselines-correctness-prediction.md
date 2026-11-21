---
type: claim
title: Modified SANN outperforms baseline models in predicting program correctness
description: Modified SANN outperforms baseline models in predicting program correctness
id: sann-outperforms-baselines-correctness-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: muntasir-hoq-2025
    resource: "https://doi.org/10.48550/arXiv.2505.10913"
    title: "Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)"
    author: Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Modified SANN outperforms baseline models in predicting program correctness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On a binary correctness classification task over 50 CS1 problems, the modified SANN achieved the highest accuracy (0.87), precision (0.86), recall (0.88), and F1-score (0.87) compared to code2vec, ASTNN, and traditional ML baselines. [→ Muntasir Hoq 2025](#muntasir-hoq-2025)

## Evidence

### Muntasir Hoq 2025

Muntasir Hoq, Ananya Rao, Reisha Jaishankar, Krish Piryani, Nithya Janapati, Jessica Vandenberg, Bradford Mott, Narges Norouzi, James Lester, Bita Akram. (2025). Automated Identification of Logical Errors in Programs: Advancing Scalable Analysis of Student Misconceptions. arXiv preprint. [doi:10.48550/arXiv.2505.10913](https://doi.org/10.48550/arXiv.2505.10913)

`q2 · i?` · `design · r2`

Comparative evaluation on 47,764 compilable submissions (18,787 correct, 28,977 incorrect) split 80:10:10 stratified. The article reports the modified SANN 'outperformed the other models' against code2vec, ASTNN, XGBoost, KNN, and SVM; no effect size is printed.

> "Table 1 shows that our modified SANN model outperformed the other models with the highest accuracy, precision, recall, and F1-score with values of 0.87, 0.86, 0.88, and 0.87, respectively."

## Discussion


## Related Claims
- [SANN code vectors outperform explainable baseline code2vec in logical error identification](sann-beats-code2vec-error-identification.md) — related
- [Expert evaluation shows high recall and precision for SANN-identified logical errors across five problems](sann-high-recall-precision-logical-errors.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — related
- [An LSTM-based strategy temporal analytics framework outperforms random forest, SVM, and majority-class baselines for stealth assessment predictive accuracy](lstm-strategy-temporal-analytics-outperforms-baselines.md) — related
- [Random Forest is the best-performing classification model for predicting postgraduate public health students' CGPA category, with 71.43% accuracy and AUC 0.87](random-forest-best-classifier-ap.md) — related
- [A SANN model pretrained on FalconCode and fine-tuned on LLM-generated synthetic code outperformed synthetic-only, pretrained-only, and GPT-4o baselines at predicting correctness on an unseen problem](fine-tuned-sann-outperforms-baselines-unseen-problem.md) — related

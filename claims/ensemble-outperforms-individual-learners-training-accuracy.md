---
type: claim
title: "Ensemble learning models (XGB, RF, Stacking) achieve higher cross-validated accuracy than individual learners (SVM, DT, LR, LDA) in predicting primary school students' academic achievement"
description: "Ensemble learning models (XGB, RF, Stacking) achieve higher cross-validated accuracy than individual learners (SVM, DT, LR, LDA) in predicting primary school students' academic achievement"
id: ensemble-outperforms-individual-learners-training-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: sun-zhiyuan-2024
    resource: "https://doi.org/10.1186/s12889-024-17769-7"
    title: "Sun Zhiyuan, Yuan Yunhao, Xiong Xuan, Meng Shuqiao, Shi Yifan, Chen Aiguo. (2024). Predicting academic achievement from the collaborative influences of executive function, physical fitness, and demographic factors among primary school students in China: ensemble learning methods. BMC Public Health. https://doi.org/10.1186/s12889-024-17769-7"
    author: Sun Zhiyuan, Yuan Yunhao, Xiong Xuan, Meng Shuqiao, Shi Yifan, Chen Aiguo
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Ensemble learning models (XGB, RF, Stacking) achieve higher cross-validated accuracy than individual learners (SVM, DT, LR, LDA) in predicting primary school students' academic achievement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In repeated five-fold cross-validation on the training set, the lowest, highest, and average accuracy of the three ensemble models exceeded those of the four individual learners. [→ Sun Zhiyuan 2024](#sun-zhiyuan-2024)

## Evidence

### Sun Zhiyuan 2024

Sun Zhiyuan, Yuan Yunhao, Xiong Xuan, Meng Shuqiao, Shi Yifan, Chen Aiguo. (2024). Predicting academic achievement from the collaborative influences of executive function, physical fitness, and demographic factors among primary school students in China: ensemble learning methods. BMC Public Health. https://doi.org/10.1186/s12889-024-17769-7

`q2 · i?` · `associational · r2`

Repeated five-fold cross-validation on the 80% training set (n = 240) comparing seven models' average accuracy. Ensemble models XGB (70.21%), RF (70.42%), and Stacking (68.33%) exceeded individual learners SVM (61.88%), DT (61.46%), LR (61.46%), and LDA (63.33%); all permutation tests p < 0.001. No effect size printed.

> "the average accuracy of XGB, RF, SVM, DT, LR, LDA, and Stacking models was 70.21% (permutation test, iterations = 1000, p < 0.001), 70.42% (p < 0.001), 61.88% (p < 0.001), 61.46% (p < 0.001), 61.46% (p < 0.001), 63.33% (p < 0.001), and 68.33% (p < 0.001), respectively."

## Discussion


## Related Claims
- [Ensemble models generalize better than individual learners on held-out test samples for predicting academic achievement](ensemble-generalization-test-samples.md) — possibly the same claim (merge candidate)
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — reports the opposite
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related

---
type: claim
title: Ensemble models generalize better than individual learners on held-out test samples for predicting academic achievement
description: Ensemble models generalize better than individual learners on held-out test samples for predicting academic achievement
id: ensemble-generalization-test-samples
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
    rigour: 1
  - id: sun-zhiyuan-2024-2
    resource: "https://doi.org/10.1186/s12889-024-17769-7"
    title: "Sun Zhiyuan, Yuan Yunhao, Xiong Xuan, Meng Shuqiao, Shi Yifan, Chen Aiguo. (2024). Predicting academic achievement from the collaborative influences of executive function, physical fitness, and demographic factors among primary school students in China: ensemble learning methods. BMC Public Health. https://doi.org/10.1186/s12889-024-17769-7"
    author: Sun Zhiyuan, Yuan Yunhao, Xiong Xuan, Meng Shuqiao, Shi Yifan, Chen Aiguo
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Ensemble models generalize better than individual learners on held-out test samples for predicting academic achievement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the 20% test set, the XGB model achieved accuracy, precision, and recall of 68.33%, 70.37%, and 63.33%. [→ Sun Zhiyuan 2024](#sun-zhiyuan-2024)
`q2 i?` The evaluation indices of the three ensemble models on test samples were generally higher than those of the four individual learners. [→ Sun Zhiyuan 2024 (2)](#sun-zhiyuan-2024-2)

## Evidence

### Sun Zhiyuan 2024

Sun Zhiyuan, Yuan Yunhao, Xiong Xuan, Meng Shuqiao, Shi Yifan, Chen Aiguo. (2024). Predicting academic achievement from the collaborative influences of executive function, physical fitness, and demographic factors among primary school students in China: ensemble learning methods. BMC Public Health. https://doi.org/10.1186/s12889-024-17769-7

`q2 · i?` · `associational · r1`

Test-set evaluation applying trained models to the held-out 20% test samples, re-evaluated with accuracy, precision, and recall. The XGB model's printed scores were 68.33% accuracy, 70.37% precision, and 63.33% recall (ps = 0.004). No effect size printed.

> "In Fig. 4, the XGB model achieved accuracy, precision, and recall of 68.33%, 70.37%, and 63.33% (ps = 0.004), respectively."

### Sun Zhiyuan 2024 (2)

Sun Zhiyuan, Yuan Yunhao, Xiong Xuan, Meng Shuqiao, Shi Yifan, Chen Aiguo. (2024). Predicting academic achievement from the collaborative influences of executive function, physical fitness, and demographic factors among primary school students in China: ensemble learning methods. BMC Public Health. https://doi.org/10.1186/s12889-024-17769-7

`q2 · i?` · `associational · r2`

Test-sample evaluation of the same trained models. The article states the ensemble models' indices were "generally higher than those of the four individual learners," which it says once again validated stronger ensemble performance. No effect size printed.

> "In addition, the evaluation indices scores of the three ensemble learning models in the test samples were generally higher than those of the four individual learners."

## Discussion


## Related Claims
- [Ensemble learning models (XGB, RF, Stacking) achieve higher cross-validated accuracy than individual learners (SVM, DT, LR, LDA) in predicting primary school students' academic achievement](ensemble-outperforms-individual-learners-training-accuracy.md) — possibly the same claim (merge candidate)
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — related
- [Cross-validated ensemble models performed better on the test set than hold-out models on internal evaluation, suggesting cross-validation leverages data more effectively](cross-validation-ensemble-outperformed-hold-out-internal-evaluation.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — a broader claim this one bears on

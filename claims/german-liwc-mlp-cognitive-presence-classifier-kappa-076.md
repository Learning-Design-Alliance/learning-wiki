---
type: claim
title: "A multilayer perceptron classifier using German LIWC features classifies cognitive presence phases with accuracy of 0.82 and Cohen's κ of 0.76"
description: "A multilayer perceptron classifier using German LIWC features classifies cognitive presence phases with accuracy of 0.82 and Cohen's κ of 0.76"
id: german-liwc-mlp-cognitive-presence-classifier-kappa-076
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: dornauer-2024
    resource: "https://doi.org/10.1007/s40593-023-00335-4"
    title: "Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E. (2024). Automatic Classification of Online Discussions and Other Learning Traces to Detect Cognitive Presence. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00335-4"
    author: "Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A multilayer perceptron classifier using German LIWC features classifies cognitive presence phases with accuracy of 0.82 and Cohen's κ of 0.76

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the holdout evaluation set, the MLP classifier trained only on standard-scaled LIWC features reached accuracy 0.82, macro average 0.77, and Cohen's κ 0.76. [→ Dornauer 2024](#dornauer-2024)

## Evidence

### Dornauer 2024

Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E. (2024). Automatic Classification of Online Discussions and Other Learning Traces to Detect Cognitive Presence. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00335-4

`q2 · i?` · `design · r2`

Machine-learning evaluation on a German-language dataset of 1,521 meaningful units from an online postgraduate course; scenario 1 used only LIWC features with SMOTE oversampling. The MLP reached "accuracy ... at 0.82" and "a Cohen's κ value of 0.76"; mean development-set accuracy was 0.81 ± 0.02. No effect size is printed, so impact is null.

> "The highest accuracy on the holdout evaluation set for the first variation of the classification based only on LIWC features was reached by the MLP classifier at 0.82, with macro average values of 0.77 and a Cohen's κ value of 0.76."

## Discussion


## Related Claims
- [Adding non-textual learning traces (attachments, glossary links, tags, formatting) did not improve cognitive presence classification accuracy](learning-traces-no-classifier-improvement.md) — related
- [SMOTEENN over- and undersampling produced significantly higher classifier accuracy (p < 0.01) than SMOTE-only scenarios, though the authors judge such classifiers not applicable in real time](smoteenn-denoising-higher-accuracy.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related

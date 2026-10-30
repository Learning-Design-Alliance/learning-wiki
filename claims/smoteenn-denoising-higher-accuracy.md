---
type: claim
title: SMOTEENN over- and undersampling produced significantly higher classifier accuracy (p < 0.01) than SMOTE-only scenarios, though the authors judge such classifiers not applicable in real time
description: SMOTEENN over- and undersampling produced significantly higher classifier accuracy (p < 0.01) than SMOTE-only scenarios, though the authors judge such classifiers not applicable in real time
id: smoteenn-denoising-higher-accuracy
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
  - id: dornauer-2024-2
    resource: "https://doi.org/10.1007/s40593-023-00335-4"
    title: "Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E. (2024). Automatic Classification of Online Discussions and Other Learning Traces to Detect Cognitive Presence. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00335-4"
    author: "Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SMOTEENN over- and undersampling produced significantly higher classifier accuracy (p < 0.01) than SMOTE-only scenarios, though the authors judge such classifiers not applicable in real time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After denoising with SMOTEENN, accuracy was significantly higher (p < 0.01, Mann–Whitney U test) than in scenarios 1 and 2. [→ Dornauer 2024](#dornauer-2024)
`q2 i?` Scenario 3 (LIWC only) reached accuracy 0.92 with Cohen's κ 0.89 (KNN) and 0.88 (MLP). [→ Dornauer 2024 (2)](#dornauer-2024-2)

## Evidence

### Dornauer 2024

Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E. (2024). Automatic Classification of Online Discussions and Other Learning Traces to Detect Cognitive Presence. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00335-4

`q2 · i?` · `design · r2`

Statistical comparison reported in the discussion comparing the denoised scenarios 3 and 4 against scenarios 1 and 2; only a p-value is printed, no effect size, so impact is null.

> "Compared to scenarios 1 and 2, this resulted in significantly higher accuracy values (p < 0.01) using a Mann–Whitney U test."

### Dornauer 2024 (2)

Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E. (2024). Automatic Classification of Online Discussions and Other Learning Traces to Detect Cognitive Presence. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00335-4

`q2 · i?` · `design · r2`

Numerical machine-learning results for scenario 3, trained on LIWC features only with SMOTEENN; KNN and MLP both reached "an accuracy of 0.92" with "Cohen's κ values were 0.89 and 0.88".

> "The KNN and MLP classifier obtained the highest accuracy in this scenario. Both methods achieved an accuracy of 0.92. The corresponding Cohen's κ values were 0.89 and 0.88."

## Discussion


## Related Claims
- [A multilayer perceptron classifier using German LIWC features classifies cognitive presence phases with accuracy of 0.82 and Cohen's κ of 0.76](german-liwc-mlp-cognitive-presence-classifier-kappa-076.md) — related
- [Adding non-textual learning traces (attachments, glossary links, tags, formatting) did not improve cognitive presence classification accuracy](learning-traces-no-classifier-improvement.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related

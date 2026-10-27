---
type: claim
title: Adding non-textual learning traces (attachments, glossary links, tags, formatting) did not improve cognitive presence classification accuracy
description: Adding non-textual learning traces (attachments, glossary links, tags, formatting) did not improve cognitive presence classification accuracy
id: learning-traces-no-classifier-improvement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
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

# Adding non-textual learning traces (attachments, glossary links, tags, formatting) did not improve cognitive presence classification accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In scenario 2, adding one-hot encoded learning traces to LIWC features left performance unchanged at accuracy 0.82 and Cohen's κ 0.76. [→ Dornauer 2024](#dornauer-2024)

## Evidence

### Dornauer 2024

Dornauer, V., Netzer, M., Kaczkó, É., Norz, L.-M., & Ammenwerth, E. (2024). Automatic Classification of Online Discussions and Other Learning Traces to Detect Cognitive Presence. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00335-4

`q2 · i?` · `design · r2`

Machine-learning comparison of scenario 2 (LIWC features plus learning traces such as glossary links, literature citations, PDF solutions, pictures, structuring, tags, URLs, videos) against scenario 1 on the same 1,521 meaningful units. The quote states "including these features did not improve the predictive ability"; no effect size is printed.

> "Interestingly, including these features did not improve the predictive ability. Our machine learning classifier also achieved "substantial" agreement here with a Cohen's κ of 0.76 (Landis & Koch, 1977)."

## Discussion


## Related Claims
- [A multilayer perceptron classifier using German LIWC features classifies cognitive presence phases with accuracy of 0.82 and Cohen's κ of 0.76](german-liwc-mlp-cognitive-presence-classifier-kappa-076.md) — related
- [SMOTEENN over- and undersampling produced significantly higher classifier accuracy (p < 0.01) than SMOTE-only scenarios, though the authors judge such classifiers not applicable in real time](smoteenn-denoising-higher-accuracy.md) — related

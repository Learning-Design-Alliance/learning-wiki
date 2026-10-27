---
type: claim
title: Lower-performing groups gain relative advantage because the scorer detects incorrect responses better for them, producing more false positives
description: Lower-performing groups gain relative advantage because the scorer detects incorrect responses better for them, producing more false positives
id: lower-performers-more-false-positives-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: nico-andersen-2025
    resource: "https://doi.org/10.1007/s40593-025-00495-5"
    title: "Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5"
    author: Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Lower-performing groups gain relative advantage because the scorer detects incorrect responses better for them, producing more false positives

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The scoring model exhibited better detection rates for incorrect responses among lower-performing groups (boys and non-native speakers), which, combined with their higher prevalence of incorrect responses, produced more false positives and overestimation for these groups. [→ Nico Andersen 2025](#nico-andersen-2025)

## Evidence

### Nico Andersen 2025

Nico Andersen, Julia Mang, Frank Goldhammer, Fabian Zehner. (2025). Algorithmic Fairness in Automatic Short Answer Scoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00495-5

`q2 · i?` · `design · r2`

Group-comparison analysis of the RoBERTa-SVM confusion matrices (Table 6): TPR was consistent across groups, but incorrect responses of lower-performing groups were better detected, yielding a higher absolute number of false positives for non-native speakers despite a slightly better FPR.

> "While the true positive rate (TPR) is consistent across all groups, the results show a minor difference in the detection rate of incorrect responses. For those incorrect responses, the scoring model exhibits better detection rates for the lower performing groups (i.e., boys and non-native speakers)."

## Discussion


## Related Claims
- [The most accurate scorer showed no gender disparity but a small significant language-background disparity favoring foreign-language speakers](language-bias-favors-foreign-speakers-roberta-svm.md) — related
- [No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model](no-consistent-fp-fn-pattern.md) — related
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](aggregate-accuracy-group-fairness-detectors.md) — related
- [AI-text detectors misclassify authentic TOEFL essays by non-native English speakers at a mean false-positive rate of 61.3% across seven detectors, far more often than native-speaker essays](detector-61-3-percent-false-positives-non-native-toefl.md) — related

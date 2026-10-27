---
type: claim
title: Science readability models classify texts substantially more accurately in a 2-level setup than in the 4-level ESO-grade setup
description: Science readability models classify texts substantially more accurately in a 2-level setup than in the 4-level ESO-grade setup
id: two-level-readability-easier-than-four-level
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
sources:
  - id: uçar-2024
    resource: "https://doi.org/10.1007/s40593-024-00393-2"
    title: "Uçar, S.-Ş., Aldabe, I., Aranberri, N., & Arruarte, A. (2024). Exploring Automatic Readability Assessment for Science Documents within a Multilingual Educational Context. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00393-2"
    author: "Uçar, S.-Ş., Aldabe, I., Aranberri, N., & Arruarte, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Science readability models classify texts substantially more accurately in a 2-level setup than in the 4-level ESO-grade setup

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Merging the four ESO grades into two stages raises accuracy for both ML and DL approaches: SVM models gain over 20 points for Basque and over 30 for Spanish and English, and DL models gain over 15 points. [→ Uçar 2024](#ucar-2024)

## Evidence

### Uçar 2024

Uçar, S.-Ş., Aldabe, I., Aranberri, N., & Arruarte, A. (2024). Exploring Automatic Readability Assessment for Science Documents within a Multilingual Educational Context. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00393-2

`q2 · i?` · `design · r2`

Cross-validation comparison of 4-level versus 2-level classification on the three compiled corpora. For the 2-level setup DL models score 81%, 89% and 86.95% accuracy for Basque, Spanish and English respectively, and 'all approaches score over 60% in accuracy.'

> "Not surprisingly, the models perform substantially better for both the feature-based ML approach and the DL approach for the 2-level setup. SVM models obtain an improvement of over 20 points for Basque and over 30 points for Spanish and English. The accuracy of the DL models increases over 15 points."

## Discussion


## Related Claims
- [4-level science readability models struggle most with distinguishing adjacent grades 1 and 2](ara-confusion-adjacent-levels-1-2.md) — related
- [Fine-tuned transformer DL models outperform feature-based SVM models for science readability classification across all three languages and configurations](dl-transformers-beat-svm-science-ara.md) — related
- [Linguistic complexity features show few clear progressions across ESO grades in the compiled science corpora](linguistic-features-lack-grade-progressions-science-corpora.md) — related
- [Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages](science-ara-models-poor-generalization-unseen-corpora.md) — related
- [Multilingual XLM-Longformer fine-tuning fails on Basque and Spanish science corpora while the English Longformer succeeds](xlm-longformer-fails-basque-spanish.md) — related

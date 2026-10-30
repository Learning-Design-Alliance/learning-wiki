---
type: claim
title: Multilingual XLM-Longformer fine-tuning fails on Basque and Spanish science corpora while the English Longformer succeeds
description: Multilingual XLM-Longformer fine-tuning fails on Basque and Spanish science corpora while the English Longformer succeeds
id: xlm-longformer-fails-basque-spanish
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
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

# Multilingual XLM-Longformer fine-tuning fails on Basque and Spanish science corpora while the English Longformer succeeds

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-tuned XLM-Longformer models scored very poorly on BasqueARA and Agrega2-Es across all configurations and setups (best accuracy 30%) and were discarded, whereas the English Longformer model achieved among the best results. [→ Uçar 2024](#ucar-2024)

## Evidence

### Uçar 2024

Uçar, S.-Ş., Aldabe, I., Aranberri, N., & Arruarte, A. (2024). Exploring Automatic Readability Assessment for Science Documents within a Multilingual Educational Context. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00393-2

`q2 · i?` · `design · r2`

Fine-tuning comparison during the experimental set-up for the multilingual Longformer variant versus language-specific BERT models. The original English-only Longformer was retained, reaching 83.66-84.61% accuracy on Agrega2-En+ in the 4-level setup.

> "It is worth mentioning here that DL models ﬁne-tuned on BasqueARA and Agrega2-Es with XLM-Longformer scored very poorly for all conﬁgurations and setups, with the best model achieving an accuracy of 30%, and were therefore discarded for further analysis."

## Discussion


## Related Claims
- [Fine-tuned transformer DL models outperform feature-based SVM models for science readability classification across all three languages and configurations](dl-transformers-beat-svm-science-ara.md) — related
- [Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages](science-ara-models-poor-generalization-unseen-corpora.md) — related
- [Science readability models classify texts substantially more accurately in a 2-level setup than in the 4-level ESO-grade setup](two-level-readability-easier-than-four-level.md) — related

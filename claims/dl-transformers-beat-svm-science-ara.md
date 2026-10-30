---
type: claim
title: Fine-tuned transformer DL models outperform feature-based SVM models for science readability classification across all three languages and configurations
description: Fine-tuned transformer DL models outperform feature-based SVM models for science readability classification across all three languages and configurations
id: dl-transformers-beat-svm-science-ara
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

# Fine-tuned transformer DL models outperform feature-based SVM models for science readability classification across all three languages and configurations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In cross-validation on the three compiled science corpora, transformer-based DL models obtain higher accuracy and F1 than SVM models in every language and configuration, improving over the SVM models by more than 20 points in the 4-level setup. [→ Uçar 2024](#ucar-2024)

## Evidence

### Uçar 2024

Uçar, S.-Ş., Aldabe, I., Aranberri, N., & Arruarte, A. (2024). Exploring Automatic Readability Assessment for Science Documents within a Multilingual Educational Context. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00393-2

`q2 · i?` · `design · r2`

Cross-validation experiments (10-fold) with SVM (SMO) and BERT-based/Longformer-based models on the three corpora. For the 4-level setup the best SVM accuracy was 62.94% (English) while the best DL accuracy was 87.33% (Longformer on English); 'all the DL models showed an improvement of over 20 points with respect to the SVM models.'

> "Overall, the results show that our feature-based ML models lag behind the DL models regardless of the language, corpus and conﬁguration tested (the balanced and unbalanced corpus, the 2-level and 4-level set-up)."

## Discussion


## Related Claims
- [Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages](science-ara-models-poor-generalization-unseen-corpora.md) — related
- [Science readability models classify texts substantially more accurately in a 2-level setup than in the 4-level ESO-grade setup](two-level-readability-easier-than-four-level.md) — related
- [Multilingual XLM-Longformer fine-tuning fails on Basque and Spanish science corpora while the English Longformer succeeds](xlm-longformer-fails-basque-spanish.md) — related
- [Linguistic complexity features show few clear progressions across ESO grades in the compiled science corpora](linguistic-features-lack-grade-progressions-science-corpora.md) — related
- [A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation](german-transformer-sag-approximates-feature-models.md) — related

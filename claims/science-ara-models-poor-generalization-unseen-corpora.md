---
type: claim
title: Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages
description: Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages
id: science-ara-models-poor-generalization-unseen-corpora
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

# Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When the best per-language models are applied to newly compiled unseen corpora (IkasElkar, Intef, NSC), accuracy drops sharply: English models fall from 86.01% cross-validation accuracy to 36.61% on NSC in the 4-level setup, and Basque DL drops from 80.60% to 70.65% in the 2-level balanced setting. [→ Uçar 2024](#ucar-2024)

## Evidence

### Uçar 2024

Uçar, S.-Ş., Aldabe, I., Aranberri, N., & Arruarte, A. (2024). Exploring Automatic Readability Assessment for Science Documents within a Multilingual Educational Context. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00393-2

`q2 · i?` · `design · r2`

Automatic evaluation of trained models on three newly compiled test corpora from proprietary and ministerial sources. In cross-validation the English best model had reached 86.01% accuracy; on unseen NSC data it reaches only 36.61% for 4-level, and 2-level Longformer reaches 73.77% (0.73 F1).

> "The English models, trained on Agrega2-En+, show the highest drop when compared to previous experiments. The best SVM model obtains an accuracy of 36.61% while the best DL model only achieves an accuracy of 36.61%."

## Discussion


## Related Claims
- [Fine-tuned transformer DL models outperform feature-based SVM models for science readability classification across all three languages and configurations](dl-transformers-beat-svm-science-ara.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — a broader claim this one bears on
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](sag-performance-varies-across-corpora.md) — a broader claim this one bears on
- [Science readability models classify texts substantially more accurately in a 2-level setup than in the 4-level ESO-grade setup](two-level-readability-easier-than-four-level.md) — related
- [Multilingual XLM-Longformer fine-tuning fails on Basque and Spanish science corpora while the English Longformer succeeds](xlm-longformer-fails-basque-spanish.md) — related

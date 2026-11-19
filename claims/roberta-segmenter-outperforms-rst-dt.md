---
type: claim
title: A RoBERTa-based discourse segmentation model outperforms prior LSTM- and BERT-based segmenters on the RST-DT test set
description: A RoBERTa-based discourse segmentation model outperforms prior LSTM- and BERT-based segmenters on the RST-DT test set
id: roberta-segmenter-outperforms-rst-dt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: matt-grenander-2021
    resource: "https://doi.org/10.1609/aaai.v35i17.17829"
    title: "Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)"
    author: Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A RoBERTa-based discourse segmentation model outperforms prior LSTM- and BERT-based segmenters on the RST-DT test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The proposed segmentation model achieves F1 of 97.5% on the RST-DT test set, outperforming Lukasik et al. (2020) (94.6) and Wang, Li, and Yang (2018) (94.3) despite a simpler formulation. [→ Matt Grenander 2021](#matt-grenander-2021)

## Evidence

### Matt Grenander 2021

Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)

`q2 · i?` · `design · r2`

Segmentation experiment trained on the RST-DT dataset (385 WSJ articles; 347 train, 38 test), reporting precision, recall and F1 on the test set. Table 2 prints Our Model at P 97.6, R 97.4, F1 97.5, versus F1 94.6 for Lukasik et al. (2020) and 94.3 for Wang, Li, and Yang (2018).

> "Our model outperforms Lukasik et al. (2020)’s model, despite using a much simpler model formulation."

## Discussion


## Related Claims
- [A RoBERTa-based discourse relation classifier achieves strong implicit relation results on PDTB 2.0 while also handling explicit relations](roberta-discourse-classifier-pdtb-implicit-sota.md) — related
- [Fine-tuning the discourse classifier on RST-DT-style segments reconciles the PDTB–RST framework mismatch and raises accuracy from 65.7% to 81.1%](rst-style-finetuning-raises-relation-accuracy.md) — related

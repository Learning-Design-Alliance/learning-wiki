---
type: claim
title: A RoBERTa-based discourse relation classifier achieves strong implicit relation results on PDTB 2.0 while also handling explicit relations
description: A RoBERTa-based discourse relation classifier achieves strong implicit relation results on PDTB 2.0 while also handling explicit relations
id: roberta-discourse-classifier-pdtb-implicit-sota
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

# A RoBERTa-based discourse relation classifier achieves strong implicit relation results on PDTB 2.0 while also handling explicit relations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On PDTB 2.0, the model reaches implicit F1 64.43 and accuracy 70.46, exceeding Dai and Huang (2018) and Liu et al. (2020), and achieves explicit F1 94.20 and accuracy 95.15. [→ Matt Grenander 2021](#matt-grenander-2021)

## Evidence

### Matt Grenander 2021

Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)

`q2 · i?` · `design · r2`

Discourse classification experiment on the PDTB 2.0 test set (around 36,000 paired sentences across 2,159 WSJ articles), evaluating implicit and explicit relations separately. Table 3 prints implicit F1 64.43 / Acc 70.46 for Our Model versus 63.39 / 69.06 for Liu et al. (2020) and 48.82 / 57.44 for Dai and Huang (2018); explicit F1 94.20 / Acc 95.15.

> "Interestingly, our model achieves similar results to Liu et al. (2020), although our model design is considerably simpler and extends to explicit relations as well."

## Discussion


## Related Claims
- [Augmenting a state-of-the-art intervention predictor with PDTB discourse features improves out-of-domain prediction of instructor intervention by 3.4% F1 on average across 14 MOOCs](pdtb-features-improve-out-of-domain-intervention-prediction.md) — related
- [With PDTB discourse features added, the combined model outperforms the EDM'15 baseline on average in the in-domain setting across 14 MOOC offerings](pdtb-features-improve-in-domain-intervention-prediction.md) — related
- [A RoBERTa-based discourse segmentation model outperforms prior LSTM- and BERT-based segmenters on the RST-DT test set](roberta-segmenter-outperforms-rst-dt.md) — related
- [Fine-tuning the discourse classifier on RST-DT-style segments reconciles the PDTB–RST framework mismatch and raises accuracy from 65.7% to 81.1%](rst-style-finetuning-raises-relation-accuracy.md) — related

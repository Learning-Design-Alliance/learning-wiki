---
type: claim
title: Dialogue features predict lexical density (content richness) of training phrases better than log features
description: Dialogue features predict lexical density (content richness) of training phrases better than log features
id: dialogue-better-predicts-lexical-density
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: conrad-borchers-2025
    resource: "https://doi.org/10.48550/arXiv.2506.11326"
    title: "Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)"
    author: Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Dialogue features predict lexical density (content richness) of training phrases better than log features

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The dialogue-only model predicted lexical density of training phrases with higher holdout AUC (0.6551) than the log-only model (0.5112). [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)

`q2 · i?` · `associational · r2`

Same held-out test-set evaluation of SBERT-embedding dialogue models versus log-feature models on intent-level outcomes; the dialogue-only model reached "AUC = 0.6551" against 0.5112 for logs on lexical density.

> "Conversely, lexical density was better captured by the dialogue-only model (AUC = 0.6551 vs. 0.5112), indicating student talk features capture the richness of their written training phrases."

## Discussion


## Related Claims
- [Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count](ablation-without-phrase-count-features.md) — related
- [Multimodal fusion improves prediction of training phrase count but not lexical density, and only marginally lexical variation](fusion-gains-outcome-dependent.md) — related
- [System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development](logs-better-predict-training-phrase-count.md) — related

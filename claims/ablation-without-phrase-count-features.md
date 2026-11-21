---
type: claim
title: Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count
description: Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count
id: ablation-without-phrase-count-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
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

# Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After removing features dependent on add-training-phrase, delete-phrase, and add-response logs, AUCs dropped to 0.6865 (log only) and 0.6759 (combined). [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)

`q2 · i?` · `associational · r2`

Ablation study reported in a reviewer-prompted footnote, recomputing holdout accuracies without phrase-count-revealing log features; log-only AUC fell to "0.6865" and combined to 0.6759 for the training phrase count outcome.

> "We performed an ablation study, recomputing these accuracies without features dependent on 'add-training-phrase', 'delete-phrase', and 'add-response'. For completeness outcome, AUCs changed to 0.6865 (log only) and 0.6759 in the combined modalities, respectively."

## Discussion


## Related Claims
- [Multimodal fusion improves prediction of training phrase count but not lexical density, and only marginally lexical variation](fusion-gains-outcome-dependent.md) — related
- [System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development](logs-better-predict-training-phrase-count.md) — related
- [Dialogue features predict lexical density (content richness) of training phrases better than log features](dialogue-better-predicts-lexical-density.md) — related
- [Ablation study: removing any component lowers evaluation AUC, and removing all additional features yields the lowest public and private AUCs](ablation-all-features-maximize-auc.md) — a broader claim this one bears on
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [Outcome measures validated via learning curves and correlations with expert ratings and end-user satisfaction](intent-quality-measures-validated.md) — related

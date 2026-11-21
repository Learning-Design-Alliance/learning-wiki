---
type: claim
title: System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development
description: System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development
id: logs-better-predict-training-phrase-count
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
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

# System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Log-based features predicted training phrase count with higher holdout AUC (0.8053) than dialogue-based features (0.5971). [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)

`q2 · i?` · `associational · r2`

Predictive modeling study of 121 collaboration sessions from 47 student pairs (94 individuals) in a 10-hour middle school AI module; feedforward neural network regression evaluated on a held-out test set with bootstrapped 95% AUC CIs, showing "log-based features (AUC = 0.8053)" outperformed dialogue features for phrase count.

> "Training phrase count was better predicted by log-based features (AUC = 0.8053) than dialogue-based features (AUC = 0.5971), suggesting system interaction logs (e.g., frequency and timing of edits) are stronger indicators of phrase production."

## Discussion


## Related Claims
- [Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count](ablation-without-phrase-count-features.md) — related
- [Dialogue features predict lexical density (content richness) of training phrases better than log features](dialogue-better-predicts-lexical-density.md) — related
- [Multimodal fusion improves prediction of training phrase count but not lexical density, and only marginally lexical variation](fusion-gains-outcome-dependent.md) — related
- [Outcome measures validated via learning curves and correlations with expert ratings and end-user satisfaction](intent-quality-measures-validated.md) — related
- [Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior](sensor-free-disengagement-detectors-accuracy.md) — related

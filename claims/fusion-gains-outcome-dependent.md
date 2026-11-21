---
type: claim
title: Multimodal fusion improves prediction of training phrase count but not lexical density, and only marginally lexical variation
description: Multimodal fusion improves prediction of training phrase count but not lexical density, and only marginally lexical variation
id: fusion-gains-outcome-dependent
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

# Multimodal fusion improves prediction of training phrase count but not lexical density, and only marginally lexical variation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The combined model did not outperform the dialogue-only model for lexical density (0.5700 vs. 0.6551). [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Xiaoyi Tian, Kristy Elizabeth Boyer, Maya Israel. (2025). Combining Log Data and Collaborative Dialogue Features to Predict Project Quality in Middle School AI Education. CSEDM'25: 9th Educational Data Mining in Computer Science Education (CSEDM) Workshop. [doi:10.48550/arXiv.2506.11326](https://doi.org/10.48550/arXiv.2506.11326)

`q2 · i?` · `associational · r2`

Same fusion evaluation for lexical density: the combined model reached "AUC = 0.5700", below the dialogue-only model's 0.6551, indicating adding log features did not help this outcome.

> "for lexical density of training phrases, the combined model (AUC = 0.5700) did not outperform the dialogue-only model (AUC = 0.6551), suggesting that log-based features provide limited insight into the content richness of learner input."

## Discussion


## Related Claims
- [Removing phrase-count-dependent log features substantially lowers predictive accuracy for training phrase count](ablation-without-phrase-count-features.md) — related
- [Dialogue features predict lexical density (content richness) of training phrases better than log features](dialogue-better-predicts-lexical-density.md) — related
- [System interaction logs predict training phrase count (productivity) better than dialogue features in collaborative middle school chatbot development](logs-better-predict-training-phrase-count.md) — related

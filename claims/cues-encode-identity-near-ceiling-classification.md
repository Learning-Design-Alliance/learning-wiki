---
type: claim
title: Dialogue-derived interactional cues robustly encode ground-truth identity, achieving near-ceiling AI identification under cross-validation
description: Dialogue-derived interactional cues robustly encode ground-truth identity, achieving near-ceiling AI identification under cross-validation
id: cues-encode-identity-near-ceiling-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lixiang-yan-2026
    resource: "https://doi.org/10.48550/arxiv.2605.23426"
    title: "Lixiang Yan, Yueqiao Jin, Xibin Han, Dragan Gasevic. (2026). Socially fluent AI decouples conversational signals from source identity in online interaction. https://arxiv.org/abs/2605.23426 [doi:10.48550/arxiv.2605.23426](https://doi.org/10.48550/arxiv.2605.23426)"
    author: Lixiang Yan, Yueqiao Jin, Xibin Han, Dragan Gasevic
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Dialogue-derived interactional cues robustly encode ground-truth identity, achieving near-ceiling AI identification under cross-validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` A Top-1 identification analysis correctly identified the AI teammate in 95.3% of triads, far exceeding the 33.3% chance baseline, and performance remained high when timing features were excluded. [→ Lixiang Yan 2026](#lixiang-yan-2026)

## Evidence

### Lixiang Yan 2026

Lixiang Yan, Yueqiao Jin, Xibin Han, Dragan Gasevic. (2026). Socially fluent AI decouples conversational signals from source identity in online interaction. https://arxiv.org/abs/2605.23426 [doi:10.48550/arxiv.2605.23426](https://doi.org/10.48550/arxiv.2605.23426)

`q3 · i?` · `causal · r2`

A Top-1 identification analysis per triad "correctly identified the AI teammate in 95.3% of triads" (95% CI [0.91, 1.00]) versus a 33.3% chance baseline; performance remained comparably high without timing features (96.6%). Permutation tests confirmed the observed AUC lay far in the upper tail (p < .001).

> "At the group level, a Top-1 identification analysis, selecting the single teammate with the highest predicted probability per triad, correctly identified the AI teammate in 95.3% of triads (95% CI [0.91, 1.00]), far exceeding the chance baseline of 33.3%."

## Discussion


## Related Claims
- [Participants fail to distinguish undisclosed AI teammates from human teammates above chance in synchronous text-based group interaction](chance-level-ai-identity-detection-undisclosed-teammates.md) — reports the opposite
- [Judgment-truth dissociation: the same cues that predict ground-truth identity are only weakly incorporated into explicit identity judgments](judgment-truth-dissociation-cues.md) — related
- [Systems adapt to the specified learner persona in ways human raters can perceive, scoring well above chance in persona identification](persona-adaptation-perceptible-to-raters.md) — related

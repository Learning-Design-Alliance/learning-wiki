---
type: claim
title: Frontal EEG spectral activity shows no statistically significant differences across AI interaction modes or between with-AI and no-AI conditions
description: Frontal EEG spectral activity shows no statistically significant differences across AI interaction modes or between with-AI and no-AI conditions
id: no-significant-eeg-differences-across-ai-modes
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: kashika-khurana-and-ally-liew-2026
    resource: "https://www.kaggle.com/datasets/allyliew/participant-data"
    title: "Kashika Khurana and Ally Liew. (2026). An exploratory behavioral and electroencephalographic study of artificial intelligence-assisted learning modes in high school students. https://www.kaggle.com/datasets/allyliew/participant-data"
    author: Kashika Khurana and Ally Liew
    q: 2
    i: 0
    kind: causal
    rigour: 2
  - id: kashika-khurana-and-ally-liew-2026-2
    resource: "https://www.kaggle.com/datasets/allyliew/participant-data"
    title: "Kashika Khurana and Ally Liew. (2026). An exploratory behavioral and electroencephalographic study of artificial intelligence-assisted learning modes in high school students. https://www.kaggle.com/datasets/allyliew/participant-data"
    author: Kashika Khurana and Ally Liew
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Frontal EEG spectral activity shows no statistically significant differences across AI interaction modes or between with-AI and no-AI conditions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i0` negligible

## Subclaims
`q2 i0` A paired t-test comparing with-AI and no-AI conditions found no significant difference, with a negligible printed effect size (Cohen's d = -0.037). [→ Kashika Khurana and Ally Liew 2026](#kashika-khurana-and-ally-liew-2026)
`q2 i?` One-way repeated-measures ANOVAs across all six EEG bands found no statistically significant differences across AI modes (all p > 0.29). [→ Kashika Khurana and Ally Liew 2026 (2)](#kashika-khurana-and-ally-liew-2026-2)

## Evidence

### Kashika Khurana and Ally Liew 2026

Kashika Khurana and Ally Liew. (2026). An exploratory behavioral and electroencephalographic study of artificial intelligence-assisted learning modes in high school students. https://www.kaggle.com/datasets/allyliew/participant-data

`q2 · i0` · `causal · r2`

Paired t-test of frontal EEG spectral power (AI vs. no-AI) in the within-subject EEG study of 48 participants, reported in the statistical test results table with p-value = 0.823 and Cohen's d = -0.037. The authors report "no significant differences were observed between the with-AI and no-AI conditions."

> "No significant differences were observed between the with-AI and no-AI conditions, as a negative effect size emerged."

### Kashika Khurana and Ally Liew 2026 (2)

Kashika Khurana and Ally Liew. (2026). An exploratory behavioral and electroencephalographic study of artificial intelligence-assisted learning modes in high school students. https://www.kaggle.com/datasets/allyliew/participant-data

`q2 · i?` · `causal · r2`

One-way repeated-measures ANOVA across the three AI modes for all six frequency bands (gamma, beta, alpha, theta, delta, SMR), all with p-values above 0.29. The authors report the null hypothesis was not rejected, so no post-hoc inference was applied and EEG findings are descriptive only.

> "Stable p-value failed to reject the null hypothesis. This means no statistically significant differences observed across AI modes."

## Discussion


## Related Claims
- [AI interaction mode (Tutor, Collaborator, Solver) significantly influences high school students' observed behavior during problem-solving](ai-interaction-mode-significantly-influences-observed-behavior.md) — related
- [Engagement-index EEG metrics show no significant differences across AI modes, and a possible short-term AI carryover effect remains unconfirmed](engagement-index-null-and-unconfirmed-carryover.md) — related
- [Tutor mode elicits more stress-related behaviors than Collaborator and Solver modes, which do not differ from each other](tutor-mode-elicits-more-stress-behaviors.md) — related

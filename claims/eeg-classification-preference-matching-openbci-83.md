---
type: claim
title: "EEG theta and alpha spectral features classify preference-matched versus mismatched instructional epochs at 83.21% accuracy with OpenBCI hardware"
description: "EEG theta and alpha spectral features classify preference-matched versus mismatched instructional epochs at 83.21% accuracy with OpenBCI hardware"
id: eeg-classification-preference-matching-openbci-83
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-11-22
recheck_by: 2029
sources:
  - id: adusumilli-2026
    resource: "https://doi.org/10.1109/icalt68022.2026.00126"
    title: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. [doi:10.1109/icalt68022.2026.00126](https://doi.org/10.1109/icalt68022.2026.00126)"
    author: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: adusumilli-2026-2
    resource: "https://doi.org/10.1109/icalt68022.2026.00126"
    title: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. [doi:10.1109/icalt68022.2026.00126](https://doi.org/10.1109/icalt68022.2026.00126)"
    author: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# EEG theta and alpha spectral features classify preference-matched versus mismatched instructional epochs at 83.21% accuracy with OpenBCI hardware

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-22 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Adusumilli 2026 (2): no comparison group (read from the study by two models, 2026-11-22)

## Subclaims
`q2 i?` A binary logistic regression classifier with LOPOCV distinguished matched from mismatched epochs at 83.21% mean accuracy (95% CI: 82.42-84.04) using OpenBCI data. [→ Adusumilli 2026](#adusumilli-2026)
`q2 i?` The consumer-grade Emotiv EpocX achieved only 56.27% accuracy, near chance, in the same classification task. [→ Adusumilli 2026 (2)](#adusumilli-2026-2)

## Evidence

### Adusumilli 2026

Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. [doi:10.1109/icalt68022.2026.00126](https://doi.org/10.1109/icalt68022.2026.00126)

`q2 · i?` · `causal · r1`

Classification analysis of EEG epochs from the neurophysiological subsample (n=8) under LOPOCV; spectral power in theta (4-8 Hz) and alpha (8-13 Hz) bands carried the discriminative information. No effect size printed. Accuracy is not an effect size, so impact is coded i? (no magnitude reported; not a null effect).

> "the OpenBCI system achieved a mean classification accuracy of83.21%(95% CI: [82.42, 84.04]), substantially exceeding the theoretical chance baseline of 50%."

### Adusumilli 2026 (2)

Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. [doi:10.1109/icalt68022.2026.00126](https://doi.org/10.1109/icalt68022.2026.00126)

`q2 · i?` · `causal · r1`

Same binary logistic regression LOPOCV task on Emotiv EpocX data from the parallel-instrumented participants; the printed accuracy of "56.27%" is near the 50% chance baseline. Impact null, as accuracy is not an effect size.

> "the consumer-grade Emotiv EpocX yielded only marginal predictive power (56.27%), hovering just above chance."

## Discussion


## Related Claims
- [Subjective preference modulates neural engagement states (theta/alpha patterns) even though it does not optimize test performance](preference-modulates-neural-engagement-not-performance.md) — related
- [MRMR feature ranking identifies occipital alpha PSD as the most discriminative feature, followed by frontal gamma, high-beta, and theta](mrmr-occipital-alpha-top-feature.md) — related
- [Temporal leakage from shuffled neighboring epochs inflates EEG familiarity classification, with peak weighted F1 dropping from 0.9853 (CNN, stratified) to 0.6038 (CNN, Group K-Fold)](temporal-leakage-inflates-eeg-familiarity-classification.md) — related

---
type: claim
title: ERP and alpha-band EEG signals decode old vs new faces above chance, with the high-alpha band more discriminative than the low-alpha band
description: ERP and alpha-band EEG signals decode old vs new faces above chance, with the high-alpha band more discriminative than the low-alpha band
id: erp-alpha-band-decoding-old-new-faces
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: guoyang-liu-2025
    resource: "https://doi.org/10.1038/s41539-025-00316-3"
    title: "Guoyang Liu, Yueyuan Zheng, Michelle Hei Lam Tsang, Yazhou Zhao & Janet H. Hsiao. (2025). Understanding the role of eye movement pattern and consistency during face recognition through EEG decoding. npj Science of Learning. https://doi.org/10.1038/s41539-025-00316-3"
    author: "Guoyang Liu, Yueyuan Zheng, Michelle Hei Lam Tsang, Yazhou Zhao & Janet H. Hsiao"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: guoyang-liu-2025-2
    resource: "https://doi.org/10.1038/s41539-025-00316-3"
    title: "Guoyang Liu, Yueyuan Zheng, Michelle Hei Lam Tsang, Yazhou Zhao & Janet H. Hsiao. (2025). Understanding the role of eye movement pattern and consistency during face recognition through EEG decoding. npj Science of Learning. https://doi.org/10.1038/s41539-025-00316-3"
    author: "Guoyang Liu, Yueyuan Zheng, Michelle Hei Lam Tsang, Yazhou Zhao & Janet H. Hsiao"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# ERP and alpha-band EEG signals decode old vs new faces above chance, with the high-alpha band more discriminative than the low-alpha band

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ERP decoding was significantly above chance from 440 ms, peaking at AUC 0.56 at 720 ms. [→ Guoyang Liu 2025](#guoyang-liu-2025)
`q2 i?` High-alpha band decoding was above chance from 720–2020 ms with peak AUC 0.54 at 1080 ms, and contained more discriminative features than the low-alpha band (peak AUC 0.53 at 1240 ms). [→ Guoyang Liu 2025 (2)](#guoyang-liu-2025-2)

## Evidence

### Guoyang Liu 2025

Guoyang Liu, Yueyuan Zheng, Michelle Hei Lam Tsang, Yazhou Zhao & Janet H. Hsiao. (2025). Understanding the role of eye movement pattern and consistency during face recognition through EEG decoding. npj Science of Learning. https://doi.org/10.1038/s41539-025-00316-3

`q2 · i?` · `associational · r2`

Group-level SVM decoding of ERP amplitude features (0.5–6 Hz) across 84 participants. The article reports decoding "signiﬁcantly higher than the chance level from 440 ms" with "the peak AUC of 0.56 at 720 ms", followed by a sharp drop to 940 ms.

> "the average decoding AUC over all participants was signiﬁcantly higher than the chance level from 440 ms and quickly reached the peak AUC of 0.56 at 720 ms."

### Guoyang Liu 2025 (2)

Guoyang Liu, Yueyuan Zheng, Michelle Hei Lam Tsang, Yazhou Zhao & Janet H. Hsiao. (2025). Understanding the role of eye movement pattern and consistency during face recognition through EEG decoding. npj Science of Learning. https://doi.org/10.1038/s41539-025-00316-3

`q2 · i?` · `associational · r2`

Group-level SVM decoding of high-alpha (10–12 Hz) instantaneous power across 84 participants: above-chance AUC from 720–2020 ms and 2060–2160 ms, "the peak AUC of 0.54 occurring at 1080 ms". The low-alpha band peaked at AUC 0.53 at 1240 ms, leading the authors to conclude the high-alpha band contained more discriminative features.

> "For the high-alpha band decoding, the time period with above-chance AUC was found from 720 ms to 2020 ms, as well as from 2060 ms to 2160 ms, with the peak AUC of 0.54 occurring at 1080 ms."

## Discussion


## Related Claims
- [Decoding results are not confounded by oculomotor artifacts: raw eye movement, fixation, and EOG data fail to decode old vs new faces](decoding-not-oculomotor-confound.md) — related
- [A more eye-focused eye movement pattern is associated with higher EEG decoding accuracy for old vs new faces in the high-alpha band](eyes-focused-pattern-higher-high-alpha-decoding-accuracy.md) — related
- [Familiarity recognition is represented by a distributed multivariate spatial-spectral pattern rather than localized single-feature shifts, necessitating multivariate machine learning](multivariate-distributed-familiarity-pattern.md) — a broader claim this one bears on
- [Trial-level spectral features robustly differentiate stimulus domains (faces vs. equations) but no familiarity-driven spectral shift survives FDR correction](domain-robust-familiarity-subtle-univariate-eeg.md) — related
- [Domain-separated EEG classifiers decode familiarity within each stimulus category, with peak LOGO Mean Recall of 0.8992 for faces-only (HistGradient Boosting) and 0.8670 for equations-only (CNN)](domain-separated-eeg-familiarity-decoding.md) — related
- [Higher eye movement consistency is associated with shorter peak latency of high-alpha decoding accuracy, reflecting more efficient neural representation development](eye-movement-consistency-shorter-decoding-latency.md) — related
- [Higher eye movement consistency is associated with higher ERP decoding accuracy and faster face recognition responses](consistency-erp-decoding-accuracy-faster-responses.md) — related
- [Random Forest and SHAP analyses identify Gamma and Beta band power at temporal and frontal channels (T3, P3, F7, T4, T4, F8, F7) as the most critical features for EEG familiarity classification](gamma-beta-temporal-frontal-familiarity-biomarkers.md) — related
- [SVM weight topography shows central and parietal electrodes contribute most to decoding, with eyes-focused participants showing more right-central contribution](svm-topography-central-parietal-eyes-right-bias.md) — related

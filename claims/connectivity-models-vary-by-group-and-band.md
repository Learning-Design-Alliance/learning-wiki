---
type: claim
title: EEG functional-connectivity classification models of CRA correctness differ by tDCS group and frequency band, with alpha-band models underperforming beta-band models specifically in the L+R− group
description: EEG functional-connectivity classification models of CRA correctness differ by tDCS group and frequency band, with alpha-band models underperforming beta-band models specifically in the L+R− group
id: connectivity-models-vary-by-group-and-band
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: xie-2024
    resource: "https://doi.org/10.1038/s41539-024-00285-z"
    title: "Xie, C., Zhang, S., Qiao, X., & Hao, N. (2024). Transcranial direct current stimulation targeting the bilateral IFG alters cognitive processes during creative ideation. npj Science of Learning, 9, 75. https://doi.org/10.1038/s41539-024-00285-z"
    author: "Xie, C., Zhang, S., Qiao, X., & Hao, N."
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: xie-2024-2
    resource: "https://doi.org/10.1038/s41539-024-00285-z"
    title: "Xie, C., Zhang, S., Qiao, X., & Hao, N. (2024). Transcranial direct current stimulation targeting the bilateral IFG alters cognitive processes during creative ideation. npj Science of Learning, 9, 75. https://doi.org/10.1038/s41539-024-00285-z"
    author: "Xie, C., Zhang, S., Qiao, X., & Hao, N."
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
---

# EEG functional-connectivity classification models of CRA correctness differ by tDCS group and frequency band, with alpha-band models underperforming beta-band models specifically in the L+R− group

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Group and frequency band exert significant effects on classification AUC. [→ Xie 2024](#xie-2024)
`q3 i?` Within the L+R− group, alpha-band models significantly underperform beta-band models. [→ Xie 2024 (2)](#xie-2024-2)

## Evidence

### Xie 2024

Xie, C., Zhang, S., Qiao, X., & Hao, N. (2024). Transcranial direct current stimulation targeting the bilateral IFG alters cognitive processes during creative ideation. npj Science of Learning, 9, 75. https://doi.org/10.1038/s41539-024-00285-z

`q3 · i?` · `causal · r2`

Two-way ANOVA over 480 nested-ensemble classification models (80 per group per band) built from task-related phase-locking connectivity; the quote reports the significant group and band effects on AUC, with the group×band interaction approaching significance (F2,474 = 2.68, p = 0.07).

> "According to the ANOVA results presented in Fig.2a, both the group factor ( F2,474 = 24.64, p < 0.001, ηp 2 = 0.094) and the frequency band (F1,474 = 31.68, p < 0.001, ηp 2 = 0.063) exerted signiﬁcant effects on AUC"

### Xie 2024 (2)

Xie, C., Zhang, S., Qiao, X., & Hao, N. (2024). Transcranial direct current stimulation targeting the bilateral IFG alters cognitive processes during creative ideation. npj Science of Learning, 9, 75. https://doi.org/10.1038/s41539-024-00285-z

`q3 · i?` · `causal · r?`

Post-hoc comparison within the L+R− group of model AUCs; the authors report alpha-band models "under- performed compared to those based on beta band data" (t474 = −5.08, Bonferroni-corrected p < 0.001), attributing overall model-performance differences to variance within this group.

> "it was observed that speciﬁcally in the L+R− group, models based on alpha band data signiﬁcantly under- performed compared to those based on beta band data"

## Discussion


## Related Claims
- [Frontal lateralization of classification-model activity differs by tDCS group: reversed (left-dominant) alpha-band lateralization after L+R− and reduced left prefrontal beta-band engagement after L−R+](frontal-lateralization-shifts-after-tdcs.md) — related
- [The relationship between RSD and CRA reaction time differs by tDCS group: U-shaped under Sham, monotonically decreasing under L−R+, and no clear relationship under L+R−](rsd-rt-relationship-varies-by-tdcs-group.md) — related
- [tDCS over the bilateral IFG does not change overall CRA convergent-thinking performance compared across stimulation groups](tdcs-bilateral-ifg-no-overall-cra-change.md) — related
- [HD-tDCS facilitated and enhanced training-induced increases in frontal task-related theta, alpha, beta, and gamma power](tdcs-enhances-task-related-eeg-power-gains.md) — related

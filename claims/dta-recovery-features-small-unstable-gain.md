---
type: claim
title: Recovery-related behavioral features add only a small, unstable held-out Macro-F1 gain for final-success prediction in DTA logs (0.725 to 0.743), with negligible average window-sensitivity differences
description: Recovery-related behavioral features add only a small, unstable held-out Macro-F1 gain for final-success prediction in DTA logs (0.725 to 0.743), with negligible average window-sensitivity differences
id: dta-recovery-features-small-unstable-gain
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: wang-s-and-zhao-j-2026
    title: Wang S and Zhao J 2026
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: wang-s-and-zhao-j-2026-2
    title: Wang S and Zhao J 2026 (2)
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Recovery-related behavioral features add only a small, unstable held-out Macro-F1 gain for final-success prediction in DTA logs (0.725 to 0.743), with negligible average window-sensitivity differences

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r2` · `q2`

## Subclaims
`q2 i?` On the untouched held-out split, Baseline + Reflective increased final-success Macro-F1 from 0.725 to 0.743 and changed the Brier score from 0.177 to 0.175; the article states these differences are small and not educationally important. [→ Wang S and Zhao J 2026](#wang-s-and-zhao-j-2026)
`q2 i?` Across repeated and calendar-window sensitivity analyses the reflective-feature Macro-F1 difference was negligible (mean difference 0.006 in the repeated analysis; between –0.001 and 0.002 across 30%–50% windows). [→ Wang S and Zhao J 2026 (2)](#wang-s-and-zhao-j-2026-2)

## Evidence

### Wang S and Zhao J 2026

Wang S and Zhao J (2026) Reflective AI use and student engagement in AI-supported programming: technology acceptance, programming self-efficacy, and behavioral trace evidence. Front. Psychol. 17:1929887. https://doi.org/10.3389/fpsyg.2026.1929887

`q2 · i?` · `associational · r2`

Held-out comparison on the DTA programming-log dataset (N = 1,423; early-window N = 1,122) using a locked pipeline with a stratified 70%/30% split. The article reports "For ﬁnal_success_all_11, Baseline + Reﬂective increased Macro-F1 from 0.725 to 0.743"; the Full Model reached the highest ROC-AUC (0.808) but did not outperform all configurations across all metrics.

> "For ﬁnal_success_all_11, Baseline + Reﬂective increased Macro-F1 from 0.725 to 0.743 and changed the Brier score from 0.177 to 0.175. These absolute diﬀerences are small and are not evidence of educationally important improvement."

### Wang S and Zhao J 2026 (2)

Wang S and Zhao J (2026) Reflective AI use and student engagement in AI-supported programming: technology acceptance, programming self-efficacy, and behavioral trace evidence. Front. Psychol. 17:1929887. https://doi.org/10.3389/fpsyg.2026.1929887

`q2 · i?` · `associational · r2`

Repeated five-fold cross-validation and 30%–50% calendar-window sensitivity analyses with locked learner specifications. The article reports "The original repeated analysis showed a mean diﬀerence of 0.006" and that the reflective-feature Macro-F1 difference remains between –0.001 and 0.002 as the window expands, so the held-out 0.018 difference should not be generalized as a stable practical gain.

> "The original repeated analysis showed a mean diﬀerence of 0.006, whereas the calendar-window rerununderthecurrentlockedpipelineshoweda40%diﬀerenceof 0.001."

## Discussion


## Related Claims

- [For activity-defined engagement prediction in DTA logs, the activity-only Baseline remained strongest, and permutation importance was dominated by activity indicators](activity-baseline-strongest-engagement-prediction.md) — related

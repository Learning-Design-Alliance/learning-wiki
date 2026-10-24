---
type: claim
title: PTA traits significantly predict per-session success in the SWE-Chat developer corpus beyond a prior-outcome baseline
description: PTA traits significantly predict per-session success in the SWE-Chat developer corpus beyond a prior-outcome baseline
id: pta-traits-predict-swe-chat-session-success
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: hunter-mcnichols-2026
    resource: "https://doi.org/10.48550/arxiv.2608.11460"
    title: "Hunter McNichols, Kai Du, Andrew Lan. (2026). PRINCIPAL TRAIT ANALYSIS: TOWARDS DERIVING \"SKILLS\" IN HUMAN-AI COLLABORATION. A preprint - August 13, 2026. https://arxiv.org/abs/2608.11460 [doi:10.48550/arxiv.2608.11460](https://doi.org/10.48550/arxiv.2608.11460)"
    author: Hunter McNichols, Kai Du, Andrew Lan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# PTA traits significantly predict per-session success in the SWE-Chat developer corpus beyond a prior-outcome baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In difficulty-aligned held-out regressions on SWE-Chat, adding 10 PTA traits yields consistently significant predictive R2 improvements over the prior-outcome baseline (lens-ensemble ΔR2 +0.048, p<.001). [→ Hunter McNichols 2026](#hunter-mcnichols-2026)

## Evidence

### Hunter McNichols 2026

Hunter McNichols, Kai Du, Andrew Lan. (2026). PRINCIPAL TRAIT ANALYSIS: TOWARDS DERIVING "SKILLS" IN HUMAN-AI COLLABORATION. A preprint - August 13, 2026. https://arxiv.org/abs/2608.11460 [doi:10.48550/arxiv.2608.11460](https://doi.org/10.48550/arxiv.2608.11460)

`q2 · i?` · `associational · r2`

Predictive regression on the SWE-Chat corpus (2,774 sessions from developers with at least two sessions) using an item-response-theory-style difficulty-aligned model with 4-fold cross-validation across collaborators; Table 1 reports ΔR2 of +0.048 (p<.001) for the lens-ensemble pool and +0.035 (p<.001) for the generic pool.

> "On the SWE-chat dataset, we observe that PTA derived traits provide stronger behavior signals that are predictive of session outcome. Given the more granular task of session outcome prediction, the SWE-Chat dataset has an order of magnitude more samples than StudyChat, an we observe consistently significant predictive improvements over the baseline prior."

## Discussion


## Related Claims
- [PTA traits show stronger statistical explanatory power than dialogue-act and Bloom's taxonomy coded baselines on StudyChat](pta-traits-beat-dialogue-act-bloom-baselines.md) — related
- [PTA-derived traits significantly improve explained exam-score variance over a prior-outcome baseline in one semester of StudyChat but not the other](pta-traits-explain-studychat-exam-variance-semester-inconsistent.md) — related
- [In SWE-Chat, traits where developers give the agent a clear role correlate positively with session success while evidence-based oversight traits correlate negatively](swe-chat-clear-role-positive-evidence-oversight-negative.md) — related

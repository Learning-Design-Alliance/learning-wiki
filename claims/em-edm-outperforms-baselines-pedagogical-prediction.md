---
type: claim
title: EM-EDM outperforms AL and DRL baselines on predicting student pedagogical decisions with as few as 24 expert demonstrations
description: EM-EDM outperforms AL and DRL baselines on predicting student pedagogical decisions with as few as 24 expert demonstrations
id: em-edm-outperforms-baselines-pedagogical-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: md-mirajul-islam-2026
    resource: "https://doi.org/10.48550/arXiv.2610.28716"
    title: "Md Mirajul Islam. (2026). Offline Apprenticeship Learning for Human-Centric Environments. Doctoral dissertation, North Carolina State University. [doi:10.48550/arXiv.2610.28716](https://doi.org/10.48550/arXiv.2610.28716)"
    author: Md Mirajul Islam
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# EM-EDM outperforms AL and DRL baselines on predicting student pedagogical decisions with as few as 24 expert demonstrations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` EM-EDM, an Expectation-Maximization framework built on Energy-based Distribution Matching, simultaneously clusters demonstrations by latent reward functions and induces cluster-specific policies, outperforming four AL baselines and two DRL baselines on student pedagogical decision prediction even with as few as 24 expert demonstrations. [→ Md Mirajul Islam 2026](#md-mirajul-islam-2026)

## Evidence

### Md Mirajul Islam 2026

Md Mirajul Islam. (2026). Offline Apprenticeship Learning for Human-Centric Environments. Doctoral dissertation, North Carolina State University. [doi:10.48550/arXiv.2610.28716](https://doi.org/10.48550/arXiv.2610.28716)

`q2 · i?` · `design · r2`

Retrospective evaluation of the EM-EDM framework on ITS tutoring logs with continuous state spaces of over 140 features, comparing against AL and DRL baselines on pedagogical action prediction; the article reports EM-EDM "outperforms four state-of-the-art AL baselines and two DRL baselines" with as few as 24 demonstrations. No effect size is printed.

> "Even with as few as 24 expert demonstrations, EM-EDM outperforms four state-of-the-art AL baselines and two DRL baselines on predicting student pedagogical decisions."

## Discussion


## Related Claims
- [THEMES, which models temporally evolving reward functions via sub-trajectory partitioning, consistently outperforms flat and hierarchical AL baselines across educational and clinical datasets](themes-evolving-rewards-outperforms-baselines.md) — related
- [CCHAL, combining decision-level outcome attribution, dual-arm contrastive criticality scoring, and Bradley-Terry contrastive IRL over failures, outperforms flat and hierarchical AL baselines including HALIDE](cchal-decision-level-criticality-outperforms-halide.md) — related

---
type: claim
title: CCHAL, combining decision-level outcome attribution, dual-arm contrastive criticality scoring, and Bradley-Terry contrastive IRL over failures, outperforms flat and hierarchical AL baselines including HALIDE
description: CCHAL, combining decision-level outcome attribution, dual-arm contrastive criticality scoring, and Bradley-Terry contrastive IRL over failures, outperforms flat and hierarchical AL baselines including HALIDE
id: cchal-decision-level-criticality-outperforms-halide
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
    rigour: 3
---

# CCHAL, combining decision-level outcome attribution, dual-arm contrastive criticality scoring, and Bradley-Terry contrastive IRL over failures, outperforms flat and hierarchical AL baselines including HALIDE

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` CCHAL distributes trajectory-level demonstration ranks to per-decision weights via Bayesian credit assignment, scores each decision's criticality by contrasting expert against non-expert behavior in a dual-arm design, and sharpens reward learning with a Bradley-Terry pairwise contrastive IRL objective over failure trajectories, outperforming flat and hierarchical AL baselines including its direct predecessor HALIDE. [→ Md Mirajul Islam 2026](#md-mirajul-islam-2026)

## Evidence

### Md Mirajul Islam 2026

Md Mirajul Islam. (2026). Offline Apprenticeship Learning for Human-Centric Environments. Doctoral dissertation, North Carolina State University. [doi:10.48550/arXiv.2610.28716](https://doi.org/10.48550/arXiv.2610.28716)

`q2 · i?` · `design · r3`

Evaluation across three clinical EHR datasets and one student ITS dataset (Table 6.2 includes an ablation study of CCHAL variants); the article reports CCHAL "outperforms flat and hierarchical AL baselines, including its direct predecessor HALIDE". No effect size is printed.

> "Evaluated across three clinical EHR datasets and a student ITS dataset, CCHAL outperforms flat and hierarchical AL baselines, including its direct predecessor HALIDE, establishing that decision-level outcome attribution and behavioral criticality are both necessary to fully exploit demonstration quality signals."

## Discussion


## Related Claims
- [THEMES, which models temporally evolving reward functions via sub-trajectory partitioning, consistently outperforms flat and hierarchical AL baselines across educational and clinical datasets](themes-evolving-rewards-outperforms-baselines.md) — related
- [In HALIDE, incorporating suboptimal demonstrations without quality-aware ranking degrades performance, while ranked hierarchical learning yields consistent cross-semester generalization gains](halide-ranked-mixed-quality-demonstrations.md) — related
- [EM-EDM outperforms AL and DRL baselines on predicting student pedagogical decisions with as few as 24 expert demonstrations](em-edm-outperforms-baselines-pedagogical-prediction.md) — related

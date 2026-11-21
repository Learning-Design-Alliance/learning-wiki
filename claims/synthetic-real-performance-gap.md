---
type: claim
title: Agents trained exclusively on synthetic data perform well in simulated environments but show measurable gaps against human assessments in real-world settings
description: Agents trained exclusively on synthetic data perform well in simulated environments but show measurable gaps against human assessments in real-world settings
id: synthetic-real-performance-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhang-2025
    resource: "https://doi.org/10.48550/arXiv.2502.06371"
    title: "Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)"
    author: "Zhang, L., Zhang, M., Wang, W. L., & Luo, Y."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Agents trained exclusively on synthetic data perform well in simulated environments but show measurable gaps against human assessments in real-world settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The synthetic-data-trained agent achieved superior results in simulated environments yet showed measurable gaps compared to human assessments in real-world applications. [→ Zhang 2025](#zhang-2025)

## Evidence

### Zhang 2025

Zhang, L., Zhang, M., Wang, W. L., & Luo, Y. (2025). Simulation as Reality? The Effectiveness of LLM-Generated Data in Open-ended Question Assessment. [doi:10.48550/arXiv.2502.06371](https://doi.org/10.48550/arXiv.2502.06371)

`q1 · i?` · `design · r2`

Authors' interpretation in the Discussion of the two-phase results: the agent trained only on synthetic data excelled in synthetic contexts but underperformed relative to teacher assessments on real student answers. No effect size is printed for the gap; this is the authors' explanatory claim, not a tested comparison.

> "The simulation-trained assessment agent consistently achieved superior results in simulative environments by synthetic, yet showed measurable gaps when compared to human assessments in real-world applications."

## Discussion


## Related Claims
- [Models trained on synthetic classroom incident data transfer zero-shot to real-world footage, with the proposed method best at 63.41% though a synthetic-to-real domain gap remains](zero-shot-synthetic-to-real-classroom-incident-transfer.md) — a broader claim this one bears on
- [GPT-4o outperformed the agent on Theories and Relationships Top1 accuracy and NDCG, the agent's weakest real-world category](theories-relationships-gpt4o-advantage.md) — related

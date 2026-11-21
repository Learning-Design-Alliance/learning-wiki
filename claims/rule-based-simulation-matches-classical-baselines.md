---
type: claim
title: Rule-based simulated cognitive structures alone nearly match or slightly surpass classical KT and CD baselines
description: Rule-based simulated cognitive structures alone nearly match or slightly surpass classical KT and CD baselines
id: rule-based-simulation-matches-classical-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: hengnian-gu-2025
    resource: "https://doi.org/10.48550/arXiv.2508.12647"
    title: "Hengnian Gu, Zhifu Chen, Yuxin Chen, Jin Peng Zhou, and Dongdai Zhou. (2025). Cognitive Structure Generation: From Educational Priors to Policy Optimization. arXiv preprint. [doi:10.48550/arXiv.2508.12647](https://doi.org/10.48550/arXiv.2508.12647)"
    author: Hengnian Gu, Zhifu Chen, Yuxin Chen, Jin Peng Zhou, and Dongdai Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Rule-based simulated cognitive structures alone nearly match or slightly surpass classical KT and CD baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Variant V1, which uses only rule-based simulated structures with educational priors, nearly matches or slightly surpasses DKT in KT and IRT/NCD in CD. [→ Hengnian Gu 2025](#hengnian-gu-2025)

## Evidence

### Hengnian Gu 2025

Hengnian Gu, Zhifu Chen, Yuxin Chen, Jin Peng Zhou, and Dongdai Zhou. (2025). Cognitive Structure Generation: From Educational Priors to Policy Optimization. arXiv preprint. [doi:10.48550/arXiv.2508.12647](https://doi.org/10.48550/arXiv.2508.12647)

`q2 · i?` · `design · r2`

Ablation variant V1 trains downstream KT/CD models directly on the rule-based simulated structure set across the four datasets. The authors write that "the embedded educational priors provide a reasonable approximation of student learning states".

> "For variant V1, performance nearly matches or even slightly surpasses classical baselines (e.g., DKT in KT and IRT, NCD in CD), demonstrating the effectiveness of our rule-based cognitive structure simulation."

## Discussion


## Related Claims
- [CSG-CD significantly outperforms classical, neural and graph-based cognitive diagnosis baselines across four datasets](csg-cd-outperforms-cd-baselines.md) — related
- [CSG-KT significantly outperforms classical, graph-based and SOTA knowledge tracing baselines across four real-world datasets](csg-kt-outperforms-kt-baselines.md) — related
- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — related

---
type: claim
title: In the EduAgent framework, removing past cognitive states from memory significantly reduced simulation performance
description: In the EduAgent framework, removing past cognitive states from memory significantly reduced simulation performance
id: eduagent-ablation-contextual-memory-critical
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: luis-marquez-carpintero-2025
    resource: "https://doi.org/10.48550/arxiv.2511.06078"
    title: "Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla. (2025). Simulating Students with Large Language Models: A Review of Architecture, Mechanisms, and Role Modelling in Education with Generative AI. https://arxiv.org/abs/2511.06078 [doi:10.48550/arxiv.2511.06078](https://doi.org/10.48550/arxiv.2511.06078)"
    author: Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# In the EduAgent framework, removing past cognitive states from memory significantly reduced simulation performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Ablation studies in the EduAgent preprint showed that removing past cognitive states from memory significantly reduced performance, indicating contextual memory is critical for simulating learning behaviours. [→ Luis Marquez-Carpintero 2025](#luis-marquez-carpintero-2025)

## Evidence

### Luis Marquez-Carpintero 2025

Luis Marquez-Carpintero, Alberto Lopez-Sellers, Miguel Cazorla. (2025). Simulating Students with Large Language Models: A Review of Architecture, Mechanisms, and Role Modelling in Education with Generative AI. https://arxiv.org/abs/2511.06078 [doi:10.48550/arxiv.2511.06078](https://doi.org/10.48550/arxiv.2511.06078)

`q2 · i?` · `review · r2`

The review reports, from the EduAgent preprint by Xu et al. [2024], ablation results on agents that simulate gaze, motor action, cognitive state and test responses slide by slide. The article reports a statistically significant reduction with no printed effect size.

> "Notably, only behaviours from the most recent slide are used as demonstrations, and ablation studies showed that removing past cognitive states from memory significantly reduced performance, highlighting the critical role of contextual memory."

## Discussion


## Related Claims
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [Federated aggregation is the primary driver of performance gains, contributing an average 11.99% improvement](federated-aggregation-primary-performance-driver.md) — related
- [Knowledge and behavior profile components provide complementary signals: removing either hurts metrics tied to the other](knowledge-behavior-profile-complementary-signals.md) — related
- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](beagle-ablation-semi-markov-and-decoupling.md) — related
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
- [Removing the cognitive load module causes the largest ablation performance drop, while state fusion has a smaller effect](cognitive-load-module-largest-ablation-drop.md) — related
- [Ablations show the trustworthiness module contributes most to performance, and the explanation generator cuts human review time by 41%](ablation-trust-module-largest-contribution.md) — related

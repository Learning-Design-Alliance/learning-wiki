---
type: strategy
id: longitudinal-auditing-governance-adaptive-systems
title: Govern adaptive learning systems through longitudinal auditing rather than deployment-time static fairness checks
description: "The article proposes a governance framework for the longitudinal auditing of adaptive learning systems, motivated by its argument that static, snapshot fairness auditing \"fails to capture the temporal and cumulative n..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
sources:
  - id: firuz-kamalov-2026
    resource: "https://arxiv.org/abs/2610.31041"
    title: "Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. https://arxiv.org/abs/2610.31041"
    author: Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani
---

# Govern adaptive learning systems through longitudinal auditing rather than deployment-time static fairness checks

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article proposes a governance framework for the longitudinal auditing of adaptive learning systems, motivated by its argument that static, snapshot fairness auditing "fails to capture the temporal and cumulative nature of the educational process." The framework treats algorithmic fairness as a temporal property of a closed loop: institutions should audit the served-difficulty trajectory, estimation bias, and group-fairness metrics over the lifecycle of a degree program, and rerun grader measurements as graders, prompts, and versions change. The released protocol and simulator are designed to support such repeated auditing.

## Design Implications

### Context
#### Requirements
- Continuous or periodic auditing across the deployment lifecycle, including re-measurement of grader asymmetry as graders and prompts change
#### Constraints
- The authors state that what remains to be validated with real learners is open; the simulation and measurement establish the mechanism and its order of magnitude, not deployed-system behaviour

### Target Learners
- higher education learners using GenAI-driven adaptive tutoring systems

### Target Learning Goals
- sustaining equitable learning trajectories over longitudinal AI-driven instruction

## Claims

- [In a reduced mean-field model, an adaptive policy targeting a fixed success rate exhibits a bifurcation under asymmetric false-negative noise: below a critical threshold the protected group is served easier content but still learns, above it ability decays geometrically](../claims/algorithmic-drift-bifurcation-trapping-threshold.md) [+W]
- [In a matched-pair grading protocol, open-weight LLM graders show demographically asymmetric false-negative behaviour against second-language variants, with the most affected grader rejecting 5% of correct second-language answers it accepts in Standard English](../claims/llm-grader-asymmetric-false-negatives.md) [+W]
- [In the agent-based simulation at baseline noise ϵ = 0.05, the protected group shows trajectory decoupling: lower final latent ability, a positive gap widening, and excess estimation pessimism relative to the reference group, with the gap growing substantially at higher noise](../claims/simulation-baseline-algorithmic-drift.md) [+W]

## Related Strategies

- [Audit educational LLM deployments for differential treatment before serving marginalized learners](audit-llm-tutors-for-paternalistic-bias.md)

## Examples
-

## Key Sources
- Firuz Kamalov, Hana Sulieman, Ahmed El Sayed, Sivaraj R., Nitesh Sughnani. (2026). Algorithmic drift in generative adaptive learning. arXiv. https://arxiv.org/abs/2610.31041

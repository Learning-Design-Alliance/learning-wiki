---
type: strategy
id: executable-theory-hypothesis-generation-strategy
title: Use executable computational models of learning to generate and test hypotheses about when instructional interventions will be effective
description: The article recommends using agent-based models like Procedural ABICAP as executable theories that simulate educational settings where empirical literature is sparse, generating hypotheses that can later be verified e...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: rismanchian-2024
    resource: "https://arxiv.org/abs/2408.13364"
    title: "Rismanchian, S., & Doroudi, S. (2024). Reconciling Different Theories of Learning with an Agent-based Model of Procedural Learning. arXiv. https://arxiv.org/abs/2408.13364"
    author: "Rismanchian, S., & Doroudi, S"
---

# Use executable computational models of learning to generate and test hypotheses about when instructional interventions will be effective

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends using agent-based models like Procedural ABICAP as executable theories that simulate educational settings where empirical literature is sparse, generating hypotheses that can later be verified experimentally. Such models can also serve as theoretically grounded environments for comparing adaptive sequencing algorithms for instructional activities. As the authors put it, the true power of agent-based modeling lies in making predictions about novel settings where there is little empirical literature.

## Design Implications

### Context
#### Requirements
- Accurate simulation requires a concrete sense of the knowledge graph and the cognitive load of different engagement modes; robustness tests are recommended when parameters are uncertain
#### Constraints
- 

### Target Learners
- Researchers designing instructional interventions and intelligent tutoring systems

### Target Learning Goals
- Predicting when instructional interventions of different engagement modes will be more or less effective

### Affordances
- [Procedural Abicap Agent Based Model](../theories/icap-four-mode-engagement-taxonomy.md)

## Claims

- [Under Procedural ABICAP's assumptions, cognitive load increases monotonically with engagement mode, and constructive practice reinforces connections rather than transferring skill immediately](../claims/abicap-two-assumptions.md) [+W]
- [After step 35, active and constructive learning gradually overtake passive learning, consistent with the expertise reversal effect](../claims/expertise-reversal-in-simulation.md) [+W]
- [In Procedural ABICAP simulations, the ICAP ordering (interactive > constructive > active > passive) holds after enough steps](../claims/icap-holds-after-step-35.md) [+W]
- [For rationale-free procedural knowledge components with no graph edges, Procedural ABICAP predicts passive learning is best](../claims/passive-best-for-rationale-free-kcs.md) [+W]
- [Before around step 35, passive learning is consistently at least as good as (and typically better than) active and constructive learning, replicating the worked example effect](../claims/worked-example-effect-low-expertise.md) [+W]

## Related Strategies

- [Using the CoMSA to formalize assumptions about how interventions map onto learning curve changes](comsa-intervention-mapping-strategy.md)

## Examples
-

## Key Sources
- Rismanchian, S., & Doroudi, S. (2024). Reconciling Different Theories of Learning with an Agent-based Model of Procedural Learning. arXiv. https://arxiv.org/abs/2408.13364

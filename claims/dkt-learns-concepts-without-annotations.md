---
type: claim
title: DKT matches an oracle on simulated data without concept labels, while BKT degrades as hidden concepts increase
description: DKT matches an oracle on simulated data without concept labels, while BKT degrades as hidden concepts increase
id: dkt-learns-concepts-without-annotations
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-14
evidence_strength: moderate
sources:
  - id: chris-piech-2015
    resource: "https://github.com/chrispiech/DeepKnowledgeTracing"
    title: "Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing"
    author: Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein
    q: 2
    i: "?"
    kind: design
    rigour: "?"
  - id: chris-piech-2015-2
    resource: "https://github.com/chrispiech/DeepKnowledgeTracing"
    title: "Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing"
    author: Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
---

# DKT matches an oracle on simulated data without concept labels, while BKT degrades as hidden concepts increase

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r?` · `q2`

## Subclaims
`q2 i?` On synthetic data with hidden concept labels withheld, both LSTM and RNN models predicted student responses as well as an oracle with perfect knowledge of the generative model parameters. [→ Chris Piech 2015](#chris-piech-2015)
`q2 i?` BKT prediction degraded substantially as the number of hidden concepts increased because it cannot learn unlabelled concepts. [→ Chris Piech 2015 (2)](#chris-piech-2015-2)

## Evidence

### Chris Piech 2015

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `design · r?`

Simulation experiment generating 4,000 virtual students per run answering 50 exercises drawn from 1-5 concepts, repeated 20 times per concept count. The article reports RNN and LSTM matched the oracle and would have to mimic latent concepts, exercise difficulty, priors, and skill increases.

> "Both the LSTM and RNN models did as well at predicting student responses as an oracle which had perfect knowledge of all model parameters"

### Chris Piech 2015 (2)

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `causal · r?`

Same simulated-data experiment (Figure 3(a)): as the number of hidden concepts grew from 1 to 5, BKT accuracy fell while RNN and LSTM held near the oracle, which the article attributes to BKT's lack of a mechanism to learn unlabelled concepts.

> "In contrast, the BKT prediction degraded substantially as the number of hidden concepts increased as it doesn't have a mechanism to learn unlabelled concepts"

## Discussion


## Related Claims
- [DKT influence graphs recover latent concept structure from unlabeled interaction data](dkt-influence-graphs-exercise-structure.md) — related
- [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags](dynemb-tracks-knowledge-without-skill-tags.md) — related
- [The skill discovery model partially recovers the true problem-KC assignment matrix in synthetic datasets when provided with problem representations](skill-discovery-partially-recovers-true-kc-assignments.md) — related
- [BKT implemented as an RNN layer in PyTorch recovers generating parameters comparably to brute-force grid-search BKT while scaling to large datasets](bkt-rnn-matches-brute-force-parameter-recovery.md) — related

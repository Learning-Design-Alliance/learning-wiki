---
type: claim
title: DKT influence graphs recover latent concept structure from unlabeled interaction data
description: DKT influence graphs recover latent concept structure from unlabeled interaction data
id: dkt-influence-graphs-exercise-structure
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-14
evidence_strength: weak
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
    kind: associational
    rigour: "?"
---

# DKT influence graphs recover latent concept structure from unlabeled interaction data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r?` · `q2`

## Subclaims
`q2 i?` Directed influence graphs computed from a trained DKT model perfectly clustered the five latent concepts in the synthetic dataset. [→ Chris Piech 2015](#chris-piech-2015)
`q2 i?` On the Khan dataset, DKT influence graphs recovered coherent relationships among 8th grade Common Core concepts, while two baseline methods generated discordant graphs. [→ Chris Piech 2015 (2)](#chris-piech-2015-2)

## Evidence

### Chris Piech 2015

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `design · r?`

Structural analysis of the trained model using an influence function (Equation 4) over directed pairs of exercises; the graph showed "a perfect clustering of the ﬁve latent concepts" in the synthetic data (Figure 4).

> "The graph of our model's conditional inﬂuences for the synthetic dataset reveals a perfect clustering of the ﬁve latent concepts (see Figure 4), with directed edges set using the inﬂuence function in Equation 4."

### Chris Piech 2015 (2)

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `associational · r?`

Analysis of Khan data restricted to ordered exercise pairs where the successor appeared more than 1% of the time. Compared against transition-probability and dataset-conditional-probability baselines, both baselines produced discordant graphs, supporting that the DKT network learned a coherent model.

> "Both baseline methods generated discordant graphs, which are shown in the Appendix. While many of the relationships we uncovered may be unsurprising to an education expert their discovery is afﬁrmation that the DKT network learned a coherent model."

## Discussion


## Related Claims
- [DKT matches an oracle on simulated data without concept labels, while BKT degrades as hidden concepts increase](dkt-learns-concepts-without-annotations.md) — related
- [Visualization analysis indicates the learned graph topology recovers interpretable relational structures such as modular node clusters and directed dependency hierarchies](adaptive-g-ukt-learned-topology-interpretable.md) — a broader claim this one bears on
- [Existing deep sequential knowledge tracing encoders treat concept nodes as isolated deterministic vectors, limiting handling of structural sparsity and epistemic uncertainty](kt-encoders-entity-isolated-deterministic-limits.md) — related

---
type: design
id: plumed-tutorials-directed-graph-navigation
title: Directed-graph navigation and transitive-reduction ordering of tutorials as a mastery path
description: Each tutorial renders a Mermaid directed graph guiding learners through its resources, with solid lines for essential and dashed lines for supplementary material and hover tooltips describing each node.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: tribello-2024
    resource: "https://arxiv.org/abs/2412.03595"
    title: "Tribello, G. A., et al. (2024). PLUMED Tutorials: a collaborative, community-driven learning ecosystem. https://arxiv.org/abs/2412.03595"
    author: Tribello, G. A., et al
---

# Directed-graph navigation and transitive-reduction ordering of tutorials as a mastery path

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Each tutorial renders a Mermaid directed graph guiding learners through its resources, with solid lines for essential and dashed lines for supplementary material and hover tooltips describing each node. Across the site, links contributors include between tutorials are assembled into a directed graph from which circular dependencies are removed and a transitive reduction is performed, giving "students advice on the order in which students should work through the tutorials." The ordering is "democratically determined by contributors to the site."

## Design Implications

### Context
#### Requirements
- contributors must include links to other tutorials (via EMBED.yml with type: internal) for a tutorial to appear in the site-wide graph
#### Constraints
- the site deliberately does not impose a single order; guidance emerges from contributor links, and unlinked tutorials do not appear in the graph

### Target Learners
- new PLUMED users seeking a structured learning path through the tutorial collection

### Learning Goals
- progressing from basic PLUMED usage to advanced enhanced-sampling methods in a sensible sequence

### Claims
- Plumed Tutorials Website [+M]

## Related Designs

- [Sequenced tutorial progression in which each alignment skill builds on previously mastered skills](sequenced-prerequisite-tutorial-progression.md)

## Examples
-

## Key Sources
- Tribello, G. A., et al. (2024). PLUMED Tutorials: a collaborative, community-driven learning ecosystem. https://arxiv.org/abs/2412.03595. [doi:10.48550/arxiv.2412.03595](https://doi.org/10.48550/arxiv.2412.03595)

---
type: strategy
id: tutorials-as-miniature-research-literature
title: Design tutorial sites as a miniaturized research literature with contributor-controlled linking rather than an imposed order
description: Rather than imposing a canonical sequence, the PLUMED Tutorials site lets contributors link their tutorials to others, with the site-wide ordering emerging from these links.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: tribello-2024
    resource: "https://arxiv.org/abs/2412.03595"
    title: "Tribello, G. A., et al. (2024). PLUMED Tutorials: a collaborative, community-driven learning ecosystem. https://arxiv.org/abs/2412.03595"
    author: Tribello, G. A., et al
---

# Design tutorial sites as a miniaturized research literature with contributor-controlled linking rather than an imposed order

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Rather than imposing a canonical sequence, the PLUMED Tutorials site lets contributors link their tutorials to others, with the site-wide ordering emerging from these links. The authors state the site "is designed in a way that more closely resembles a miniaturized version of the research literature than a textbook," and that multiple tutorials on the same topic are not necessarily to be avoided, reflecting "the diversity of views about these techniques that exist in the literature."

## Design Implications

### Context
#### Requirements
- a linking mechanism (EMBED.yml with type: internal) and an automatically constructed, transitive-reduced dependency graph
#### Constraints
- contributors who neither link to other tutorials nor are linked do not appear in the site-wide ordering graph

### Target Learners
- early-career researchers embarking on research careers who must navigate diverse methods literature

### Target Learning Goals
- navigating a pluralistic body of methods tutorials and choosing an appropriate learning path

## Related Strategies

- [Use repository management and continuous integration to keep community tutorials current as software evolves](continuous-integration-tutorial-maintenance.md)
- [Use a skills consensus statement to recommend an order of tutorial participation to students](consensus-statement-tutorial-ordering-strategy.md)

## Examples
-

## Key Sources
- Tribello, G. A., et al. (2024). PLUMED Tutorials: a collaborative, community-driven learning ecosystem. https://arxiv.org/abs/2412.03595

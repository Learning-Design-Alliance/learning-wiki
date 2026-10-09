---
type: element
id: openalex-workshop-organizer-bibliometric-corpus
title: OpenAlex-seeded bibliometric corpus of workshop organizer publications
description: "The study's dataset is built from publication records of 22 workshop organizers retrieved from the OpenAlex database, yielding a coauthorship corpus of \"2,197 authors and over 4,000 publications.\" A topic-filtered sub..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: risha-z-roschelle-j
    resource: "https://doi.org/10.51388/20.500.12265/305"
    title: "Risha, Z. & Roschelle, J. (2026, July). A bibliographic analysis of digital learning platforms as research infrastructure. Digital Promise. https://doi.org/10.51388/20.500.12265/305"
---

# OpenAlex-seeded bibliometric corpus of workshop organizer publications

> **Element** · [All elements](index.md)
> **Evidence** · 4 claims (4 for) · 6 studies (6 associational), `q2` · 0 of 6 report an effect size · 2 claims rest on one study

## Description
The study's dataset is built from publication records of 22 workshop organizers retrieved from the OpenAlex database, yielding a coauthorship corpus of "2,197 authors and over 4,000 publications." A topic-filtered subset of 724 papers supported bibliographic coupling, and semantic expansion via SPECTER embeddings and snowball sampling produced "a much larger corpus of over 1,200 publications" for identifying related work outside the workshop's social network.

## Design Implications

### Context
#### Requirements
- Access to the OpenAlex bibliographic database and SemanticScholar's SPECTER embeddings API
#### Constraints
- Only three out of six workshops were indexed by OpenAlex, so the corpus incompletely covers the workshop series

### Target Learners
- education researchers
- bibliometric analysts

### Target Learning Goals
- identifying the community structure, intellectual foundations, and related literature of an emerging research area

### Affordances
- [Three Perspective Bibliometric Mapping Emerging Subfields](../theories/three-perspective-bibliometric-mapping-emerging-subfields.md)

## Claims

- [Coauthorship analysis of workshop organizers yields a 2,197-author network with six communities, 80% of nodes in the largest three, spanning diverse research lineages](../claims/coauthorship-network-six-communities.md) [+M]
- [The DLP-as-research-infrastructure community is small and fragmented: the DLP-focused cluster was one of five bibliographic-coupling communities and only 20.6% of filtered papers](../claims/dlp-subfield-small-and-fragmented.md) [+W]
- [Platform-enabled experimentation research draws on multiple intellectual lineages, including intelligent tutoring systems, formative feedback, and exemplar platforms like ASSISTments](../claims/multiple-intellectual-lineages-shared-foundations.md) [+M]
- [Removing the workshop's coauthorship edges increased average path length and network diameter, indicating the workshop publications bridge otherwise separate researcher groups](../claims/workshop-papers-bridge-researcher-groups.md) [+W]

## Related Elements
- 

## Examples

- [Research Map Visualization](../strategies/research_map_visualization.md)
- [Educational Research Map Visualization](../strategies/educational_research_map_visualization.md)

## Key Sources
- Risha, Z. & Roschelle, J. (2026, July). A bibliographic analysis of digital learning platforms as research infrastructure. Digital Promise. https://doi.org/10.51388/20.500.12265/305

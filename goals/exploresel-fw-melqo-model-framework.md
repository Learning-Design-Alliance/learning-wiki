---
type: goal-map
title: ExploreSEL Framework — MELQO MODEL Framework
description: To support the accurate and feasible measurement of early child development
  in low- and middle-income countries and to create a globally comparable monitoring
  system while also generating locally relevant data that can inform national policies.
status: draft
generated:
  by: claude/unspecified
  at: '2026-08-30'
source:
  framework: MELQO MODEL Framework
  kind: standard
  framework_full_name: MELQO MODEL Framework
  description: 'Measuring Early Learning Quality and Outcomes (MELQO) Measure of Development
    and Early Learning (MODEL) module is a measurement framework and tool designed
    to assess school readiness. The MODEL module was developed as part of the MELQO
    initiative, a collaboration between multilateral organizations and research institutions
    including  UNESCO, the World Bank, the Center for Universal Education at the Brookings
    Institution, and UNICEF with a goal of promoting feasible, adaptable, accurate,
    and useful measurement of children’s development and learning at the start of
    primary school. The MODEL module focuses on age-appropriate and culturally-relevant
    skills and competencies that reflect normative development within three basic
    domains of early learning and school readiness. It is one of two modules under
    the MELQO initiative; the other is the

    Measure of Early Learning Environments (MELE) module, designed to measure the
    quality of pre-primary learning environments. Together, these tools help assess
    progress towards the UN Sustainable Development Goal 4.2 to improve the quality,
    feasibility, and accessibility of early childhood education.'
  purpose: To support the accurate and feasible measurement of early child development
    in low- and middle-income countries and to create a globally comparable monitoring
    system while also generating locally relevant data that can inform national policies
  age_range: Early childhood, school age child
  setting: School, home, community, non-formal education
  source_url: http://ecdmeasure.org/about-melqo
  eselURL: http://exploresel.gse.harvard.edu/frameworks/55/
  publisher: UNESCO, UNICEF, the Center for Universal Education at Brookings, World
    Bank
  publisher_type: Multilateral/Intergovernmental, research
nodes:
- id: term_627
  label: executive functioning
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/627/
- id: term_628
  label: working memory
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/628/
- id: term_629
  label: inhibitory control
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/629/
- id: term_630
  label: social-emotional development
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/630/
- id: term_631
  label: self-regulation
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/631/
- id: term_632
  label: social cognition
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/632/
- id: term_633
  label: social competence
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/633/
- id: term_634
  label: emotional well-being
  competency_framework: MELQO MODEL Framework
  external_id: http://exploresel.gse.harvard.edu/terms/634/
relationships:
- source: term_627
  target: term_628
  type: default
- source: term_627
  target: term_629
  type: default
- source: term_630
  target: term_631
  type: default
- source: term_630
  target: term_632
  type: default
- source: term_630
  target: term_633
  type: default
- source: term_630
  target: term_634
  type: default
---

# ExploreSEL Framework — MELQO MODEL Framework

> Ingested from a real scraped ExploreSEL/EASEL graph export. 8 of this framework's own competency terms, 6 internal `default` (hierarchical) edges among them.

## Description
Measuring Early Learning Quality and Outcomes (MELQO) Measure of Development and Early Learning (MODEL) module is a measurement framework and tool designed to assess school readiness. The MODEL module was developed as part of the MELQO initiative, a collaboration between multilateral organizations and research institutions including  UNESCO, the World Bank, the Center for Universal Education at the Brookings Institution, and UNICEF with a goal of promoting feasible, adaptable, accurate, and useful measurement of children’s development and learning at the start of primary school. The MODEL module focuses on age-appropriate and culturally-relevant skills and competencies that reflect normative development within three basic domains of early learning and school readiness. It is one of two modules under the MELQO initiative; the other is the
Measure of Early Learning Environments (MELE) module, designed to measure the quality of pre-primary learning environments. Together, these tools help assess progress towards the UN Sustainable Development Goal 4.2 to improve the quality, feasibility, and accessibility of early childhood education.

## Alignment to the shared taxonomy
This framework's terms carry 72 crosswalk edges into the canonical [ExploreSEL taxonomy](exploresel-taxonomy.md) (which of the six domains/23 subdomains/skill descriptors this framework's competencies map onto), plus 65 cross-framework similarity edges to other frameworks. Both are kept as separate datasets rather than embedded here — grep them by this page's node ids:

```
grep '"source": "{term_id}"' goals/data/exploresel-framework-taxonomy-crosswalk.ndjson
grep '"source": "{term_id}"' goals/data/exploresel-cross-framework-similarity.ndjson
```
(paths relative to the wiki root; substitute one of this page's node ids for `{term_id}`)

## Key Sources
- ExploreSEL framework profile: http://exploresel.gse.harvard.edu/frameworks/55/
- Publisher: UNESCO, UNICEF, the Center for Universal Education at Brookings, World Bank

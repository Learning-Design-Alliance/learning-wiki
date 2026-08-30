---
type: goal-map
title: ExploreSEL Framework — WHO Skills for Health
description: To support policy-makers, NGOs, community leaders, and school communities
  who are interested in advocating for, initiating, and strengthening skills-based
  health and life skills education as their approach to health education.
status: draft
generated:
  by: claude/unspecified
  at: '2026-08-30'
source:
  framework: WHO Skills for Health
  kind: standard
  framework_full_name: WHO Skills for Health
  description: The Word Health Organization (WHO)'s Skills for Health outline life
    skills important for skills-based health and life skills education. The WHO is
    a United Nations agency specializing in international public health, and the Skills
    for Health focus on the knowledge, attitudes, and skills that enable individuals
    to deal effectively with the demands and challenges of everyday life, including
    psychosocial competencies and interpersonal skills. The Skills for Health are
    part of the Focusing Resources on Effective School Health (FRESH) initiative,
    a collaboration between WHO, UNICEF, UNESCO, and the World Bank designed to promote
    effective school health programming.
  purpose: To support policy-makers, NGOs, community leaders, and school communities
    who are interested in advocating for, initiating, and strengthening skills-based
    health and life skills education as their approach to health education
  age_range: Preschool through early adulthood
  setting: School
  source_url: https://www.who.int/school_youth_health/gshi/en/
  eselURL: http://exploresel.gse.harvard.edu/frameworks/58/
  publisher: World Health Organization (WHO)
  publisher_type: Multilateral/intergovernmental
nodes:
- id: term_614
  label: communication and interpersonal skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/614/
- id: term_615
  label: interpersonal communication skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/615/
- id: term_616
  label: negotiation/refusal skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/616/
- id: term_617
  label: empathy building
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/617/
- id: term_618
  label: cooperation and teamwork
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/618/
- id: term_619
  label: advocacy skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/619/
- id: term_620
  label: decision-making and critical thinking skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/620/
- id: term_621
  label: decision-making / problem-solving skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/621/
- id: term_622
  label: critical thinking skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/622/
- id: term_623
  label: coping and self-management skills
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/623/
- id: term_624
  label: skills for increasing personal confidence and abilities to assume control,
    take responsibility, make a difference, or bring about change
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/624/
- id: term_625
  label: skills for managing feelings
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/625/
- id: term_626
  label: skills for managing stress
  competency_framework: WHO Skills for Health
  external_id: http://exploresel.gse.harvard.edu/terms/626/
relationships:
- source: term_614
  target: term_615
  type: default
- source: term_614
  target: term_616
  type: default
- source: term_614
  target: term_617
  type: default
- source: term_614
  target: term_618
  type: default
- source: term_614
  target: term_619
  type: default
- source: term_620
  target: term_621
  type: default
- source: term_620
  target: term_622
  type: default
- source: term_623
  target: term_624
  type: default
- source: term_623
  target: term_625
  type: default
- source: term_623
  target: term_626
  type: default
---

# ExploreSEL Framework — WHO Skills for Health

> Ingested from a real scraped ExploreSEL/EASEL graph export. 13 of this framework's own competency terms, 10 internal `default` (hierarchical) edges among them.

## Description
The Word Health Organization (WHO)'s Skills for Health outline life skills important for skills-based health and life skills education. The WHO is a United Nations agency specializing in international public health, and the Skills for Health focus on the knowledge, attitudes, and skills that enable individuals to deal effectively with the demands and challenges of everyday life, including psychosocial competencies and interpersonal skills. The Skills for Health are part of the Focusing Resources on Effective School Health (FRESH) initiative, a collaboration between WHO, UNICEF, UNESCO, and the World Bank designed to promote effective school health programming.

## Alignment to the shared taxonomy
This framework's terms carry 130 crosswalk edges into the canonical [ExploreSEL taxonomy](exploresel-taxonomy.md) (which of the six domains/23 subdomains/skill descriptors this framework's competencies map onto), plus 176 cross-framework similarity edges to other frameworks. Both are kept as separate datasets rather than embedded here — grep them by this page's node ids:

```
grep '"source": "{term_id}"' goals/data/exploresel-framework-taxonomy-crosswalk.ndjson
grep '"source": "{term_id}"' goals/data/exploresel-cross-framework-similarity.ndjson
```
(paths relative to the wiki root; substitute one of this page's node ids for `{term_id}`)

## Key Sources
- ExploreSEL framework profile: http://exploresel.gse.harvard.edu/frameworks/58/
- Publisher: World Health Organization (WHO)

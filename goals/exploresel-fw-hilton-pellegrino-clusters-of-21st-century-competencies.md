---
type: goal-map
title: ExploreSEL Framework — Hilton & Pellegrino Clusters of 21st Century Competencies
description: Helping the public understand the research related to the teaching and
  learning of 21st century skills.
status: draft
generated:
  by: claude/unspecified
  at: '2026-08-30'
source:
  framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  kind: standard
  framework_full_name: Hilton & Pellegrino Clusters of 21st Century Competencies
  description: The Hilton & Pellegrino Clusters of 21st Century Competencies is a
    framework developed by the National Research Council, a non-profit that conducts
    research to advise the government, the public, and the scientific community. The
    framework focuses on a set of key skills that promote deeper learning, college
    and career readiness, student-centered learning, and higher order thinking, and
    was developed by aligning common 21st century skills with existing taxonomies
    of cognitive, interpersonal, and intrapersonal skills.
  purpose: Helping the public understand the research related to the teaching and
    learning of 21st century skills
  age_range: Grades K-12
  setting: School
  source_url: http://www.nationalacademies.org/nrc
  eselURL: http://exploresel.gse.harvard.edu/frameworks/9/
  publisher: National Research Council
  publisher_type: NGO/non-profit
nodes:
- id: term_200
  label: cognitive
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/200/
- id: term_201
  label: cognitive processes and strategies
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/201/
- id: term_202
  label: knowledge
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/202/
- id: term_203
  label: creativity
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/203/
- id: term_204
  label: intrapersonal
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/204/
- id: term_205
  label: intellectual openness
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/205/
- id: term_206
  label: work ethic and conscientiousness
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/206/
- id: term_207
  label: positive core self-evaluation
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/207/
- id: term_208
  label: interpersonal
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/208/
- id: term_209
  label: teamwork and collaboration
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/209/
- id: term_210
  label: leadership
  competency_framework: Hilton & Pellegrino Clusters of 21st Century Competencies
  external_id: http://exploresel.gse.harvard.edu/terms/210/
relationships:
- source: term_200
  target: term_201
  type: default
- source: term_200
  target: term_202
  type: default
- source: term_200
  target: term_203
  type: default
- source: term_204
  target: term_205
  type: default
- source: term_204
  target: term_206
  type: default
- source: term_204
  target: term_207
  type: default
- source: term_208
  target: term_209
  type: default
- source: term_208
  target: term_210
  type: default
---

# ExploreSEL Framework — Hilton & Pellegrino Clusters of 21st Century Competencies

> Ingested from a real scraped ExploreSEL/EASEL graph export. 11 of this framework's own competency terms, 8 internal `default` (hierarchical) edges among them.

## Description
The Hilton & Pellegrino Clusters of 21st Century Competencies is a framework developed by the National Research Council, a non-profit that conducts research to advise the government, the public, and the scientific community. The framework focuses on a set of key skills that promote deeper learning, college and career readiness, student-centered learning, and higher order thinking, and was developed by aligning common 21st century skills with existing taxonomies of cognitive, interpersonal, and intrapersonal skills.

## Alignment to the shared taxonomy
This framework's terms carry 118 crosswalk edges into the canonical [ExploreSEL taxonomy](exploresel-taxonomy.md) (which of the six domains/23 subdomains/skill descriptors this framework's competencies map onto), plus 154 cross-framework similarity edges to other frameworks. Both are kept as separate datasets rather than embedded here — grep them by this page's node ids:

```
grep '"source": "{term_id}"' goals/data/exploresel-framework-taxonomy-crosswalk.ndjson
grep '"source": "{term_id}"' goals/data/exploresel-cross-framework-similarity.ndjson
```
(paths relative to the wiki root; substitute one of this page's node ids for `{term_id}`)

## Key Sources
- ExploreSEL framework profile: http://exploresel.gse.harvard.edu/frameworks/9/
- Publisher: National Research Council

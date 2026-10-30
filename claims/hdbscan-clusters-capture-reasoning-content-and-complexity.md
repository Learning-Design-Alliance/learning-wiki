---
type: claim
title: "HDBSCAN clustering of BERT embeddings yielded fifteen clusters capturing the content and complexity of students' mechanistic reasoning"
description: "HDBSCAN clustering of BERT embeddings yielded fifteen clusters capturing the content and complexity of students' mechanistic reasoning"
id: hdbscan-clusters-capture-reasoning-content-and-complexity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: martin-2025
    resource: "https://doi.org/10.1007/s40593-024-00440-y"
    title: "Martin, P. P., Kranz, D., & Graulich, N. (2025). Revealing Rubric Relations: Investigating the Interdependence of a Research-Informed and a Machine Learning-Based Rubric in Assessing Student Reasoning in Chemistry. International Journal of Artificial Intelligence in Education, 35, 1465–1503. https://doi.org/10.1007/s40593-024-00440-y"
    author: "Martin, P. P., Kranz, D., & Graulich, N."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: martin-2025-2
    resource: "https://doi.org/10.1007/s40593-024-00440-y"
    title: "Martin, P. P., Kranz, D., & Graulich, N. (2025). Revealing Rubric Relations: Investigating the Interdependence of a Research-Informed and a Machine Learning-Based Rubric in Assessing Student Reasoning in Chemistry. International Journal of Artificial Intelligence in Education, 35, 1465–1503. https://doi.org/10.1007/s40593-024-00440-y"
    author: "Martin, P. P., Kranz, D., & Graulich, N."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: martin-2025-3
    resource: "https://doi.org/10.1007/s40593-024-00440-y"
    title: "Martin, P. P., Kranz, D., & Graulich, N. (2025). Revealing Rubric Relations: Investigating the Interdependence of a Research-Informed and a Machine Learning-Based Rubric in Assessing Student Reasoning in Chemistry. International Journal of Artificial Intelligence in Education, 35, 1465–1503. https://doi.org/10.1007/s40593-024-00440-y"
    author: "Martin, P. P., Kranz, D., & Graulich, N."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# HDBSCAN clustering of BERT embeddings yielded fifteen clusters capturing the content and complexity of students' mechanistic reasoning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r1`–`r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The detected clusters encompassed chemical topics at varying grain sizes, capturing both the content and complexity of students' mechanistic reasoning. [→ Martin 2025](#martin-2025)
`q2 i?` Clusters did not segregate responses by task; responses to both case comparisons were similarly reflected in all clusters. [→ Martin 2025 (2)](#martin-2025-2)
`q2 i?` Clusters positioned at lower dimension-1 and higher dimension-2 values in the embedding space demonstrated higher reasoning complexity. [→ Martin 2025 (3)](#martin-2025-3)

## Evidence

### Martin 2025

Martin, P. P., Kranz, D., & Graulich, N. (2025). Revealing Rubric Relations: Investigating the Interdependence of a Research-Informed and a Machine Learning-Based Rubric in Assessing Student Reasoning in Chemistry. International Journal of Artificial Intelligence in Education, 35, 1465–1503. https://doi.org/10.1007/s40593-024-00440-y

`q2 · i?` · `associational · r2`

Qualitative interpretation of the HDBSCAN cluster solution (Table 1, Fig. 6) in the Results section. The authors describe clusters spanning structural, energetic, phenomenological, and electronic reasoning, noting the method "captured the content and complexity of students' mechanistic reasoning".

> "The detected patterns encompass a range of chemical topics discussed at varying grain sizes, highlighting that the clustering method captured the content and complexity of students' mechanistic reasoning."

### Martin 2025 (2)

Martin, P. P., Kranz, D., & Graulich, N. (2025). Revealing Rubric Relations: Investigating the Interdependence of a Research-Informed and a Machine Learning-Based Rubric in Assessing Student Reasoning in Chemistry. International Journal of Artificial Intelligence in Education, 35, 1465–1503. https://doi.org/10.1007/s40593-024-00440-y

`q2 · i?` · `associational · r1`

Results on the two case-comparison tasks: the authors report that "responses to both tasks are similarly reflected in all clusters", indicating the data-driven categories were not artifacts of a single task's requirements.

> "Surprisingly, responses to both tasks are similarly reflected in all clusters, so the clusters did not segregate the two tasks."

### Martin 2025 (3)

Martin, P. P., Kranz, D., & Graulich, N. (2025). Revealing Rubric Relations: Investigating the Interdependence of a Research-Informed and a Machine Learning-Based Rubric in Assessing Student Reasoning in Chemistry. International Journal of Artificial Intelligence in Education, 35, 1465–1503. https://doi.org/10.1007/s40593-024-00440-y

`q2 · i?` · `associational · r2`

A pattern observed in the two-dimensional embedding visualization (Fig. 6): the authors noticed that clusters with "lower values in dimension 1 and higher values in dimension 2" showed higher reasoning complexity, a descriptive rather than statistically tested observation.

> "Generally, we noticed that clusters having lower values in dimension 1 and higher values in dimension 2 (Fig. 6) demonstrated higher complexity."

## Discussion


## Related Claims
- [k-means and k-medoids clustering merged conceptually distinct mechanistic reasoning types, making them less effective than HDBSCAN for this data](kmeans-kmedoids-merged-distinct-reasoning-types.md) — related
- [Clusters computed from pre-trained LLM embeddings show low overall alignment with theory-driven Knowledge Profiles of student biology responses](llm-embedding-clusters-low-alignment-kps.md) — related
- [Research-informed and ML-based rubrics assess students' mechanistic reasoning comparably, supporting ML techniques in rubric development](ml-and-research-informed-rubrics-assess-comparably.md) — related

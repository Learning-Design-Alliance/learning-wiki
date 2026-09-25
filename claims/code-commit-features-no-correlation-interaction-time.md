---
type: claim
title: Code commit features before a help request show no correlation with interaction time, and commit-based scheduling strategies perform no better than FCFS
description: Code commit features before a help request show no correlation with interaction time, and commit-based scheduling strategies perform no better than FCFS
id: code-commit-features-no-correlation-interaction-time
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: z-gao-2024
    resource: "https://doi.org/10.5281/zenodo.12729866"
    title: "Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866"
    author: Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman
    q: 2
    i: 0
  - id: z-gao-2024-2
    resource: "https://doi.org/10.5281/zenodo.12729866"
    title: "Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866"
    author: Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman
    q: 2
    i: "?"
---

# Code commit features before a help request show no correlation with interaction time, and commit-based scheduling strategies perform no better than FCFS

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i0` negligible

## Subclaims
`q2 i0` Pearson correlations between commit frequency, last-commit elapsed time, last-commit LOC and interaction time are negligible and non-significant. [→ Z. Gao 2024](#z-gao-2024)
`q2 i?` Simulated commit-feature strategies yield no significant difference from FCFS on any queue metric. [→ Z. Gao 2024 (2)](#z-gao-2024-2)

## Evidence

### Z. Gao 2024

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i0`

Correlational analysis of real request data (Table 2): commit frequency r = 0.0035 (p = 0.913), last commit elapsed time r = -0.0017 (p = 0.984), last commit LOC r = 0.0098 (p = 0.852) — "we could not find any correlation between the requests' interaction time and any code commit features".

> "We tracked students' code commits before they raised a re-quest and while they waited in the queue and calculated the Pearson correlation of their code features and the interaction time for each request. Results are in Table 2, and we could not find any correlation between the requests' interaction time and any code commit features"

### Z. Gao 2024 (2)

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i?`

Normal-load simulation repeated with three commit-feature strategies (highest commit frequency, lowest elapsed time since last commit, largest LOC). The results show no significant difference from FCFS on resolved requests, helped students, long wait requests, or overall wait time.

> "the results show that compared with the FCFS strategy, using code commit features strategies does not yield any significant difference in resolved requests, helped students, long wait requests, and overall wait time"

## Discussion


## Related Claims
-

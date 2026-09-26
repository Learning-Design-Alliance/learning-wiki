---
type: claim
title: "Choice of scheduling strategy does not significantly affect the number of resolved requests or students' overall wait time"
description: "Choice of scheduling strategy does not significantly affect the number of resolved requests or students' overall wait time"
id: scheduling-strategy-no-effect-resolved-requests-wait-time
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
    i: "?"
  - id: z-gao-2024-2
    resource: "https://doi.org/10.5281/zenodo.12729866"
    title: "Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866"
    author: Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman
    q: 2
    i: "?"
---

# Choice of scheduling strategy does not significantly affect the number of resolved requests or students' overall wait time

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` No significant difference in percentage of resolved requests among the four strategies under busy or normal load. [→ Z. Gao 2024](#z-gao-2024)
`q2 i?` No significant difference in average or median wait time across strategies at any load. [→ Z. Gao 2024 (2)](#z-gao-2024-2)

## Evidence

### Z. Gao 2024

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i?`

Normal-load simulation results: "on average, 65% of the requests would get resolved" regardless of strategy, with no significant pairwise differences (p>0.05 for all pairs). The busy-load condition showed a similar null result (45% resolved, p>0.05 for all pairs).

> "No significant difference in the percentage of resolved requests was found among all four strategies (p > 0.05 for all pairs); on average, 65% of the requests would get resolved no matter which scheduling strategy was applied"

### Z. Gao 2024 (2)

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i?`

Wait-time analysis across all simulations (Table 1): average wait was around 80 minutes under busy load, 50 minutes under normal load, and 18 minutes under relaxed load, with no significant difference between strategies (all pair p>0.05).

> "We did not find any significant difference in students' wait time when choosing different scheduling strategies (all pair p> 0.05)"

## Discussion


## Related Claims
- [The NSF advantage over FCFS appears only above an arrival-rate threshold (λ > 0.06); under relaxed queues no strategy makes a difference](arrival-rate-threshold-nsf-advantage.md) — reports the opposite
- [Under busy or normal queue load, the New Student First (NSF) strategy significantly increases the percentage of students who receive help compared with FCFS, LWF, and VLWF](nsf-strategy-increases-helped-students-busy-normal-queues.md) — reports the opposite
- [Code commit features before a help request show no correlation with interaction time, and commit-based scheduling strategies perform no better than FCFS](code-commit-features-no-correlation-interaction-time.md) — related

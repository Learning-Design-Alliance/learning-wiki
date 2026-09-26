---
type: claim
title: "The NSF advantage over FCFS appears only above an arrival-rate threshold (λ > 0.06); under relaxed queues no strategy makes a difference"
description: "The NSF advantage over FCFS appears only above an arrival-rate threshold (λ > 0.06); under relaxed queues no strategy makes a difference"
id: arrival-rate-threshold-nsf-advantage
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

# The NSF advantage over FCFS appears only above an arrival-rate threshold (λ > 0.06); under relaxed queues no strategy makes a difference

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

## Subclaims
`q2 i?` When λ > 0.06, choosing NSF over FCFS significantly increases the percentage of students who receive help (p<0.05). [→ Z. Gao 2024](#z-gao-2024)
`q2 i?` Under relaxed load (λ = 0.05), no significant differences among the four strategies on any metric. [→ Z. Gao 2024 (2)](#z-gao-2024-2)

## Evidence

### Z. Gao 2024

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i?`

Sensitivity simulation across 20 arrival rates from 0.05 to 0.10. The results show that "when λ > 0.06, the significant difference in the percentage of helped students exists (p < 0.05)", locating the boundary of NSF's benefit.

> "we repeated the simulation with 20 different ar-rival rates λ, ranging from 0.05 to 0.10, and found that when λ > 0.06, the significant difference in the per-centage of helped students exists ( p < 0.05)"

### Z. Gao 2024 (2)

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i?`

Relaxed-load simulation (λ = 0.05): long-wait requests were almost always 0 and no significant differences appeared among the four strategies on any metric (all p>0.05), so strategy choice does not affect resolved requests or helped students.

> "We also found that when the queue was relaxed( λ = 0.05), the percentage of long wait requests was almost always 0. We did not observe any significant difference in those metrics among all four strategies (all p >0.05)"

## Discussion


## Related Claims
- [Under busy or normal queue load, the New Student First (NSF) strategy significantly increases the percentage of students who receive help compared with FCFS, LWF, and VLWF](nsf-strategy-increases-helped-students-busy-normal-queues.md) — related
- [Choice of scheduling strategy does not significantly affect the number of resolved requests or students' overall wait time](scheduling-strategy-no-effect-resolved-requests-wait-time.md) — reports the opposite
- [Code commit features before a help request show no correlation with interaction time, and commit-based scheduling strategies perform no better than FCFS](code-commit-features-no-correlation-interaction-time.md) — related

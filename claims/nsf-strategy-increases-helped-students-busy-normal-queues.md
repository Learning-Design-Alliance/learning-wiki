---
type: claim
title: Under busy or normal queue load, the New Student First (NSF) strategy significantly increases the percentage of students who receive help compared with FCFS, LWF, and VLWF
description: Under busy or normal queue load, the New Student First (NSF) strategy significantly increases the percentage of students who receive help compared with FCFS, LWF, and VLWF
id: nsf-strategy-increases-helped-students-busy-normal-queues
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
    i: 2
  - id: z-gao-2024-2
    resource: "https://doi.org/10.5281/zenodo.12729866"
    title: "Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866"
    author: Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman
    q: 2
    i: 2
---

# Under busy or normal queue load, the New Student First (NSF) strategy significantly increases the percentage of students who receive help compared with FCFS, LWF, and VLWF

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i2` Under busy load, around 65% of students receive help with NSF versus around 54% with the other three strategies (p<0.01). [→ Z. Gao 2024](#z-gao-2024)
`q2 i2` Under normal load, NSF raises the percentage of students receiving at least one help from 70% (FCFS) to 82% (p<0.01). [→ Z. Gao 2024 (2)](#z-gao-2024-2)

## Evidence

### Z. Gao 2024

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i2`

Simulation of a busy-load queue (λ = 0.15) repeated 100 times per condition, evaluated with Mann–Whitney U tests. The busy-load results show "around 65% of the students would receive help" under NSF versus around 54% under the other strategies, a significant difference (p<0.01).

> "the NSF strategy appears to be significantly higher than the other three ( p <0.01); on average, around 65% of the students would receive help if the teacher used the NSF strategy, while only around 54% of the students would receive help if one of the other three strategies was applied"

### Z. Gao 2024 (2)

Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

`q2 · i2`

Normal-load simulation (λ = 0.10) comparing FCFS and NSF on percentage of students receiving help. The normal-load results show the helped-student percentage "would increase to 82%" under NSF versus 70% under FCFS, significant at p<0.01.

> "When the teacher applied the FCFS strategy, 70% of the students would at least receive one help on average, while when the scheduling strategy changed to NSF, this percentage would increase to 82%, and such difference is significant as well (p <0.01)"

## Discussion


## Related Claims
- [The NSF advantage over FCFS appears only above an arrival-rate threshold (λ > 0.06); under relaxed queues no strategy makes a difference](arrival-rate-threshold-nsf-advantage.md) — related
- [Code commit features before a help request show no correlation with interaction time, and commit-based scheduling strategies perform no better than FCFS](code-commit-features-no-correlation-interaction-time.md) — related
- [Choice of scheduling strategy does not significantly affect the number of resolved requests or students' overall wait time](scheduling-strategy-no-effect-resolved-requests-wait-time.md) — reports the opposite

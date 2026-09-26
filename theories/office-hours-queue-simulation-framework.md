---
type: theory
title: Office-hours queue simulation framework combining survival-analysis patience modeling with Poisson arrivals
description: A simulation framework for comparing office-hours queue scheduling strategies without live experimentation.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: z-gao-2024
    resource: "https://doi.org/10.5281/zenodo.12729866"
    title: "Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866"
    author: Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman
---

# Office-hours queue simulation framework combining survival-analysis patience modeling with Poisson arrivals

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (2 for, 1 mixed, 1 against) · 1 study, `q2` · 1 of 1 report an effect size · 4 claims rest on one study

## Description
A simulation framework for comparing office-hours queue scheduling strategies without live experimentation. It generates synthetic requests by sampling four features — request author, arrival time, tolerable wait time, and interaction time — independently: "we sampled and generated each feature independently". Tolerable wait time is drawn from a Kaplan-Meier survival function S(t) fitted to real cancellation data, arrivals follow a Poisson process with load-dependent rates, and interaction times are copied from real requests. Strategies are then compared on wait time, resolved requests, and helped students.

## Design Implications

### Context
#### Requirements
- Real office-hours log data providing request, start, cancel, and resolved times to fit the survival function and interaction-time distribution
#### Constraints
- The article states the arrival-rate model is a simplified model, since students' arrival time could be influenced by time of day, personal schedules, or other unmeasured factors; data come from one semester of a single course

### Target Learners
- CS2 undergraduate students in large courses

### Target Learning Objectives
- Timely resolution of student help requests during office hours

### Claims

- [Nsf Strategy Increases Helped Students Busy Normal Queues](../claims/nsf-strategy-increases-helped-students-busy-normal-queues.md) [+M]
- [Scheduling Strategy No Effect Resolved Requests Wait Time](../claims/scheduling-strategy-no-effect-resolved-requests-wait-time.md) [+M]
- [The NSF advantage over FCFS appears only above an arrival-rate threshold (λ > 0.06); under relaxed queues no strategy makes a difference](../claims/arrival-rate-threshold-nsf-advantage.md) [~M]
- [Code commit features before a help request show no correlation with interaction time, and commit-based scheduling strategies perform no better than FCFS](../claims/code-commit-features-no-correlation-interaction-time.md) [-M]

## Related Theories
- 

## Examples

- [Use New Student First scheduling for online office hours queues and FCFS for in-person queues](../strategies/nsf-for-online-office-hours-scheduling.md)

## Key Sources
- Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

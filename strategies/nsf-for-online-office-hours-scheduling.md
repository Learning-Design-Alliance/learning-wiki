---
type: strategy
id: nsf-for-online-office-hours-scheduling
title: Use New Student First scheduling for online office hours queues and FCFS for in-person queues
description: "An implementable queue-management recipe derived from the simulation findings: instructors hosting online office hours should prioritize students who have not yet received help that day (NSF), falling back to FCFS whe..."
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

# Use New Student First scheduling for online office hours queues and FCFS for in-person queues

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
An implementable queue-management recipe derived from the simulation findings: instructors hosting online office hours should prioritize students who have not yet received help that day (NSF), falling back to FCFS when no such student exists. The article states: "We recommend the instructors use NSF for online office hours queue scheduling." For in-person office hours, FCFS is more appropriate because students rarely return the same day and can see the queue order.

## Design Implications

### Context
#### Requirements
- A ticketing or queue system that records which students have already been helped that day, so NSF selection can be executed
#### Constraints
- The article states NSF's advantage disappears for in-person office hours settings, where students rarely return the same day and would complain about late arrivals being helped early

### Target Learners
- Students in large CS courses seeking help during office hours

### Target Learning Goals
- Fair access to instructor help and reduced queue inequity

## Related Strategies

- [Make queue waiting time productive by offering LLM-based help tools such as CodeHelp to waiting students](llm-tools-for-productive-queue-waiting.md)

## Examples
-

## Key Sources
- Z. Gao, G. S. de Oliveira, D. Babalola, C. Lynch, and S. Heckman. (2024). Who should i help next? simulation of office hours queue scheduling strategy in a cs2 course. Proceedings of the 17th International Conference on Educational Data Mining. https://doi.org/10.5281/zenodo.12729866

---
type: design
id: mira-three-component-architecture
title: MIRA three-component containerised architecture (web application, workflow engine, telescope-control service)
description: "The article states that \"MIRA is organised as three independent, containerised components: a web application, a workflow engine, and a telescope-control service.\" The web application (SvelteKit, SQLite via Drizzle) ha..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: pedersen-2026
    resource: "https://arxiv.org/abs/2607.14801"
    title: "Pedersen, P. P., Garcia, L., Alimi, M., Degen, D., Lienhard, F., and Queloz, D. (2026). MIRA: a data management and education platform connecting students to robotic telescopes. https://arxiv.org/abs/2607.14801"
    author: Pedersen, P. P., Garcia, L., Alimi, M., Degen, D., Lienhard, F., and Queloz, D
---

# MIRA three-component containerised architecture (web application, workflow engine, telescope-control service)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article states that "MIRA is organised as three independent, containerised components: a web application, a workflow engine, and a telescope-control service." The web application (SvelteKit, SQLite via Drizzle) handles plan drafting, review, authentication and archive browsing with role-based permissions; the workflow engine (Apache Airflow DAGs on a Celery worker) performs scheduling, reduction and derived products asynchronously; and the telescope-control service (Astra over ASCOM Alpaca) executes schedules and reports status. Components exchange schedules, metadata and FITS files through a shared data volume and API callbacks, decoupling educational logic from low-level hardware control.

## Design Implications

### Context
#### Requirements
- A shared data volume through which the workflow engine passes plans and FITS products to Astra
- API callbacks from the telescope-control service to trigger automated data reduction
#### Constraints
- SQLite is currently used for simplicity, though Drizzle supports alternative engines such as PostgreSQL and MySQL

### Target Learners
- Swiss secondary-school students
- ETH Zurich undergraduates

### Learning Goals
- Supporting mentor-guided learning while automating routine observatory operations for larger student cohorts

### Claims
- 

## Related Designs
- Mira Robotic Astronomy Education Platform

## Examples
-

## Key Sources
- Pedersen, P. P., Garcia, L., Alimi, M., Degen, D., Lienhard, F., and Queloz, D. (2026). MIRA: a data management and education platform connecting students to robotic telescopes. https://arxiv.org/abs/2607.14801

---
type: claim
title: Explicit API interception from a pilot cohort of 19 students yielded 1,880 events over about 57 active student-hours
description: Explicit API interception from a pilot cohort of 19 students yielded 1,880 events over about 57 active student-hours
id: vismatic-pilot-cohort-1880-events
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: germán-arroyo-2026
    resource: "https://doi.org/10.48550/arxiv.2606.05929"
    title: "Germán Arroyo, Luis López, and Juan Carlos Torres. (2026). Securing the Sandbox: A Rootless Containerized Framework for Process-Oriented Monitoring in Computer Graphics Education. https://arxiv.org/abs/2606.05929 [doi:10.48550/arxiv.2606.05929](https://doi.org/10.48550/arxiv.2606.05929)"
    author: Germán Arroyo, Luis López, and Juan Carlos Torres
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Explicit API interception from a pilot cohort of 19 students yielded 1,880 events over about 57 active student-hours

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In a pilot evaluation with 19 active students on a Raspberry Pi 5, the platform recorded 1,880 discrete API events over approximately 57 active student-hours. [→ Germán Arroyo 2026](#german-arroyo-2026)

## Evidence

### Germán Arroyo 2026

Germán Arroyo, Luis López, and Juan Carlos Torres. (2026). Securing the Sandbox: A Rootless Containerized Framework for Process-Oriented Monitoring in Computer Graphics Education. https://arxiv.org/abs/2606.05929 [doi:10.48550/arxiv.2606.05929](https://doi.org/10.48550/arxiv.2606.05929)

`q2 · i?` · `design · r2`

Pilot cohort evaluation of the deployed platform. Data were collected by intercepting explicit human-driven HTTP API interactions—file modifications, kernel code executions, and terminal usage—after discarding the automated heartbeat telemetry. The article reports "1,880 discrete API events over approximately 57 active student-hours" as a substantial dataset for behavioral analysis.

> "The VISMATIC framework was evaluated using a pilot cohort of 19 active students. Deployed on a resource-efficient Raspberry Pi 5 system, the platform recorded 1,880 discrete API events over approximately 57 active student-hours"

## Discussion


## Related Claims
- [Macro-level behavioral metrics flagged anomalies consistent with automated workflows and off-platform AI code synthesis](behavioral-metrics-flag-automated-anomalies.md) — related
- [Rootless Podman isolation maintained containment with no observed privilege escalation or cross-identity contamination under classroom load](rootless-podman-containment-no-violations.md) — related
- [Session intensity and duration distributions flagged physically impossible persistence as severe statistical outliers](session-intensity-duration-outlier-flagging.md) — related
- [Cumulative engagement showed staircase growth with deadline-driven peaks of 348 events on April 4th and 205 events around April 9th](cumulative-engagement-staircase-deadline-peaks.md) — related

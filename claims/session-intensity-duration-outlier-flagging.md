---
type: claim
title: Session intensity and duration distributions flagged physically impossible persistence as severe statistical outliers
description: Session intensity and duration distributions flagged physically impossible persistence as severe statistical outliers
id: session-intensity-duration-outlier-flagging
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

# Session intensity and duration distributions flagged physically impossible persistence as severe statistical outliers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Accounts in the extreme regions of the intensity-versus-duration distribution, such as continuous sessions spanning 24+ hours without a 30-minute break, were flagged as severe statistical outliers consistent with automated behavior. [→ Germán Arroyo 2026](#german-arroyo-2026)

## Evidence

### Germán Arroyo 2026

Germán Arroyo, Luis López, and Juan Carlos Torres. (2026). Securing the Sandbox: A Rootless Containerized Framework for Process-Oriented Monitoring in Computer Graphics Education. https://arxiv.org/abs/2606.05929 [doi:10.48550/arxiv.2606.05929](https://doi.org/10.48550/arxiv.2606.05929)

`q2 · i?` · `design · r2`

Session intensity analysis (Figure 4b) of the pilot cohort, defining intensity as the ratio of recorded explicit actions to reconstructed session duration. The article reports that such extreme profiles "are physically impossible for human operators and are consistent with continuous server-side execution, browser macros, or automated 'stay-alive' scripts hitting the platform APIs."

> "Accounts located in the extreme regions of the intensity-versus-duration distribution—such as continuous sessions spanning 24+ hours without a single 30-minute cognitive break to segment the session—are flagged as severe statistical outliers."

## Discussion


## Related Claims
- [Macro-level behavioral metrics flagged anomalies consistent with automated workflows and off-platform AI code synthesis](behavioral-metrics-flag-automated-anomalies.md) — possibly the same claim (merge candidate)
- [Explicit API interception from a pilot cohort of 19 students yielded 1,880 events over about 57 active student-hours](vismatic-pilot-cohort-1880-events.md) — related

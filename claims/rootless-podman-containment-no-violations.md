---
type: claim
title: Rootless Podman isolation maintained containment with no observed privilege escalation or cross-identity contamination under classroom load
description: Rootless Podman isolation maintained containment with no observed privilege escalation or cross-identity contamination under classroom load
id: rootless-podman-containment-no-violations
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

# Rootless Podman isolation maintained containment with no observed privilege escalation or cross-identity contamination under classroom load

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across the observation window, no indicators of privilege escalation, inter-user interference, boundary violations, or cross-identity contamination were identified, suggesting the rootless Podman isolation layer maintained effective containment. [→ Germán Arroyo 2026](#german-arroyo-2026)

## Evidence

### Germán Arroyo 2026

Germán Arroyo, Luis López, and Juan Carlos Torres. (2026). Securing the Sandbox: A Rootless Containerized Framework for Process-Oriented Monitoring in Computer Graphics Education. https://arxiv.org/abs/2606.05929 [doi:10.48550/arxiv.2606.05929](https://doi.org/10.48550/arxiv.2606.05929)

`q2 · i?` · `design · r2`

Operational security analysis of system-wide API event logs under a single-tenant configuration on the deployed Raspberry Pi platform. The article also reports that "No evidence of cross-identity contamination or simultaneous multi-session identity collision was observed in the dataset," with workload variation attributed to normal user interaction differences.

> "Although the system was exposed to continuous network access over an extended period, no indicators of privilege escalation, inter-user interference, or boundary violations were identified. Overall, the results suggest that the rootless Podman isolation layer maintained effective containment of execution environments"

## Discussion


## Related Claims
- [Under high extraneous load (hint presentation and L and rL condition), no test-score increases were observed on identical or near-transfer problems](extraneous-load-eliminates-germane-load-learning-gains.md) — related
- [Explicit API interception from a pilot cohort of 19 students yielded 1,880 events over about 57 active student-hours](vismatic-pilot-cohort-1880-events.md) — related

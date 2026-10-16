---
type: claim
title: "Module 3 code execution success dropped to approximately 60% before a missing-dependency infrastructure fix, recovering to match the 86–87% rates of Modules 1 and 2"
description: "Module 3 code execution success dropped to approximately 60% before a missing-dependency infrastructure fix, recovering to match the 86–87% rates of Modules 1 and 2"
id: itas-module3-success-rate-infrastructure-fix
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: iizalaarab-elhaimeur-and-nikos-chrisochoides-2026
    resource: "https://doi.org/10.48550/arxiv.2604.24807"
    title: "Iizalaarab Elhaimeur and Nikos Chrisochoides. (2026). From Prototype to Classroom: An Intelligent Tutoring System for Quantum Education. https://arxiv.org/abs/2604.24807 [doi:10.48550/arxiv.2604.24807](https://doi.org/10.48550/arxiv.2604.24807)"
    author: Iizalaarab Elhaimeur and Nikos Chrisochoides
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: iizalaarab-elhaimeur-and-nikos-chrisochoides-2026-2
    resource: "https://arxiv.org/abs/2604.24807"
    title: "Iizalaarab Elhaimeur and Nikos Chrisochoides. (2026). From Prototype to Classroom: An Intelligent Tutoring System for Quantum Education. https://arxiv.org/abs/2604.24807"
    author: Iizalaarab Elhaimeur and Nikos Chrisochoides
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Module 3 code execution success dropped to approximately 60% before a missing-dependency infrastructure fix, recovering to match the 86–87% rates of Modules 1 and 2

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The Module 3 code execution success rate dropped to approximately 60% before the pylatexenc dependency fix, recovering to match the 86–87% rates observed in Modules 1 and 2 afterward. [→ Iizalaarab Elhaimeur and Nikos Chrisochoides 2026](#iizalaarab-elhaimeur-and-nikos-chrisochoides-2026)
`q2 i?` Deployment code execution produced 387 total executions with a 77% overall success rate. [→ Iizalaarab Elhaimeur and Nikos Chrisochoides 2026 (2)](#iizalaarab-elhaimeur-and-nikos-chrisochoides-2026-2)

## Evidence

### Iizalaarab Elhaimeur and Nikos Chrisochoides 2026

Iizalaarab Elhaimeur and Nikos Chrisochoides. (2026). From Prototype to Classroom: An Intelligent Tutoring System for Quantum Education. https://arxiv.org/abs/2604.24807 [doi:10.48550/arxiv.2604.24807](https://doi.org/10.48550/arxiv.2604.24807)

`q2 · i?` · `design · r2`

Log analysis of code executions from the pilot deployment. The Module 3 success rate "dropped to approximately 60% before the infrastructure fix", then recovered to the 86–87% levels of Modules 1 and 2; the figures are descriptive, with no test statistic printed.

> "The Module 3 code execution success rate, defined as the percentage of executions that completed without throwing a runtime error, dropped to approximately 60% before the infrastructure fix, recovering to match the 86–87% rates observed in Modules 1 and 2 afterward."

### Iizalaarab Elhaimeur and Nikos Chrisochoides 2026 (2)

Iizalaarab Elhaimeur and Nikos Chrisochoides. (2026). From Prototype to Classroom: An Intelligent Tutoring System for Quantum Education. https://arxiv.org/abs/2604.24807

`q2 · i?` · `design · r2`

Aggregate code execution telemetry from the same pilot deployment: 387 total executions with a 77% overall success rate, reported descriptively. Error analysis identified Qiskit API errors, missing library errors, and mathematical errors.

> "Code execution across the deployment produced 387 total executions with a 77% overall success rate."

## Discussion


## Related Claims
- [In archived sessions, no operator code changes or quantum-logic corrections were needed; eight of nine notebook executions only required one permitted fix of a missing visualization dependency](archived-qiskit-sessions-needed-only-environment-fixes.md) — related
- [ChatGPT could not execute R code for statistics MCQs, achieving 60% accuracy when its code was run with corrected dataset naming](chatgpt-r-code-questions-60-percent-accuracy.md) — related

---
type: claim
title: "The first billed calibration run failed both pedagogy gates badly, with a 43% earnest revise rate and 54% reported hint-ceiling compliance"
description: "The first billed calibration run failed both pedagogy gates badly, with a 43% earnest revise rate and 54% reported hint-ceiling compliance"
id: first-run-failed-pedagogy-gates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: yusuf-pisan-2026
    resource: "https://doi.org/10.48550/arXiv.2608.12292"
    title: "Yusuf Pisan. (2026). Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior. [doi:10.48550/arXiv.2608.12292](https://doi.org/10.48550/arXiv.2608.12292)"
    author: Yusuf Pisan
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# The first billed calibration run failed both pedagogy gates badly, with a 43% earnest revise rate and 54% reported hint-ceiling compliance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The starting point of the calibration loop was a run that both over-blocked honest students (43% earnest revise rate) and appeared to leak under pressure (54% hint-ceiling compliance). [→ Yusuf Pisan 2026](#yusuf-pisan-2026)

## Evidence

### Yusuf Pisan 2026

Yusuf Pisan. (2026). Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior. [doi:10.48550/arXiv.2608.12292](https://doi.org/10.48550/arXiv.2608.12292)

`q2 · i?` · `design · r3`

First billed run of the live test loop over the scripted-persona suites (§5, Results). The printed rates are "a 43% earnest revise rate (G2) and 54% hint-ceiling compliance (G3)".

> "The first billed run failed both pedagogy gates badly: a 43% earnest revise rate (G2) and 54% hint-ceiling compliance (G3), seemingly a system that both over-blocked honest students and leaked under pressure, a contradiction worth resolving first."

## Discussion


## Related Claims
- [Half of the apparent ceiling violations in the first run were auditor grounding rejections, not over-help; real ceiling compliance was about 77%](auditor-artifact-real-compliance-77.md) — related
- [An automated calibration loop drove a deployed LLM tutor to full compliance on all four acceptance gates, reaching a 0% earnest revise rate and 100% hint-ceiling compliance](llm-tutor-full-compliance-four-gates.md) — reports the opposite
- [Withholding failures of a capable LLM tutor form a descending over-help ladder, from blatant solution leaks to naming the exact bug to over-citing general facts](over-help-ladder-gross-to-subtle.md) — related

---
type: claim
title: "Half of the apparent ceiling violations in the first run were auditor grounding rejections, not over-help; real ceiling compliance was about 77%"
description: "Half of the apparent ceiling violations in the first run were auditor grounding rejections, not over-help; real ceiling compliance was about 77%"
id: auditor-artifact-real-compliance-77
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Half of the apparent ceiling violations in the first run were auditor grounding rejections, not over-help; real ceiling compliance was about 77%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Sorting rejections by cause revealed a measurement artifact: the auditor re-judged turns without the retrieved sources, so real hint-ceiling compliance was about 77%, not the reported 54%. [→ Yusuf Pisan 2026](#yusuf-pisan-2026)

## Evidence

### Yusuf Pisan 2026

Yusuf Pisan. (2026). Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior. [doi:10.48550/arXiv.2608.12292](https://doi.org/10.48550/arXiv.2608.12292)

`q2 · i?` · `design · r3`

Offline diagnostic of the auditor in the calibration loop (§5, Rung 0). The article prints "Real ceiling compliance was about 77%, still failing, but now genuine" after persisting the sources the live judge saw.

> "Sorting G3 rejections by cause (§4.4) showed that half of the apparent ceiling violations were grounding rejections, not over-help."

## Discussion


## Related Claims
- [An automated calibration loop drove a deployed LLM tutor to full compliance on all four acceptance gates, reaching a 0% earnest revise rate and 100% hint-ceiling compliance](llm-tutor-full-compliance-four-gates.md) — related
- [The first billed calibration run failed both pedagogy gates badly, with a 43% earnest revise rate and 54% reported hint-ceiling compliance](first-run-failed-pedagogy-gates.md) — related
- [Withholding failures of a capable LLM tutor form a descending over-help ladder, from blatant solution leaks to naming the exact bug to over-citing general facts](over-help-ladder-gross-to-subtle.md) — related

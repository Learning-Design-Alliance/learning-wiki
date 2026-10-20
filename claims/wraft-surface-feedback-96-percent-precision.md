---
type: claim
title: "Directly prompted GPT-4o surface-level corrective edits were judged necessary and effective in 96.14% of 2049 identified edits"
description: "Directly prompted GPT-4o surface-level corrective edits were judged necessary and effective in 96.14% of 2049 identified edits"
id: wraft-surface-feedback-96-percent-precision
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: adnan-labib-2026
    resource: "https://doi.org/10.48550/arxiv.2607.14524"
    title: "Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524 [doi:10.48550/arxiv.2607.14524](https://doi.org/10.48550/arxiv.2607.14524)"
    author: Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Directly prompted GPT-4o surface-level corrective edits were judged necessary and effective in 96.14% of 2049 identified edits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Expert raters judged 1970 of 2049 ERRANT-tagged edits (96.14%) both necessary and effective in the surface-level feedback test of 40 essays. [→ Adnan Labib 2026](#adnan-labib-2026)

## Evidence

### Adnan Labib 2026

Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524 [doi:10.48550/arxiv.2607.14524](https://doi.org/10.48550/arxiv.2607.14524)

`q2 · i?` · `design · r2`

Human evaluation of GPT-4o corrective edits on 40 test essays, with edits aligned via ERRANT v3.0.0 and rated by two expert raters on necessity and effectiveness. The "96.14%" precision indicates the system is nearly always correct when it identifies errors.

> "Human evaluation deemed 1985 edits deemed necessary (96.88%), out of which 1970 were deemed both necessary and effective (96.14%)."

## Discussion


## Related Claims
- [Directly prompted Claude 3.7 micro-level deep feedback was judged both necessary and effective in 94.69% of 630 comments](wraft-micro-feedback-95-percent-necessary-effective.md) — related
- [Directly prompted Claude 3.7 macro-level deep feedback was judged effective for 93.03% of 201 paragraph-level comments](wraft-macro-feedback-93-percent-effective.md) — related
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — a broader claim this one bears on
- [Supervised fine-tuning was less effective than direct prompting of SOTA LLMs for generating deep-level feedback, a task with non-deterministic output](sft-less-effective-than-prompting-for-feedback-generation.md) — related

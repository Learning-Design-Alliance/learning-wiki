---
type: claim
title: In a pre-guardrail deployment, students actively probed for answer-giving behavior and the baseline system sometimes complied, with boundary testing highest in the homework context
description: In a pre-guardrail deployment, students actively probed for answer-giving behavior and the baseline system sometimes complied, with boundary testing highest in the homework context
id: baseline-boundary-testing-homework-context
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: belle-li-lily-tan-wei-zakharov-colby-ben-acton-qiang-qiu-2026
    resource: "https://doi.org/10.48550/arXiv.2606.09845"
    title: "Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu. (2026). Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat. [doi:10.48550/arXiv.2606.09845](https://doi.org/10.48550/arXiv.2606.09845)"
    author: Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: belle-li-lily-tan-wei-zakharov-colby-ben-acton-qiang-qiu-2026-2
    resource: "https://doi.org/10.48550/arXiv.2606.09845"
    title: "Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu. (2026). Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat. [doi:10.48550/arXiv.2606.09845](https://doi.org/10.48550/arXiv.2606.09845)"
    author: Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In a pre-guardrail deployment, students actively probed for answer-giving behavior and the baseline system sometimes complied, with boundary testing highest in the homework context

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Boundary Testing / System Probing appeared in 13.4% of student messages overall and 22.0% in the homework context, while Direct Answer / Solution Seeking appeared in 7.0% of student messages and the system still produced direct solutions across contexts. [→ Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu 2026](#belle-li-lily-tan-wei-zakharov-colby-ben-acton-qiang-qiu-2026)
`q2 i?` The dual-family coding of the 284-message corpus reached strong inter-rater agreement (Cohen's kappa = .82) on a 60-message stratified random sample. [→ Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu 2026 (2)](#belle-li-lily-tan-wei-zakharov-colby-ben-acton-qiang-qiu-2026-2)

## Evidence

### Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu 2026

Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu. (2026). Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat. [doi:10.48550/arXiv.2606.09845](https://doi.org/10.48550/arXiv.2606.09845)

`q2 · i?` · `design · r2`

Directed content analysis of all interactions logged during a pre-guardrail deployment in the focal undergraduate Python course (Fall 2025): 284 messages from 31 conversations across exam preparation, homework debugging, and mini-project contexts. The article reports "Boundary Testing / System Probing (A8) reached 13.4% overall and 22.0% in the homework context"; no effect size is printed.

> "Direct Answer / Solution Seeking (A5) appeared in 7.0% of student messages, while Boundary Testing / System Probing (A8) reached 13.4% overall and 22.0% in the homework context."

### Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu 2026 (2)

Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu. (2026). Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat. [doi:10.48550/arXiv.2606.09845](https://doi.org/10.48550/arXiv.2606.09845)

`q2 · i?` · `design · r2`

Reliability check on the same baseline corpus coding: a stratified random sample of 60 messages (21.1% of the corpus) was independently coded, "yielding Cohen'sκ =.82, indicating strong agreement". Kappa is an agreement statistic, not an effect size, so impact is coded i? (no magnitude reported; not a null effect).

> "a second independent coder coded a stratified random sample of 60 messages (21.1% of the corpus), yielding Cohen'sκ =.82, indicating strong agreement"

## Discussion


## Related Claims
- [In the pre-guardrail baseline corpus, self-regulated-learning behaviors were nearly absent: hint utilization was not observed and self-evaluation appeared in only two messages](srl-behaviors-absent-baseline-corpus.md) — related
- [The pre-guardrail baseline system produced a high proportion of generic, non-instructional output (29.6%) and surfaced stale or incorrect course information](generic-stale-baseline-responses.md) — related
- [The mean marginal information gain criterion for active data selection prefers samples where the decision boundary is uncertain, improving on sampling on and near decision boundaries, but may give artifacts for poorly matched models](mean-marginal-information-gain-active-selection.md) — related

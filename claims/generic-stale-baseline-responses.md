---
type: claim
title: "The pre-guardrail baseline system produced a high proportion of generic, non-instructional output (29.6%) and surfaced stale or incorrect course information"
description: "The pre-guardrail baseline system produced a high proportion of generic, non-instructional output (29.6%) and surfaced stale or incorrect course information"
id: generic-stale-baseline-responses
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
    kind: qualitative
    rigour: 3
---

# The pre-guardrail baseline system produced a high proportion of generic, non-instructional output (29.6%) and surfaced stale or incorrect course information

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Although most baseline responses were not major failures, the corpus surfaced Stale or Incorrect Course Information (B7) and a high proportion of Generic / Non-Instructional output (B0, 29.6%). [→ Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu 2026](#belle-li-lily-tan-wei-zakharov-colby-ben-acton-qiang-qiu-2026)

## Evidence

### Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu 2026

Belle Li; Lily Tan; Wei Zakharov; Colby Ben Acton; Qiang Qiu. (2026). Tutor, Not Solver: Designing a Guardrailed AI Assistant for Learning in Higher Education: A Design Case of PeteChat. [doi:10.48550/arXiv.2606.09845](https://doi.org/10.48550/arXiv.2606.09845)

`q2 · i?` · `qualitative · r3`

System-response coding (Category B, 9 codes) of the same 284-message pre-guardrail baseline corpus in the Python course. The article reports "a high proportion of Generic / Non-Instructional output (B0, 29.6%)" plus stale or incorrect course information; the percentages are descriptive, with no effect size printed.

> "the corpus still surfaced Stale or Incorrect Course Information (B7) and a high proportion of Generic / Non-Instructional output (B0, 29.6%)."

## Discussion


## Related Claims
- [In a pre-guardrail deployment, students actively probed for answer-giving behavior and the baseline system sometimes complied, with boundary testing highest in the homework context](baseline-boundary-testing-homework-context.md) — related
- [Gen-AI hallucinates sources and values and produces convincing but incorrect explanations, risking student misinformation](genai-hallucination-convincing-incorrect-explanations.md) — related
- [Hallucinations and erroneous output are the most significant constraint on GenAI usage, keeping academic literature the primary knowledge source](hallucinations-most-significant-genai-constraint.md) — related
- [In the pre-guardrail baseline corpus, self-regulated-learning behaviors were nearly absent: hint utilization was not observed and self-evaluation appeared in only two messages](srl-behaviors-absent-baseline-corpus.md) — related

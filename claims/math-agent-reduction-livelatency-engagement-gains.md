---
type: claim
title: Reducing Math Agent output and disabling it for non-math courses reduced latency and increased behavioral engagement
description: Reducing Math Agent output and disabling it for non-math courses reduced latency and increased behavioral engagement
id: math-agent-reduction-livelatency-engagement-gains
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: udeshi-2026
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: udeshi-2026-2
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Reducing Math Agent output and disabling it for non-math courses reduced latency and increased behavioral engagement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` A concise-response prompt on the Math Agent decreased time to full response latency (P50) by 32.7% ± 1.0% and increased behavioral engagement by 4.65 ± 2.98%. [→ Udeshi 2026](#udeshi-2026)
`q2 i?` Disabling the Math Agent for non-math conversations decreased time-to-first-token latency (P50) by 6.91 ± .71% (LLM classifier variation) and 5.98 ± .79% (course-domain variation) while increasing behavioral engagement; the deterministic course-domain check was launched. [→ Udeshi 2026 (2)](#udeshi-2026-2)

## Evidence

### Udeshi 2026

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment on the Exercise surface adding a concision instruction to the Math Agent prompt, aiming "for under 50 words total." The reported point estimates are midpoints of 95% confidence intervals with margins of error, with LLM-judge metrics rectified for judge error.

> "Statistically significant Changes: ● Time to full response latency (P50) decreased by 32.7% ± 1.0% ● Behavioral engagement increased by 4.65 ± 2.98%"

### Udeshi 2026 (2)

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment with two variations for skipping the Math Agent on non-math conversations: an LLM classifier versus the Exercise's course domain. Results are shown in Table 1 for both variations; "Due to simplicity of implementation we launched the deterministic check of the Exercise's course domain (Variation 2)."

> "Time to first token Latency (P50) decreased by 6.91 ± .71% decreased by 5.98 ± .79% Time to full response Latency (P50) decreased by 6.92 ± .81% decreased by 6.12 ± .81% Behavioral engagement increased by 2.74 ± 2.01% increased by 2.63 ± 2.04%"

## Discussion


## Related Claims
- [Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement](math-agent-guidance-limit-tradeoff.md) — related

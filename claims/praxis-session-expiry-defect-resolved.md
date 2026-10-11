---
type: claim
title: Authentication regressions exposed a session-expiry defect in the preceding release, and the recorded release establishes a fresh anonymous session after timeout
description: Authentication regressions exposed a session-expiry defect in the preceding release, and the recorded release establishes a fresh anonymous session after timeout
id: praxis-session-expiry-defect-resolved
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: nizam-kadir-2026
    resource: "https://arxiv.org/abs/2610.02699"
    title: "Nizam Kadir. (2026). LearnAdapt Praxis: Controlled AI Assistance and Evidence Traces for Adult Workplace Learning. Technical research report. https://arxiv.org/abs/2610.02699"
    author: Nizam Kadir
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Authentication regressions exposed a session-expiry defect in the preceding release, and the recorded release establishes a fresh anonymous session after timeout

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The authentication harness reproduced a defect where a destroyed timed-out session could render a login form without persisting a new session token, causing the subsequent login POST to fail CSRF validation; the recorded release establishes a fresh anonymous session after timeout. [→ Nizam Kadir 2026](#nizam-kadir-2026)

## Evidence

### Nizam Kadir 2026

Nizam Kadir. (2026). LearnAdapt Praxis: Controlled AI Assistance and Evidence Traces for Adult Workplace Learning. Technical research report. https://arxiv.org/abs/2610.02699

`q2 · i?` · `design · r2`

Separate authentication regression harnesses (router/session harness with 58 HTTP checks passed; authentication UI harness with 37 assertions passed), reported separately from the 3,990 rehearsal checks. The report states "The recorded release establishes a fresh anonymous session after timeout"; no effect size applies.

> "The authentication harness reproduced a concrete defect in the preceding release. When timeout enforcement destroyed an authenticated session, the same request could render a new login form without persisting a new session for its token."

## Discussion


## Related Claims
-

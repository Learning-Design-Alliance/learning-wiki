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
    resource: "https://doi.org/10.48550/arxiv.2610.02699"
    title: "Nizam Kadir. (2026). LearnAdapt Praxis: Controlled AI Assistance and Evidence Traces for Adult Workplace Learning. Technical research report. https://arxiv.org/abs/2610.02699 [doi:10.48550/arxiv.2610.02699](https://doi.org/10.48550/arxiv.2610.02699)"
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

Nizam Kadir. (2026). LearnAdapt Praxis: Controlled AI Assistance and Evidence Traces for Adult Workplace Learning. Technical research report. https://arxiv.org/abs/2610.02699 [doi:10.48550/arxiv.2610.02699](https://doi.org/10.48550/arxiv.2610.02699)

`q2 · i?` · `design · r2`

Separate authentication regression harnesses (router/session harness with 58 HTTP checks passed; authentication UI harness with 37 assertions passed), reported separately from the 3,990 rehearsal checks. The report states "The recorded release establishes a fresh anonymous session after timeout"; no effect size applies.

> "The authentication harness reproduced a concrete defect in the preceding release. When timeout enforcement destroyed an authenticated session, the same request could render a new login form without persisting a new session for its token."

## Discussion


## Related Claims

- [A frozen synthetic rehearsal of 120 serial project episodes passed all 3,990 recorded checks with zero unexpected failures](praxis-120-episode-rehearsal-all-checks-passed.md)
- [Injected provider failures produced recorded unavailability and zero fabricated hints, while valid and reentrant conditions stored 30 synthetic hints each](praxis-provider-failure-no-fabricated-hints.md)
- [During active transfer, the application rejected learner coaching and export requests and redacted earlier project content in all 120 episodes](praxis-transfer-restrictions-enforced.md)

---
type: claim
title: During active transfer, the application rejected learner coaching and export requests and redacted earlier project content in all 120 episodes
description: During active transfer, the application rejected learner coaching and export requests and redacted earlier project content in all 120 episodes
id: praxis-transfer-restrictions-enforced
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# During active transfer, the application rejected learner coaching and export requests and redacted earlier project content in all 120 episodes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In all 120 episodes, active-transfer responses passed the redaction check, coaching requests were rejected without reaching the provider, and learner exports were rejected, while the facilitator retained inspection access. [→ Nizam Kadir 2026](#nizam-kadir-2026)

## Evidence

### Nizam Kadir 2026

Nizam Kadir. (2026). LearnAdapt Praxis: Controlled AI Assistance and Evidence Traces for Adult Workplace Learning. Technical research report. https://arxiv.org/abs/2610.02699 [doi:10.48550/arxiv.2610.02699](https://doi.org/10.48550/arxiv.2610.02699)

`q2 · i?` · `design · r2`

Results of the 120-episode synthetic rehearsal (Results section, workflow and authority group: 1,080 transfer-restriction checks with zero unexpected failures). The report states "All 120 active-transfer coaching requests were rejected without calling the injected provider"; no effect size applies.

> "All 120 active-transfer responses passed the composite redaction check. All 120 active-transfer coaching requests were rejected without calling the injected provider; all 120 learner exports during that phase were rejected."

## Discussion


## Related Claims

- [A frozen synthetic rehearsal of 120 serial project episodes passed all 3,990 recorded checks with zero unexpected failures](praxis-120-episode-rehearsal-all-checks-passed.md) — related
- [Injected provider failures produced recorded unavailability and zero fabricated hints, while valid and reentrant conditions stored 30 synthetic hints each](praxis-provider-failure-no-fabricated-hints.md) — related
- [GPT-4 over-redacts famous names, locations, and mythological creatures that are not PII in educational forum discussions](gpt4-over-redaction-of-non-pii-names-and-locations.md) — related
- [GPT-4 achieves high recall (average 0.958) but low precision (average 0.526) when de-identifying MOOC forum posts](gpt4-high-recall-low-precision-pii-redaction.md) — related
- [Supervised machine learning de-identification still outperforms GPT-4, though GPT-4 exceeds class-list/regular-expression and transformer approaches in recall](gpt4-redaction-compared-to-prior-methods.md) — related
- [Authentication regressions exposed a session-expiry defect in the preceding release, and the recorded release establishes a fresh anonymous session after timeout](praxis-session-expiry-defect-resolved.md)

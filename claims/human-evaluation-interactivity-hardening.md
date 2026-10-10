---
type: claim
title: "In directional manual testing, reward hardening halved unusable interactive pages (25%→10%) and eliminated page-entry failures (2/24→0/30)"
description: "In directional manual testing, reward hardening halved unusable interactive pages (25%→10%) and eliminated page-entry failures (2/24→0/30)"
id: human-evaluation-interactivity-hardening
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: cogevol-team-2026
    resource: "https://arxiv.org/abs/2608.30968"
    title: "CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968"
    author: "CogEvol Team, CogEvol Inc. & Tsinghua University"
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# In directional manual testing, reward hardening halved unusable interactive pages (25%→10%) and eliminated page-entry failures (2/24→0/30)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Pages that cannot be entered went from 2/24 to 0/30, all eight games in the second round were playable on entry, fully usable pages rose from 58.3% to 66.7%, and unusable pages halved (25%→10%). [→ CogEvol Team 2026](#cogevol-team-2026)

## Evidence

### CogEvol Team 2026

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968

`q2 · i?` · `design · r3`

Two rounds of internal manual testing on the local OpenMAIC deployment (pre-hardening build n=24 vs CogEvol-27B n=30), each page graded by hand; the report labels the rounds "directional rather than strictly controlled".

> "pages that cannot be entered go from 2/24 to0/30, and all eight games generated in the second round were playable on entry—the interactivity hardening shows up in human hands, not only under the probe."

## Discussion


## Related Claims
- [On the report's internal suites CogEvol-27B scores 83.7 on slides and 63.7 on HTML-500 with zero hard failures, while no external flagship leads both modalities](cogevol-benchmark-no-flagship-leads-both-modalities.md) — related
- [A screenshot-only reward was reward-hacked into producing visually convincing but unplayable games; hardening the reward with an interactivity probe and hard-fail gate reversed the collapse](reward-hacking-games-interactivity-probe.md) — related
- [SFT reliably teaches the two output contracts but cannot raise interactive-HTML quality, which declines monotonically with update count](sft-teaches-contracts-not-html-quality.md) — related

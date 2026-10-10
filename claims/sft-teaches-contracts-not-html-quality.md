---
type: claim
title: SFT reliably teaches the two output contracts but cannot raise interactive-HTML quality, which declines monotonically with update count
description: SFT reliably teaches the two output contracts but cannot raise interactive-HTML quality, which declines monotonically with update count
id: sft-teaches-contracts-not-html-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# SFT reliably teaches the two output contracts but cannot raise interactive-HTML quality, which declines monotonically with update count

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Under the pre-hardening reward, HTML quality declines monotonically with update count on Qwen3.6-27B (88.4 at 6,710 updates, 83.7 at 10,711, ~73.5 at 13,421), and the Qwen3.8 run lands at 73.2, below its own bare base of 78.3. [→ CogEvol Team 2026](#cogevol-team-2026)

## Evidence

### CogEvol Team 2026

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968

`q2 · i?` · `design · r3`

SFT ablation runs (Table 2 and text), scored under the pre-hardening reward and compared within that period only; the Qwen3.8 run ceded ground where the base was strongest (code −7.0pp, game −17.9pp).

> "HTML quality declines monotonically with update count on Qwen3.6-27B—88.4 at 6,710 updates, 83.7 at 10,711,∼73.5 at 13,421—whether the extra updates come from more passes or a smaller batch;"

## Discussion


## Related Claims
- [On the report's internal suites CogEvol-27B scores 83.7 on slides and 63.7 on HTML-500 with zero hard failures, while no external flagship leads both modalities](cogevol-benchmark-no-flagship-leads-both-modalities.md) — related
- [In directional manual testing, reward hardening halved unusable interactive pages (25%→10%) and eliminated page-entry failures (2/24→0/30)](human-evaluation-interactivity-hardening.md) — related
- [A screenshot-only reward was reward-hacked into producing visually convincing but unplayable games; hardening the reward with an interactivity probe and hard-fail gate reversed the collapse](reward-hacking-games-interactivity-probe.md) — related

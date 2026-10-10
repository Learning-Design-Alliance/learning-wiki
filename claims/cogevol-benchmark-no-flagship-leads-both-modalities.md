---
type: claim
title: "On the report's internal suites CogEvol-27B scores 83.7 on slides and 63.7 on HTML-500 with zero hard failures, while no external flagship leads both modalities"
description: "On the report's internal suites CogEvol-27B scores 83.7 on slides and 63.7 on HTML-500 with zero hard failures, while no external flagship leads both modalities"
id: cogevol-benchmark-no-flagship-leads-both-modalities
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
    rigour: 2
  - id: cogevol-team-2026-2
    resource: "https://arxiv.org/abs/2608.30968"
    title: "CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968"
    author: "CogEvol Team, CogEvol Inc. & Tsinghua University"
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# On the report's internal suites CogEvol-27B scores 83.7 on slides and 63.7 on HTML-500 with zero hard failures, while no external flagship leads both modalities

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`

## Subclaims
`q2 i?` Qwen3.8-Max ties CogEvol-27B's 83.7 slide score only with the full 34 KB specification, but collapses to 35.3 on HTML-500 with 204 of 500 pages dead at the probe. [→ CogEvol Team 2026](#cogevol-team-2026)
`q2 i?` Claude Opus 4.8 posts the best external HTML average (67.2 vs 63.7) while failing 19 pages outright on dead interactions; GLM-5.3 has 115 of 500 pages dead. [→ CogEvol Team 2026 (2)](#cogevol-team-2026-2)

## Evidence

### CogEvol Team 2026

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968

`q2 · i?` · `design · r2`

Main results (Table 3 protocol): external flagships run the identical harness with slide columns under the generous 34 KB specification; Qwen3.8-Max scores 23.9 zero-shot on the slim contract.

> "the same model collapses on the other modality: 35.3 on HTML-500 with 204 of 500 pages dead at the probe, where CogEvol-27B scores 63.7 with zero hard failures."

### CogEvol Team 2026 (2)

CogEvol Team, CogEvol Inc. & Tsinghua University. (2026). CogEvol: Towards Efficient and Reliable Learning Environment Generation. arXiv:2608.30968v2. https://arxiv.org/abs/2608.30968

`q2 · i?` · `design · r3`

Main results table reading: the report concludes "no model leads both modalities under either condition"; GLM-5.3 shows the same fluent-but-broken split with 115 of 500 pages dead.

> "Claude Opus 4.8 posts the best external HTML average (67.2 vs. 63.7, leading four of six sub-types) while failing 19 pages outright on dead interactions, and GPT-5.4 (66.0) fails 13;"

## Discussion


## Related Claims
- [SFT reliably teaches the two output contracts but cannot raise interactive-HTML quality, which declines monotonically with update count](sft-teaches-contracts-not-html-quality.md) — related
- [Purpose-trained single-pass generation completes a slide in a median of 17 seconds and an interactive page in 59 seconds over 220k production requests, and delivers artifacts at 15–22× lower per-artifact API cost than flagship models](cogevol-single-pass-latency-and-cost.md) — related
- [A screenshot-only reward was reward-hacked into producing visually convincing but unplayable games; hardening the reward with an interactivity probe and hard-fail gate reversed the collapse](reward-hacking-games-interactivity-probe.md) — related
- [In directional manual testing, reward hardening halved unusable interactive pages (25%→10%) and eliminated page-entry failures (2/24→0/30)](human-evaluation-interactivity-hardening.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related

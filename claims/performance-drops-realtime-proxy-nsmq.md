---
type: claim
title: LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally
description: LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally
id: performance-drops-realtime-proxy-nsmq
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: george-boateng-2026
    resource: "https://arxiv.org/abs/2605.07051"
    title: "George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051"
    author: George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Performance for offline evaluation drops across models in the real-time proxy evaluation, showing that settings without all clues available pose a challenge. [→ George Boateng 2026](#george-boateng-2026)

## Evidence

### George Boateng 2026

George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051

`q2 · i?` · `design · r2`

Real-time proxy evaluation on 2019 riddles (156), feeding 7-word chunks of clues and letting models decide whether to answer with a confidence judgment. For example, GPT-5.4 (high) fell from 86.54% EM offline to 75.64% EM in the proxy setting.

> "Noticeably, the performance for offline evaluation drops across models for the real-time proxy evaluation, demonstrating that real-time settings, during which not all the clues will be available, will pose a challenge."

## Discussion


## Related Claims
- [The best LLMs perform below the best student contestants in the real-time proxy riddle round](best-llms-below-best-students-nsmq-riddles.md) — related
- [In offline evaluation on NSMQ Riddles, closed LLMs generally outperform open models and higher reasoning settings improve performance](closed-models-and-high-reasoning-outperform-offline-nsmq.md) — related
- [Answering early on few clues correlates with worse real-time proxy performance](early-answering-correlates-worse-realtime-performance.md) — a narrower finding that bears on this claim
- [LLMs struggle most with Chemistry riddles, with best EM accuracy at or below 75% versus above 90% in other subjects](llms-struggle-most-chemistry-nsmq-riddles.md) — related

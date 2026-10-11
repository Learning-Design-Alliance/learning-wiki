---
type: claim
title: Answering early on few clues correlates with worse real-time proxy performance
description: Answering early on few clues correlates with worse real-time proxy performance
id: early-answering-correlates-worse-realtime-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
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

# Answering early on few clues correlates with worse real-time proxy performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Claude Opus 4.6's tendency to answer early correlates with its worse real-time proxy performance relative to other models, despite strong offline performance; GPT-OSS-120B behaves similarly. [→ George Boateng 2026](#george-boateng-2026)

## Evidence

### George Boateng 2026

George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051

`q2 · i?` · `design · r2`

Behavioral analysis of the real-time proxy evaluation, computing the average number of clues each model waits for before answering. Claude Opus 4.6 answers earliest (avg clue correct 3.188 at high reasoning) and GPT-OSS-120B similarly early, while Kimi-K2.5 and DeepSeek-V3.1 wait for at least 4 clues on average.

> "This tendency to answer early correlates with Claude Opus 4.6's worse performance in the real-time proxy test compared to the other models, despite its strong performance in the offline evaluation."

## Discussion


## Related Claims
- [The best LLMs perform below the best student contestants in the real-time proxy riddle round](best-llms-below-best-students-nsmq-riddles.md) — related
- [LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally](performance-drops-realtime-proxy-nsmq.md) — a broader claim this one bears on

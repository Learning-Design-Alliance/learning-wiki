---
type: claim
title: In offline evaluation on NSMQ Riddles, closed LLMs generally outperform open models and higher reasoning settings improve performance
description: In offline evaluation on NSMQ Riddles, closed LLMs generally outperform open models and higher reasoning settings improve performance
id: closed-models-and-high-reasoning-outperform-offline-nsmq
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: george-boateng-2026
    resource: "https://doi.org/10.48550/arxiv.2605.07051"
    title: "George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051 [doi:10.48550/arxiv.2605.07051](https://doi.org/10.48550/arxiv.2605.07051)"
    author: George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In offline evaluation on NSMQ Riddles, closed LLMs generally outperform open models and higher reasoning settings improve performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Closed models generally performed better than open models offline, with GPT-5.4 (reasoning=high) best at 86.54% EM accuracy. [→ George Boateng 2026](#george-boateng-2026)

## Evidence

### George Boateng 2026

George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051 [doi:10.48550/arxiv.2605.07051](https://doi.org/10.48550/arxiv.2605.07051)

`q2 · i?` · `design · r2`

Offline evaluation of six state-of-the-art LLMs (closed and open) on the 2019 NSMQ riddles (156 riddles), giving each model all clues and scoring Exact Match and Fuzzy Match accuracy. The article reports "GPT-5.4 (with reasoning=high) performing the best with 86.54% on EM accuracy".

> "Our evaluation showed that closed models generally performed better than open models, with GPT-5.4 (with reasoning=high) performing the best with 86.54% on EM accuracy."

## Discussion


## Related Claims
- [LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally](performance-drops-realtime-proxy-nsmq.md) — related
- [The best LLMs perform below the best student contestants in the real-time proxy riddle round](best-llms-below-best-students-nsmq-riddles.md) — related
- [LLMs struggle most with Chemistry riddles, with best EM accuracy at or below 75% versus above 90% in other subjects](llms-struggle-most-chemistry-nsmq-riddles.md) — related

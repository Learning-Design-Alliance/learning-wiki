---
type: claim
title: "LLMs struggle most with Chemistry riddles, with best EM accuracy at or below 75% versus above 90% in other subjects"
description: "LLMs struggle most with Chemistry riddles, with best EM accuracy at or below 75% versus above 90% in other subjects"
id: llms-struggle-most-chemistry-nsmq-riddles
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

# LLMs struggle most with Chemistry riddles, with best EM accuracy at or below 75% versus above 90% in other subjects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across all models, performance was strong in all subjects except Chemistry, where the best models scored equal to or below 75% EM accuracy while other subjects exceeded 90%. [→ George Boateng 2026](#george-boateng-2026)

## Evidence

### George Boateng 2026

George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051

`q2 · i?` · `design · r2`

Subject breakdown of the offline evaluation on 2019 NSMQ riddles (Table 5). The article attributes the Chemistry difficulty to handling of organic compounds and complex terminology, with models oversimplifying answers, e.g. answering "alkane" instead of "Cyclohexane".

> "Across all models, our evaluation indicated that they performed quite well across all subjects except Chemistry, which posed a significant challenge, with the best models performing equal to or below 75% EM accuracy compared to the other subjects, which had the best models above 90%."

## Discussion


## Related Claims
- [The best LLMs perform below the best student contestants in the real-time proxy riddle round](best-llms-below-best-students-nsmq-riddles.md) — related
- [In offline evaluation on NSMQ Riddles, closed LLMs generally outperform open models and higher reasoning settings improve performance](closed-models-and-high-reasoning-outperform-offline-nsmq.md) — related
- [LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally](performance-drops-realtime-proxy-nsmq.md) — related

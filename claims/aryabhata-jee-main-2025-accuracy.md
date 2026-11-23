---
type: claim
title: "Aryabhata 1.0 achieves 86.0% accuracy on the JEE Main 2025 January session and 90.2% on the April session with roughly 2K tokens per response"
description: "Aryabhata 1.0 achieves 86.0% accuracy on the JEE Main 2025 January session and 90.2% on the April session with roughly 2K tokens per response"
id: aryabhata-jee-main-2025-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ritvik-rastogi-2025
    resource: "https://doi.org/10.48550/arXiv.2508.08665"
    title: "Ritvik Rastogi, Sachin Dharashivkar, Sandeep Varma. (2025). Aryabhata: An exam-focused language model for JEE Math. arXiv. [doi:10.48550/arXiv.2508.08665](https://doi.org/10.48550/arXiv.2508.08665)"
    author: Ritvik Rastogi, Sachin Dharashivkar, Sandeep Varma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Aryabhata 1.0 achieves 86.0% accuracy on the JEE Main 2025 January session and 90.2% on the April session with roughly 2K tokens per response

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the in-distribution JEE Main 2025 benchmark, Aryabhata 1.0 scores 86.0% (January, 250 questions) and 90.2% (April, 225 questions) while averaging approximately 2K tokens per response. [→ Ritvik Rastogi 2025](#ritvik-rastogi-2025)

## Evidence

### Ritvik Rastogi 2025

Ritvik Rastogi, Sachin Dharashivkar, Sandeep Varma. (2025). Aryabhata: An exam-focused language model for JEE Math. arXiv. [doi:10.48550/arXiv.2508.08665](https://doi.org/10.48550/arXiv.2508.08665)

`q2 · i?` · `design · r2`

Evaluation on official JEE Main 2025 exam papers (January: 250 questions across 10 papers; April: 225 across 9 papers), scored by pass@1 with greedy decoding and an answer-matching pipeline. The article reports "an accuracy of 86.0% on the January session and 90.2% on the April session".

> "Figure 1 shows that Aryabhata 1.0 achieves an accuracy of 86.0% on the January session and 90.2% on the April session, while maintaining to- ken efficiency with an average of approximately ~2K tokens per response."

## Discussion


## Related Claims
- On JEE Main 2025, Aryabhata outperforms all compared open-weight and proprietary baselines in accuracy while remaining competitive in inference cost — related
- Aryabhata 1.0 generalizes out of distribution, scoring 83.6 on MATH 500 and 94.8 on GSM8K and outperforming its base models on both — related
- [Accuracy-cost value frontier: at $0.10 per million tokens, CDPK performance rose from 50% (April 2024) to 82% (June 2025)](cdpk-value-frontier-rapid-cost-performance-improvement.md) — related
- [Grok XI improved from 90.7% to 92.7% and Gemini from 87.3% to 88.7% between the two testing sessions, while DeepSeek-V3 declined from 87.3% to 86.7%](grok-gemini-accuracy-shift-between-sessions.md) — related

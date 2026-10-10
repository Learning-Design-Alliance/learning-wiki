---
type: claim
title: On the live single-node deployment, short-answer rounds take ≈32 s (≈$0.015/round) while multiple-choice rounds are ≈4× faster (≈7.6 s, ≈$0.005/round) because grading is deterministic
description: On the live single-node deployment, short-answer rounds take ≈32 s (≈$0.015/round) while multiple-choice rounds are ≈4× faster (≈7.6 s, ≈$0.005/round) because grading is deterministic
id: collearn-latency-cost-efficiency
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: kailai-he-2026
    resource: "https://arxiv.org/abs/2609.21154"
    title: "Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154"
    author: Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the live single-node deployment, short-answer rounds take ≈32 s (≈$0.015/round) while multiple-choice rounds are ≈4× faster (≈7.6 s, ≈$0.005/round) because grading is deterministic

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Measured on the live backend, short-answer rounds cost ≈32 s and ≈$0.015 each, while multiple-choice rounds take ≈7.6 s and ≈$0.005 because only next-item generation calls the LLM. [→ Kailai He 2026](#kailai-he-2026)

## Evidence

### Kailai He 2026

Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li. (2026). CoLearn: An Agentic Tutor that Learns its Learner in a Human–AI Co-Learning Loop. https://arxiv.org/abs/2609.21154

`q2 · i?` · `design · r2`

Latency and cost measured on the live single-node deployment (AWS Bedrock, Claude Sonnet 4.5); the article reports "Short-answer ≈32 s/round (grade+feedback dominate); MCQ ≈7.6 s (determin- istic answer)" with cost estimated from token usage.

> "Short-answer ≈32 s/round (grade+feedback dominate); MCQ ≈7.6 s (determin- istic answer). Cost is estimated from token usage."

## Discussion


## Related Claims
- [Taking initial multiple-choice tests without feedback can lead students to later produce the incorrect lure answers they selected, even when an overall retrieval practice benefit occurs](multiple-choice-lures-can-be-learned-as-false-knowledge.md) — related

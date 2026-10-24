---
type: claim
title: "Retrieval augmentation is essential for on-premise educational QA: a local LLM without retrieval scores below even a TF-IDF baseline"
description: "Retrieval augmentation is essential for on-premise educational QA: a local LLM without retrieval scores below even a TF-IDF baseline"
id: retrieval-augmentation-essential-local-llm-below-tfidf
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: shen-x-2026
    title: Shen X 2026
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Retrieval augmentation is essential for on-premise educational QA: a local LLM without retrieval scores below even a TF-IDF baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Local LLM (no retrieval) configuration achieves 52.3% overall accuracy, below the TF-IDF baseline's 55.4% and far below RAG-based configurations. [→ Shen X 2026](#shen-x-2026)

## Evidence

### Shen X 2026

Shen X, Feng L, Hua S, Liu D, Xie Z and Liu B (2026) Towards sustainable AI knowledge-base assistants in computer science education: on-premise deployment and optimization with open educational resources. Front. Psychol. 17:1843444. https://doi.org/10.3389/fpsyg.2026.1843444

`q2 · i?` · `design · r2`

Results section (5.1, Table 3) comparison across baseline conditions on the n = 300 query evaluation set. The article reports the no-retrieval LLM at "only 52.3% overall accuracy, substantially below even the TF-IDF baseline (55.4%)". No standardized effect size is printed.

> "Retrieval augmentation is essential: the Local LLM (no retrieval) configuration achieves only 52.3% overall accuracy, substantially below even the TF-IDF baseline (55.4%)"

## Discussion


## Related Claims

- [DeepSeek-MoE (Ours) achieves the strongest overall balance of accuracy among tested configurations, reaching 78.6% overall and 81.2% multi-hop reasoning accuracy on a 300-query OER evaluation set](deepseek-moe-ours-strongest-accuracy-balance.md) — related
- [The RAG-enhanced assistant achieves context recall above 0.93 and answer relevance of 0.87 on an expert-built 52-question evaluation set](rag-assistant-high-recall-relevance.md) — related
- [Post-deployment diagnostics attributed many remaining retrieval misses to query formulation, with bounded expansion recovering eleven of 24 original queries without lowering the relevance floor](retrieval-misses-attributed-to-query-formulation.md)
- [Indexing LLM-generated artifacts nearly doubles retrieval recall on analytical queries compared with transcript-only retrieval, while direct queries perform comparably across configurations](artifact-indexing-improves-analytical-retrieval.md) — a narrower finding that bears on this claim
- [Targeted enhancements (retrieval-augmented inference, multimodal training) substantially raise open-source models' phonology mastery to near-ceiling levels](targeted-enhancements-raise-phonology-mastery.md) — related

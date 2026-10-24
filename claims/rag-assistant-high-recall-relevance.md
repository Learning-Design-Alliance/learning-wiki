---
type: claim
title: The RAG-enhanced assistant achieves context recall above 0.93 and answer relevance of 0.87 on an expert-built 52-question evaluation set
description: The RAG-enhanced assistant achieves context recall above 0.93 and answer relevance of 0.87 on an expert-built 52-question evaluation set
id: rag-assistant-high-recall-relevance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ronghua-xu-2026
    resource: "https://doi.org/10.48550/arxiv.2608.08163"
    title: "Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian. (2026). Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform for High Dose Rate (HDR) Brachytherapy. arXiv. https://arxiv.org/abs/2608.08163 [doi:10.48550/arxiv.2608.08163](https://doi.org/10.48550/arxiv.2608.08163)"
    author: Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The RAG-enhanced assistant achieves context recall above 0.93 and answer relevance of 0.87 on an expert-built 52-question evaluation set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Evaluated with the RAGAS framework on 52 expert-developed question-answer pairs, the system retrieved sufficient clinical content (context recall above 0.93) and generated responses closely aligned with query intent (answer relevance 0.87). [→ Ronghua Xu 2026](#ronghua-xu-2026)

## Evidence

### Ronghua Xu 2026

Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian. (2026). Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform for High Dose Rate (HDR) Brachytherapy. arXiv. https://arxiv.org/abs/2608.08163 [doi:10.48550/arxiv.2608.08163](https://doi.org/10.48550/arxiv.2608.08163)

`q2 · i?` · `design · r2`

RAGAS evaluation of the prototype's RAG assistant on 52 question-answer pairs developed by medical professionals, categorized as basic, medium, and advanced. The article reports context recall "above 0.93" and separately an answer relevance score of 0.87; answer completeness was consistently high across configurations.

> "We found that recall successfully captured the required information to answer the question, with a score above 0.93 showing a strong retrieval capacity for retrieving sufficient clinical content."

## Discussion


## Related Claims
- [Retrieval augmentation is essential for on-premise educational QA: a local LLM without retrieval scores below even a TF-IDF baseline](retrieval-augmentation-essential-local-llm-below-tfidf.md) — related
- [Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower](rq-higher-relevancy-lower-grounding.md) — related

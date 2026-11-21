---
type: claim
title: RAG with slide text improves exam-question performance across all tested LLMs, with the smallest model showing the least improvement
description: RAG with slide text improves exam-question performance across all tested LLMs, with the smallest model showing the least improvement
id: rag-slide-text-improves-all-llm-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tu-anh-dinh-2026
    resource: "https://doi.org/10.63317/5bjdtya4ui69"
    title: "Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)"
    author: Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# RAG with slide text improves exam-question performance across all tested LLMs, with the smallest model showing the least improvement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Incorporating RAG with slide text improves the performance of all tested LLMs on SciEx exams, with LLaMA 3.1 8B showing the least improvement (+0.8 points). [→ Tu Anh Dinh 2026](#tu-anh-dinh-2026)

## Evidence

### Tu Anh Dinh 2026

Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)

`q2 · i?` · `causal · r2`

Experiment comparing each LLM with and without RAG using slide text on SciEx exams (exam-level scores 0-60), graded automatically by Mistral Large 2 (Pearson correlation of 0.84 with expert grades). Average score rises from 39.40 baseline to 41.05 with RAG. The article reports it "shows the least improvement (+0.8 points)" for LLaMA 3.1 8B.

> "Overall, incorporating RAG with slide text improves the performance of all models. Among them, LLaMA 3.1 8B, the smallest model, shows the least improvement (+0.8 points), likely due to its more limited capacity to leverage additional context."

## Discussion


## Related Claims
- [CPT on course materials does not bring consistent improvement, performing on average worse than both baseline and RAG](cpt-inconsistent-gains-catastrophic-forgetting.md) — related
- [RAG mitigates knowledge gaps on topics where LLMs are weak, yielding the largest topic-level gains on Human–Computer Interaction](rag-mitigates-topic-knowledge-gaps-hci.md) — related
- [RAG provides greater benefits on difficult questions, with the largest gains on hard questions](rag-bigger-gains-hard-questions.md) — related
- [Multimodal RAG with slide images outperforms text-only slide retrieval for a vision-capable LLM](multimodal-rag-slide-images-outperform-text.md) — related
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related

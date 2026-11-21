---
type: claim
title: Multimodal RAG with slide images outperforms text-only slide retrieval for a vision-capable LLM
description: Multimodal RAG with slide images outperforms text-only slide retrieval for a vision-capable LLM
id: multimodal-rag-slide-images-outperform-text
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

# Multimodal RAG with slide images outperforms text-only slide retrieval for a vision-capable LLM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Providing retrieved slides as images to Qwen2-VL leads to higher performance than providing extracted slide text, because visual information such as images, layout, and formulas contributes to better comprehension. [→ Tu Anh Dinh 2026](#tu-anh-dinh-2026)

## Evidence

### Tu Anh Dinh 2026

Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)

`q2 · i?` · `causal · r2`

Experiment comparing slide text retrieval versus slide image input under multimodal RAG with Qwen2-VL (exam-level scores 0-60): average rises from 38.05 baseline to 40.87 with slide text and 42.50 with slide images. The authors give an example where the slide image preserves "the arrows illustrating the temporal scope".

> "The results show that providing slide images leads to higher performance, confirming that visual information, such as images, layout, and formulas, contributes to better comprehension."

## Discussion


## Related Claims
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](multimodality-size-reasoning-mixed-effects.md) — a broader claim this one bears on
- [LLM accuracy drops from 96% on text-only to 74% on multimodal physics problems, with significant differences emerging among models](multimodal-physics-accuracy-drops-to-74-percent.md) — related
- [The OCR-based text input uses far fewer tokens than image-based multimodal input for the same slide, making it more cost-effective](ocr-input-lower-token-cost-than-image-input.md) — related
- [Multimodal LLMs outperform the OCR-based pipeline on visually dense slides, while the OCR pipeline produces comparable instruction on text-centric slides](multimodal-vs-ocr-pipeline-slide-type-comparison.md) — related
- [RAG with slide text improves exam-question performance across all tested LLMs, with the smallest model showing the least improvement](rag-slide-text-improves-all-llm-performance.md) — related

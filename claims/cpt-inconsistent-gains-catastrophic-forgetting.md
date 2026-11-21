---
type: claim
title: CPT on course materials does not bring consistent improvement, performing on average worse than both baseline and RAG
description: CPT on course materials does not bring consistent improvement, performing on average worse than both baseline and RAG
id: cpt-inconsistent-gains-catastrophic-forgetting
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
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
  - id: tu-anh-dinh-2026-2
    resource: "https://doi.org/10.63317/5bjdtya4ui69"
    title: "Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)"
    author: Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# CPT on course materials does not bring consistent improvement, performing on average worse than both baseline and RAG

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On average, CPT on combined slide text and polished transcripts performs worse than both the vanilla baseline and RAG for LLaMA 3.1 8B, with improvements in some exams and significant drops in others. [→ Tu Anh Dinh 2026](#tu-anh-dinh-2026)
`q2 i?` The overall performance loss under CPT is attributed to catastrophic forgetting, which is difficult to avoid with the limited course material data. [→ Tu Anh Dinh 2026 (2)](#tu-anh-dinh-2026-2)

## Evidence

### Tu Anh Dinh 2026

Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)

`q2 · i?` · `causal · r2`

CPT experiment with LLaMA 3.1 8B trained on combined slide text and polished transcripts, evaluated on SciEx (exam-level scores 0-60): CPT averages 28.86 versus baseline 31.17 and RAG 31.97. A language breakdown shows gains on some exams (e.g., HCI English, NLP German) and drops on others (notably HCI German, 39.40 to 33.80).

> "On average, CPT performs worse than both the baseline and RAG."

### Tu Anh Dinh 2026 (2)

Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)

`q2 · i?` · `causal · r2`

The authors' interpretation of the CPT result, offered in the results and discussion as the likely cause rather than a separately tested mechanism; validation perplexity monitoring and early stopping were used to limit overfitting.

> "The overall loss in performance is likely due to catastrophic forgetting, which is difficult to avoid when conducting CPT on the limited amount of course material data."

## Discussion


## Related Claims
- [Early stopping on course-material perplexity lets CPT adapt to course materials while minimizing forgetting, per validation-loss dynamics](cpt-early-stopping-validation-perplexity-dynamics.md) — related
- [Among CPT configurations on the HCI course, polished transcripts yield the best performance, though still not matching RAG](polished-transcripts-best-cpt-configuration.md) — related
- [RAG with slide text improves exam-question performance across all tested LLMs, with the smallest model showing the least improvement](rag-slide-text-improves-all-llm-performance.md) — related

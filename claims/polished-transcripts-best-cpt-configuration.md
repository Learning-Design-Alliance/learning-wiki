---
type: claim
title: Among CPT configurations on the HCI course, polished transcripts yield the best performance, though still not matching RAG
description: Among CPT configurations on the HCI course, polished transcripts yield the best performance, though still not matching RAG
id: polished-transcripts-best-cpt-configuration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
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

# Among CPT configurations on the HCI course, polished transcripts yield the best performance, though still not matching RAG

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In an HCI-only ablation, the best CPT results are achieved when using polished transcripts, which the authors attribute to polished transcripts more closely resembling natural text; CPT still generally performs worse than RAG. [→ Tu Anh Dinh 2026](#tu-anh-dinh-2026)

## Evidence

### Tu Anh Dinh 2026

Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)

`q2 · i?` · `causal · r2`

Ablation study limited by computational constraints to the HCI topic with LLaMA 3.1 8B (exam-level scores 0-60): CPT with polished transcripts averages 39.45, versus 38.03 with slide text and 36.70 with raw transcripts, while RAG with slide text reaches 42.62 and the baseline 39.05.

> "Among the CPT configurations, the best results are achieved when using polished transcripts. This outcome is expected, as the polished transcripts more closely resemble the natural text that LLMs are typically trained on."

## Discussion


## Related Claims
- [CPT on course materials does not bring consistent improvement, performing on average worse than both baseline and RAG](cpt-inconsistent-gains-catastrophic-forgetting.md) — related
- [RAG mitigates knowledge gaps on topics where LLMs are weak, yielding the largest topic-level gains on Human–Computer Interaction](rag-mitigates-topic-knowledge-gaps-hci.md) — related

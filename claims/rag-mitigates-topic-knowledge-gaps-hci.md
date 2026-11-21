---
type: claim
title: RAG mitigates knowledge gaps on topics where LLMs are weak, yielding the largest topic-level gains on Human–Computer Interaction
description: RAG mitigates knowledge gaps on topics where LLMs are weak, yielding the largest topic-level gains on Human–Computer Interaction
id: rag-mitigates-topic-knowledge-gaps-hci
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

# RAG mitigates knowledge gaps on topics where LLMs are weak, yielding the largest topic-level gains on Human–Computer Interaction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` RAG yields substantial improvements on topics where LLMs lack context, such as Human–Computer Interaction (+6.11 points), while other topics improve modestly or remain stable. [→ Tu Anh Dinh 2026](#tu-anh-dinh-2026)

## Evidence

### Tu Anh Dinh 2026

Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)

`q2 · i?` · `causal · r2`

Per-topic analysis of RAG with slide text across SciEx exams (exam-level scores 0-60): HCI rises from 41.91 baseline to 48.02 with RAG, while Algo (35.38 to 35.13) and TGI (41.38 to 41.25) remain stable or slightly decline. The article states RAG appears "the most useful for filling knowledge gaps".

> "On certain topics, such as Hu- man–Computer Interaction (HCI), RAG yields sub- stantial improvements (+6.11 points). For others, performance either improves modestly or remains stable."

## Discussion


## Related Claims
- [Among CPT configurations on the HCI course, polished transcripts yield the best performance, though still not matching RAG](polished-transcripts-best-cpt-configuration.md) — related
- [LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry](llm-teaching-effectiveness-varies-by-domain.md) — related
- [DeepTutor's interactive tutoring gains are stable across five university-level domains, varying only 0.16 points in overall quality](deeptutor-gains-stable-across-five-domains.md) — related
- [RAG with slide text improves exam-question performance across all tested LLMs, with the smallest model showing the least improvement](rag-slide-text-improves-all-llm-performance.md) — related

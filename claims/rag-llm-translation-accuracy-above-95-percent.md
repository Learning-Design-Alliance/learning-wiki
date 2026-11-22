---
type: claim
title: "A RAG-augmented LLM translation pipeline raised pre-human-review translation accuracy from approximately 80% to over 95%"
description: "A RAG-augmented LLM translation pipeline raised pre-human-review translation accuracy from approximately 80% to over 95%"
id: rag-llm-translation-accuracy-above-95-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: morris-2026
    resource: "https://doi.org/10.48550/arXiv.2609.35830"
    title: "Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. [doi:10.48550/arXiv.2609.35830](https://doi.org/10.48550/arXiv.2609.35830)"
    author: Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A RAG-augmented LLM translation pipeline raised pre-human-review translation accuracy from approximately 80% to over 95%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Vanilla LLM translations of HEP documentation required manual correction on roughly 20% of sentences (~80% baseline accuracy), and a RAG architecture with a verified glossary elevated pre-human accuracy beyond 95%. [→ Morris 2026](#morris-2026)

## Evidence

### Morris 2026

Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. [doi:10.48550/arXiv.2609.35830](https://doi.org/10.48550/arXiv.2609.35830)

`q2 · i?` · `design · r2`

Reported pipeline evaluation in the RAG implementation section: manual audits found vanilla LLM output needed correcting at roughly an 80% baseline, and "translation accuracy before human intervention was successfully elevated beyond 95%" after glossary-based RAG retrieval. No effect size or test statistic is printed.

> "By specializing the generative capabilities of the selected Qwen3.5-35B-A3B model using a verified knowledge base, the translation accuracy before human intervention was successfully elevated beyond 95%."

## Discussion


## Related Claims
- [Retrieval-augmented generation grounding achieves near-perfect correctness compared to untuned LLM baseline](rag-grounding-near-perfect-correctness.md) — related
- [Retrieval-augmented generation reduces but does not eliminate hallucinations in AI-assisted verification](rag-reduces-not-eliminates-hallucinations.md) — related
- [LLM transcription of the FCI PDF omitted question parts, misnumbered items, and introduced formatting inconsistencies requiring manual correction](llm-pdf-transcription-formatting-errors.md) — related
- [Qwen3.5-35B-A3B offered the best throughput and memory balance of three open-source LLMs benchmarked on consumer-grade hardware for translation](qwen-selected-optimal-throughput-memory-balance.md) — related

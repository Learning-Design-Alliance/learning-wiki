---
type: claim
title: Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient
description: Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient
id: evidence-tracing-114-claims-retrieval-limit
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: dana-rezazadegan-2026
    resource: "https://arxiv.org/abs/2606.27619"
    title: "Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619"
    author: Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: dana-rezazadegan-2026-2
    resource: "https://arxiv.org/abs/2606.27619"
    title: "Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619"
    author: Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Of 114 unique claims across 30 responses, 96 link to at least one source-chunk identifier, and three claims with average retrieval scores of 0.50 or below show retrieval similarity alone does not guarantee claim-level evidential support. [→ Dana Rezazadegan 2026](#dana-rezazadegan-2026)

## Evidence

### Dana Rezazadegan 2026

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

Evidence-tracing results across the 30 generated responses from the RAGAS evaluation, counting claims and their source-chunk links; 29 of 30 responses include at least one chunk identifier.

> "At the sentence level, the export contained 114 unique claims, of which 96 are linked to at least one source-chunk identifier and 18 have no source-chunk identifier."

### Dana Rezazadegan 2026 (2)

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

Same evidence-tracing analysis noting that despite a mean retrieval score of 0.85 for identified claims, three claims score 0.50 or below, indicating a limit of similarity-based retrieval.

> "However, three identified claims have an average retrieval score of 0.50 or below, showing that retrieval similarity alone is not sufficient for strong claim-level evidential support."

## Discussion


## Related Claims
- [DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data](dyslexlens-mean-answer-relevancy-075.md) — related
- [Standard semantic retrieval alone does not reliably recover the pedagogically required chunk types, with comparison chunks retrieved worst (14.3% on the real corpus)](semantic-retrieval-insufficient-pedagogical-content.md) — related
- [Retrieval Failure Reduces Benefit](retrieval-failure-reduces-benefit.md) — related
- [Retrieval practice improves long-term retention](retrieval-practice-improves-retention.md) — related

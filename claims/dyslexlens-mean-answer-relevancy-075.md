---
type: claim
title: DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data
description: DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data
id: dyslexlens-mean-answer-relevancy-075
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
---

# DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 30 queries, DysLexLens responses reach a mean Answer Relevancy score of 0.75, with 25 of 30 responses scoring at least 0.65. [→ Dana Rezazadegan 2026](#dana-rezazadegan-2026)

## Evidence

### Dana Rezazadegan 2026

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

Automated RAGAS evaluation of 30 queries (5 research questions plus follow-ups) run on the filtered dyslexia-AI Reddit corpus using gpt-4o-mini. The article reports "a mean Answer Relevancy score of 0.75" and that 25 of 30 responses scored at least 0.65, noting this alone does not show evidential support.

> "Across all 30 responses, DysLexLens achieves a mean Answer Relevancy score of 0.75. In total, 25 of the 30 responses scored at least 0.65 forAnswer Relevancy."

## Discussion


## Related Claims
- [Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower](rq-higher-relevancy-lower-grounding.md) — related
- [DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)](query-robustness-paraphrase-keyword-perturbation.md) — related
- [Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient](evidence-tracing-114-claims-retrieval-limit.md) — related
- [Of 100 human-audited claims, 39 are fully verifiable, 55 partially verifiable, and 6 not verifiable, with main responses showing stronger provenance than follow-ups](human-audit-claim-verifiability.md) — related

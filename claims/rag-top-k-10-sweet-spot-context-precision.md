---
type: claim
title: "Retrieval context has a sweet spot at Top-K = 10: raising it to 15 did not improve recall but significantly worsened context precision via the distraction issue"
description: "Retrieval context has a sweet spot at Top-K = 10: raising it to 15 did not improve recall but significantly worsened context precision via the distraction issue"
id: rag-top-k-10-sweet-spot-context-precision
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: anna-ostrowska-2026
    resource: "https://doi.org/10.24963/ijcai.2026/984"
    title: "Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr [doi:10.24963/ijcai.2026/984](https://doi.org/10.24963/ijcai.2026/984)"
    author: Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Retrieval context has a sweet spot at Top-K = 10: raising it to 15 did not improve recall but significantly worsened context precision via the distraction issue

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Increasing retrieval context from Top-K = 10 to 15 did not improve recall but significantly worsened context precision due to irrelevant information distracting the generator. [→ Anna Ostrowska 2026](#anna-ostrowska-2026)

## Evidence

### Anna Ostrowska 2026

Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr [doi:10.24963/ijcai.2026/984](https://doi.org/10.24963/ijcai.2026/984)

`q2 · i?` · `causal · r1`

Retrieval-setting experiments within the RAGAS evaluation of the system's pipelines. The authors report the "sweet spot" at Top-K = 10 and that raising it to 15 "significantly worsened context precision" without recall gains.

> "the ”sweet spot” for context was found to be Top-K = 10; increasing this to 15 did not improve recall but significantly worsened context precision due to the ”distraction issue”"

## Discussion


## Related Claims
- [Interesting but irrelevant details can impair comprehension and transfer, with effects that vary with the material and the learner](seductive-details-effect.md) — a broader claim this one bears on
- [Adding relevant pictures or graphics to text improves learning from it, with a small pooled effect on reading comprehension, though whether dual coding explains the benefit is disputed](dual-coding-improves-learning.md) — related
- [A WestEd research bulletin reports a curriculum revision that replaced a decorative photograph in a math problem with a problem-relevant sketch, on the developers' view that such photographs distract students](decorative-images-distract-from-math-problems.md) — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related
- [NCERT-tailored RAG preprocessing and figure-aware indexing improve retrieval precision over a generic-chunking baseline, per the authors' assertion](ncert-tailored-rag-improves-retrieval-precision.md) — related

---
type: claim
title: "The wiki's advantage over vector RAG is roughly three times larger on cross-page questions than on topic-page questions, in both score and groundedness"
description: "The wiki's advantage over vector RAG is roughly three times larger on cross-page questions than on topic-page questions, in both score and groundedness"
id: wiki-advantage-triples-cross-page-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: brian-wright-2026
    resource: "https://doi.org/10.48550/arxiv.2609.25303"
    title: "Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303 [doi:10.48550/arxiv.2609.25303](https://doi.org/10.48550/arxiv.2609.25303)"
    author: Brian Wright
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The wiki's advantage over vector RAG is roughly three times larger on cross-page questions than on topic-page questions, in both score and groundedness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Splitting 59 questions by class, the wiki arm was nearly indifferent to question class (9.96 vs. 9.93 score) while vector RAG dropped from 9.33 on topic-page to 8.14 on cross-page questions, widening the score gap from 0.62 to 1.79 points and the groundedness gap from 87% vs. 98% to 64% vs. 100%. [→ Brian Wright 2026](#brian-wright-2026)

## Evidence

### Brian Wright 2026

Brian Wright. (2026). Potential for Enhanced Learning in Machine Learning Classes by Using Wiki LLM Indexing. https://arxiv.org/abs/2609.25303 [doi:10.48550/arxiv.2609.25303](https://doi.org/10.48550/arxiv.2609.25303)

`q2 · i?` · `causal · r2`

Question-class split of the same head-to-head evaluation (45 topic-page and 14 cross-page questions). The article reports the wiki arm "nearly indifferent to question class" at 9.96 vs. 9.93, while RAG's gap widened to 1.79 on cross-page questions with groundedness falling to 64% vs. 100%.

> "vector RAG is not (9.33 vs. 8.14 score, an 0.62 point gap on topic page [95% CI on the gap: 0.16, 1.18] widening to 1.79 oncrosspage[95%CI:0.57,3.14];87%vs.64%grounded)"

## Discussion


## Related Claims
- [The topic-page groundedness gap between wiki and vector RAG was the study's only comparison not reaching significance at the 95% level](topic-page-groundedness-gap-not-significant.md) — related
- [Retrieval failure explained only 2 of vector RAG's 11 ungrounded answers; 9 answers retrieved the correct material and were still ungrounded, suggesting chunked context invites fabrication](fabrication-despite-successful-retrieval.md) — related

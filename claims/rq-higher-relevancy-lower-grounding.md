---
type: claim
title: Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower
description: Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower
id: rq-higher-relevancy-lower-grounding
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

# Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Research-question responses achieve stronger Answer Relevancy than follow-up responses (mean 0.87 vs 0.72), but mean Faithfulness is 0.52, Context Relevancy 0.40, and Response Groundedness 0.43 across all 30 queries. [→ Dana Rezazadegan 2026](#dana-rezazadegan-2026)
`q2 i?` RQ3 achieves strong Faithfulness but a Response Groundedness score of zero, and RQ5 achieves the highest Answer Relevancy but a Context Relevancy score of zero. [→ Dana Rezazadegan 2026 (2)](#dana-rezazadegan-2026-2)

## Evidence

### Dana Rezazadegan 2026

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

RAGAS evaluation section comparing research-question and follow-up responses over the same 30-query test set. The authors suggest performance is better when questions include keywords closely aligned with the concept dictionary, and report the comparison with mean scores of 0.87 and 0.72.

> "The research question responses achieve stronger Answer Relevancy than follow-up responses, with mean scores of 0.87 and 0.72, respectively."

### Dana Rezazadegan 2026 (2)

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

Same RAGAS evaluation reporting evidential-support metrics for all 30 query responses: Faithfulness 0.52, Context Relevancy 0.40, Response Groundedness 0.43, all lower than Answer Relevancy for research questions.

> "Across all 30 queries’ responses, the mean Faithfulness score is 0.52, mean Context Relevancy is 0.40, and mean Response Groundedness is 0.43."

## Discussion


## Related Claims
- [DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data](dyslexlens-mean-answer-relevancy-075.md) — related
- [DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)](query-robustness-paraphrase-keyword-perturbation.md) — related
- [Of 100 human-audited claims, 39 are fully verifiable, 55 partially verifiable, and 6 not verifiable, with main responses showing stronger provenance than follow-ups](human-audit-claim-verifiability.md) — related

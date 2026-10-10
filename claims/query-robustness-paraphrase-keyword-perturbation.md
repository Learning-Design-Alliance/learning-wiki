---
type: claim
title: DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)
description: DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)
id: query-robustness-paraphrase-keyword-perturbation
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

# DysLexLens is moderately robust to paraphrased queries (Answer Relevancy 0.58) but sensitive to keyword-perturbed queries (0.34)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Keyword-perturbed queries show a clear decrease in Answer Relevancy to 0.34 versus 0.75 for original queries, indicating greater sensitivity when domain-specific terms are changed. [→ Dana Rezazadegan 2026](#dana-rezazadegan-2026)

## Evidence

### Dana Rezazadegan 2026

Dana Rezazadegan, Atie Kia, Phongpadid Nandavong, Dominique Carlon, Jeremy Nguyen, Abhik Banerjee, James Marshall, Anthony McCosker, Yong-Bin Kang. (2026). DysLexLens: A Low-Resource LLM Framework for Analysing Dyslexic Learners' Insights from Online Forums. https://arxiv.org/abs/2606.27619

`q2 · i?` · `design · r2`

Query robustness analysis comparing original, paraphrased, and keyword-perturbed variants of all 30 questions under the same configuration (Table 1: original 0.75, paraphrased 0.58, keyword-perturbed 0.34 for Answer Relevancy).

> "However, the keyword-perturbed queries show a clear decrease in Answer Relevancy (0.34), indicating that the framework is more sensitive when domain-specific terms are changed."

## Discussion


## Related Claims
- [DysLexLens achieves a mean Answer Relevancy of 0.75 across 30 responses to research questions and follow-ups on dyslexia-AI Reddit data](dyslexlens-mean-answer-relevancy-075.md) — related
- [Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower](rq-higher-relevancy-lower-grounding.md) — related
- [Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign](rubric-structure-part-of-assessment-construct.md) — related

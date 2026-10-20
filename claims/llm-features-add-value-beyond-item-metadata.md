---
type: claim
title: LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)
description: LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)
id: llm-features-add-value-beyond-item-metadata
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: pooya-razavi-2026
    resource: "https://doi.org/10.1016/j.ijaied.2026.100015"
    title: "Razavi, P., & Powers, S. (2026). Estimating item difficulty using large language models and tree-based machine learning algorithms. *International Journal of Artificial Intelligence in Education*, 36. https://doi.org/10.1016/j.ijaied.2026.100015"
    author: "Razavi, P., & Powers, S."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Full models combining metadata with LLM-rated features improved on metadata-only models: reading RF cut RMSE 17.6% and math GBM cut RMSE 11.2% versus the strongest metadata-only baselines, on average. [→ Pooya Razavi 2026](#pooya-razavi-2026)

## Evidence

### Pooya Razavi 2026

Razavi, P., & Powers, S. (2026). Estimating item difficulty using large language models and tree-based machine learning algorithms. *International Journal of Artificial Intelligence in Education*, 36. https://doi.org/10.1016/j.ijaied.2026.100015

`q2 · i?` · `design · r2`

Reading holdout comparison of full feature-based models against metadata-only models trained with identical algorithms and procedures. For math, GBM reduced RMSE "relative to the strongest benchmark (i.e., the metadata-only gradient boosting model) by 11.2% on average".

> "Compared to the dummy regressor, the random forest reduced RMSE by 31.6% on average, and improved upon the metadata-only random forest by 17.6% on average."

## Discussion


## Related Claims
- [Feature Based Llm Models Outperform Direct Estimation And Benchmarks](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md)
- [Direct zero-shot GPT-4o difficulty ratings beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](direct-llm-estimation-beats-dummy-regressor-k5-items.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [Episode-composition and transition features contribute predictive process evidence beyond semantics, with Epi.+Tran. reaching 0.136 permutation importance versus 0.084 for Sem. in the Both (Role) setting](episode-features-predictive-importance-beyond-semantics.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [Test item construction, including avoidance of cognate L1 equivalents, often affects KVL difficulty scores beyond the genuine difficulty of the words](test-item-construction-affects-kvl-difficulty-scores.md) — related
- [All three assertion sources (word, corpus-derived, construct-derived) contribute to predictive accuracy](all-assertion-sources-contribute-predictive-accuracy.md) — a narrower finding that bears on this claim
- [The explainable feature-based model with LLM-extracted features outperforms the closed-track encoder baseline by a wide margin](explainable-model-outperforms-closed-track-baseline.md) — related

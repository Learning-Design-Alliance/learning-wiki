---
type: claim
title: "Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%"
description: "Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%"
id: zero-shot-comparative-difficulty-ranking-outperforms-absolute
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: vatsal-raina-2024
    resource: "https://doi.org/10.48550/arXiv.2404.10704"
    title: "Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)"
    author: Vatsal Raina, Mark Gales
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Zero-shot comparative assessment of ChatGPT3.5 achieved a Spearman's rank correlation of 40.4±0.6 with true difficulty scores, exceeding absolute assessment (18.3±0.3) on CMCQRD. [→ Vatsal Raina 2024](#vatsal-raina-2024)

## Evidence

### Vatsal Raina 2024

Vatsal Raina, Mark Gales. (2024). Question Difficulty Ranking for Multiple-Choice Reading Comprehension. ALTA Institute, University of Cambridge. [doi:10.48550/arXiv.2404.10704](https://doi.org/10.48550/arXiv.2404.10704)

`q2 · i?` · `design · r2`

Zero-shot evaluation on CMCQRD using ChatGPT3.5: 250 samples for absolute scoring and 250 pairwise comparisons per question, with standard deviation over 30 draws; absolute 18.3±0.3 vs comparative 40.4±0.6 Spearman's correlation. The article reports the models are "more effective at ranking question diffi- culty if used for comparative rather than absolute assessment".

> "The instruction-tuned models are more effective at ranking question diffi- culty if used for comparative rather than absolute assessment."

## Discussion


## Related Claims
- [Combining level classification and zero-shot comparative systems by averaging ranks boosts difficulty-ranking correlation to 43.7%](combining-level-classification-and-comparative-boosts-correlation.md) — related
- [A RACE++-trained level classification system transfers to difficulty ranking better than a fine-tuned reading comprehension system (38.7% vs 30.8% Spearman)](level-classification-transfers-better-than-reading-comprehension.md) — related
- [The open-source Mistral-7B model achieves much lower comparative difficulty-ranking correlation (17.5%) than ChatGPT](mistral-7b-weaker-comparative-ranking.md) — related
- [Zero-shot difficulty-ranking performance plateaus with decreasing variance as the number of samples/comparisons K increases](zero-shot-performance-plateaus-with-k.md) — a broader claim this one bears on
- [Zero-shot GPT-4o difficulty ratings, rescaled and entered in grade-specific regressions, beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](direct-llm-estimation-beats-dummy-regressor-k5-items.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- Systems that both beat the baselines learn similar curricula across disjoint feature groups, as shown by positive Spearman rank correlations between their orderings — related
- LLMs performing in-context regression on GP-sampled functions achieve errors close to empirical GP regression and well below a 1-NN baseline — related

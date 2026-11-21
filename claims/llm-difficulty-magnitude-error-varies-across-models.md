---
type: claim
title: Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)
description: Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)
id: llm-difficulty-magnitude-error-varies-across-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: la-hadi-2026
    resource: "https://doi.org/10.48550/arxiv.2607.26067"
    title: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2026). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 Originally published 2025. [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)"
    author: "La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` RMSE and MAE values vary notably across LLM models, so correlation alone overstates practical predictive accuracy of difficulty magnitude. [→ La Hadi 2026](#la-hadi-2026)

## Evidence

### La Hadi 2026

La Hadi, A., Alibasa, M. J., Chen, G., & Asyhari, A. T. (2026). The “Easy Trap”: Why LLMs Underestimate Misconception-Driven Difficulty. https://arxiv.org/abs/2607.26067 Originally published 2025. [doi:10.48550/arxiv.2607.26067](https://doi.org/10.48550/arxiv.2607.26067)

`q2 · i?` · `associational · r2`

Analysis of the same four-model comparison against empirical IRT difficulty reports that "RMSE and MAE values vary notably across models"; Table 1 shows RMSE (IRT) from 0.809 to 0.974 and MAE from 0.638 to 0.727.

> "RMSE and MAE values vary notably across models (Table 1), showing that models with similar correlations differ in their ability to estimate difficulty magnitude."

## Discussion


## Related Claims
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — related
- [CTT-based quiz difficulty rankings are validated by IRT analysis with near-perfect rank correlation](irt-validates-ctt-quiz-difficulty-ranking.md) — related
- CDP improves item-difficulty recovery in both rank order and absolute alignment, with the largest gains for reasoning-enabled Gemini configurations — related
- [GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts](gpt-4o-mini-lowest-act-balance-mae.md) — related
- [Teacher value-added estimates are highly correlated across model specifications that differ in student and peer control variables](vam-estimates-highly-correlated-across-specifications.md) — related
- [Exploratory analysis found item difficulty differed across sources, driven by the Google Gemini versus NLE contrast](item-difficulty-differs-across-sources-gemini-nle.md) — related
- [GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error](turn-level-convergence-gpt-4o-mini.md) — related
- [Rank orderings of teachers do not change radically under mild scale transformations](teacher-rank-orderings-robust-to-mild-transformations.md) — related
- [Feature-based models (LLM-extracted features plus metadata in random forest and gradient boosting) outperform direct LLM estimation, dummy regressor, TF-IDF, and metadata-only benchmarks, with correlations up to r = .87](feature-based-llm-models-outperform-direct-estimation-and-benchmarks.md) — related
- [Zero-shot GPT-4o difficulty ratings, rescaled and entered in grade-specific regressions, beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](direct-llm-estimation-beats-dummy-regressor-k5-items.md) — related
- [Angoff estimates correlated with observed item difficulty more strongly for LLMs than for faculty judges](llm-angoff-item-difficulty-correlation.md) — related
- [LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions](llm-ospe-rank-agreement-paradox.md) — a narrower finding that bears on this claim
- [The ML regression model's predicted GOALS scores correlate strongly with expert evaluations (r = 0.86 dissection, r = 0.91 suturing) with small mean absolute errors](mocap-goals-prediction-correlation-mae.md) — related
- [Participants' and tutors' rankings of medical error types were highly similar, indicating strong agreement between the two perspectives](participant-tutor-ranking-agreement.md) — related
- [Zero-shot comparative prompting of instruction-tuned LLMs ranks MC question difficulty more effectively than absolute prompting, with a Spearman's correlation of 40.4%](zero-shot-comparative-difficulty-ranking-outperforms-absolute.md) — related
- [Question difficulty estimates are highly stable across successive years (correlation 0.98) while student ability estimates correlate only moderately (0.54)](difficulty-stable-ability-changes-across-years.md) — related
- [Absolute prevalence estimates differ across models and generally do not agree within uncertainties, despite similar trends](model-prevalence-estimates-differ-within-uncertainties.md) — a narrower finding that bears on this claim
- [False reference solutions degrade LLM absolute marking accuracy but leave rank-order agreement largely intact](false-solutions-degrade-accuracy-not-ranking.md) — related
- [Simulated-response difficulty estimates match the accuracy of a traditional 1PL analysis using approximately 5,818 real student answers (about 22.87% of available data)](rmse-efficiency-5818-real-answers.md) — related

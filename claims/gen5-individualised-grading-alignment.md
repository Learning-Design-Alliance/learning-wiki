---
type: claim
title: "With individualised grading contexts, Generation 5 models aligned strongly with human grading, Gemini 3.0 Pro reaching r = 0.9191 and MAE of 7.62%"
description: "With individualised grading contexts, Generation 5 models aligned strongly with human grading, Gemini 3.0 Pro reaching r = 0.9191 and MAE of 7.62%"
id: gen5-individualised-grading-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jonah-l-donaldson-2026
    resource: "https://doi.org/10.48550/arXiv.2605.23660"
    title: "Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)"
    author: Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli
    q: 2
    i: 3
    kind: associational
    rigour: 1
---

# With individualised grading contexts, Generation 5 models aligned strongly with human grading, Gemini 3.0 Pro reaching r = 0.9191 and MAE of 7.62%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2` · `i3` large
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i3` Gemini 3.0 Pro posted the highest Pearson correlation (r = 0.9191), an R² of 0.8448, and a low MAE of 7.62% when grading each solution individually in PB2. [→ Jonah L. Donaldson 2026](#jonah-l-donaldson-2026)

## Evidence

### Jonah L. Donaldson 2026

Jonah L. Donaldson, Aliya Nawaz, Konstantinos Doran, Alysta Lim, and Mario Campanelli. (2026). Using Large Language Models in Physics Education. [doi:10.48550/arXiv.2605.23660](https://doi.org/10.48550/arXiv.2605.23660)

`q2 · i3` · `associational · r1`

PB2 Stage III regression analysis with individualised inputs replacing PB1's batch grading, mitigating halo and U-shaped attention effects. The article reports Gemini 3.0 Pro "posted the highest Pearson correlation (r= 0.9191)" and MAE of 7.62%, indicating reduced systemic over-marking.

> "However, Gemini 3.0 Pro achieved the strongest overall statistical alignment. It posted the highest Pearson correlation (r= 0.9191), anR 2 of 0.8448, and a low Mean Absolute Error (MAE) of 7.62%."

## Discussion


## Related Claims
- [A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)](gemini-autorater-creativity-real-students.md) — related
- [LLM marking of code-based scientific plots achieves exceptionally strong rank-order agreement with human markers](llm-plot-marking-strong-rank-agreement.md) — related
- [Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration](llama-strongest-human-llm-alignment-claude-weakest.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — a broader claim this one bears on
- [Generation 5 LLMs reach near-perfect scores on text-based undergraduate physics benchmarks, with standard errors near zero](gen5-llms-saturate-text-physics-benchmarks.md) — related
- [In PB1 AI grading with a mark scheme, models showed systemic over-marking, with ChatGPT-o3 the only evaluator closely aligned with human marks](pb1-ai-grading-over-marking-o3-alignment.md) — related

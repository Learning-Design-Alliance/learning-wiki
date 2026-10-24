---
type: claim
title: GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts
description: GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts
id: gpt-4o-mini-lowest-act-balance-mae
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: pascal-riachi-2026
    resource: "https://doi.org/10.48550/arxiv.2606.17786"
    title: "Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler. (2026). Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars. https://arxiv.org/abs/2606.17786 [doi:10.48550/arxiv.2606.17786](https://doi.org/10.48550/arxiv.2606.17786)"
    author: Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 49 psychotherapy transcripts, GPT-4o mini achieved the lowest ACT balance MAE (6.12) among six evaluated LLMs, with statistically significant rank-order correlation with human ratings. [→ Pascal Riachi 2026](#pascal-riachi-2026)

## Evidence

### Pascal Riachi 2026

Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler. (2026). Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars. https://arxiv.org/abs/2606.17786 [doi:10.48550/arxiv.2606.17786](https://doi.org/10.48550/arxiv.2606.17786)

`q2 · i?` · `design · r2`

Quantitative evaluation of six LLMs on 49 psychotherapy transcripts previously rated by a human ACT supervisor, comparing model-generated ACT-FM and TES ratings to human ratings via MAE and Spearman's ρ. GPT-4o mini's ACT balance MAE was 6.12 with ρ = 0.57; all models showed statistically significant rank-order correlation (p<.001).

> "GPT-4o mini achieved the lowest ACT balance MAE (6.12), indicating closest absolute alignment with human supervisor ratings. All models showed statistically significant rank-order correlation with human ratings (p<.001)."

## Discussion


## Related Claims
- LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst — related
- [GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error](turn-level-convergence-gpt-4o-mini.md) — related
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — related
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [Full-scale LLM versions consistently achieve higher agreement with human grades than their mini and nano counterparts](full-scale-llms-outperform-mini-nano-grading.md) — related

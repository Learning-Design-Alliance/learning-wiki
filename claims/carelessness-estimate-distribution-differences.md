---
type: claim
title: Carelessness estimates from the contextual slip models are bimodally distributed while BKFC estimates are normally distributed
description: Carelessness estimates from the contextual slip models are bimodally distributed while BKFC estimates are normally distributed
id: carelessness-estimate-distribution-differences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: jiayi-zhang-2025
    resource: "https://doi.org/10.1109/cste64638.2025.11092064"
    title: "Jiayi Zhang, Ryan S. Baker, Namrata Srivastava, Jaclyn Ocumpaugh, Caitlin Mills, Bruce M. McLaren. (2025). Carelessness Detection using Performance Factor Analysis: A New Operationalization with Unexpectedly Different Relationship to Learning. arXiv. [doi:10.1109/cste64638.2025.11092064](https://doi.org/10.1109/cste64638.2025.11092064)"
    author: Jiayi Zhang, Ryan S. Baker, Namrata Srivastava, Jaclyn Ocumpaugh, Caitlin Mills, Bruce M. McLaren
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Carelessness estimates from the contextual slip models are bimodally distributed while BKFC estimates are normally distributed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` BKT-based and ML contextual slip carelessness estimates show bimodal distributions at the ends of the probability scale, whereas BKFC estimates are normally distributed between roughly 0.4 and 0.6. [→ Jiayi Zhang 2025](#jiayi-zhang-2025)

## Evidence

### Jiayi Zhang 2025

Jiayi Zhang, Ryan S. Baker, Namrata Srivastava, Jaclyn Ocumpaugh, Caitlin Mills, Bruce M. McLaren. (2025). Carelessness Detection using Performance Factor Analysis: A New Operationalization with Unexpectedly Different Relationship to Learning. arXiv. [doi:10.1109/cste64638.2025.11092064](https://doi.org/10.1109/cste64638.2025.11092064)

`q2 · i?` · `design · r2`

Descriptive comparison of the three models' carelessness distributions over the 4,880 incorrect attempts; the BKT-based average was 0.469 (SD 0.373) with a bimodal distribution, while the BKFC average was 0.473 (SD 0.035), mostly within 0.4 and 0.6 (Figure 2).

> "By contrast, carelessness estimated using the BKFC model follows a normal distribution."

## Discussion


## Related Claims
- [Carelessness detected by the BKFC model is negatively and significantly associated with post-test scores, controlling for final knowledge level](bkfc-carelessness-negative-posttest-association.md) — related
- [BKFC-detected carelessness is negatively correlated with carelessness detected by the contextual slip approaches](bkfc-contextual-slip-estimate-divergence.md) — related
- [BKFC carelessness correlates positively with gaming the system and confrustion, the opposite of the negative correlations found for contextual slip carelessness](bkfc-carelessness-gaming-confrustion-correlations.md) — related
- [Carelessness detected by the BKT-based and ML contextual slip models is positively and significantly associated with post-test and delayed post-test scores](contextual-slip-carelessness-positive-posttest-association.md) — related
- [Bimodal frequency distributions induce a 'dual spotlight' in tone detection](bimodal-dual-spotlight-detection.md) — related
- [Human item-level scores on bash command exams are strongly bimodal, concentrated at zero and near-full credit with little intermediate partial credit](human-bash-scores-bimodal-zero-or-near-full.md) — related
- [Distributional learning modulates tone detection in noise, with better detection of high-probability frequencies](distributional-learning-modulates-tone-detection.md) — related
- [All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak](llm-bash-score-distributions-bimodal-v2-amplifies.md) — related

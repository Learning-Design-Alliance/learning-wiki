---
type: claim
title: Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning
description: Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning
id: ensembling-worsens-llm-alignment-with-learning
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: michael-hardy-2026
    resource: "https://doi.org/10.48550/arxiv.2603.00883"
    title: "Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883 [doi:10.48550/arxiv.2603.00883](https://doi.org/10.48550/arxiv.2603.00883)"
    author: Michael Hardy, Yunsung Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Both pedagogy-expertise-weighted and unanimous-vote ensembles frequently worsen LLM alignment with student learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Neither benchmark-weighted ensembling nor unanimous-vote consensus improves alignment with value-added learning; both frequently worsen it on core instructional dimensions. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy, Yunsung Kim. (2026). Knowledge without Wisdom: Measuring Misalignment between LLMs and Intended Impact. arXiv. https://arxiv.org/abs/2603.00883 [doi:10.48550/arxiv.2603.00883](https://doi.org/10.48550/arxiv.2603.00883)

`q2 · i?` · `causal · r2`

Ensemble evaluation in Sec. 5.3 comparing pedagogy-expertise-weighted ensembles and unanimous-vote ensembles on all model-prompt combinations (Fig. 4). Worsening was "especially on core instructional dimensions such as remediation of student errors and behavior management."

> "Neither strategy improves alignment with stu- dent learning. Instead, both frequentlyworsen"

## Discussion


## Related Claims
- [LLM accuracy on the CDPK pedagogy benchmark ranges from 28% to 89%, with closed-weight reasoning models dominating the top of the leaderboard](cdpk-accuracy-range-28-89-closed-models-lead.md) — related
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — related
- [Ensemble modeling of multiple LLM scorers yields performance gains in automated divergent thinking scoring](ensemble-models-performance-gains-llm-scoring.md) — reports the opposite
- Majority-vote ensembling across three runs produced only modest accuracy gains (1% to 5%) with no model showing degradation — reports the opposite
- [Ensembles of operational raters outperform the LLMs: two raters suffice on average across aspects, but larger ensembles are needed for individual aspects](rater-ensembles-outperform-llms-feedback.md) — related
- [Current GenAI tools are not designed to support active learning and their apparent domain expertise is brittle](genai-tools-not-designed-for-active-learning.md) — related

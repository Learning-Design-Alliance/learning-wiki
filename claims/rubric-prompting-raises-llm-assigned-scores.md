---
type: claim
title: Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels
description: Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels
id: rubric-prompting-raises-llm-assigned-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: alonso-carracedo-2026
    resource: "https://doi.org/10.48550/arxiv.2607.02432"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432 [doi:10.48550/arxiv.2607.02432](https://doi.org/10.48550/arxiv.2607.02432)"
    author: Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: alonso-carracedo-2026-2
    resource: "https://doi.org/10.48550/arxiv.2607.02432"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432. [doi:10.48550/arxiv.2607.02432](https://doi.org/10.48550/arxiv.2607.02432)"
    author: Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` GPT shows a positive V2 gap at every taxonomy level, largest at L3 (approximately 7.5 percentage points). [→ Alonso-Carracedo 2026](#alonso-carracedo-2026)
`q2 i?` Gemini shows an unusually large V2 gap at L2 (62.97% vs 53.78%), not observed at adjacent levels. [→ Alonso-Carracedo 2026 (2)](#alonso-carracedo-2026-2)

## Evidence

### Alonso-Carracedo 2026

Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432 [doi:10.48550/arxiv.2607.02432](https://doi.org/10.48550/arxiv.2607.02432)

`q2 · i?` · `causal · r2`

Per-level comparison of GPT 5.2's assigned grades under Variant 1 versus Variant 2 (Section 4.2.2, Figure 6). The article also reports GPT V2 reached 50.80% at L4 versus 45.07% under V1, the highest L4 proportion among the four models.

> "GPT maintains a consistent positive gap in favour of V2 across all taxonomy levels, with the largest advantage observed at L3 (approximately 7.5 percentage points)."

### Alonso-Carracedo 2026 (2)

Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432. [doi:10.48550/arxiv.2607.02432](https://doi.org/10.48550/arxiv.2607.02432)

`q2 · i?` · `causal · r2`

Per-level comparison of Gemini 3.0 Pro's assigned grades under the two prompt variants (Section 4.2.2, Figure 6). The article describes this approximately 9 percentage point gap as specific to basic-level tasks and notes the variants converge at L4 (59%).

> "Gemini shows a notable difference at L2, where questions receive on average 62.97% of the available mark under V2 (the highest proportion at that level among all four models) compared to 53.78% under V1."

## Discussion

## Related Claims

- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — the general claim this finding bears on, with the studies behind it
- [All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak](llm-bash-score-distributions-bimodal-v2-amplifies.md) — related
- [All four LLMs award a smaller share of available marks as bash question cognitive complexity increases, with L4 questions receiving the lowest proportions](llm-scores-decline-with-cogtax-level.md) — related
- [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive](llm-logical-inconsistency-scoring-feedback.md) — related
- Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign — related
- [gpt-4o graded student submissions most correctly in almost all assignments, but gemini-1.0-pro graded the boolean-algebra assignment most correctly](grader-llm-correctness-comparison-socrates.md) — related

---
type: claim
title: All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak
description: All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak
id: llm-bash-score-distributions-bimodal-v2-amplifies
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: alonso-carracedo-2026
    resource: "https://arxiv.org/abs/2607.02432"
    title: "Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432"
    author: Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# All four evaluated LLMs produce strongly bimodal item-level score distributions on bash exams, and rubric-enhanced prompts amplify the near-perfect-score peak

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` GPT 5.2, Claude Opus 4.6, Gemini 3.0 Pro and GLM 5 all show a dominant 90% peak and secondary 0% peak, with Variant 2 generally amplifying the 90% peak while modestly reducing the 0% bin. [→ Alonso-Carracedo 2026](#alonso-carracedo-2026)

## Evidence

### Alonso-Carracedo 2026

Alonso-Carracedo, M., Fernandez-Boullon, R., Celard, P., Rodríguez-Martínez, F. J., Otero-Cerdeira, L. (2026). Automated grading of Linux/bash examinations using large language models: a four-level cognitive taxonomy approach. https://arxiv.org/abs/2607.02432

`q2 · i?` · `causal · r2`

Descriptive distribution analysis of the four LLMs' grades under both prompt variants on the same 1200 responses (Section 4.2.1, Figure 5). The article states "The V2 variants generally amplify the 90% peak while modestly reducing the 0% bin" and that Gemini is most extreme in bimodality.

> "All four models share a common structural feature: a strongly right-skewed distribution with a dominant peak at 90% and a secondary at 0%, indicating that item-level scoring is inherently bimodal in nature."

## Discussion


## Related Claims
- [Three independent expert instructors reached exceptionally high inter-rater reliability when grading 1200 bash exam responses, establishing a reliable human reference standard](expert-triad-high-inter-rater-reliability-bash-grading.md) — related
- [Human item-level scores on bash command exams are strongly bimodal, concentrated at zero and near-full credit with little intermediate partial credit](human-bash-scores-bimodal-zero-or-near-full.md) — related
- [Rubric-enhanced prompting (Variant 2) raises LLM assigned scores relative to the no-rubric baseline, with model-specific gaps at particular taxonomy levels](rubric-prompting-raises-llm-assigned-scores.md) — related
- [All four LLMs award a smaller share of available marks as bash question cognitive complexity increases, with L4 questions receiving the lowest proportions](llm-scores-decline-with-cogtax-level.md) — related
- [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive](llm-logical-inconsistency-scoring-feedback.md) — related

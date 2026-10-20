---
type: claim
title: "AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency"
description: "AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency"
id: ai-consistency-high-except-spelling-languagetool-replacement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: curi-2026
    resource: "https://doi.org/10.48550/arxiv.2609.05143"
    title: "Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)"
    author: Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: curi-2026-2
    resource: "https://doi.org/10.48550/arxiv.2609.05143"
    title: "Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143. [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)"
    author: Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Across 10 repeated evaluations of each calibration text, consistency approached or exceeded 90% for the vast majority of rubric items, with spelling substantially lower. [→ Curi 2026](#curi-2026)
`q2 i?` A filtered LanguageTool-based deterministic approach for spelling achieved comparable performance to the LLM (68%) with 100% consistency. [→ Curi 2026 (2)](#curi-2026-2)

## Evidence

### Curi 2026

Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143 [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)

`q2 · i?` · `design · r2`

Consistency analysis of the 2024 calibration phase, where each of the 50 texts was evaluated 10 times by the AI model (Fig. 4). The article reports consistency "approaches or exceeds 90%" for most items, with spelling the only substantially lower item.

> "For the vast majority of rubric items, consistency approaches or exceeds 90%. This indicates that, on average, the same score is assigned in 9 out of 10 repeated evaluations, reflecting a high degree of stability."

### Curi 2026 (2)

Curi, M. E., Capdehourat, G., Amigo, I., Romano, M., Serra, R., Silveira, A., Peri, A. (2026). A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment. arXiv. https://arxiv.org/abs/2609.05143. [doi:10.48550/arxiv.2609.05143](https://doi.org/10.48550/arxiv.2609.05143)

`q2 · i?` · `design · r2`

Validation of a LanguageTool-based spelling scorer with a filter removing corrections belonging to other rubric items, on the 2024 calibration sample. The article reports 68% accuracy comparable to the LLM, with 100% consistency due to determinism.

> "This approach was validated with the calibration sample, where a comparable performance was achieved with that obtained with LLMs (68%), but with the advantage that this approach, being deterministic, all executions give the same result (its consistency is 100%)."

## Discussion


## Related Claims
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [LLM-based scoring of Spanish argumentative writing achieves 60–80% per-item accuracy, slightly below human inter-rater agreement](llm-scoring-spanish-writing-60-80-accuracy-below-human-agreement.md) — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — a broader claim this one bears on
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](hint-prompts-raise-llm-scoring-agreement.md) — related
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](llm-overrate-short-essays-overpenalize-errors.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — related
- [Prompt-based scoring prompts developed on one year's test generalize to the next year's edition with only minor adjustments](prompt-scoring-generalizes-across-test-editions.md) — related
- [Human inter-rater agreement on the writing rubric is imperfect: no rubric item reaches full agreement and the most discrepant rater generally falls below 80%](human-inter-rater-agreement-imperfect-upper-bound.md) — related

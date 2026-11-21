---
type: claim
title: Blind AI essay marking is harsher and more variable than human marking, and adding a marking scheme does not improve rank-order agreement
description: Blind AI essay marking is harsher and more variable than human marking, and adding a marking scheme does not improve rank-order agreement
id: llm-essay-marking-harsh-low-rank-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: will-yeadon-2026
    resource: "https://doi.org/10.48550/arXiv.2603.14732"
    title: "Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)"
    author: Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: will-yeadon-2026-2
    resource: "https://doi.org/10.48550/arXiv.2603.14732"
    title: "Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)"
    author: Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Blind AI essay marking is harsher and more variable than human marking, and adding a marking scheme does not improve rank-order agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Blind and scheme-only AI essay mark distributions sit approximately 14 marks below the human mean with inflated variance. [→ Will Yeadon 2026](#will-yeadon-2026)
`q2 i?` Adding the scheme leaves all rank correlations near zero and statistically indistinguishable from blind conditions (e.g., GPT-5.2 scheme rho = 0.006). [→ Will Yeadon 2026 (2)](#will-yeadon-2026-2)

## Evidence

### Will Yeadon 2026

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

Distributional analysis of 55 physics essay scripts (275 essays) marked by five blinded human markers and five LLMs. The article reports AI distributions "shifted approximately 14 marks below the human mean" with inflated variance (blind pooled sigma = 11.0 vs human 6.1).

> "Blind and scheme-only AI distributions are both shifted approximately 14 marks below the human mean and display considerably inflated variance."

### Will Yeadon 2026 (2)

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

Spearman and QWK analysis at script level (n=55) against the unrounded mean of five human markers. The article reports scheme-condition rho values "remain near-zero", with no confidence interval excluding zero in any condition.

> "Adding the scheme does not improve rank-order agreement: all scheme-conditionρvalues remain near-zero and statistically indistinguishable from the blind values given the width of the confidence intervals (e.g., GPT-5.2 scheme:ρ= 0.006, 95% CI [−0.25,0.26]; committee scheme:ρ=−0.044, 95% CI [−0.29,0.21])."

## Discussion


## Related Claims
- [Anchored exemplars shift AI essay means close to the human mean and compress variance below the human standard deviation, but rank-order agreement remains near-zero](anchored-exemplars-fix-distribution-not-ranking.md) — related
- [Providing a mark scheme substantially improves LLM grading accuracy and consistency, with GPT-4 shifting closest to human grades](mark-scheme-improves-llm-grading.md) — reports the opposite
- [LLM marking of code-based scientific plots achieves exceptionally strong rank-order agreement with human markers](llm-plot-marking-strong-rank-agreement.md) — related
- [Blind LLM grading of undergraduate physics solutions is substantially more lenient than human grading, driven by mathematical hallucinations](llm-blind-grading-lenient-hallucinations.md) — related
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
- [LLM markers show robust rank-order agreement with human markers on blind university exam questions and structured curriculum questions](llm-rank-order-agreement-structured-physics-questions.md) — related
- [In PB1 AI grading with a mark scheme, models showed systemic over-marking, with ChatGPT-o3 the only evaluator closely aligned with human marks](pb1-ai-grading-over-marking-o3-alignment.md) — related

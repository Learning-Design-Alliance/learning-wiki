---
type: claim
title: Anchored exemplars shift AI essay means close to the human mean and compress variance below the human standard deviation, but rank-order agreement remains near-zero
description: Anchored exemplars shift AI essay means close to the human mean and compress variance below the human standard deviation, but rank-order agreement remains near-zero
id: anchored-exemplars-fix-distribution-not-ranking
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
---

# Anchored exemplars shift AI essay means close to the human mean and compress variance below the human standard deviation, but rank-order agreement remains near-zero

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Despite this, anchored-condition rank correlations remain consistent with zero (committee rho = 0.034, 95% CI [−0.22,0.28]). [→ Will Yeadon 2026](#will-yeadon-2026)

## Evidence

### Will Yeadon 2026

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

Rank-order analysis of anchored essay marking (n=55 scripts). The article reports committee rho "sits at 0.034" with individual models likewise consistent with zero, so anchoring reduces error against a noisy reference without solving the validity problem.

> "The anchoring condition shows a similar pattern: committeeρsits at 0.034 (95% CI [−0.22,0.28]), with individual models GPT-5.2 (ρ=−0.021) and Claude (ρ=−0.016) likewise consistent with zero."

## Discussion


## Related Claims
- [Blind AI essay marking is harsher and more variable than human marking, and adding a marking scheme does not improve rank-order agreement](llm-essay-marking-harsh-low-rank-agreement.md) — related
- [LLMs use fewer extreme grades than human examiners, with grade-dependent opposing biases compressing grades toward the middle](llm-central-tendency-grade-compression.md) — related
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
- [Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination](llm-evaluator-leniency-ceiling-effects.md) — related
- [LLM marking of code-based scientific plots achieves exceptionally strong rank-order agreement with human markers](llm-plot-marking-strong-rank-agreement.md) — related
- Participants who received algorithm match scores showed no evidence of anchoring their probability judgments to those scores — related

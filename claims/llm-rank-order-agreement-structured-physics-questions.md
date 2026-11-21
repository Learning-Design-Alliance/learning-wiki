---
type: claim
title: LLM markers show robust rank-order agreement with human markers on blind university exam questions and structured curriculum questions
description: LLM markers show robust rank-order agreement with human markers on blind university exam questions and structured curriculum questions
id: llm-rank-order-agreement-structured-physics-questions
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

# LLM markers show robust rank-order agreement with human markers on blind university exam questions and structured curriculum questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under blind marking of 771 Durham exam questions, models achieve strong rank correlations with human marks (e.g., Claude Spearman rho = 0.690), ranking responses by physics quality without reference solutions. [→ Will Yeadon 2026](#will-yeadon-2026)
`q2 i?` On curriculum structured questions (n=1151), blind rank correlations are stronger still (e.g., Gemini rho = 0.845), and committee blind rho = 0.849. [→ Will Yeadon 2026 (2)](#will-yeadon-2026-2)

## Evidence

### Will Yeadon 2026

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

Blind LLM marking of 771 Durham University exam questions (2018–2022) previously marked by 22 question setters. The article reports strong rank correlations, e.g. "Claude: Spearmanρ= 0.690", showing models rank responses by quality without solutions.

> "Rank correlations against human marks remain strong (e.g., Claude: Spearmanρ= 0.690, QWK = 0.659; GPT-5.2:ρ= 0.646, QWK = 0.608), indicating that models successfully rank student responses by physics quality even without reference solutions."

### Will Yeadon 2026 (2)

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

Analysis of GCSE, A-Level and textbook structured questions (n=1151) with majority-vote human reference from three markers. The article reports "Gemini blindρ= 0.845" under blind conditions and higher values with solutions.

> "Under blind and correct-solution conditions, models show strong alignment with human rankings (e.g., Gemini blindρ= 0.845, QWK = 0.860; Claude solutionρ= 0.885, QWK = 0.907)."

## Discussion


## Related Claims
- [False reference solutions degrade LLM absolute marking accuracy but leave rank-order agreement largely intact](false-solutions-degrade-accuracy-not-ranking.md) — related
- [Blind AI essay marking is harsher and more variable than human marking, and adding a marking scheme does not improve rank-order agreement](llm-essay-marking-harsh-low-rank-agreement.md) — related
- [LLM marking of code-based scientific plots achieves exceptionally strong rank-order agreement with human markers](llm-plot-marking-strong-rank-agreement.md) — a narrower finding that bears on this claim
- [Blind LLM grading of undergraduate physics solutions is substantially more lenient than human grading, driven by mathematical hallucinations](llm-blind-grading-lenient-hallucinations.md) — related
- [LLM marking agrees with human markers on only about half of graded Physics answers, and assigns higher, less variable normalized scores than humans](llm-marking-concordance-with-humans-about-half.md) — related
- [Providing official reference solutions consistently reduces LLM marking error on structured physics questions](official-solutions-reduce-llm-marking-error.md) — related

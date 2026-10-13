---
type: claim
title: Under LLM evaluators, structured rubrics produced larger negative deviations from the human baseline than free-form rubrics, the opposite direction of the human-evaluator pattern
description: Under LLM evaluators, structured rubrics produced larger negative deviations from the human baseline than free-form rubrics, the opposite direction of the human-evaluator pattern
id: structured-free-form-llm-deviation-contrast
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: pedro-c-mendonça-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100663"
    title: "Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663"
    author: Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Under LLM evaluators, structured rubrics produced larger negative deviations from the human baseline than free-form rubrics, the opposite direction of the human-evaluator pattern

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Pooled across LLM evaluators, structured rubrics differed from the human baseline by −4.46 points and free-form rubrics by −0.66 points, a statistically significant difference (p < 0.001). [→ Pedro C. Mendonça 2026](#pedro-c-mendonca-2026)

## Evidence

### Pedro C. Mendonça 2026

Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663

`q3 · i?` · `causal · r2`

Paired Wilcoxon signed-rank comparisons of structured versus free-form rubric performance across three LLM evaluators (Table 6; 1848 pairs overall from 308 responses). Format differences were significant for text (p < 0.001) and code (p < 0.001) pooled rows.

> "The pooled comparison showed mean differences of  4.46 points for structured rubrics and  0.66 points for free-form rubrics, with a statistically significant difference between the two approaches (p < 0.001), as reported in Table 6."

## Discussion


## Related Claims

- [When applied by human evaluators, all four AI-generated rubrics met pooled scoring equivalence with a human-created baseline within a ±5-point margin](ai-rubrics-pooled-equivalence-human-evaluators.md) — related
- [In automated evaluation, equivalence with the human baseline depended on the evaluator model: DeepSeek V3 met equivalence for all rubric sources while GPT-4.1 and GPT-4o scored below the baseline](llm-evaluator-equivalence-depends-on-model.md) — possibly the same claim (merge candidate)
- [Equivalence failures under human evaluators were confined to five assignment-by-question-type cells, four of them on code questions](five-cells-exceeded-equivalence-margin.md)
- [Systematic underestimation of human scores is the dominant bias trend across LLM essay scoring, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md)

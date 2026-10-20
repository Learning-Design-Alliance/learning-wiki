---
type: claim
title: "91% of LLM-simulated ideas fell within grade-level knowledge scope, but within-scope proportions were significantly lower for elementary and middle school than high school"
description: "91% of LLM-simulated ideas fell within grade-level knowledge scope, but within-scope proportions were significantly lower for elementary and middle school than high school"
id: llm-ideas-knowledge-scope-91-percent-lower-grades-lag
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: nguyen-2026
    resource: "https://doi.org/10.1007/s10956-026-10333-5"
    title: "Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5"
    author: "Nguyen, H., & Cao, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: nguyen-2026-2
    resource: "https://doi.org/10.1007/s10956-026-10333-5"
    title: "Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5"
    author: "Nguyen, H., & Cao, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# 91% of LLM-simulated ideas fell within grade-level knowledge scope, but within-scope proportions were significantly lower for elementary and middle school than high school

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Overall, 91% of simulated ideas were within the corresponding grade-level knowledge scope, with GPT-4o and Llama-4 performing best and GPT-5-mini most likely to exceed scope. [→ Nguyen 2026](#nguyen-2026)
`q2 i?` Compared to high school, within-scope proportions were significantly lower for middle school (OR = 0.14) and elementary school (OR = 0.07). [→ Nguyen 2026 (2)](#nguyen-2026-2)

## Evidence

### Nguyen 2026

Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5

`q2 · i?` · `design · r2`

LLM-as-a-judge coding (GPT-5, κ = 0.69 with a human coder; robustness check with Claude-Sonnet-4, κ = 0.64) of knowledge scope against NGSS grade-band expectations. GPT-5-mini ideas were more likely to exceed scope (Δ proportion = −0.27 vs GPT-4o and Llama-4).

> "Overall, 91% of the simulated ideas were within the corresponding knowledge scope (Fig. 10). Specifically, GPT-4o and Llama-4 performed the best: their simulated ideas fell within the expected knowledge scope for the target grades."

### Nguyen 2026 (2)

Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5

`q2 · i?` · `design · r2`

Generalized linear mixed models with grade as fixed effect (χ² = 17.18, p <.001). Within each LLM, significant grade differences appeared only for GPT-5-mini (χ² = 9.18, p =.01), e.g., overly complex atom-level ideas in a fourth-grade energy lesson.

> "Compared to high school, the within-scope proportion was significantly lower for middle school (Δ proportion = −0.09; OR = 0.14, 95% CI [0.03, 0.68], p =.02) and elementary school (Δ proportion = −0.16; OR = 0.07, 95% CI [0.02, 0.33], p <.001)."

## Discussion


## Related Claims
- [Only 69% of LLM-simulated ideas met the target grade's language level, with elementary grades faring worst and Llama-4 performing best](llm-ideas-language-level-69-percent-elementary-worst.md) — related
- [Iterative prompting to revise overly complex responses raised readability alignment, with most regenerated responses falling at or below target grade levels](iterative-prompting-improves-readability-alignment.md) — related
- [Teachers judged LLM-simulated student ideas realistic and most useful when the ideas sparked sensemaking about student thinking and suggested scaffolds](teachers-perceive-llm-ideas-realistic-sensemaking-useful.md) — related
- [Direct zero-shot GPT-4o difficulty ratings beat a grade-level dummy regressor and correlate strongly with true Rasch difficulties overall, for K-5 math and reading items](direct-llm-estimation-beats-dummy-regressor-k5-items.md) — related

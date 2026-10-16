---
type: claim
title: Iterative prompting to revise overly complex responses raised readability alignment, with most regenerated responses falling at or below target grade levels
description: Iterative prompting to revise overly complex responses raised readability alignment, with most regenerated responses falling at or below target grade levels
id: iterative-prompting-improves-readability-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: nguyen-2026
    resource: "https://doi.org/10.1007/s10956-026-10333-5"
    title: "Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5"
    author: "Nguyen, H., & Cao, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Iterative prompting to revise overly complex responses raised readability alignment, with most regenerated responses falling at or below target grade levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A follow-up revision prompt improved most regenerated responses to at or below target grade levels, ranging from 55.10% (GPT-5-mini) to 95.92% (Gemini-2.5-Flash). [→ Nguyen 2026](#nguyen-2026)

## Evidence

### Nguyen 2026

Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5

`q2 · i?` · `design · r2`

Multi-prompt pipeline evaluation: responses exceeding readability thresholds were re-prompted to "Revise this response to match the language expected for {grade_level}." Readability alignment reached 100% for high school grades but varied widely for elementary grades (6.67%–80%).

> "Overall, most of the regenerated responses improved and fell at or below the target grade levels, Gemini-2.5-Flash (95.92%), Llama-4 (91.84%), Mistral-7B (91.84%), GPT-4o (89.80%), Claude-Sonnet-4 (83.67%), and GPT-5-mini (55.10%)."

## Discussion


## Related Claims
- [91% of LLM-simulated ideas fell within grade-level knowledge scope, but within-scope proportions were significantly lower for elementary and middle school than high school](llm-ideas-knowledge-scope-91-percent-lower-grades-lag.md) — related
- [Only 69% of LLM-simulated ideas met the target grade's language level, with elementary grades faring worst and Llama-4 performing best](llm-ideas-language-level-69-percent-elementary-worst.md) — related
- [Revising texts to improve readability-formula scores often produces nonexistent or insignificant comprehension gains](readability-revision-gains-nonexistent-insignificant.md) — related

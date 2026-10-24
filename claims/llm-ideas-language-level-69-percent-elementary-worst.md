---
type: claim
title: "Only 69% of LLM-simulated ideas met the target grade's language level, with elementary grades faring worst and Llama-4 performing best"
description: "Only 69% of LLM-simulated ideas met the target grade's language level, with elementary grades faring worst and Llama-4 performing best"
id: llm-ideas-language-level-69-percent-elementary-worst
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Only 69% of LLM-simulated ideas met the target grade's language level, with elementary grades faring worst and Llama-4 performing best

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Overall, 69% of simulated ideas were at or below the target students' grade level, and Llama-4 exceeded 80%, significantly higher than Mistral-7B and GPT-5-mini. [→ Nguyen 2026](#nguyen-2026)
`q2 i?` The proportion of ideas within the appropriate language level was significantly higher for high school and middle school than for elementary school. [→ Nguyen 2026 (2)](#nguyen-2026-2)

## Evidence

### Nguyen 2026

Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5

`q2 · i?` · `design · r2`

Flesch–Kincaid Grade Level analysis of 8820 simulated ideas across six LLMs. Llama-4's within-level proportion was statistically higher than Mistral-7B (OR = 67.57, 95% CI [10.33, 443], p <.001) and GPT-5-mini (OR = 153, 95% CI [21.2, 1103], p <.001).

> "Overall, 69% of the simulated ideas were at or below the target students' grade level. A likelihood ratio test suggested that the model with LLM produced better fit than a model without (χ²(5) = 57.44, p <.001). Llama-4 performed best, with over 80% of its outputs meeting or falling below the expected grade level"

### Nguyen 2026 (2)

Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5

`q2 · i?` · `design · r2`

Generalized linear mixed models on language-level proportions by grade. The authors conclude that "LLM-generated ideas showed more complex language than what would be expected for lower grades."

> "Post-hoc analyses revealed significant pairwise differences: the proportion for high school and middle school was significantly higher than elementary school (high school: OR = 160, 95% CI [31.1, 819], z = 6.08, p <.001; middle school: OR = 3.16, 95% CI [1.29, 7.74], z = 2.51, p =.01)."

## Discussion


## Related Claims
- [91% of LLM-simulated ideas fell within grade-level knowledge scope, but within-scope proportions were significantly lower for elementary and middle school than high school](llm-ideas-knowledge-scope-91-percent-lower-grades-lag.md) — related
- [Iterative prompting to revise overly complex responses raised readability alignment, with most regenerated responses falling at or below target grade levels](iterative-prompting-improves-readability-alignment.md) — related
- [LLM-simulated student ideas moderately overlap with teacher- and student-generated lesson ideas (mean cosine similarity 0.52), with larger LLMs slightly outperforming Mistral-7B](llm-simulated-ideas-moderate-overlap-lesson-ideas.md) — related
- [Teachers judged LLM-simulated student ideas realistic and most useful when the ideas sparked sensemaking about student thinking and suggested scaffolds](teachers-perceive-llm-ideas-realistic-sensemaking-useful.md) — related

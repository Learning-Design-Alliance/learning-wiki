---
type: claim
title: LLM-simulated student ideas moderately overlap with teacher- and student-generated lesson ideas (mean cosine similarity 0.52), with larger LLMs slightly outperforming Mistral-7B
description: LLM-simulated student ideas moderately overlap with teacher- and student-generated lesson ideas (mean cosine similarity 0.52), with larger LLMs slightly outperforming Mistral-7B
id: llm-simulated-ideas-moderate-overlap-lesson-ideas
status: draft
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

# LLM-simulated student ideas moderately overlap with teacher- and student-generated lesson ideas (mean cosine similarity 0.52), with larger LLMs slightly outperforming Mistral-7B

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Across 49 lesson plans, the mean cosine similarity between LLM-generated and lesson ideas was 0.52 (SD = 0.07), and all six LLMs scored higher than Mistral-7B (M = 0.47). [→ Nguyen 2026](#nguyen-2026)
`q2 i?` Semantic similarity was significantly lower for high school lessons (M = 0.50) than for elementary (M = 0.54) and middle school (M = 0.55) lessons. [→ Nguyen 2026 (2)](#nguyen-2026-2)

## Evidence

### Nguyen 2026

Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5

`q2 · i?` · `design · r2`

Computational evaluation of 8820 LLM-generated ideas clustered via embeddings and compared to lesson ideas from 49 OpenSciEd lesson plans. The mean cosine similarity was "0.52 (SD = 0.07)"; a likelihood ratio test (χ²(5) = 218.69, p <.001) showed all LLMs beat Mistral-7B (M = 0.47).

> "Across 49 lesson plans spanning science domains and grade levels, the mean cosine similarity reflecting the overlap between LLM-generated and lesson ideas was 0.52 (SD = 0.07)."

### Nguyen 2026 (2)

Nguyen, H., & Cao, J. (2026). Exploring the Capacity of Large Language Models to Simulate Students' Scientific Thinking: Insights for Responsive Teaching. Journal of Science Education and Technology. https://doi.org/10.1007/s10956-026-10333-5

`q2 · i?` · `design · r2`

Linear mixed models with activity ID as random intercept compared similarity across grade levels. High school similarity (M = 0.50) was significantly lower than elementary (β = 0.05, p =.01) and middle school (β = 0.05, p =.01), suggesting "weaker performance in matching the lessons' learning objectives for higher grade levels."

> "cosine similarity differed significantly by grade level (elementary: M = 0.54, SD = 0.07; middle school: M = 0.55, SD = 0.07; high school: M = 0.50, SD = 0.05; χ²(2) = 10.94, p =.004; Fig. 6)."

## Discussion


## Related Claims
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [Only 69% of LLM-simulated ideas met the target grade's language level, with elementary grades faring worst and Llama-4 performing best](llm-ideas-language-level-69-percent-elementary-worst.md) — related
- [Teachers judged LLM-simulated student ideas realistic and most useful when the ideas sparked sensemaking about student thinking and suggested scaffolds](teachers-perceive-llm-ideas-realistic-sensemaking-useful.md) — related

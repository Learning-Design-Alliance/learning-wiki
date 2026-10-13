---
type: strategy
id: interview-informed-llm-survey-simulation-strategy
title: Design interview-informed LLM survey simulations with persona-based prompts, low temperature, and item-level discrepancy review
description: The article proposes an interview-informed LLM approach in which qualitative interview transcripts are embedded in persona-based prompts to generate synthetic Likert survey responses that are compared against real res...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: zhang-2026
    resource: "https://osf.io/AFQG3"
    title: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3"
    author: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N"
---

# Design interview-informed LLM survey simulations with persona-based prompts, low temperature, and item-level discrepancy review

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes an interview-informed LLM approach in which qualitative interview transcripts are embedded in persona-based prompts to generate synthetic Likert survey responses that are compared against real responses. Its procedure combines research background, item information, personal interview, and demographic components, and uses "well -crafted prompts and low -temperature settings" to enhance alignment. It is positioned as a complement, not a substitute, for human data in mixed-methods research.

## Design Implications

### Context
#### Requirements
- Prompts must include item information and response scale; interview-informed prompts require de-identified interview transcripts from the same participants whose responses are being proxied
#### Constraints
- LLM-generated data are not intended to replace human data
- lower variability than human responses and poor reproduction of psychometric structure limit use
- small sample (n=19) limits conclusions

### Target Learners
- after-school program staff
- adult survey respondents in education and psychology research

### Target Learning Goals
- validating consistency between qualitative narratives and quantitative self-reports
- identifying response patterns and items for review

## Claims

- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](../claims/claude-highest-human-alignment-interview-prompts.md) [+W]
- [Interview length was not significantly associated with person-level alignment between LLM and human responses](../claims/interview-length-null-person-level-alignment.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

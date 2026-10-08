---
type: claim
title: Interview length was not significantly associated with person-level alignment between LLM and human responses
description: Interview length was not significantly associated with person-level alignment between LLM and human responses
id: interview-length-null-person-level-alignment
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: zhang-2026
    resource: "https://osf.io/AFQG3"
    title: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3"
    author: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N."
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Interview length was not significantly associated with person-level alignment between LLM and human responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` The correlation between interview token count and average person-level RMSE was moderate but not statistically significant, suggesting interview relevance matters more than length. [→ Zhang 2026](#zhang-2026)

## Evidence

### Zhang 2026

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `associational · r1`

Correlational analysis over 19 participants using Prompts 2 and 4, relating interview token count to average person-level RMSE: r = .404, p = .086, not statistically significant. The article attributes the inconclusive result partly to the small sample.

> "the correlation between the number of tokens in individual interviews and the average person -level RMSE f or Prompt 2 and Prompt 4 was moderate while not statistically significant ( = .404, p = .086), suggesting that longer interviews (greater number of tokens in prompts) did not necessarily lead to better alignment between LLM -generated and human re- sponses."

## Discussion


## Related Claims
- [At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index](test-level-rai-only-claude-improved.md) — related
- [LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses](llm-survey-responses-extreme-low-variability.md) — related

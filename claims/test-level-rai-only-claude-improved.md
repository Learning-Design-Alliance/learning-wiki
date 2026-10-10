---
type: claim
title: At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index
description: At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index
id: test-level-rai-only-claude-improved
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: zhang-2026
    resource: "https://osf.io/AFQG3"
    title: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3"
    author: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Compared to the baseline prompt, only Claude with Prompts 2, 3, and 4 showed higher test-level alignment with humans on the RAI; more personal information did not necessarily improve alignment for Gemini and GPT. [→ Zhang 2026](#zhang-2026)

## Evidence

### Zhang 2026

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Test-level RMSE analysis of the relative autonomy index across all 24 conditions (Figure 8). Only Claude with Prompts 2–4 beat the baseline; for Gemini and GPT added personal information did not necessarily improve test-level alignment. No effect size printed.

> "compared to Prompt 1, only claude with Prompt 2, Prompt 3, and Prompt 4 showed higher alignment with human respondents at the test level, which indicated, for some chatbots ( gemini and gpt), more personal information in the prompts (e.g., interview data and demographic information) may not necessarily improve the alignment"

## Discussion


## Related Claims
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [Interview length was not significantly associated with person-level alignment between LLM and human responses](interview-length-null-person-level-alignment.md) — related
- [Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts](interview-prompts-increase-llm-response-diversity.md) — related
- [LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses](llm-survey-responses-extreme-low-variability.md) — related
- [Item-level discrepancies between LLM and human responses were higher for negatively worded BREQ items](llm-higher-discrepancy-negative-worded-items.md) — related
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](llm-choice-affects-human-ai-coding-correspondence.md) — related
- [The author reports that prompt phrasing and the specific foundational model had secondary impact on final material quality compared with the structure of the workflow itself.](workflow-architecture-outweighs-prompt-phrasing.md) — related

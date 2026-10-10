---
type: claim
title: Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts
description: Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts
id: interview-prompts-increase-llm-response-diversity
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
  - id: zhang-2026-2
    resource: "https://osf.io/AFQG3"
    title: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3"
    author: "Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Claude produced more diverse responses when prompts contained interview data (Prompts 2 and 4). [→ Zhang 2026](#zhang-2026)
`q2 i?` Higher temperature (0.5) yielded higher item-response variances than temperature 0 for all chatbots. [→ Zhang 2026 (2)](#zhang-2026-2)

## Evidence

### Zhang 2026

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Descriptive variance analysis across the 24 conditions (Figure 4) showing a chatbot-by-prompt interaction in diversity: Claude diversified with interview prompts, Gemini with demographic-only prompts. No effect size printed.

> "the variances of LLM-generated responses interacted with LLM chatbots— claude had more diverse responses when prompts contained the interview data (Prompt 2 and Prompt 4). In contrast, gemini had more diverse responses when prompts contained demographic information only (Prompt 3)."

### Zhang 2026 (2)

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Variance comparison between temperature 0 and 0.5 across all three chatbots in the same simulation. The article reports higher variance at Temp = .5 for all chatbots; no effect size printed.

> "higher temperature conditions (Temp = .5) showed higher variances of item responses than lower temperature conditions (Temp = 0) for all LLM chatbots, which was consistent with the definition of temperature."

## Discussion


## Related Claims
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index](test-level-rai-only-claude-improved.md) — related
- [LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses](llm-survey-responses-extreme-low-variability.md) — related
- [LLM-annotated EPITOME scores show the Non-Empathetic chatbot expresses significantly lower empathy on all three dimensions, while Standard and Empathetic chatbots are not significantly different](llm-epitome-scores-differentiate-nonempathetic.md) — related
- [The author reports that prompt phrasing and the specific foundational model had secondary impact on final material quality compared with the structure of the workflow itself.](workflow-architecture-outweighs-prompt-phrasing.md) — related

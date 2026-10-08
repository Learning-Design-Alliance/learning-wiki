---
type: claim
title: LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses
description: LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses
id: llm-survey-responses-extreme-low-variability
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

# LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Across conditions, LLMs generated more extreme item means than humans, with lower means for low-rated items and higher means for high-rated items. [→ Zhang 2026](#zhang-2026)
`q2 i?` Variances of LLM-generated responses were much lower than human responses under all conditions, indicating lower diversity. [→ Zhang 2026 (2)](#zhang-2026-2)

## Evidence

### Zhang 2026

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Descriptive comparison of item-level means across 24 conditions (3 chatbots × 4 prompts × 2 temperatures) shown in Figure 3. The article reports LLMs "tended to generate more extreme responses than humans" in both directions; no effect size is printed.

> "Across all conditions, LLMs tended to generate more extreme responses than humans; that is, for items with lower human ratings (e.g., items 1–7), LLM mean scores were even lower, and for items with higher human ratings (e.g., items 8–15), LLM mean scores were even higher."

### Zhang 2026 (2)

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Item-level variance comparison across all conditions shown in Figure 4. The article states LLM variances were "much lower than human responses under all conditions"; no effect size is printed.

> "variances of LLM-generated responses were much lower than human responses under all conditions, indicating that LLM-generated responses were less diverse than human responses."

## Discussion


## Related Claims
- [Interview length was not significantly associated with person-level alignment between LLM and human responses](interview-length-null-person-level-alignment.md) — related
- [Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts](interview-prompts-increase-llm-response-diversity.md) — related
- [Item-level discrepancies between LLM and human responses were higher for negatively worded BREQ items](llm-higher-discrepancy-negative-worded-items.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index](test-level-rai-only-claude-improved.md) — related

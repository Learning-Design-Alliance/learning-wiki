---
type: claim
title: Item-level discrepancies between LLM and human responses were higher for negatively worded BREQ items
description: Item-level discrepancies between LLM and human responses were higher for negatively worded BREQ items
id: llm-higher-discrepancy-negative-worded-items
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

# Item-level discrepancies between LLM and human responses were higher for negatively worded BREQ items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Items 6, 7, and 11, which contain negative emotional words such as ashamed, failure, and restless, showed relatively higher RMSEs than other items. [→ Zhang 2026](#zhang-2026)

## Evidence

### Zhang 2026

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Item-level RMSE analysis across 15 BREQ items (Figure 6) identifying items 6, 7, and 11 as highest-discrepancy items, attributed by the authors to their negative emotional wording. No effect size printed.

> "items 6, 7, and 11 displayed relatively higher RMSEs than other items. After screening those items carefully, we found that item 6 ( I feel ashamed when I miss an exercise session), item 7 (I feel like a failure when I haven’t exercised in a while), and item 11 (I get restless if I don’t exercise regularly) contain relatively negative emotional words, such as “ashamed”, “failure”, and “restless”"

## Discussion


## Related Claims
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses](llm-survey-responses-extreme-low-variability.md) — related
- [At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index](test-level-rai-only-claude-improved.md) — related

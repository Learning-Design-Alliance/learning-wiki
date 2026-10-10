---
type: claim
title: Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts
description: Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts
id: claude-highest-human-alignment-interview-prompts
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

# Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Average Pearson correlations between LLM and human responses ranged from .5 to .73, with Claude highest and Gemini lowest across conditions. [→ Zhang 2026](#zhang-2026)
`q2 i?` Claude showed lower item-level RMSEs than Gemini and GPT, indicating the highest alignment with human respondents. [→ Zhang 2026 (2)](#zhang-2026-2)

## Evidence

### Zhang 2026

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Pearson correlations between LLM-generated and human responses across four prompts (Figure 5), with correlations in the medium-to-high range (ρ ∈ [.5, .73]). Claude ranked highest, Gemini lowest; no effect size printed.

> "claude shows the highest correlations with humans for all four prompts, followed by gpt. In contrast, gemini has the lowest correlations with humans across conditions."

### Zhang 2026 (2)

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Item-level RMSE comparison across the three chatbots (Figure 6). The article reports Claude's RMSEs were lower than both Gemini's and GPT's; no effect size printed.

> "Overall, claude shows lower RMSEs than gemini and gpt, suggesting that claude has the highest alignment with human respondents."

## Discussion


## Related Claims
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — related
- [Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts](interview-prompts-increase-llm-response-diversity.md) — related
- [At the test level, only Claude with interview or demographic prompts improved alignment on the relative autonomy index](test-level-rai-only-claude-improved.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Item-level discrepancies between LLM and human responses were higher for negatively worded BREQ items](llm-higher-discrepancy-negative-worded-items.md) — related
- [LLM-generated BREQ responses capture overall item-mean patterns but are more extreme and less variable than human responses](llm-survey-responses-extreme-low-variability.md) — related
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](llm-choice-affects-human-ai-coding-correspondence.md) — related
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)](llm-communication-grading-insufficient-alignment-ttx.md) — related
- [Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items](ca-selective-best-average-agreement-drawings.md) — related

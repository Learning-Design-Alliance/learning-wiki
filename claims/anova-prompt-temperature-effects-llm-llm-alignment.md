---
type: claim
title: Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots
description: Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots
id: anova-prompt-temperature-effects-llm-llm-alignment
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

# Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` A three-way ANOVA on inter-LLM Pearson correlations found significant main effects of prompt settings and temperature settings. [→ Zhang 2026](#zhang-2026)

## Evidence

### Zhang 2026

Zhang, J., Liang, X., Deng, A., Bonge, N., Tan, L., Zhang, L., & Zarrett, N. (2026). Leveraging Interview-Informed LLMs to Model Survey Responses: Comparative Insights from AI-Generated and Human Data. Journal of Educational Data Mining, 18(1). https://osf.io/AFQG3

`q2 · i?` · `causal · r1`

Three-way ANOVA with Pearson correlations among gpt, claude, and gemini as the dependent variable across the 24 conditions. The article prints F(3,17) = 16.657, p < .001 for prompts and F(1,17) = 8.133, p = .011 for temperature; no effect size is printed.

> "The results of three-way ANOVAs show that prompt settings (𝐹3,17 = 16.657, 𝑝 < .001) and temperature settings (𝐹1,17 = 8.133, 𝑝 = .011) have significant main effects on the correlations among the three LLM chatbots."

## Discussion


## Related Claims
- [Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts](interview-prompts-increase-llm-response-diversity.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [Lowering an LLM's temperature setting is one lever for improving output consistency](lowering-temperature-improves-llm-consistency.md) — related
- [LLM choice significantly influences human-AI coding correspondence, with Claude Sonnet 4 performing best and GPT 4.1 Mini worst](llm-choice-affects-human-ai-coding-correspondence.md) — related
- [Zero-shot prompt type has minimal impact on LLM-human coding concordance](prompt-type-minimal-impact-llm-coding.md) — reports the opposite
- [Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models](cross-model-rpla-degradation-consistent.md) — related

---
type: claim
title: LLM-annotated EPITOME scores show the Non-Empathetic chatbot expresses significantly lower empathy on all three dimensions, while Standard and Empathetic chatbots are not significantly different
description: LLM-annotated EPITOME scores show the Non-Empathetic chatbot expresses significantly lower empathy on all three dimensions, while Standard and Empathetic chatbots are not significantly different
id: llm-epitome-scores-differentiate-nonempathetic
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: li-siyan-2026
    resource: "https://arxiv.org/abs/2606.26641"
    title: "Li Siyan, Kai-Hui Liang, Shopnil Shahriar, Yilin Ye, Shiyoh Goetsu, Wei-Wei Du, Masahiro Yoshida, Tsunayuki Ohwa, Xuhai Xu, and Zhou Yu. (2026). Invisible Impact of Empathy on Behavioral Change: Isolating the Effect of Empathy in Long-term Physical Activity Coaching Chatbot Interactions. https://arxiv.org/abs/2606.26641"
    author: Li Siyan, Kai-Hui Liang, Shopnil Shahriar, Yilin Ye, Shiyoh Goetsu, Wei-Wei Du, Masahiro Yoshida, Tsunayuki Ohwa, Xuhai Xu, and Zhou Yu
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM-annotated EPITOME scores show the Non-Empathetic chatbot expresses significantly lower empathy on all three dimensions, while Standard and Empathetic chatbots are not significantly different

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` One-way ANOVA on Gemini-annotated EPITOME scores over 237 conversations found significant between-condition differences; post hoc tests show the Non-Empathetic chatbot significantly lower on all three dimensions and Standard vs. Empathetic differences not significant. [→ Li Siyan 2026](#li-siyan-2026)

## Evidence

### Li Siyan 2026

Li Siyan, Kai-Hui Liang, Shopnil Shahriar, Yilin Ye, Shiyoh Goetsu, Wei-Wei Du, Masahiro Yoshida, Tsunayuki Ohwa, Xuhai Xu, and Zhou Yu. (2026). Invisible Impact of Empathy on Behavioral Change: Isolating the Effect of Empathy in Long-term Physical Activity Coaching Chatbot Interactions. https://arxiv.org/abs/2606.26641

`q2 · i?` · `causal · r1`

LLM-based annotation of 237 collected conversations (76 Non-Empathetic, 80 Standard, 81 Empathetic) using Gemini-2.5-Pro with the EPITOME three-dimensional empathy framework, one-way ANOVA with Bonferroni-corrected post hoc t-tests. No standardized effect size is printed; the article notes the Empathetic chatbot's average interpretation level is higher though not significant post-adjustment.

> "In particular, the Non-Empathetic chatbot scores significantly lower along all three empathy dimensions. However, the differences in means between the Standard and Empathetic chatbots are not sufficiently significant."

## Discussion


## Related Claims
- [In a six-week within-subject study, the Empathetic PA coaching chatbot improves intention to follow and self-efficacy faster over time than the Non-Empathetic condition](empathetic-chatbot-faster-intention-selfefficacy-growth.md) — related
- [Starting interaction with the Empathetic chatbot is associated with the least attrition in the six-week study](empathetic-condition-least-attrition.md) — related
- [LLM-annotated empathy dimensions correlate positively with intention to follow, self-efficacy, and chatbot usefulness despite participants not preferring empathetic chatbots](empathy-dimensions-correlate-with-outcomes.md) — related
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — related
- [Average check-in and weekly ratings show no significant differences between chatbot conditions, with the Non-Empathetic chatbot often rated as more engaging and useful](no-significant-average-differences-nonempathetic-rated-higher.md) — related
- [Interview-containing prompts increased response diversity for Claude and GPT, while Gemini diversified with demographic-only prompts](interview-prompts-increase-llm-response-diversity.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [Non-expert participants often fail to notice empathy differences between chatbot versions, so self-reported perceived empathy alone is an unreliable assessment method](nonexpert-perceived-empathy-unreliable.md) — related

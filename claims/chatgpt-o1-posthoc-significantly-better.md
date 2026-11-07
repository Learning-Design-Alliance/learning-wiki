---
type: claim
title: Post-hoc comparisons show ChatGPT o1 performed significantly better than most other models across both question types (p < 0.0031)
description: Post-hoc comparisons show ChatGPT o1 performed significantly better than most other models across both question types (p < 0.0031)
id: chatgpt-o1-posthoc-significantly-better
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yilmaz-birkan-eyup-2025
    resource: "https://doi.org/10.1186/s12903-025-05926-2"
    title: "Yilmaz Birkan Eyup, Gokkurt Yilmaz Busra Nur, Ozbey Furkan. (2025). Artificial intelligence performance in answering multiple-choice oral pathology questions: a comparative analysis. BMC Oral Health. https://doi.org/10.1186/s12903-025-05926-2"
    author: Yilmaz Birkan Eyup, Gokkurt Yilmaz Busra Nur, Ozbey Furkan
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Post-hoc comparisons show ChatGPT o1 performed significantly better than most other models across both question types (p < 0.0031)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` After Bonferroni correction, ChatGPT o1 differed significantly from Gemini 1.5, Gemini 2, Deepseek, Claude, ChatGPT 4o, and ChatGPT 4 on all questions (p < 0.0031). [→ Yilmaz Birkan Eyup 2025](#yilmaz-birkan-eyup-2025)

## Evidence

### Yilmaz Birkan Eyup 2025

Yilmaz Birkan Eyup, Gokkurt Yilmaz Busra Nur, Ozbey Furkan. (2025). Artificial intelligence performance in answering multiple-choice oral pathology questions: a comparative analysis. BMC Oral Health. https://doi.org/10.1186/s12903-025-05926-2

`q3 · i?` · `design · r2`

Post-hoc pairwise Chi-square comparisons with Bonferroni correction (significance adjusted to p < 0.0031) among the eight LLMs on all 100 questions. The article reports "significant differences were identified between ChatGPT o1 and Gemini 1.5, Gemini 2, Deepseek, Claude, ChatGPT 4o, and ChatGPT 4". No effect size is printed.

> "Additionally, significant differences were identified between ChatGPT o1 and Gemini 1.5, Gemini 2, Deepseek, Claude, ChatGPT 4o, and ChatGPT 4 (p < 0.0031)."

## Discussion


## Related Claims
- [Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies](llm-company-comparison-biomedical-mcq-accuracy.md) — related
- [Pairwise McNemar comparisons showed OpenAI o1 significantly better than GPT-4o, Gemini, and Copilot in Respiratory Medicine, with mixed significance across other courses](mcnemar-pairwise-openai-o1-vs-other-llms-mixed.md) — a narrower finding that bears on this claim
- [DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy](deepseek-qwen32b-outperform-gpt4o-clinical-cases.md) — related
- [LLM performance differs significantly on case-based oral pathology questions (p = 0.034), where ChatGPT o1 and Claude excelled](llm-case-based-question-performance.md) — related

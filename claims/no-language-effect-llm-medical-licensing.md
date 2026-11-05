---
type: claim
title: Language of presentation (Chinese vs. English) has no significant main effect on LLM accuracy on Chinese medical licensing exam questions
description: Language of presentation (Chinese vs.
id: no-language-effect-llm-medical-licensing
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tang-yuxia-2026
    resource: "https://doi.org/10.1371/journal.pone.0346518"
    title: "Tang Yuxia, Chen Jian, Wang Shouju. (2026). Performance benchmarking of LLMs on Chinese national medical licensing education: Cross-lingual and question-type effects. PLoS One. https://doi.org/10.1371/journal.pone.0346518"
    author: Tang Yuxia, Chen Jian, Wang Shouju
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Language of presentation (Chinese vs. English) has no significant main effect on LLM accuracy on Chinese medical licensing exam questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The ANOVA found no significant effect of language on accuracy (F(1,5) = 0.39, P = 0.56), and the Chinese vs. English paired comparison was not significant after correction. [→ Tang Yuxia 2026](#tang-yuxia-2026)

## Evidence

### Tang Yuxia 2026

Tang Yuxia, Chen Jian, Wang Shouju. (2026). Performance benchmarking of LLMs on Chinese national medical licensing education: Cross-lingual and question-type effects. PLoS One. https://doi.org/10.1371/journal.pone.0346518

`q2 · i?` · `design · r2`

Two-way repeated-measures ANOVA reported in Results, testing language (Chinese, English) as a within-subject factor across six models. The article reports "no significant effect of language" with F(1,5) = 0.39, P = 0.56; no effect size is printed, and equivalence was not tested.

> "There was a significant main effect of question type (F(2,10) = 10.22, P = 0.0038), but no significant effect of language (F(1,5) = 0.39, P = 0.56) (Fig 4)."

## Discussion


## Related Claims
- [Question type significantly affects LLM accuracy on Chinese medical licensing exam questions, with Type A basic-knowledge items answered better than Type B and Type C items](question-type-effect-llm-chinese-medical-licensing.md) — related
- [Subgroup analyses show significant between-model differences, with Copilot (75.25%) and ChatGPT-4 (72.97%) achieving the highest pooled accuracies](llm-subgroup-copilot-chatgpt4-highest-accuracy.md) — related
- [GPT-4 achieves the highest pooled accuracy among LLMs (81%), significantly outperforming GPT-3.5 (60%)](gpt4-highest-accuracy-81-outperforms-gpt35.md) — related

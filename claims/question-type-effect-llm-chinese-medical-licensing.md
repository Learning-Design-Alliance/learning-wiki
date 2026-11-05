---
type: claim
title: Question type significantly affects LLM accuracy on Chinese medical licensing exam questions, with Type A basic-knowledge items answered better than Type B and Type C items
description: Question type significantly affects LLM accuracy on Chinese medical licensing exam questions, with Type A basic-knowledge items answered better than Type B and Type C items
id: question-type-effect-llm-chinese-medical-licensing
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
  - id: tang-yuxia-2026-2
    resource: "https://doi.org/10.1371/journal.pone.0346518"
    title: "Tang Yuxia, Chen Jian, Wang Shouju. (2026). Performance benchmarking of LLMs on Chinese national medical licensing education: Cross-lingual and question-type effects. PLoS One. https://doi.org/10.1371/journal.pone.0346518"
    author: Tang Yuxia, Chen Jian, Wang Shouju
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Question type significantly affects LLM accuracy on Chinese medical licensing exam questions, with Type A basic-knowledge items answered better than Type B and Type C items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A two-way repeated-measures ANOVA found a significant main effect of question type on LLM accuracy (F(2,10) = 10.22, P = 0.0038). [→ Tang Yuxia 2026](#tang-yuxia-2026)
`q2 i?` Post hoc tests showed Type A performance significantly exceeded both Type B (P = 0.002) and Type C (P = 0.025), while B vs. C did not differ after correction. [→ Tang Yuxia 2026 (2)](#tang-yuxia-2026-2)

## Evidence

### Tang Yuxia 2026

Tang Yuxia, Chen Jian, Wang Shouju. (2026). Performance benchmarking of LLMs on Chinese national medical licensing education: Cross-lingual and question-type effects. PLoS One. https://doi.org/10.1371/journal.pone.0346518

`q2 · i?` · `design · r2`

Two-way repeated-measures ANOVA with mean accuracy as dependent variable, models as subject factor, and question type and language as within-subject factors, reported in the Results section. The article reports the significant question-type main effect with "F(2,10) = 10.22, P = 0.0038"; no effect size is printed.

> "There was a significant main effect of question type (F(2,10) = 10.22, P = 0.0038), but no significant effect of language (F(1,5) = 0.39, P = 0.56)"

### Tang Yuxia 2026 (2)

Tang Yuxia, Chen Jian, Wang Shouju. (2026). Performance benchmarking of LLMs on Chinese national medical licensing education: Cross-lingual and question-type effects. PLoS One. https://doi.org/10.1371/journal.pone.0346518

`q2 · i?` · `design · r2`

Bonferroni-corrected post hoc paired t-tests between question-type pairs, reported in Results. Type A beat both other types; the Type B vs. Type C contrast was not significant, and equivalence was not tested. No effect size is printed.

> "The performance of Type A was significantly better than both Type B (P = 0.002) and Type C (P = 0.025). However, neither the Type B vs. Type C comparison nor the Chinese vs. English comparison reached statistical significance after correction."

## Discussion


## Related Claims
- [A marginal, non-significant interaction between question type and language was observed for LLM accuracy (F(2,10) = 3.57, P = 0.068)](marginal-question-type-language-interaction.md) — related
- [Language of presentation (Chinese vs. English) has no significant main effect on LLM accuracy on Chinese medical licensing exam questions](no-language-effect-llm-medical-licensing.md) — related
- [Question type affects accuracy: feature-to-concept questions are answered best and applied questions worst](question-type-accuracy-ordering.md) — a broader claim this one bears on

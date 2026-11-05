---
type: claim
title: Gemini 2.5 Pro significantly outperformed GPT-5 on EDAIC questions as the only significant pairwise difference after Holm correction
description: Gemini 2.5 Pro significantly outperformed GPT-5 on EDAIC questions as the only significant pairwise difference after Holm correction
id: gemini-outperformed-gpt5-edaic-pairwise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: stefan-andrei-2026
    resource: "https://doi.org/10.2196/95859"
    title: "Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie. (2026). Performance and Hallucination Analysis of Large Language Models on European Anesthesiology Examinations: Cross-Sectional Comparative Study. JMIR Formative Research. https://doi.org/10.2196/95859"
    author: Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# Gemini 2.5 Pro significantly outperformed GPT-5 on EDAIC questions as the only significant pairwise difference after Holm correction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i2` medium
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i2` On EDAIC questions, Gemini 2.5 Pro significantly outperformed GPT-5 (Z=2.75; r=0.32; adjusted P=.04); no other pairwise comparison was significant. [→ Stefan Andrei 2026](#stefan-andrei-2026)

## Evidence

### Stefan Andrei 2026

Stefan Andrei, Giet Thibault, Belouard Alexis, Stefan Mihai, Popescu Mihai, Tanaka Sébastien, Montravers Philippe, Gouel Aurélie. (2026). Performance and Hallucination Analysis of Large Language Models on European Anesthesiology Examinations: Cross-Sectional Comparative Study. JMIR Formative Research. https://doi.org/10.2196/95859

`q2 · i2` · `design · r2`

EDAIC analysis of 219 questions answered by 4 LLMs, using Friedman and Wilcoxon signed-rank tests with Holm-Bonferroni correction. The article reports "Gemini 2.5 Pro significantly outperformed GPT-5 (Z=2.75; r=0.32; adjusted P=.04)" with r=0.32 as the printed effect size.

> "In pairwise Wilcoxon signed-rank comparisons, Gemini 2.5 Pro significantly outperformed GPT-5 (Z=2.75; r=0.32; adjusted P=.04). No other pairwise comparisons were significant (adjusted P≥.09 in all cases)."

## Discussion


## Related Claims
- [Claude Sonnet 4.5 significantly outperformed Grok 4 on OLA questions, the only significant pairwise difference on that examination](claude-outperformed-grok4-ola-pairwise.md) — related
- [Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models.](mcnemar-pairwise-llm-ebhs-significant-differences.md) — related
- [Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.](proprietary-llms-outperform-open-source-ebhs.md) — related
- [Hallucination rates ranged from 11% to 20.1% across LLMs without significant intermodel differences](hallucination-rates-11-20-percent-no-model-differences.md) — related
- [Gemini 2.5 Pro achieved the highest accuracy (92.44%) on pediatric dentistry DUS questions, significantly outperforming most other LLMs](gemini-2-5-pro-highest-accuracy-pediatric-dus.md) — related
- [No statistically significant performance gap existed between Turkish and English administration of the same radiology questions to ChatGPT-5 and Gemini 2.5 Pro](no-language-gap-turkish-english-llm-radiology-accuracy.md) — related
- [ChatGPT-5 achieved the highest overall accuracy on ophthalmology board-style questions (92.59%), with no statistically significant differences among the four LLMs](chatgpt-5-highest-overall-accuracy-ophthalmology-board-questions.md) — related
- [Four reasoning-enhanced LLMs exceed 95% accuracy on the JNME, with Gemini 2.5 Pro highest at 97.2% and no significant pairwise differences](four-llms-exceed-95-jnme-2026.md) — related
- [Pairwise chi-square comparisons found no significant difference only between Grok and ChatGPT 4.5, while all other model pairs differed significantly](pairwise-llm-comparisons-grok-chatgpt45-nonsignificant.md) — related
- [LLM performance does not differ significantly between 2019 and 2025 exam questions despite training-cutoff differences](no-performance-difference-exam-year.md) — related

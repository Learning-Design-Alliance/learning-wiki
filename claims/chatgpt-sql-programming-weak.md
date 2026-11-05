---
type: claim
title: "ChatGPT performs poorly on health database SQL programming tasks, with the best AI version scoring 56% against a top student score of 100%"
description: "ChatGPT performs poorly on health database SQL programming tasks, with the best AI version scoring 56% against a top student score of 100%"
id: chatgpt-sql-programming-weak
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: wani-tafheem-ahmad-2026
    resource: "https://doi.org/10.2196/82988"
    title: "Wani Tafheem Ahmad, Liem Michael, Prasad Natasha, Robinson Kerin, Nexhip Abbey, Tassos Melanie, Gjorgioski Stephanie, Khan Urooj Raza, Boyd James, Riley Merilyn. (2026). Susceptibility of Assessment Types to AI-Generated Content in Digital Health and Health Information Management Education: Quasi-Experimental Pilot Study. JMIR Medical Education. https://doi.org/10.2196/82988"
    author: Wani Tafheem Ahmad, Liem Michael, Prasad Natasha, Robinson Kerin, Nexhip Abbey, Tassos Melanie, Gjorgioski Stephanie, Khan Urooj Raza, Boyd James, Riley Merilyn
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# ChatGPT performs poorly on health database SQL programming tasks, with the best AI version scoring 56% against a top student score of 100%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across SQL submission versions, scores rose from 17% (V1, no schema) to 56% (o1 Preview V4), but persistent errors in counts, grouping, and interpretation remained, while the top student scored 100%. [→ Wani Tafheem Ahmad 2026](#wani-tafheem-ahmad-2026)

## Evidence

### Wani Tafheem Ahmad 2026

Wani Tafheem Ahmad, Liem Michael, Prasad Natasha, Robinson Kerin, Nexhip Abbey, Tassos Melanie, Gjorgioski Stephanie, Khan Urooj Raza, Boyd James, Riley Merilyn. (2026). Susceptibility of Assessment Types to AI-Generated Content in Digital Health and Health Information Management Education: Quasi-Experimental Pilot Study. JMIR Medical Education. https://doi.org/10.2196/82988

`q2 · i?` · `causal · r1`

Blinded marking of AI-generated SQL submissions in the pilot quasi-experiment, with schema and rubric provided in later versions. Results report V1 at 17% with all table and column names incorrect, and the top student submission at 100%. No effect size is printed.

> "The most advanced model, o1 Preview (V4), achieved the highest AI score (56%), correctly executing about half of the queries and demonstrating improved adherence to SQL conventions, but still suffered from inaccuracies in age group breakdowns, incorrect counts, and missing contextual details such as diagnosis descriptions."

## Discussion


## Related Claims
- [ChatGPT performs best on objective health classification quiz items (88%) but scores only 7% on scenario-based clinical coding, far below the top student (87%)](chatgpt-objective-strong-scenario-coding-weak.md) — related
- [ChatGPT scores rose from V1 to V3 across assessment types in one uncontrolled pre-post study, with V3 achieving the highest average scores](rubric-integration-improves-chatgpt-scores.md) — a broader claim this one bears on
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [On descriptive analytical tasks ChatGPT produced logically structured work but lacked deep contextualization, domain-specific insights, and visual elements](chatgpt-descriptive-tasks-generic-outputs.md) — related
- [The advanced o1 Preview model did not consistently outperform GPT-4, underperforming V3 on descriptive tasks](o1-preview-no-consistent-advantage.md) — related

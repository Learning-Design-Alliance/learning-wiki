---
type: claim
title: LLM performance does not differ significantly between 2019 and 2025 exam questions despite training-cutoff differences
description: LLM performance does not differ significantly between 2019 and 2025 exam questions despite training-cutoff differences
id: no-performance-difference-exam-year
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: liu-mingxin-2026
    resource: "https://doi.org/10.1186/s12911-026-03370-y"
    title: "Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y"
    author: Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM performance does not differ significantly between 2019 and 2025 exam questions despite training-cutoff differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For each LLM, accuracy did not differ significantly between the 2025 and 2019 JNME (all p > 0.05), even though no model had prior access to 2025 content. [→ Liu Mingxin 2026](#liu-mingxin-2026)

## Evidence

### Liu Mingxin 2026

Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y

`q2 · i?` · `design · r2`

Comparison of accuracy on 393 questions from the 2019 JNME and 400 questions from the 2025 JNME, the latter published after all models' knowledge cutoffs; the article reports "all p > 0.05".

> "Similarly, for each LLM, the performance did not differ significantly between the 2025 and 2019 JNME (all p > 0.05)"

## Discussion


## Related Claims
- [All four LLMs passed both JNME exams under official scoring, with near-perfect scores in essential sections](llms-pass-jnme-official-scoring.md) — related
- [Four reasoning-enhanced LLMs exceed 95% accuracy on the JNME, with Gemini 2.5 Pro highest at 97.2% and no significant pairwise differences](four-llms-exceed-95-jnme-2026.md) — related
- [Large language models achieve a pooled accuracy of 72% on medical licensing examination questions across 36 studies](llm-pooled-accuracy-72-medical-licensing-exams.md) — a broader claim this one bears on
- [LLM accuracy does not differ significantly across question languages, ranging from 62% in Polish to 77% in German](llm-accuracy-language-differences-nonsignificant.md) — related
- [Gemini 2.5 Pro significantly outperformed GPT-5 on EDAIC questions as the only significant pairwise difference after Holm correction](gemini-outperformed-gpt5-edaic-pairwise.md) — related

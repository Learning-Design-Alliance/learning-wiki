---
type: claim
title: Accuracy on difficult questions is significantly lower than on easy questions for all four LLMs
description: Accuracy on difficult questions is significantly lower than on easy questions for all four LLMs
id: difficulty-effect-attenuated-llms
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

# Accuracy on difficult questions is significantly lower than on easy questions for all four LLMs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All four LLMs showed significantly lower accuracy on difficult than easy questions, but no significant differences between easy and moderate or moderate and difficult questions. [→ Liu Mingxin 2026](#liu-mingxin-2026)

## Evidence

### Liu Mingxin 2026

Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y

`q2 · i?` · `design · r2`

Accuracy was compared across difficulty strata (easy ≥90%, moderate 70–89%, difficult <70% student correctness); the article reports "all p-values < 0.05" for easy versus difficult, with Gemini 2.5 Pro highest in each stratum (98.4%, 97.3%, 93.2%).

> "When comparing easy versus difficult questions, all four LLMs showed significant differences (all p-values < 0.05)"

## Discussion


## Related Claims
- [Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs](image-based-questions-lower-accuracy.md) — related
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — related
- [All four LLMs show higher accuracy on general than clinical questions, significant only for Grok-4](general-vs-clinical-accuracy-gap.md) — related

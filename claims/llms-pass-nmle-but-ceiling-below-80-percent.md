---
type: claim
title: "All tested LLMs exceeded the NMLE passing threshold yet stayed below 80% accuracy across all units and years"
description: "All tested LLMs exceeded the NMLE passing threshold yet stayed below 80% accuracy across all units and years"
id: llms-pass-nmle-but-ceiling-below-80-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: diao-y-2025
    resource: "https://doi.org/10.2196/77978"
    title: "Diao Y, Wu M, Xu J, Pan Y. (2025). Multiple Large Language Models’ Performance on the Chinese Medical Licensing Examination: Quantitative Comparative Study. JMIR Human Factors. https://doi.org/10.2196/77978"
    author: Diao Y, Wu M, Xu J, Pan Y.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: diao-y-2025-2
    resource: "https://doi.org/10.2196/77978"
    title: "Diao Y, Wu M, Xu J, Pan Y. (2025). Multiple Large Language Models’ Performance on the Chinese Medical Licensing Examination: Quantitative Comparative Study. JMIR Human Factors. https://doi.org/10.2196/77978"
    author: Diao Y, Wu M, Xu J, Pan Y.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# All tested LLMs exceeded the NMLE passing threshold yet stayed below 80% accuracy across all units and years

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`–`q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Every tested model consistently scored above the 360-point passing threshold across the seven examination years. [→ Diao Y 2025](#diao-y-2025)
`q1 i?` No tested LLM exceeded 80% average accuracy in any NMLE unit or year, including GPT-4 (highest 80.67% in unit 4) and DeepSeek (highest 73.2% in unit 1). [→ Diao Y 2025 (2)](#diao-y-2025-2)

## Evidence

### Diao Y 2025

Diao Y, Wu M, Xu J, Pan Y. (2025). Multiple Large Language Models’ Performance on the Chinese Medical Licensing Examination: Quantitative Comparative Study. JMIR Human Factors. https://doi.org/10.2196/77978

`q2 · i?` · `design · r2`

Across the 2018-2024 Chinese LLM comparison (Figure 3), "All models consistently exceeded the passing threshold (360)" against official answer keys.

> "All models consistently exceeded the passing threshold (360), confirming their fundamental competence in medical knowledge assessment"

### Diao Y 2025 (2)

Diao Y, Wu M, Xu J, Pan Y. (2025). Multiple Large Language Models’ Performance on the Chinese Medical Licensing Examination: Quantitative Comparative Study. JMIR Human Factors. https://doi.org/10.2196/77978

`q1 · i?` · `design · r2`

The authors' discussion of the performance ceiling identifies three factors: emphasis on high-order clinical reasoning, training-data timeliness limits, and text-based input losing visual details. "did not exceed 80% across all NMLE units and years."

> "the performance of all tested LLMs—including GPT-4 (highest average accuracy=80.67% in unit 4) and the top-performing Chinese model, DeepSeek (highest average accuracy=73.2% in unit 1)—did not exceed 80% across all NMLE units and years"

## Discussion


## Related Claims
- [DeepSeek achieved the highest overall NMLE performance among the four Chinese LLMs tested](deepseek-highest-chinese-llm-nmle-performance.md) — related
- [GPT-4 performed comparably to average human NMLE examinees, DeepSeek slightly exceeded them, and no tested LLM reached the top-10% human threshold](llm-nmle-performance-versus-human-examinees.md) — related
- [LLM scores typically exceeded the student median and, in several instances, the highest student score in every course](llm-scores-exceed-student-median-and-maximum.md) — related
- [GPT-4 exceeds pass marks on India NEET-PG and UK PLAB 1 but falls below pass on clinical reasoning and procedural items](gpt4-neetpg-plab-pass-clinical-reasoning-below.md) — related
- [All four LLMs passed both JNME exams under official scoring, with near-perfect scores in essential sections](llms-pass-jnme-official-scoring.md) — related
- [GPT-4 and GPT-4o accuracy exceeds the NMLE passing threshold and the typical national pass rate](gpt4-gpt4o-exceed-nmle-passing-threshold.md) — a narrower finding that bears on this claim

---
type: claim
title: "LLM error profiles differ by model: GPT-4o shows frequent hallucination, Gemini 2.5 Flash systematic visual-interpretation errors, Gemini 2.5 Pro balanced but reasoning-limited performance"
description: "LLM error profiles differ by model: GPT-4o shows frequent hallucination, Gemini 2.5 Flash systematic visual-interpretation errors, Gemini 2.5 Pro balanced but reasoning-limited performance"
id: model-specific-llm-error-profiles-csat
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: seok-hyun-ga-2025
    resource: "https://doi.org/10.48550/arXiv.2512.15298"
    title: "Seok-Hyun Ga, Chun-Yen Chang. (2025). ChatGPT and Gemini participated in the Korean College Scholastic Ability Test - Earth Science I. [doi:10.48550/arXiv.2512.15298](https://doi.org/10.48550/arXiv.2512.15298)"
    author: Seok-Hyun Ga, Chun-Yen Chang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM error profiles differ by model: GPT-4o shows frequent hallucination, Gemini 2.5 Flash systematic visual-interpretation errors, Gemini 2.5 Pro balanced but reasoning-limited performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4o had the lowest OCR accuracy and frequent hallucinations, Gemini 2.5 Flash showed systematic visual-interpretation errors but relatively accurate calculation, and Gemini 2.5 Pro was most balanced overall with consistent limits on complex reasoning. [→ Seok-Hyun Ga 2025](#seok-hyun-ga-2025)

## Evidence

### Seok-Hyun Ga 2025

Seok-Hyun Ga, Chun-Yen Chang. (2025). ChatGPT and Gemini participated in the Korean College Scholastic Ability Test - Earth Science I. [doi:10.48550/arXiv.2512.15298](https://doi.org/10.48550/arXiv.2512.15298)

`q2 · i?` · `causal · r1`

Authors' comparative characterization of the three models across Experiments 1-3 on the 2025 CSAT Earth Science I section, based on the quantitative scores and the qualitative error analysis of Experiment 3 incorrect cases. The article reports these as observed differences in cognitive characteristics among the models.

> "GPT-4o, while relatively maintaining logical consistency, had the lowest OCR accuracy and frequent hallucinations. Gemini 2.5 Flash showed systematic errors in visual information interpretation but was relatively accurate in calculation processes. Gemini 2.5 Pro demonstrated the most balanced performance overall but still revealed consistent limitations in problems requiring complex reasoning."

## Discussion


## Related Claims
- [LLMs perform at or below random-choice levels when given unstructured full-page exam images on the 2025 CSAT Earth Science I](llms-below-random-full-page-csat-earth-science.md) — related
- [LLMs exhibit Process Hallucination, skipping visual verification and applying plausible but unverified background knowledge](process-hallucination-skipped-visual-verification.md) — related
- [Even under optimized multimodal input eliminating OCR errors, a large performance gap persists between LLMs on CSAT Earth Science I](optimized-input-persistent-llm-gap-csat.md) — related
- [LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments](llms-differ-liberal-restrictive-balanced-grading-styles.md) — related
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
- [Perception Errors are the dominant LLM error type under optimized conditions, accounting for 43.06% of errors](perception-errors-dominant-llm-failures.md) — related
- [Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o](claude-copilot-gemini-topic-strengths-reliability.md) — related

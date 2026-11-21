---
type: claim
title: LLMs exhibit Process Hallucination, skipping visual verification and applying plausible but unverified background knowledge
description: LLMs exhibit Process Hallucination, skipping visual verification and applying plausible but unverified background knowledge
id: process-hallucination-skipped-visual-verification
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
    kind: qualitative
    rigour: 2
---

# LLMs exhibit Process Hallucination, skipping visual verification and applying plausible but unverified background knowledge

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In Process Hallucination (category 4.2), models skipped complex reasoning steps such as visual verification of data and hastily applied related background knowledge without data verification to justify conclusions. [→ Seok-Hyun Ga 2025](#seok-hyun-ga-2025)

## Evidence

### Seok-Hyun Ga 2025

Seok-Hyun Ga, Chun-Yen Chang. (2025). ChatGPT and Gemini participated in the Korean College Scholastic Ability Test - Earth Science I. [doi:10.48550/arXiv.2512.15298](https://doi.org/10.48550/arXiv.2512.15298)

`q2 · i?` · `qualitative · r2`

Qualitative case analysis from Experiment 3 error review (GPT-4o, Question 3, detailed in Table 8). The article describes this as "the deceptive nature of AI attempting to evade difficult reasoning and generate plausible answers"; Process Hallucination was observed in both Gemini 2.5 Flash (2 cases) and GPT-4o (2 cases).

> "This question required “visual verification” of a P -T diagram, but GPT -4o “Skipped” this core reasoning process. Instead, it activated related background knowledge of “decompression melting” in the context of “mantle rising” and hastily  applied it without data verification to justify its conclusion."

## Discussion


## Related Claims
- [LLM error profiles differ by model: GPT-4o shows frequent hallucination, Gemini 2.5 Flash systematic visual-interpretation errors, Gemini 2.5 Pro balanced but reasoning-limited performance](model-specific-llm-error-profiles-csat.md) — related
- [Hallucination — the generation of inaccurate, unverified, or illogical content — is the most frequently reported technical challenge for LLMs in dental education](hallucination-most-frequent-technical-challenge.md) — a broader claim this one bears on
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related

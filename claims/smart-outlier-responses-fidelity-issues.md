---
type: claim
title: SMART occasionally generates outlier responses with fidelity issues that are inaccurately scored and hurt difficulty prediction
description: SMART occasionally generates outlier responses with fidelity issues that are inaccurately scored and hurt difficulty prediction
id: smart-outlier-responses-fidelity-issues
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: alexander-scarlatos-2025
    resource: "https://doi.org/10.18653/v1/2025.emnlp-main.1274"
    title: "Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. [doi:10.18653/v1/2025.emnlp-main.1274](https://doi.org/10.18653/v1/2025.emnlp-main.1274)"
    author: Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SMART occasionally generates outlier responses with fidelity issues that are inaccurately scored and hurt difficulty prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Outlier failure patterns include repeating the passage, irrelevant responses, and highly repetitive responses. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Nigel Fernandez, Christopher Ormerod, Susan Lottridge, Andrew Lan. (2025). SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction. [doi:10.18653/v1/2025.emnlp-main.1274](https://doi.org/10.18653/v1/2025.emnlp-main.1274)

`q2 · i?` · `design · r2`

In the qualitative failure analysis, the authors observe that these outlier responses are often inaccurately scored by the scoring model, affecting downstream item difficulty prediction. No effect sizes are printed.

> "SMART occasionally generates outlier responses with fidelity issues, with failure patterns including 1) repeating the passage, 2) not being relevant to the item, and 3) being highly repetitive."

## Discussion


## Related Claims
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — a broader claim this one bears on
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [Hallucination — the generation of inaccurate, unverified, or illogical content — is the most frequently reported technical challenge for LLMs in dental education](hallucination-most-frequent-technical-challenge.md) — a broader claim this one bears on
- [Learner-level challenges of ChatGPT in STEAM IBL include over-reliance, inaccurate or irrelevant feedback, conceptual confusion, and diminished creativity](chatgpt-steam-ibl-learner-challenges.md) — a broader claim this one bears on
- [Recurring risks of GenAI in STEAM education include hallucination, bias, superficial completion strategies, and compromised assessment validity](genai-steam-risks-hallucination-bias.md) — a broader claim this one bears on
- [LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs](llm-hallucination-rate-education.md) — a broader claim this one bears on
- [A VLM-based screenplay-to-video fidelity proxy shows scene and element structure are usually preserved while action-level fidelity is the primary failure mode](anvil-video-fidelity-proxy-action-failure.md) — related
- [Interesting but irrelevant details can impair comprehension and transfer, with effects that vary with the material and the learner](seductive-details-effect.md) — related

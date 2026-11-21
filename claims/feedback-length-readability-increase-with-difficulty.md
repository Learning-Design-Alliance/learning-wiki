---
type: claim
title: AI-generated feedback length and readability increase with question difficulty
description: AI-generated feedback length and readability increase with question difficulty
id: feedback-length-readability-increase-with-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: antoun-yaacoub-2025
    resource: "https://doi.org/10.1109/iccsm66818.2025.00026"
    title: "Antoun Yaacoub, Zainab Assaghir, Lionel Prevost, Jérôme Da-Rugna. (2025). Analyzing Feedback Mechanisms in AI-Generated MCQs: Insights into Readability, Lexical Properties, and Levels of Challenge. ESIEA Lab / Lebanese University. [doi:10.1109/iccsm66818.2025.00026](https://doi.org/10.1109/iccsm66818.2025.00026)"
    author: Antoun Yaacoub, Zainab Assaghir, Lionel Prevost, Jérôme Da-Rugna
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# AI-generated feedback length and readability increase with question difficulty

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Feedback length rises from easy (15.8 characters) to medium (18.5) to hard (20.5), with Flesch-Kincaid readability rising from 10.0 to 12.4 across difficulty levels. [→ Antoun Yaacoub 2025](#antoun-yaacoub-2025)

## Evidence

### Antoun Yaacoub 2025

Antoun Yaacoub, Zainab Assaghir, Lionel Prevost, Jérôme Da-Rugna. (2025). Analyzing Feedback Mechanisms in AI-Generated MCQs: Insights into Readability, Lexical Properties, and Levels of Challenge. ESIEA Lab / Lebanese University. [doi:10.1109/iccsm66818.2025.00026](https://doi.org/10.1109/iccsm66818.2025.00026)

`q2 · i?` · `associational · r2`

Descriptive analysis of 1,236 Gemini 1.5-flash-generated MCQ feedback fields across easy, medium, and hard difficulty. Mean length increased from 15.8 to 18.5 to 20.5 characters and Flesch-Kincaid from 10.0 to 12.4; the article calls the increase "significantly" but prints no test statistic for this contrast.

> "As hypothesized, both feedback length and readability (Flesch-Kincaid) increase significantly with question difficulty. This indicates that the AI model adapts its language complexity to match the cognitive demands of the question."

## Discussion


## Related Claims
- [Challenging feedback is easier to read than other tones for easy questions but converges with them at hard difficulty](challenging-tone-readability-interaction.md) — a narrower finding that bears on this claim
- [LLM difficulty labels track structural question features: stem length, option length, and digits in stems rise monotonically across Easy, Medium, and Hard labels](llm-difficulty-labels-track-structural-item-features.md) — related
- [A fine-tuned RoBERTa multi-task model predicts feedback linguistic metrics with low test MAEs](roberta-mtl-predicts-feedback-linguistic-metrics.md) — related
- [The three fine-tuned LLMs differ significantly in response length, readability, and similarity to posts](llm-response-length-readability-differences.md) — related
- [Feedback tone and question difficulty interact significantly on all examined linguistic metrics](tone-difficulty-interaction-linguistic-metrics.md) — related

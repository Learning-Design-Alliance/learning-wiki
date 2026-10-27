---
type: claim
title: LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select
description: LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select
id: llm-distractor-prediction-asymmetry
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: eamon-worden-2026
    resource: "https://doi.org/10.48550/arxiv.2602.00070"
    title: "Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)"
    author: Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs predict common distractors above chance but fall 15 percentage points below chance at predicting which errors students rarely select

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models achieve 47.9% accuracy identifying which wrong answer students choose most often, exceeding the 35.8% random baseline, but fall 15 percentage points below chance predicting least-selected distractors. [→ Eamon Worden 2026](#eamon-worden-2026)

## Evidence

### Eamon Worden 2026

Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)

`q2 · i?` · `design · r2`

Zero-shot evaluation on most- and least-common distractor prediction tasks over 236 multiple-choice problems with at least 10 responses. The article reports the asymmetry quoted above and concludes LLMs "have learned to recognize some common misconceptions but cannot distinguish likely from unlikely distractors".

> "models achieve 47.9% accuracy at identifying which wrong answer students choose most often, exceeding the 35.8% random baseline, but fall 15 percentage pointsbelowchance when predicting which errors students rarely select."

## Discussion

## Related Claims

- [AI-generated assessment items frequently need faculty correction, supporting AI as a draft generator within quality assurance](genai-assessment-items-draft-generator-quality-assurance.md) — the general claim this finding bears on, with the studies behind it
- [Cognitive modeling of exact student responses is hardest for multi-select problems and rare-error answers, with select-all accuracy of only 12-15% and cognitive accuracy dropping to as low as 3.7% when answers are incorrect](cognitive-modeling-by-problem-type.md) — related
- [LLMs perform competently at comparing item difficulty but fall below random chance on comparing item discrimination](llms-below-chance-item-discrimination.md) — related
- [LLM error simulation rarely fails, but the model is less likely to reproduce a targeted distractor on problems with longer correct solutions](error-simulation-accurate-but-longer-solutions-harder.md) — related
- [On the misconception-annotated math dataset, LLMs predominantly follow a solve-first, error-injection process aligned with misconception-based distractor design](llms-solve-first-error-injection-edi.md) — related
- [LLMs show discoverability bias: they accurately identify only high-quality open-ended biology responses and miss nuanced misconceptions](llm-discoverability-bias-open-ended-biology-assessment.md) — related

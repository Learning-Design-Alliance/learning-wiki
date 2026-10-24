---
type: claim
title: "Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability."
description: "Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability."
id: expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: alexander-scarlatos-2024
    resource: "https://doi.org/10.48550/arxiv.2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490 [doi:10.48550/arxiv.2409.16490](https://doi.org/10.48550/arxiv.2409.16490)"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alexander-scarlatos-2024-2
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Three former math teachers rating 166 turn pairs from 30 CoMTA dialogues gave GPT-4o very high scores for correctness and moderate-to-high scores for KCs. [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q2 i?` Inter-rater reliability was volatile: high overlap and low alpha on correctness, low overlap but moderate alpha on KCs. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490 [doi:10.48550/arxiv.2409.16490](https://doi.org/10.48550/arxiv.2409.16490)

`q2 · i?` · `design · r2`

IRB-approved human evaluation in which 3 former math teachers scored GPT-4o's labels on 30 randomly selected CoMTA dialogues (166 turn pairs). Annotators "give GPT-4o very high scores for correctness and moderate-to-high scores for KCs"; Table 4 reports 0.9317 / 1 and 3.2831 / 4.

> "We see that our annotators give GPT-4o very high scores for correctness and moderate-to-high scores for KCs, indicating that GPT-4o is able to competently perform these tasks."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

`q2 · i?` · `design · r2`

Inter-rater reliability from the same human evaluation, using exact overlap and Krippendorff's alpha: "IRR is volatile, with high overlap and lowα on correctness, and low overlap but moderateα on KCs".

> "IRR is volatile, with high overlap and lowα on correctness, and low overlap but moderateα on KCs."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can an LLM label the turns of a tutoring dialogue (correctness, knowledge components) about as well as human experts?* This table gathers the studies behind this claim and the 3 narrower claims that bear on it: **2 distinct studies** (2 design), `q1`–`q2`, 0 of 2 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Alexander Scarlatos 2024](https://doi.org/10.48550/arxiv.2409.16490) | q1 / q2 · design · r2 | i? | this claim; [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expe](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) (supports); [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calcul](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) (qualifies) |
| [Menggian Wu 2026](https://doi.org/10.48550/arxiv.2607.00211) | q2 · design · r2 | i? | [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation](regex-rules-improve-fewshot-llm-labeling-accuracy.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Gpt 4O Final Turn Correctness Labeling Is Close To Human Level](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md)
- [In one community-college lab class, six scorers rating six teams with an engineering rubric differed by a mean of 1.2 of 9 points, which the authors read as a sign the rubric may not be reliable](engineering-rubric-low-scoring-reliability.md) — related
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related
- [Three independent expert instructors reached exceptionally high inter-rater reliability when grading 1200 bash exam responses, establishing a reliable human reference standard](expert-triad-high-inter-rater-reliability-bash-grading.md) — related
- [GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)](llm-communication-grading-insufficient-alignment-ttx.md) — related
- [Making trustworthiness metrics and visualizations explicit increased inter-rater reliability among learning engineers evaluating LLM responses](trustworthiness-metrics-visualizations-increase-expert-agreement.md) — related
- [LLM-generated 7C collaboration assessment scores fall within the range of human expert variability across ten discussions](llm-7c-scores-within-expert-variability.md) — related
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) — related
- [GPT-4o-mini natural language feedback was overwhelmingly helpful and never harmful in quality annotation](nl-feedback-quality-92-percent-helpful.md) — related
- [State-of-the-art conversational agents (Blender and GPT-3) replied adequately to students but were well behind human performance in helping the student (reported from a dialogue study)](conversational-agents-behind-human-helping-students.md) — related

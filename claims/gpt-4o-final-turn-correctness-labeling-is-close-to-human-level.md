---
type: claim
title: "GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task."
description: "GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task."
id: gpt-4o-final-turn-correctness-labeling-is-close-to-human-level
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: weak
newest_evidence: 2024
source_checked: 2026-10-27
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
---

# GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · checked against its sources 2026-10-27 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The average human annotator's final turn correctness accuracy is only slightly higher than GPT-4o's, so GPT-4o achieves close to human-level performance on a challenging labeling task. [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490 [doi:10.48550/arxiv.2409.16490](https://doi.org/10.48550/arxiv.2409.16490)

`q2 · i?` · `design · r2`

Final-turn accuracy against CoMTA's ground-truth labels in the human evaluation: human accuracy is "only slightly higher than GPT-4o’s" (Table 4 reports 75.82 for GPT-4o on the full dataset, 83.33 on the evaluation subset, and 85.56 for humans).

> "Finally, given that the average human annotator’s final turn correctness accuracy is only slightly higher than GPT-4o’s, we can conclude that the correctness labeling task is a challenging one where GPT-4o achieves close to human-level performance."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can a large language model label whether students' responses are correct, and which skills they show, accurately enough to stand in for human annotators?* This table gathers the studies behind this claim and the 4 narrower claims that bear on it: **3 distinct studies** (3 design), `q1`–`q2`, 0 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Alexander Scarlatos 2024](https://doi.org/10.48550/arxiv.2409.16490) | q1 / q2 · design · r2 | i? | this claim; [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student co](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) (supports); [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calcul](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) (qualifies) |
| [Li Lucy 2026](https://doi.org/10.48550/arxiv.2603.00925) | q2 · design · r2 | i? | [Some VLMs perform near chance on binary judgments of student correctness, and error-assess](binary-correctness-judgments-near-chance.md) (counts against) |
| [Yoonsu Kim 2026](https://doi.org/10.48550/arxiv.2504.00843) | q2 · design · r2 | i? | [LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-at](applying-vs-knowing-skill-diagnosis-gap.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Expert Teachers Rate Gpt 4O Dialogue Annotations As Largely Accurate](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md)
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
- [GPT-4o-mini natural language feedback was overwhelmingly helpful and never harmful in quality annotation](nl-feedback-quality-92-percent-helpful.md) — related
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — related
- [A GPT-4 few-shot binary classifier effectively identifies correct/incorrect trainee responses across three tutor-training lessons, with average F1 of 0.84 and AUC of 0.85](gpt4-few-shot-classifies-trainee-responses.md) — related

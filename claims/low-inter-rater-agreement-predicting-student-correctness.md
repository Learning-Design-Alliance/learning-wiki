---
type: claim
title: "Human annotators agree poorly on which tutor utterance will elicit correct student responses (Kendall's τ = 0.06), while agreement on pedagogical rubric scoring is higher"
description: "Human annotators agree poorly on which tutor utterance will elicit correct student responses (Kendall's τ = 0.06), while agreement on pedagogical rubric scoring is higher"
id: low-inter-rater-agreement-predicting-student-correctness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: alexander-scarlatos-2025
    resource: "https://doi.org/10.1007/978-3-031-98414-3_18"
    title: "Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)"
    author: Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alexander-scarlatos-2025-2
    resource: "https://doi.org/10.1007/978-3-031-98414-3_18"
    title: "Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)"
    author: Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human annotators agree poorly on which tutor utterance will elicit correct student responses (Kendall's τ = 0.06), while agreement on pedagogical rubric scoring is higher

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For correctness ranks, Kendall's τ is only 0.06 between the two annotators and averages 0.08 between LLMKT and both annotators. [→ Alexander Scarlatos 2025](#alexander-scarlatos-2025)
`q2 i?` For rubric scores, Pearson's ρ is 0.15 between the two annotators and averages 0.27 between GPT-4o and both annotators, the latter being statistically significant. [→ Alexander Scarlatos 2025 (2)](#alexander-scarlatos-2025-2)

## Evidence

### Alexander Scarlatos 2025

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q2 · i?` · `design · r2`

Inter-rater analysis of the same 50-instance human evaluation: the study reports very low rank agreement on predicting student correctness, with many near-ties in LLMKT output probabilities.

> "For correctness ranks, Kendall’s τ is only 0.06 between the two annotators and averages 0.08 between LLMKT and both annotators."

### Alexander Scarlatos 2025 (2)

Alexander Scarlatos, Naiming Liu, Jaewook Lee, Richard Baraniuk, Andrew Lan. (2025). Training LLM-based Tutors to Improve Student Learning Outcomes in Dialogues. AIED 2025. [doi:10.1007/978-3-031-98414-3_18](https://doi.org/10.1007/978-3-031-98414-3_18)

`q2 · i?` · `design · r2`

The same analysis finds higher agreement on pedagogical rubric scoring; the authors conclude evaluating pedagogical principles is easier than predicting student correctness, though still subjective.

> "For rubric scores, the inter-rater agreement is notably higher: Pearson’s ρ is 0.15 between the two annotators and averages 0.27 between GPT-4o and both annotators, the latter being statistically significant."

## Discussion


## Related Claims
- [DPO training significantly increases the likelihood of correct next-turn student responses predicted by LLMKT, outperforming prompting, SFT, distillation, GPT-4o and human tutor utterances on the MathDial test set](dpo-tutor-training-raises-predicted-student-correctness.md) — related
- [In a human evaluation, the DPO-trained tutor outperforms both human tutors and GPT-4o on perceived student correctness and rubric score, with statistically significant differences](human-evaluation-dpo-beats-human-tutors-and-gpt4o.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — related
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) — related

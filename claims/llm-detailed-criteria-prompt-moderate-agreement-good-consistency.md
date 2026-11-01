---
type: claim
title: Prompting ChatGPT 3.5 with detailed IELTS band descriptors achieves moderate interrater agreement and good interrater consistency with official examiner grades
description: Prompting ChatGPT 3.5 with detailed IELTS band descriptors achieves moderate interrater agreement and good interrater consistency with official examiner grades
id: llm-detailed-criteria-prompt-moderate-agreement-good-consistency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: da-wei-zhang-2024
    resource: "https://doi.org/10.1038/s41539-024-00291-1"
    title: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1"
    author: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompting ChatGPT 3.5 with detailed IELTS band descriptors achieves moderate interrater agreement and good interrater consistency with official examiner grades

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Only the prompt including comprehensive band descriptors (Prompt 3) showed significant interrater agreement with official IELTS grades, at a moderate level (ICC 0.61), and good interrater consistency (ICC 0.77). [→ Da-Wei Zhang 2024](#da-wei-zhang-2024)

## Evidence

### Da-Wei Zhang 2024

Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1

`q2 · i?` · `design · r2`

Quantitative ICC analysis of 31 IELTS essays graded by ChatGPT 3.5 under three incremental prompts versus official examiner ratings; Table 1 reports Prompt 3 interrater agreement of 0.61 [0.02, 0.85] and consistency of 0.77 [0.57, 0.88]. The article reports "Only prompt 3 showed signiﬁcant interrater agreement but at a moderate level."

> "Only prompt 3 showed signiﬁcant interrater agreement but at a moderate level. Regarding int errater consistency, all prompts showed signiﬁcance, but again, it was Prompt 3 that achieved a good level."

## Discussion


## Related Claims
- [More advanced LLMs (ChatGPT 4.0, Claude 3.0 Haiku) did not improve criterion-based grading over ChatGPT 3.5 with the same prompt](advanced-llms-no-grading-improvement.md) — related
- [A teacher without IELTS-specific training showed poorer grading consistency than the best LLM prompt condition](teacher-grading-poorer-consistency-than-llm.md) — related
- [ChatGPT 3.5 grading with the best prompt was significantly lower than official IELTS examiner grades, indicating systematic bias in absolute grading](llm-grades-significantly-lower-than-examiners.md) — related
- [The best prompt showed excellent test-retest reliability (intrarater consistency ICC = 0.89) when rerun in ChatGPT 3.5](llm-grading-excellent-intrarater-consistency.md) — related
- [Prompting type shows no significant effect on rated text quality (transfer, validity of conclusions, integration), with low interrater reliability for two criteria](prompting-no-effect-rated-text-quality.md) — related
- [Most variables of the START-Play fidelity measure show good to excellent interrater reliability, with ICCs ranging from 0.77 to 0.95](start-play-fidelity-icc-077-095.md) — related

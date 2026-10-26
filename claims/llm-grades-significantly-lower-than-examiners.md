---
type: claim
title: ChatGPT 3.5 grading with the best prompt was significantly lower than official IELTS examiner grades, indicating systematic bias in absolute grading
description: ChatGPT 3.5 grading with the best prompt was significantly lower than official IELTS examiner grades, indicating systematic bias in absolute grading
id: llm-grades-significantly-lower-than-examiners
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: da-wei-zhang-2024
    resource: "https://doi.org/10.1038/s41539-024-00291-1"
    title: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1"
    author: "Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia"
    q: 2
    i: 2
    kind: causal
    rigour: 1
---

# ChatGPT 3.5 grading with the best prompt was significantly lower than official IELTS examiner grades, indicating systematic bias in absolute grading

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i2` medium
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i2` Prompt 3 grades were significantly lower than IELTS examiners' grades (t(60) = −2.81, p < 0.01, Cohen's d = 0.71), with biases evenly distributed across essay levels. [→ Da-Wei Zhang 2024](#da-wei-zhang-2024)

## Evidence

### Da-Wei Zhang 2024

Da-Wei Zhang, Melissa Boey, Yan Yu Tan & Alexis Hoh Sheng Jia. (2024). Evaluating large language models for criterion-based grading from agreement to consistency. npj Science of Learning 9:79. https://doi.org/10.1038/s41539-024-00291-1

`q2 · i2` · `causal · r1`

Bland-Altman and t-test analysis comparing Prompt 3 ChatGPT 3.5 grades with official examiner grades on the 31 IELTS essays; the article reports "the grading of Prompt 3 was signiﬁcantly lower than that of IELTS examiners" with d = 0.71, and the Bland-Altman plot showed biases evenly distributed across essay levels.

> "However, the grading of Prompt 3 was signiﬁcantly lower than that of IELTS examiners, t(60) = −2.81, p < 0.01, Cohen’s d = 0.71."

## Discussion


## Related Claims
- [Prompting ChatGPT 3.5 with detailed IELTS band descriptors achieves moderate interrater agreement and good interrater consistency with official examiner grades](llm-detailed-criteria-prompt-moderate-agreement-good-consistency.md) — related
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — a broader claim this one bears on
- [A teacher without IELTS-specific training showed poorer grading consistency than the best LLM prompt condition](teacher-grading-poorer-consistency-than-llm.md) — related
- [LLM agreement with human examiners is limited in fast mode and improves in reasoning or thinking modes](llm-fast-mode-limited-thinking-mode-better-agreement.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — a broader claim this one bears on

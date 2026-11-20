---
type: claim
title: "The GPT-4 tutor made errors in fewer than 1% of homework questions"
description: "The GPT-4 tutor made errors in fewer than 1% of homework questions"
id: gpt4-tutor-low-error-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: alessandro-vanzo-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-long.1502"
    title: "Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan. (2025). GPT-4 as a Homework Tutor can Improve Student Engagement and Learning Outcomes. Arxiv Preprint. Originally published 2024. [doi:10.18653/v1/2025.acl-long.1502](https://doi.org/10.18653/v1/2025.acl-long.1502)"
    author: Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The GPT-4 tutor made errors in fewer than 1% of homework questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The tutor made no more than 14 errors over 1549 questions, a hallucination rate below 1%. [→ Alessandro Vanzo 2025](#alessandro-vanzo-2025)

## Evidence

### Alessandro Vanzo 2025

Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan. (2025). GPT-4 as a Homework Tutor can Improve Student Engagement and Learning Outcomes. Arxiv Preprint. Originally published 2024. [doi:10.18653/v1/2025.acl-long.1502](https://doi.org/10.18653/v1/2025.acl-long.1502)

`q2 · i?` · `causal · r2`

Error audit combining weekly student error reports (16 of 160 indicated a problem) with the authors' review of all conversations from flagged weeks; four errors found in conversation review.

> "Overall, this means that the tutor made no more than 14 errors over 1549 questions (and never doubled down on its errors) giving a hallucination rate of less than 1% which is well within acceptable thresholds."

## Discussion


## Related Claims
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related
- [GPT-4 tends to assume feedback is correct when it sounds convincing but incorrectly identifies the student error or provides an invalid suggestion, and has a high false positive rate on the diagnostic label.](gpt4-feedback-evaluation-shortcomings.md) — related

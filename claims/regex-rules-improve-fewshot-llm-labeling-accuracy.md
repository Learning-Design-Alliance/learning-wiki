---
type: claim
title: Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)
description: Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)
id: regex-rules-improve-fewshot-llm-labeling-accuracy
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: menggian-wu-2026
    resource: "https://arxiv.org/abs/2607.00211"
    title: "Menggian Wu. (2026). Constructing Epistemic AI Literacy: Detecting Epistemic Aims and Processes in Student-AI Co-Programming. 2nd International Workshop on AI Literacy Education For All (ALIT4ALL 2026), co-located with AIED 2026, Seoul, Republic of Korea. https://arxiv.org/abs/2607.00211"
    author: Menggian Wu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Few-shot GPT-4o labeling evaluated against a 499-turn human-labeled gold set rose from 0.818 to 0.852 overall accuracy when regex-based rules were included in the prompts. [→ Menggian Wu 2026](#menggian-wu-2026)
`q2 i?` The largest dimension gain was Mastery-oriented aims (0.709 to 0.835, +0.126), while Verification-seeking showed a small decrease (0.834 to 0.829). [→ Menggian Wu 2026](#menggian-wu-2026)

## Evidence

### Menggian Wu 2026

Menggian Wu. (2026). Constructing Epistemic AI Literacy: Detecting Epistemic Aims and Processes in Student-AI Co-Programming. 2nd International Workshop on AI Literacy Education For All (ALIT4ALL 2026), co-located with AIED 2026, Seoul, Republic of Korea. https://arxiv.org/abs/2607.00211

`q2 · i?` · `design · r2`

Evaluation against the 499-line human-annotated gold set compared two experimental conditions: few-shot prompts with versus without expert-derived regex principles. Overall accuracy improved 0.818 to 0.852, and 'Mastery-oriented_aims (0.709->0.835, +0.126)' showed the largest gain.

> "Without regex-based rules, the LLM achieved an overall accuracy of 0.818 across seven binary dimensions. Adding lightweight regex-based rules improved overall accuracy to 0.852 (+0.035)"

## Discussion


## Related Claims
- [78.8% of student-GenAI turns lack mastery-oriented aims and reliable epistemic strategies](low-epistemic-engagement-788-percent-non-mastery.md) — related
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — related
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) — related
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related

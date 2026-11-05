---
type: claim
title: The consistency gap increases with case complexity, though the 4-question subgroup contained only 7 cases
description: The consistency gap increases with case complexity, though the 4-question subgroup contained only 7 cases
id: case-complexity-increases-consistency-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: cha-j-2026
    resource: "https://doi.org/10.2196/95342"
    title: "Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342"
    author: Cha J, Zhao Y, Zong H.
    q: 3
    i: "?"
    kind: associational
    rigour: 1
---

# The consistency gap increases with case complexity, though the 4-question subgroup contained only 7 cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Across all evaluated LLMs, the consistency gap tended to increase as the number of questions per case increased from 2 to 4. [→ Cha J 2026](#cha-j-2026)
`q3 i?` In 4-question cases, DeepSeek-R1 limited the gap to 28.6% while GPT-4o's gap rose to 57.1%, but this subgroup contained only 7 cases. [→ Cha J 2026](#cha-j-2026)

## Evidence

### Cha J 2026

Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342

`q3 · i?` · `associational · r1`

Subgroup analysis grouping the 189 cases by number of questions (2, 3, or 4). In 2-question cases gaps ranged from 7.9% (DeepSeek-R1 and Qwen2.5-32B) to 10.9% (GPT-4o); for 3-question cases gaps rose to 19.3% (Gemini-2.5-Flash) and 23.5% (GPT-4o).

> "As shown in Figure 3, the consistency gap increased with case complexity across all LLMs. This suggests that longer case sequences may be associated with greater performance degradation when moving from question-level to case-level evaluation."

## Discussion


## Related Claims
- [LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%](llm-consistency-gap-question-vs-case-level.md) — possibly the same claim (merge candidate)
- [DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy](deepseek-qwen32b-outperform-gpt4o-clinical-cases.md) — related
- [The authors argue complex integrative medical questions are particularly useful for evaluating and comparing the reasoning abilities of different LLMs](complex-questions-evaluate-llm-reasoning.md) — a broader claim this one bears on

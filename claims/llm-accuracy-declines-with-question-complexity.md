---
type: claim
title: "LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend"
description: "LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend"
id: llm-accuracy-declines-with-question-complexity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: wang-shuo-2026
    resource: "https://doi.org/10.1186/s12909-026-08704-y"
    title: "Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y"
    author: Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` LLM accuracy rates declined steadily as question complexity increased, from A1 (median 79.4–82.5%) to A2 (74.1–78.3%), A3/A4 (55%), and case-analysis questions (28.6–33.3%). [→ Wang Shuo 2026](#wang-shuo-2026)

## Evidence

### Wang Shuo 2026

Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y

`q3 · i?` · `design · r2`

Difficulty–accuracy analysis (Fig. 5) of the 30-iteration accuracy data across the four question types ordered by complexity; a similar declining trend is reported for trainees from "68.3%" (A1) to 28.6% (case analysis). No effect size is printed.

> "Accuracy rates for LLMs declined steadily as question complexity increased, from A1 (median: 79.4–82.5%) to A2 (median: 74.1–78.3%), A3/A4 (median: 55%), and case-analysis questions (median: 28.6–33.3%)"

## Discussion


## Related Claims
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [All four LLMs award a smaller share of available marks as bash question cognitive complexity increases, with L4 questions receiving the lowest proportions](llm-scores-decline-with-cogtax-level.md) — related
- [Success rates decrease monotonically from easy to medium to hard difficulty levels across all models](monotonic-difficulty-decline-turtleai.md) — a broader claim this one bears on
- [All three LLMs outscored 32 human SRTP trainees on the mock exam overall, though the gap narrowed for the most complex questions](llms-outperform-human-trainees-srtp-mock-exam.md) — related
- [Next-turn recovery from impasses declines steadily as impasse depth increases, with help-seeking impasses declining most sharply](recovery-declines-with-impasse-depth.md) — related
- [Proportions of variance explained follow a curvilinear pattern across the six taxonomy levels](curvilinear-variance-pattern-across-taxonomy-levels.md) — related
- [New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)](cdle-knowledge-vs-case-analysis-question-types.md) — related
- [GPT-4o shows a clear advantage in complex question formats, exceeding 85% accuracy on case analysis (A3/A4) and matching (B1) questions](gpt4o-advantage-complex-question-formats.md) — reports the opposite

---
type: claim
title: All three LLMs outscored 32 human SRTP trainees on the mock exam overall, though the gap narrowed for the most complex questions
description: All three LLMs outscored 32 human SRTP trainees on the mock exam overall, though the gap narrowed for the most complex questions
id: llms-outperform-human-trainees-srtp-mock-exam
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
    kind: associational
    rigour: 2
  - id: wang-shuo-2026-2
    resource: "https://doi.org/10.1186/s12909-026-08704-y"
    title: "Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y"
    author: Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# All three LLMs outscored 32 human SRTP trainees on the mock exam overall, though the gap narrowed for the most complex questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Human trainee scores (426.8 ± 25.9) fell below all three LLMs (all P values < 0.001); 26 of 32 trainees passed the 400-point threshold. [→ Wang Shuo 2026](#wang-shuo-2026)
`q3 i?` On case-analysis questions, LLM full-accuracy rates (median 28.6–33.3%) were comparable to the trainees' 28.6%, except for Gemini which was significantly higher (33.3% vs 28.6%, P = 0.029). [→ Wang Shuo 2026 (2)](#wang-shuo-2026-2)

## Evidence

### Wang Shuo 2026

Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y

`q3 · i?` · `associational · r2`

Comparison of the three LLMs against anonymized scores of 32 human SRTP trainees who took the same mock exam, analyzed with Student's t-test for total scores. Human mean was "426.8 ± 25.9"; all LLM differences significant, no effect size printed.

> "Human scores (426.8 ± 25.9; range: 386.5–477.2) fell below those of all LLMs (all P values < 0.001)"

### Wang Shuo 2026 (2)

Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y

`q3 · i?` · `design · r2`

Question-type accuracy comparison between LLMs and trainees on case-analysis questions (Kruskal–Wallis with Dunn's post-hoc). Only Gemini's "33.3%" full-accuracy rate significantly exceeded the trainees' 28.6%; the other two models did not differ significantly.

> "their full-accuracy rates (median: 28.6–33.3%) were comparable to the trainees' 28.6% (Fig. 4M-O), except for Gemini, which demonstrated a significantly higher full-accuracy rate than the trainees (33.3% [IQR: 28.6–33.3.6.3%] vs. 28.6% [IQR: 19.0–38.1.0.1%], P = 0.029)"

## Discussion


## Related Claims
- [All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score](llms-pass-chinese-anesthesiology-srtp-exam-claude-highest.md) — possibly the same claim (merge candidate)
- [The authors argue complex integrative medical questions are particularly useful for evaluating and comparing the reasoning abilities of different LLMs](complex-questions-evaluate-llm-reasoning.md) — related
- [LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend](llm-accuracy-declines-with-question-complexity.md) — related

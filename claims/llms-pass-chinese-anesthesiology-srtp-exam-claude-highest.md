---
type: claim
title: All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score
description: All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score
id: llms-pass-chinese-anesthesiology-srtp-exam-claude-highest
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

# All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro all consistently exceeded the 400-point passing threshold across 30 iterations, with Claude highest (495.4 ± 9.5), Gemini next (493.8 ± 4.3), and GPT-4o lowest (482.4 ± 10.9). [→ Wang Shuo 2026](#wang-shuo-2026)

## Evidence

### Wang Shuo 2026

Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y

`q3 · i?` · `design · r2`

Repeated-attempt evaluation of three LLMs on a 210-question Chinese mock SRTP exam (30 attempts per model). The Results section reports that all models exceeded the 400/650 threshold, with Claude's mean score of "495.4 ± 9.5" the highest; no effect size is printed.

> "All three LLMs consistently exceeded the passing threshold across 30 iterations. Among them, Claude achieved the highest mean score (495.4 ± 9.5, range: 481.5–515.0), followed closely by Gemini (493.8 ± 4.3, range: 486.3–501.6) and GPT-4o (482.4 ± 10.9, range: 460.5–509.4)"

## Discussion


## Related Claims
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](gemini-highest-response-consistency-repeated-attempts.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [All three LLMs outscored 32 human SRTP trainees on the mock exam overall, though the gap narrowed for the most complex questions](llms-outperform-human-trainees-srtp-mock-exam.md) — possibly the same claim (merge candidate)
- [All four LLMs passed both JNME exams under official scoring, with near-perfect scores in essential sections](llms-pass-jnme-official-scoring.md) — related
- [GPT-4o's accuracy on the CONACEM anesthesiology exam varies significantly by cognitive domain, highest in Understanding (90.10%) and lowest in Application (76.83%) and Analysis (76.54%)](gpt4o-conacem-accuracy-varies-by-cognitive-domain.md) — related
- [LLM performance on KMLE varies by medical specialty, with relatively weak accuracy in medical law for all three models](kmle-specialty-variation-weak-medical-law.md) — related

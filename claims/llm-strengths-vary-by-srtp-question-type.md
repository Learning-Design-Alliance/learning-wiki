---
type: claim
title: "Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis"
description: "Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis"
id: llm-strengths-vary-by-srtp-question-type
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
    rigour: 1
  - id: wang-shuo-2026-2
    resource: "https://doi.org/10.1186/s12909-026-08704-y"
    title: "Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y"
    author: Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao
    q: 3
    i: "?"
    kind: associational
    rigour: 1
---

# Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Gemini achieved the highest A1 median accuracy (82.5%) versus Claude (79.4%, P = 0.012) and GPT-4o (79.4%, P < 0.001), while Claude achieved the highest A2 median accuracy (78.3%) versus Gemini (76.4%, P = 0.002) and GPT-4o (74.1%, P < 0.001). [→ Wang Shuo 2026](#wang-shuo-2026)
`q3 i?` On A3/A4 questions no significant differences among models were observed (all median 55%), while Gemini and GPT-4o showed higher case-analysis accuracy than Claude (both P < 0.05). [→ Wang Shuo 2026](#wang-shuo-2026)
`q3 i?` On the five image-based questions Gemini achieved the highest median accuracy (60.0%) versus Claude (40.0%) and GPT-4o (20.0%), both P < 0.001. [→ Wang Shuo 2026 (2)](#wang-shuo-2026-2)

## Evidence

### Wang Shuo 2026

Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y

`q3 · i?` · `associational · r1`

Results of the 30-iteration accuracy analysis across the 210-question exam, analyzed with Kruskal–Wallis and Dunn's post-hoc tests. A1 contrast names Gemini vs both models; the article separately reports Claude's "78.3%" A2 advantage and the A3/A4 null.

> "Gemini achieved the highest accuracy in A1 questions, with a median accuracy of 82.5% (IQR: 81.0–82.5.0.5%), outperforming both Claude (79.4%, IQR: 79.4–82.1.4.1%, P = 0.012) and GPT-4o (79.4%, IQR: 77.8–79.4.8.4%, P < 0.001)"

### Wang Shuo 2026 (2)

Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y

`q3 · i?` · `associational · r1`

Results for the five image-based questions (3 electrocardiograms, 2 CT scans), Kruskal–Wallis with Dunn's post-hoc test. Gemini's "60.0%" median accuracy exceeded both other models significantly; no effect size printed.

> "For the five image-based questions, Gemini achieved the highest median accuracy (60.0%, IQR: 60.0-60.0.0.0%), followed by Claude (40.0%, IQR: 20.0–40.0.0.0%, P < 0.001) and GPT-4o (20.0%, IQR: 20.0–35.0.0.0%, P < 0.001)"

## Discussion


## Related Claims
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](gemini-highest-response-consistency-repeated-attempts.md) — related
- [Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs](image-based-questions-lower-accuracy.md) — related
- [LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend](llm-accuracy-declines-with-question-complexity.md) — related
- [On recall-type questions, all four LLMs outperformed both residents and fellows, with ChatGPT-5 highest at 92.59%](llms-outperform-trainees-recall-type-questions.md) — related
- [All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score](llms-pass-chinese-anesthesiology-srtp-exam-claude-highest.md) — related
- [New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)](cdle-knowledge-vs-case-analysis-question-types.md) — related

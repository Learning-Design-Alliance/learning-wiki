---
type: claim
title: Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude
description: Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude
id: gemini-highest-response-consistency-repeated-attempts
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
---

# Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Gemini answered 64.3% of questions correctly in all 30 attempts, significantly exceeding GPT-4o (42.7%, P = 0.04) but statistically comparable to Claude (51.2%, P > 0.05). [→ Wang Shuo 2026](#wang-shuo-2026)

## Evidence

### Wang Shuo 2026

Wang Shuo, Chi Xiaohui, Hao Quanshui, Wang Haiting, Tao Hong, Xiao Jing, Wu Cuicui, Deng Jing, Xu Hui, Sun Rao. (2026). Large language models in Chinese anesthesiology residency examinations: a comparative analysis of performance, reliability and clinical reasoning. BMC Medical Education. https://doi.org/10.1186/s12909-026-08704-y

`q3 · i?` · `associational · r1`

Response-consistency analysis over 30 repeated attempts of the same exam per model, compared with Chi-square or Fisher's exact tests with Bonferroni correction. Consistency was measured as the proportion of questions correct in all 30 attempts; no effect size is printed.

> "Gemini demonstrated superior stability, answering 64.3% of questions correctly in all 30 attempts—significantly exceeding GPT-4o (42.7%, P = 0.04) but statistically comparable to Claude (51.2%, P > 0.05)"

## Discussion


## Related Claims
- [All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score](llms-pass-chinese-anesthesiology-srtp-exam-claude-highest.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o](claude-copilot-gemini-topic-strengths-reliability.md) — reports the opposite
- [GPT-4o answers were highly consistent across attempts, whereas GPT-3.5's answers a year earlier were mostly unreliable](gpt-4o-answer-consistency-versus-gpt-3-5.md) — related
- [GPT-4o's accuracy on the CONACEM anesthesiology exam varies significantly by cognitive domain, highest in Understanding (90.10%) and lowest in Application (76.83%) and Analysis (76.54%)](gpt4o-conacem-accuracy-varies-by-cognitive-domain.md) — related
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
- [Only 29.5% of questions were answered correctly by all four current LLMs across all attempts](only-29-5-percent-answered-correctly-by-all-llms.md) — related
- [Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23](temperature-effect-negligible-gpt4o-accuracy.md) — related
- [Chatbot responses show near-perfect repeatability across no-feedback attempts (κ 0.967-1.000)](chatbot-response-consistency-kappa-near-perfect.md) — related

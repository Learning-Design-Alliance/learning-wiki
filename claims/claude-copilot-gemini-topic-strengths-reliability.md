---
type: claim
title: Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o
description: Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o
id: claude-copilot-gemini-topic-strengths-reliability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bolgova-olena-2025
    resource: "https://doi.org/10.1038/s41598-025-22437-w"
    title: "Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w"
    author: Bolgova Olena, Mavrych Volodymyr
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: bolgova-olena-2025-2
    resource: "https://doi.org/10.1038/s41598-025-22437-w"
    title: "Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w"
    author: Bolgova Olena, Mavrych Volodymyr
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: bolgova-olena-2025-3
    resource: "https://doi.org/10.1038/s41598-025-22437-w"
    title: "Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w"
    author: Bolgova Olena, Mavrych Volodymyr
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Claude answered 76.7 ± 5.7% correct, best in Lower limb and Pelvis (80.7%–86.7%) and worst in Upper limb and Abdomen (69.3%–72%), with relatively good consistency. [→ Bolgova Olena 2025](#bolgova-olena-2025)
`q2 i?` Copilot showed the most variable performance (SD 11.9%), best in Abdomen and Back (87.3%–89.3%) and lowest in Pelvis and Thorax (56%–64.8%), limited to prompts of up to 4000 characters. [→ Bolgova Olena 2025 (2)](#bolgova-olena-2025-2)
`q2 i?` Gemini finished last with 63.7 ± 6.5%, best in Pelvis and Head & Neck (71.3%–72.6%) and lowest in Upper Limb (56%), with only moderate answer consistency. [→ Bolgova Olena 2025 (3)](#bolgova-olena-2025-3)

## Evidence

### Bolgova Olena 2025

Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w

`q2 · i?` · `design · r2`

Item analysis of Claude 3.5 Sonnet across three attempts on the same questionnaire; the article reports relatively good consistency (correct-answer coincidence 71.7%–73.5%).

> "The item analysis suggested that Claude correctly answered 80.7% − 86.7% of questions from Lower limb topics and Pelvis, and the worst two topics were Upper limb and Abdomen, 69.3% − 72%."

### Bolgova Olena 2025 (2)

Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w

`q2 · i?` · `associational · r2`

Benchmark results for Copilot; the article attributes its high standard deviation (11.9%) to variability and low reliability, and notes its 4000-character prompt limit allowed only 15–25 MCQs at a time.

> "Copilot generated 73.9 ± 11.9% accurate answers for 325 MCQs from the Gross Anatomy course, showing the third-best result. It is 19% (p < 0.001) below GPT-4o but only 2.8% less than Claude’s results."

### Bolgova Olena 2025 (3)

Bolgova Olena, Mavrych Volodymyr (2025). Evolution of AI in anatomy education study based on comparison of current large language models against historical ChatGPT performance. Scientific Reports. https://doi.org/10.1038/s41598-025-22437-w

`q2 · i?` · `design · r2`

Benchmark results for Gemini 1.5 Flash across three attempts; answer coincidence with previous attempts was 62.8%–85.2% with correct-answer coincidence 50.8%–55.4%.

> "Among current LLMs, Gemini finished last with 63.7.5 ± 6.5% correct answers to the same set of questions. This result was 28.5% below GPT-4o’s performance but 19.3% above GPT-3.5’s performance; both differences were statistically significant (p < 0.001)."

## Discussion


## Related Claims
- [GPT-4o showed the highest accuracy (92.9%) on anatomy MCQs, followed by Claude, Copilot, and Gemini](gpt-4o-highest-anatomy-mcq-accuracy.md) — related
- [Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies](llm-company-comparison-biomedical-mcq-accuracy.md) — related
- [Current LLMs answer USMLE-style anatomy MCQs with an average accuracy of 76.8%, far above GPT-3.5's 44.4% a year earlier and above random guessing](current-llms-anatomy-mcq-76-8-percent-accuracy.md) — a broader claim this one bears on
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](gemini-highest-response-consistency-repeated-attempts.md) — reports the opposite
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [Only 29.5% of questions were answered correctly by all four current LLMs across all attempts](only-29-5-percent-answered-correctly-by-all-llms.md) — related
- [Correct-answer totals shifted in opposite directions over one month: CoPilot Pro and Gemini Advanced increased while both ChatGPT versions decreased](opposite-accuracy-shifts-over-one-month.md) — related
- [LLM performance on KMLE varies by medical specialty, with relatively weak accuracy in medical law for all three models](kmle-specialty-variation-weak-medical-law.md) — related
- [GPT-4o answers were highly consistent across attempts, whereas GPT-3.5's answers a year earlier were mostly unreliable](gpt-4o-answer-consistency-versus-gpt-3-5.md) — related
- [LLM performance on anatomy MCQs varies significantly across anatomical topics, with Head & Neck and Abdomen highest and Upper Limb lowest](llm-anatomy-topic-performance-variation.md) — related
- [ChatGPT-4o showed higher consistency in correct answer rates than students, with a narrow interquartile range versus wide variability among third-year students](chatgpt-4o-consistency-narrow-iqr-endodontic-accuracy.md) — related
- [Chatbot answers were largely stable across 5 successive attempts, with all chatbots answering 104 (52%) of the 200 questions correctly in every attempt](chatbot-answer-stability-across-five-attempts.md) — related
- [The four LLMs' accuracy varied across medical subject categories, with weaknesses in interdisciplinary questions, behavioral health, hematolymphoid topics, neurology and medical ethics](llm-accuracy-varies-by-medical-subject-category.md) — related

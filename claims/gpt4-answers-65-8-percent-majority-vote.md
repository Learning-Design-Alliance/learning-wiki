---
type: claim
title: "GPT-4 answers 65.8% of university assessment questions correctly by majority vote and can produce correct answers for 85.1% of questions with at least one prompting strategy"
description: "GPT-4 answers 65.8% of university assessment questions correctly by majority vote and can produce correct answers for 85.1% of questions with at least one prompting strategy"
id: gpt4-answers-65-8-percent-majority-vote
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: borges-2024
    resource: "https://doi.org/10.1073/pnas.2414955121"
    title: "Borges, et al. (2024). Could ChatGPT get an Engineering Degree? Evaluating Higher Education Vulnerability to AI Assistants. [doi:10.1073/pnas.2414955121](https://doi.org/10.1073/pnas.2414955121)"
    author: Borges, et al
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 answers 65.8% of university assessment questions correctly by majority vote and can produce correct answers for 85.1% of questions with at least one prompting strategy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using majority vote over eight prompting strategies, GPT-4 answers an average of 65.8% of questions correctly (GPT-3.5: 52.2%), and at least one strategy produces a correct answer for 85.1% of questions. [→ Borges 2024](#borges-2024)

## Evidence

### Borges 2024

Borges, et al. (2024). Could ChatGPT get an Engineering Degree? Evaluating Higher Education Vulnerability to AI Assistants. [doi:10.1073/pnas.2414955121](https://doi.org/10.1073/pnas.2414955121)

`q2 · i?` · `design · r2`

Evaluation of GPT-4 and GPT-3.5 on the 5,579-question bank using eight prompting strategies aggregated by majority vote, a zero-knowledge setting. The article reports "a correct answer to 65.8% (on average) of questions using GPT-4" and notes the trend holds in both English and French. No effect size is printed.

> "they would receive a correct answer to 65.8% (on average) of questions using GPT-4 (and 52.2% using GPT-3.5). We observe that this performance trend holds regardless of the language of the assessment, with English exhibiting slightly better results than French."

## Discussion


## Related Claims
- [LLM version progression explains about half of the variance in biomedical MCQ accuracy, with GPT‐4o_o1 over six times as likely as GPT‐3/3.5 to answer correctly](llm-version-meta-regression-explains-accuracy-variance.md) — a broader claim this one bears on
- [Bootstrapped self-consistency at temperature 1.0 flags potentially incorrect GPT-4 answers: about half of inconsistent responses were incorrect versus about 5% of consistent ones](bootstrapping-self-consistency-flags-incorrect-answers.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [ChatGPT-4 achieves passing-level accuracy on 300 ABFM-type practice questions, with correct response rates of 88.67% (Custom Robot) and 87.33% (Regular)](chatgpt4-passing-accuracy-abfm-practice-questions.md) — related
- [ChatGPT-4o mini achieved 65% (48/74) accuracy on the 2023 Portuguese PNA medical examination, surpassing ChatGPT-3.5 Turbo's 54% (40/74)](chatgpt-4o-mini-65-percent-pna-surpasses-35-turbo.md) — related
- [Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o](claude-copilot-gemini-topic-strengths-reliability.md) — related
- [GPT-4o and GPT-4-turbo demonstrate proficiency autograding open responses for low-stakes assessment, with poor GPT-4-turbo performance on some lessons](gpt-llm-autograding-proficiency-low-stakes.md) — related

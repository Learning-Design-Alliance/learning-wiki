---
type: claim
title: GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models
description: GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models
id: gpt-models-outperform-smaller-llms-on-ivda-mcqs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: markos-stamatakis-2026
    resource: "https://doi.org/10.48550/arxiv.2606.15919"
    title: "Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919 [doi:10.48550/arxiv.2606.15919](https://doi.org/10.48550/arxiv.2606.15919)"
    author: Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 12 prompt variants on 70 IVDA MCQs, GPT models reach higher accuracy and fully-correct rates (GPT-5.2 average 91.2% accuracy, 71.3% fully correct) than Mistral-7B (69.2%, 26.0%) and DeepSeek-R1 (75.2%, 38.1%). [→ Markos Stamatakis 2026](#markos-stamatakis-2026)

## Evidence

### Markos Stamatakis 2026

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919 [doi:10.48550/arxiv.2606.15919](https://doi.org/10.48550/arxiv.2606.15919)

`q2 · i?` · `causal · r2`

Benchmark evaluation of four chatbots on 70 IVDA MCQs across 12 prompt variants (Table 1). The article reports that "the GPT models achieve higher accuracy and more fully correct responses", with GPT-5.2 outperforming GPT-4o; smaller models select incorrect options for most questions. No effect size is printed.

> "In contrast, the GPT models achieve higher accuracy and more fully correct responses, likely due to their larger scale and training."

## Discussion


## Related Claims
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [Descriptive user-study patterns that the authors read as GPT output possibly scaffolding IVDA students and reducing CV students' performance, an interpretation by prior knowledge that the study did not measure](gpt-output-effect-depends-on-prior-knowledge-and-domain.md) — related
- [In a two-lecture user study, linear mixed models find no statistically significant effect of GPT-generated output on student MCQ performance, with a tendency toward a group-by-attempt interaction for IVDA](no-significant-lmm-effect-of-gpt-output-on-student-scores.md) — related
- [Model and student error patterns on IVDA MCQs show limited question-level consistency but comparable difficulty distributions for easiest and hardest questions](limited-model-student-question-level-alignment.md) — related
- [LLM-simulated student ideas moderately overlap with teacher- and student-generated lesson ideas (mean cosine similarity 0.52), with larger LLMs slightly outperforming Mistral-7B](llm-simulated-ideas-moderate-overlap-lesson-ideas.md) — related
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related
- [Newer LLM generations such as GPT-4 generally outperform GPT-3.5 in short-answer grading accuracy, but this advantage is not consistent across all tasks and domains](gpt4-advantage-uneven-across-tasks.md) — related
- [The author reports that prompt phrasing and the specific foundational model had secondary impact on final material quality compared with the structure of the workflow itself.](workflow-architecture-outweighs-prompt-phrasing.md) — related
- [ChatGPT answered unsupervised web-based MCQ assessments with a mean accuracy of 70% (range 35–100%)](chatgpt-wba-mcq-mean-70-percent.md) — related
- [Larger Llama Guard models outperform smaller ones on education-prompt classification, with the 8B model best in accuracy, recall, and F1](llama-guard-scaling-trend-education-classification.md) — related
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [GPT-4 identified a correct answer choice for nearly all generated questions, with a minority of spelling or selection errors](gpt4-correct-answer-choices-97-percent.md) — related
- [Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies](llm-company-comparison-biomedical-mcq-accuracy.md) — related

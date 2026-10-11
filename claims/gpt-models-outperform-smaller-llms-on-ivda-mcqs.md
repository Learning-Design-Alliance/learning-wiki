---
type: claim
title: GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models
description: GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models
id: gpt-models-outperform-smaller-llms-on-ivda-mcqs
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: markos-stamatakis-2026
    resource: "https://arxiv.org/abs/2606.15919"
    title: "Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919"
    author: Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across 12 prompt variants on 70 IVDA MCQs, GPT models reach higher accuracy and fully-correct rates (GPT-5.2 average 91.2% accuracy, 71.3% fully correct) than Mistral-7B (69.2%, 26.0%) and DeepSeek-R1 (75.2%, 38.1%). [→ Markos Stamatakis 2026](#markos-stamatakis-2026)

## Evidence

### Markos Stamatakis 2026

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919

`q2 · i?` · `causal · r2`

Benchmark evaluation of four chatbots on 70 IVDA MCQs across 12 prompt variants (Table 1). The article reports that "the GPT models achieve higher accuracy and more fully correct responses", with GPT-5.2 outperforming GPT-4o; smaller models select incorrect options for most questions. No effect size is printed.

> "In contrast, the GPT models achieve higher accuracy and more fully correct responses, likely due to their larger scale and training."

## Discussion


## Related Claims
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
- [Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs](minor-position-bias-and-partial-guessing-in-small-llms.md) — related
- [Descriptive user-study patterns suggest GPT output may scaffold lower-prior-knowledge IVDA students but reduce performance when prior knowledge is higher (CV)](gpt-output-effect-depends-on-prior-knowledge-and-domain.md) — related
- [In a two-lecture user study, linear mixed models find no statistically significant effect of GPT-generated output on student MCQ performance, with a tendency toward a group-by-attempt interaction for IVDA](no-significant-lmm-effect-of-gpt-output-on-student-scores.md) — related
- [Model and student error patterns on IVDA MCQs show limited question-level consistency but comparable difficulty distributions for easiest and hardest questions](limited-model-student-question-level-alignment.md) — related
- [LLM-simulated student ideas moderately overlap with teacher- and student-generated lesson ideas (mean cosine similarity 0.52), with larger LLMs slightly outperforming Mistral-7B](llm-simulated-ideas-moderate-overlap-lesson-ideas.md) — related

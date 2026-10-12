---
type: claim
title: Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent
description: Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent
id: prompt-design-affects-mcq-accuracy-asymmetrically
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
  - id: markos-stamatakis-2026-2
    resource: "https://arxiv.org/abs/2606.15919"
    title: "Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919"
    author: Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Providing slide-based context constantly reduces Mistral-7B accuracy to 62–69% while approaches without content reach over 70%, whereas GPT models improve when slide content is provided. [→ Markos Stamatakis 2026](#markos-stamatakis-2026)
`q2 i?` Different prompting approaches significantly influence results, but no consistent effect is observed for personas. [→ Markos Stamatakis 2026 (2)](#markos-stamatakis-2026-2)

## Evidence

### Markos Stamatakis 2026

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919

`q2 · i?` · `causal · r2`

Benchmark results for Mistral-7B across prompt variants (Table 1, Sec. 4). The article reports that "Providing slide con- tent constantly reduces the accuracy to62−69 %", interpreting larger input as hindering identification of question-relevant information. Descriptive percentages only; no effect size printed.

> "Providing slide con- tent constantly reduces the accuracy to62−69 %. Approaches without con- tent reach over70 %, suggesting larger input hinders identification of question- relevant information."

### Markos Stamatakis 2026 (2)

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919

`q2 · i?` · `causal · r2`

Authors' summary of the 12-prompt benchmark in Sec. 4: prompting approaches significantly influence results while persona effects show no consistent pattern. The article prints no effect size for this statement.

> "Furthermore, the different prompting approaches significantly influence the results, while no consistent effect is observed for personas (RQ2)."

## Discussion


## Related Claims
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — related

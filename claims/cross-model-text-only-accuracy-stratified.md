---
type: claim
title: Text-only accuracy across 19 LLMs spans 0.20 to 0.88 with a grand mean of 0.67, stratified by model generation and reasoning budget
description: Text-only accuracy across 19 LLMs spans 0.20 to 0.88 with a grand mean of 0.67, stratified by model generation and reasoning budget
id: cross-model-text-only-accuracy-stratified
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: anna-geißler-2025
    resource: "https://doi.org/10.48550/arXiv.2508.21452"
    title: "Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)"
    author: Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: anna-geißler-2025-2
    resource: "https://doi.org/10.48550/arXiv.2508.21452"
    title: "Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)"
    author: Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Text-only accuracy across 19 LLMs spans 0.20 to 0.88 with a grand mean of 0.67, stratified by model generation and reasoning budget

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the text-only subset, mean accuracies spanned 0.20 (gpt-3.5-turbo-0125) to 0.88 (DeepSeek R1) with a grand mean of 0.67; legacy gpt-3.5 trails newer systems and top-tier models exceed 0.80. [→ Anna Geißler 2025](#anna-geiler-2025)
`q2 i?` Within model families, higher reasoning-budget configurations outperform lighter variants, e.g., gpt-5 high versus nano. [→ Anna Geißler 2025 (2)](#anna-geiler-2025-2)

## Evidence

### Anna Geißler 2025

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `design · r2`

Cross-model comparison of 19 contemporary models (APIs and web CLI) on the 33 text-only items under the same baseline prompt, reported in the cross-model comparison section. The article reports the span from 0.20 to 0.88 and a "grand mean of 0.67"; no effect size is printed.

> "For the text-only subset (Fig. 5, mean accu- racies span 0.20 (gpt-3.5-turbo-0125) to 0.88 (DeepSeek R1), with a grand mean of 0.67."

### Anna Geißler 2025 (2)

Anna Geißler, Luca-Sophie Bien, Friedrich Schöppler, and Tobias Hertel. (2025). From Canonical to Complex: Benchmarking LLM Capabilities in Undergraduate Thermodynamics. arXiv preprint. [doi:10.48550/arXiv.2508.21452](https://doi.org/10.48550/arXiv.2508.21452)

`q2 · i?` · `associational · r2`

Same cross-model comparison on text-only items, reported as a within-family contrast between higher and lighter reasoning-budget configurations. The article names gpt-5 high versus nano as the example; no effect size is printed.

> "Within families, 6 higher “reasoning budget” configurations out- perform lighter variants (e.g., gpt-5 high vs. nano), consistent with broader evidence that capacity devoted to multi-step inference im- proves domain problem solving."

## Discussion


## Related Claims
- [Clause count shows no significant correlation with averaged LLM accuracy on text-only thermodynamics items](clause-count-no-correlation-llm-accuracy.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — a broader claim this one bears on
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [LLM accuracy on diagram-based thermodynamics items averages 32%, less than half the 67% text-only mean](llm-diagram-interpretation-thermodynamics-poor.md) — related

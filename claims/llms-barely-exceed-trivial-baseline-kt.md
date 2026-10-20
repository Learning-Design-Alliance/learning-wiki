---
type: claim
title: Frontier LLMs barely exceed a trivial baseline on knowledge tracing, with the best model surpassing always-predict-correct by only about five percentage points
description: Frontier LLMs barely exceed a trivial baseline on knowledge tracing, with the best model surpassing always-predict-correct by only about five percentage points
id: llms-barely-exceed-trivial-baseline-kt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: eamon-worden-2026
    resource: "https://doi.org/10.48550/arxiv.2602.00070"
    title: "Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)"
    author: Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Frontier LLMs barely exceed a trivial baseline on knowledge tracing, with the best model surpassing always-predict-correct by only about five percentage points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On question-level knowledge tracing over 500 sampled students, the best models (GPT-OSS-120B at 56.2%, Qwen3-Next-80B-Thinking at 55.8%) beat the 51.3% trivial baseline by only around five percentage points, while Llama-3.3-70B reached 52.3%. [→ Eamon Worden 2026](#eamon-worden-2026)

## Evidence

### Eamon Worden 2026

Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)

`q2 · i?` · `design · r2`

Zero-shot LLM evaluation of four models on question-level binary correctness prediction (approximately 27,000 predictions per model, e.g. N 27,715), described in Section 6.1.1. The authors report that the models' gains over the 51.3% baseline were limited, quoting that they "reach 56.2% and 55.8%, respectively, beating the baseline by just around 5 percentage points".

> "The best-performing models, GPT-OSS-120B and Qwen3-Next-80B-Thinking, reach 56.2% and 55.8%, respectively, beating the baseline by just around 5 percentage points."

## Discussion

## Related Claims

- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — the general claim this finding bears on, with the studies behind it
- In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students — related
- Representing exercises by KC name descriptions outperformed ID-based representation when aligning an LLM to knowledge tracing — related
- [Knowledge tracing performance on tutoring dialogues is relatively low, with a maximum of around 76% AUC, which the authors take to show dialogueKT is a challenging task.](dialogue-kt-performance-is-relatively-low-compared-to-standard-kt.md) — related

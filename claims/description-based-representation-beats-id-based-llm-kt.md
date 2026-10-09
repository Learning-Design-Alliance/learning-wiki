---
type: claim
title: Representing exercises by KC name descriptions outperformed ID-based representation when aligning an LLM to knowledge tracing
description: Representing exercises by KC name descriptions outperformed ID-based representation when aligning an LLM to knowledge tracing
id: description-based-representation-beats-id-based-llm-kt
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: heeseok-jung-2025
    resource: "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    title: "Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    author: Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Representing exercises by KC name descriptions outperformed ID-based representation when aligning an LLM to knowledge tracing

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across the ablation comparing KC-name descriptions versus bracketed KC IDs in KTLP format, the description-based method generally achieved higher AUC. [→ Heeseok Jung 2025](#heeseok-jung-2025)

## Evidence

### Heeseok Jung 2025

Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

`q2 · i?` · `causal · r2`

Ablation experiment (Table 7) comparing description-based versus ID-based exercise representation in KTLP format across all five datasets at 8-64 training students. The article states "In most cases, the description-based method was observed to outperform the ID-based method", e.g., Algebra05 at 64 students: 0.722 vs 0.659 AUC.

> "In most cases, the description-based method was observed to outperform the ID-based method."

## Discussion


## Related Claims
- [In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students](clst-outperforms-baselines-cold-start.md) — related
- [DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets](dkt-input-output-representation-affects-performance.md) — related
- [The expert-designed KC model adds little predictive power on most datasets, with significant contributions only on the two KDD Cup 2010 datasets](expert-kc-model-adds-little-predictive-power.md) — related
- [Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students](fine-tuning-improves-clst-auc.md) — related
- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — related
- [In a qualitative case study, LLMKT adjusts KC mastery estimates using the dialogue's textual content, such as the difficulty of the tutor's question, rather than only prior correctness labels.](llmkt-uses-dialogue-text-to-adjust-kc-mastery-estimates.md) — related
- [DKT-Sem, a DKT variant using semantic text embeddings, performs better than existing KT methods on tutoring dialogues, with a smaller margin on the larger MathDial dataset.](dkt-sem-outperforms-existing-kt-methods-most-with-little-training-data.md) — related

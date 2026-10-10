---
type: claim
title: Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students
description: Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students
id: fine-tuning-improves-clst-auc
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

# Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The fine-tuned CLST outperformed the untuned Mistral-7B backbone on every dataset, improving AUC by at least 1.55% (8 students) and up to 11.94% (64 students). [→ Heeseok Jung 2025](#heeseok-jung-2025)

## Evidence

### Heeseok Jung 2025

Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

`q2 · i?` · `causal · r2`

Before/after fine-tuning comparison (Table 8) evaluating untuned CLST (0 students) versus models fine-tuned on 8-64 students across all five datasets. The article reports the 64-student model "outperformed the untuned model by at least 5.33% and up to 11.94% in terms of AUC".

> "Moreover, the model fine -tuned with 64 students' data outperformed the untuned model by at least 5.33% and up to 11.94% in terms of AUC."

## Discussion


## Related Claims
- [Fine-tuning and running CLST is feasible on a single workstation GPU, with measured training cost of about 6.8 hours and 19 GB peak memory on Algebra05](clst-finetuning-compute-cost.md) — related
- [In system cold-start scenarios, CLST outperformed every baseline KT model across all five datasets, with the largest gains at 8 training students](clst-outperforms-baselines-cold-start.md) — related
- [Representing exercises by KC name descriptions outperformed ID-based representation when aligning an LLM to knowledge tracing](description-based-representation-beats-id-based-llm-kt.md) — related
- [Fine-tuning on KTLP data improved CLST output calibration, moving predictions closer to the ideal diagonal](fine-tuning-improves-clst-calibration.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related

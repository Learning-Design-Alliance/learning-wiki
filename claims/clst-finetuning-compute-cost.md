---
type: claim
title: Fine-tuning and running CLST is feasible on a single workstation GPU, with measured training cost of about 6.8 hours and 19 GB peak memory on Algebra05
description: Fine-tuning and running CLST is feasible on a single workstation GPU, with measured training cost of about 6.8 hours and 19 GB peak memory on Algebra05
id: clst-finetuning-compute-cost
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: heeseok-jung-2025
    resource: "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    title: "Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    author: Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning and running CLST is feasible on a single workstation GPU, with measured training cost of about 6.8 hours and 19 GB peak memory on Algebra05

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Empirical measurement on an NVIDIA RTX A6000 found roughly 4-second average training steps (batch size 4), about 6.8 hours to fine-tune on Algebra05's 21k samples, ~19 GB peak training memory, ~16 GB inference memory, and ~1.7 kWh estimated energy. [→ Heeseok Jung 2025](#heeseok-jung-2025)

## Evidence

### Heeseok Jung 2025

Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

`q2 · i?` · `design · r2`

Empirical cost measurement subsection (4.1.1) reporting training step duration, GPU memory, and estimated energy for CLST fine-tuning and inference. The article states fine-tuning on Algebra05 "took about 6.8 hours on an NVIDIA RTX A6000 GPU" with peak training memory around 19 GB.

> "As an example, fine-tuning on the Algebra05 dataset (21k samples) with an accumulation step size of 4 took about 6.8 hours on an NVIDIA RTX A6000 GPU."

## Discussion


## Related Claims
- [Fine-tuning CLST on KTLP-formatted data improved predictive performance across all datasets, with gains growing with training students](fine-tuning-improves-clst-auc.md) — related
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related

---
type: claim
title: Three LLMs fine-tuned on teacher-validated feedback reach reported training losses with qualitative teacher validation
description: Three LLMs fine-tuned on teacher-validated feedback reach reported training losses with qualitative teacher validation
id: aicofe-llm-finetuning-training-results
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: alvaro-becerra-2026
    resource: "https://orcid.org/0009-0003-7793-2682"
    title: "Alvaro Becerra, Alejandra Palma and Ruth Cobos. (2026). AICoFe: Implementation and Deployment of an AI-Based Collaborative Feedback System for Higher Education. LASI Spain 26: Learning Analytics Summer Institute Spain 2026. https://orcid.org/0009-0003-7793-2682"
    author: Alvaro Becerra, Alejandra Palma and Ruth Cobos
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Three LLMs fine-tuned on teacher-validated feedback reach reported training losses with qualitative teacher validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`

## Subclaims
`q1 i?` Fine-tuning GPT-4.1-mini, Gemini 2.5 Flash, and Llama 3.1 on SOPHIAS teacher-validated feedback instances yielded final training losses of 0.934, 0.759, and 1.210 respectively, with all three qualitatively validated through teacher review. [→ Alvaro Becerra 2026](#alvaro-becerra-2026)

## Evidence

### Alvaro Becerra 2026

Alvaro Becerra, Alejandra Palma and Ruth Cobos. (2026). AICoFe: Implementation and Deployment of an AI-Based Collaborative Feedback System for Higher Education. LASI Spain 26: Learning Analytics Summer Institute Spain 2026. https://orcid.org/0009-0003-7793-2682

`q1 · i?` · `design · r1`

Technical fine-tuning report in the Feedback Generation Module section. GPT-4.1-mini was adapted "via the OpenAI fine-tuning API for 3 epochs" reaching a final training loss of 0.934; Gemini 2.5 Flash reached a final loss of 0.759 with accuracy 0.798, and Llama 3.1 (LoRA, r=16, alpha=32) a loss of 1.210. No student-outcome evaluation of the fine-tuned models is reported.

> "GPT-4.1-mini was adapted via the OpenAI fine-tuning API for 3 epochs with a learning rate multiplier of 2, consuming 205,239 tokens and reaching a final training loss of 0.934."

## Discussion


## Related Claims
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
- [The three fine-tuned LLMs differ significantly in response length, readability, and similarity to posts](llm-response-length-readability-differences.md) — related
- [Counterfactual fine-tuning reduces sentiment bias in LLM-generated forum replies](counterfactual-fine-tuning-reduces-sentiment-bias.md) — related
- [Gemma and LLaMA produce higher-quality responses than GPT-2 by TIGERSCORE, with accuracy and comprehension gaps remaining](gemma-llama-outperform-gpt2-tigerscore.md) — related

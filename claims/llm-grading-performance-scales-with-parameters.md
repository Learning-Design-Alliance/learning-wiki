---
type: claim
title: LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance
description: LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance
id: llm-grading-performance-scales-with-parameters
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: pavlin-g-poliˇcar-2025
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: pavlin-g-poliˇcar-2025-2
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Larger models graded better: GPT-4o and Llama-405Bq4 performed favorably to the 70B models, which outperformed the 8B variant. [→ Pavlin G. Poliˇcar 2025](#pavlin-g-policar-2025)
`q2 i?` The quantized Llama-70Bq4 achieved comparable performance to its full-precision counterpart. [→ Pavlin G. Poliˇcar 2025 (2)](#pavlin-g-policar-2025-2)

## Evidence

### Pavlin G. Poliˇcar 2025

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Cross-model comparison of classification accuracy by model size in the classroom grading study. The authors report that 'The larger GPT-4o and Llama-405Bq4 models perform favorably to the 70B parameter models, which in turn outperform the 8B parameter Llama variant.'

> "Model performance generally correlates with their number of parameters. The larger GPT-4o and Llama-405Bq4 models perform favorably to the 70B parameter models, which in turn outperform the 8B parameter Llama variant."

### Pavlin G. Poliˇcar 2025 (2)

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Comparison of quantized Llama-70Bq4 with full-precision Llama-70B in the same evaluation: quantization 'appears to have negligible effect on performance,' with the quantized variant achieving 'comparable performance to its full-precision counterpart.'

> "Quantization appears to have negligible effect on performance, as the quantized variant of Llama-70B model achieves comparable performance to its full-precision counterpart."

## Discussion


## Related Claims
- [Larger GPT-2 variants tended to produce more coherent and contextually appropriate text, illustrating scaling laws in a simplified setting](gpt2-model-size-coherence-scaling.md) — related
- [In a real classroom, all six evaluated LLMs except Llama-8B graded student text answers with classification accuracy between 85% and 90% against TA gold-standard grades](llm-graders-match-ta-grading-accuracy.md) — related
- [Under identical LoRA hyperparameters and training data, the 27B Gemma model outperforms the 70B LLaMA model on every computed essay-scoring metric](model-scale-not-predictor-lora-scoring.md) — reports the opposite
- [GPT-4o and Llama 3 70B significantly outperform GPT-3.5 Turbo across all five homework-assessment metrics in circuit analysis](gpt4o-llama3-outperform-gpt35-circuit-homework-assessment.md) — a narrower finding that bears on this claim
- [GPT-4o shows more consistent performance than Llama 3 70B across topics and metrics, while Llama 3 70B falls below 60% on the unit metric for three advanced topics](gpt4o-consistency-vs-llama3-unit-weakness.md) — related
- [Sinusoidal steady-state analysis is the most challenging topic for both GPT-4o and Llama 3 70B in homework assessment](sinusoidal-steady-state-hardest-topic-for-llms.md) — related

---
type: claim
title: Fine-tuning on the 1,000-image nuclear dataset improves image fidelity of SD models, with KID and CMMD decreasing over training steps
description: Fine-tuning on the 1,000-image nuclear dataset improves image fidelity of SD models, with KID and CMMD decreasing over training steps
id: fine-tuning-improves-sd-nuclear-image-fidelity
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: mohammed-i-radaideh-2026
    resource: "https://arxiv.org/abs/2608.04030"
    title: "Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh. (2026). NuclearDiffusion: Text-to-Image Foundation Models for Learning Nuclear Energy Concepts. Preprint submitted to Peer Review. https://arxiv.org/abs/2608.04030"
    author: Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning on the 1,000-image nuclear dataset improves image fidelity of SD models, with KID and CMMD decreasing over training steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` KID and CMMD decrease with training steps for SDXL, SD-v3.5-Medium, and Flux.1, indicating greater similarity between generated and real nuclear images than the zero-shot models. [→ Mohammed I. Radaideh 2026](#mohammed-i-radaideh-2026)

## Evidence

### Mohammed I. Radaideh 2026

Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh. (2026). NuclearDiffusion: Text-to-Image Foundation Models for Learning Nuclear Energy Concepts. Preprint submitted to Peer Review. https://arxiv.org/abs/2608.04030

`q2 · i?` · `design · r2`

Quantitative evaluation over 300 images generated from 300 testing prompts at 15-16 saved checkpoints per model. Best scores: SDXL CMMD=0.103 (20,000 steps), KID=0.003 (37,500); SD-v3.5-Medium CMMD=0.090 (37,500), KID=0.003 (27,500); Flux.1 CMMD=0.154, KID=0.011. The "decreasing trend in both KID and CMMD" supports improved fidelity; no effect size is printed.

> "The decreasing trend in both KID and CMMD with training steps indicates greater fidelity between generated images and real images compared with the zero-shot model at training step = 0."

## Discussion


## Related Claims
- [The CLIP text-image alignment score failed to capture fine-tuning improvements, contradicting KID, CMMD, and human judgment](clip-score-fails-to-capture-fine-tuning-gains.md) — related
- [Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts](commercial-models-fail-specialized-nuclear-prompts.md) — related
- [Human qualitative assessment shows SDXL significantly outperforms SD-v3.5-Medium after fine-tuning, failing on 84 versus 250 of 300 prompts](sdxl-outperforms-sd35-medium-qualitatively.md) — related
- [Generating multiple images per prompt and re-prompting with word variations did not yield accurate nuclear images for failed concepts](multiple-images-and-reprompting-do-not-fix-accuracy.md) — related
- [LoRA fine-tuning of Flux.1 failed to learn nuclear concepts, producing wrong-concept images on all 300 test prompts](lora-flux1-fine-tuning-fails-nuclear-concepts.md) — related

---
type: claim
title: Generating multiple images per prompt and re-prompting with word variations did not yield accurate nuclear images for failed concepts
description: Generating multiple images per prompt and re-prompting with word variations did not yield accurate nuclear images for failed concepts
id: multiple-images-and-reprompting-do-not-fix-accuracy
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

# Generating multiple images per prompt and re-prompting with word variations did not yield accurate nuclear images for failed concepts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` For prompts all three models failed, generating 4 additional images and 5 prompt variations did not produce accurate images; accuracy depended mainly on fine-tuning quality. [→ Mohammed I. Radaideh 2026](#mohammed-i-radaideh-2026)

## Evidence

### Mohammed I. Radaideh 2026

Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh. (2026). NuclearDiffusion: Text-to-Image Foundation Models for Learning Nuclear Energy Concepts. Preprint submitted to Peer Review. https://arxiv.org/abs/2608.04030

`q2 · i?` · `design · r2`

Section 5.3 analysis: 20 failed prompts with 4 extra images each (images remained inaccurate for all 40 instances across Flux.1 and SD-v3.5-Medium; SDXL closer in only 3 of 20), and 5 prompts with 5 wording variations each, where the spacecraft concept "is still inaccurate". No effect size is printed.

> "As a result, as with generating multiple images, accurate generation depends mainly on accurate fine-tuning and re-prompting did not help with the performance."

## Discussion


## Related Claims
- [Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts](commercial-models-fail-specialized-nuclear-prompts.md) — related
- [Fine-tuning on the 1,000-image nuclear dataset improves image fidelity of SD models, with KID and CMMD decreasing over training steps](fine-tuning-improves-sd-nuclear-image-fidelity.md) — related
- [LoRA fine-tuning of Flux.1 failed to learn nuclear concepts, producing wrong-concept images on all 300 test prompts](lora-flux1-fine-tuning-fails-nuclear-concepts.md) — related
- [The CLIP text-image alignment score failed to capture fine-tuning improvements, contradicting KID, CMMD, and human judgment](clip-score-fails-to-capture-fine-tuning-gains.md) — related

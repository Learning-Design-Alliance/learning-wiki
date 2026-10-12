---
type: claim
title: Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts
description: Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts
id: commercial-models-fail-specialized-nuclear-prompts
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

# Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT-Image-2 and Gemini-3.1-Flash-Image were significantly better than Midjourney on nuclear concepts across nearly all 300 images, yet all three commercial models failed to generate accurate images as prompts became specific. [→ Mohammed I. Radaideh 2026](#mohammed-i-radaideh-2026)

## Evidence

### Mohammed I. Radaideh 2026

Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh. (2026). NuclearDiffusion: Text-to-Image Foundation Models for Learning Nuclear Energy Concepts. Preprint submitted to Peer Review. https://arxiv.org/abs/2608.04030

`q2 · i?` · `design · r2`

Section 6 comparison of GPT-Image-2, Gemini-3.1-Flash-Image, and Midjourney on 300 testing prompts, with qualitative inspection (e.g., the TVS-2M VVER-1000 fuel assembly prompt in Figure 9) and CMMD/KID in Table C.1. The "significantly better" GPT/Gemini versus Midjourney contrast is reported without an effect size.

> "However, as the prompts became specific, all three failed to generate accurate images, suggesting the necessity for fine-tuning."

## Discussion


## Related Claims
- [Generating multiple images per prompt and re-prompting with word variations did not yield accurate nuclear images for failed concepts](multiple-images-and-reprompting-do-not-fix-accuracy.md) — related
- [LoRA fine-tuning of Flux.1 failed to learn nuclear concepts, producing wrong-concept images on all 300 test prompts](lora-flux1-fine-tuning-fails-nuclear-concepts.md) — related
- [Human qualitative assessment shows SDXL significantly outperforms SD-v3.5-Medium after fine-tuning, failing on 84 versus 250 of 300 prompts](sdxl-outperforms-sd35-medium-qualitatively.md) — related
- [The CLIP text-image alignment score failed to capture fine-tuning improvements, contradicting KID, CMMD, and human judgment](clip-score-fails-to-capture-fine-tuning-gains.md) — related
- [Fine-tuning on the 1,000-image nuclear dataset improves image fidelity of SD models, with KID and CMMD decreasing over training steps](fine-tuning-improves-sd-nuclear-image-fidelity.md) — related
- [One student group compared outputs across three LLMs and judged Gemini more accurate overall, though it still failed fine-grained distinctions](multi-llm-comparison-gemini-more-accurate.md) — related

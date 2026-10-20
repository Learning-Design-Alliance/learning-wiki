---
type: claim
title: The CLIP text-image alignment score failed to capture fine-tuning improvements, contradicting KID, CMMD, and human judgment
description: The CLIP text-image alignment score failed to capture fine-tuning improvements, contradicting KID, CMMD, and human judgment
id: clip-score-fails-to-capture-fine-tuning-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: mohammed-i-radaideh-2026
    resource: "https://doi.org/10.48550/arxiv.2608.04030"
    title: "Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh. (2026). NuclearDiffusion: Text-to-Image Foundation Models for Learning Nuclear Energy Concepts. Preprint submitted to Peer Review. https://arxiv.org/abs/2608.04030 [doi:10.48550/arxiv.2608.04030](https://doi.org/10.48550/arxiv.2608.04030)"
    author: Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The CLIP text-image alignment score failed to capture fine-tuning improvements, contradicting KID, CMMD, and human judgment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` CLIP scores indicated zero-shot models were best for the SD models and did not agree with CMMD, KID, or the qualitative assessment of fine-tuning gains. [→ Mohammed I. Radaideh 2026](#mohammed-i-radaideh-2026)

## Evidence

### Mohammed I. Radaideh 2026

Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh. (2026). NuclearDiffusion: Text-to-Image Foundation Models for Learning Nuclear Energy Concepts. Preprint submitted to Peer Review. https://arxiv.org/abs/2608.04030 [doi:10.48550/arxiv.2608.04030](https://doi.org/10.48550/arxiv.2608.04030)

`q2 · i?` · `design · r2`

CLIP score computed at all 15-16 checkpoints for the three models (Figure B.1, Appendix B). The article explains CLIP relies on image embedding models likely to fail on unfamiliar nuclear images, whereas KID and CMMD benefit from reference-image comparison. Image Reward and VQ 2 metrics also failed to capture the improvement.

> "The CLIP scores indicate that fine-tuning is not effective for all three models and don't agree with CMMD and KID."

## Discussion


## Related Claims
- [Fine-tuning on the 1,000-image nuclear dataset improves image fidelity of SD models, with KID and CMMD decreasing over training steps](fine-tuning-improves-sd-nuclear-image-fidelity.md) — related
- [Human qualitative assessment shows SDXL significantly outperforms SD-v3.5-Medium after fine-tuning, failing on 84 versus 250 of 300 prompts](sdxl-outperforms-sd35-medium-qualitatively.md) — related
- [Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts](commercial-models-fail-specialized-nuclear-prompts.md) — related
- [Generating multiple images per prompt and re-prompting with word variations did not yield accurate nuclear images for failed concepts](multiple-images-and-reprompting-do-not-fix-accuracy.md) — related
- [LoRA fine-tuning of Flux.1 failed to learn nuclear concepts, producing wrong-concept images on all 300 test prompts](lora-flux1-fine-tuning-fails-nuclear-concepts.md) — related

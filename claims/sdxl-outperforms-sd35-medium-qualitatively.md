---
type: claim
title: Human qualitative assessment shows SDXL significantly outperforms SD-v3.5-Medium after fine-tuning, failing on 84 versus 250 of 300 prompts
description: Human qualitative assessment shows SDXL significantly outperforms SD-v3.5-Medium after fine-tuning, failing on 84 versus 250 of 300 prompts
id: sdxl-outperforms-sd35-medium-qualitatively
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

# Human qualitative assessment shows SDXL significantly outperforms SD-v3.5-Medium after fine-tuning, failing on 84 versus 250 of 300 prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In human-judged comparison against real images, SDXL failed to generate a reasonably close image in 84 of 300 instances while SD-v3.5-Medium failed in 250, so SDXL performs significantly better despite comparable CMMD/KID scores. [→ Mohammed I. Radaideh 2026](#mohammed-i-radaideh-2026)

## Evidence

### Mohammed I. Radaideh 2026

Mohammed I. Radaideh, Jeremy Moon, Andre Gala-Garza, Emma Son, Yug Shah, Majdi I. Radaideh. (2026). NuclearDiffusion: Text-to-Image Foundation Models for Learning Nuclear Energy Concepts. Preprint submitted to Peer Review. https://arxiv.org/abs/2608.04030 [doi:10.48550/arxiv.2608.04030](https://doi.org/10.48550/arxiv.2608.04030)

`q2 · i?` · `design · r2`

Human qualitative assessment (subsection 4.2): a human judge picked the checkpoint image closest to the real image across all 300 test prompts; Flux.1 failed all 300 and was excluded. Top SDXL checkpoints scored 50, 48, and 44 points; the "significantly better performance" of SDXL is reported without an effect size.

> "the bottom panel of Figure 5 shows that SD-v3.5-Medium failed to generate images reasonably close to the real ones in 250 instances, while SDXL failed in 84 instances. Accordingly, SDXL exhibits significantly better performance than SD-v3.5-Medium."

## Discussion


## Related Claims
- [The CLIP text-image alignment score failed to capture fine-tuning improvements, contradicting KID, CMMD, and human judgment](clip-score-fails-to-capture-fine-tuning-gains.md) — related
- [Commercial text-to-image models produce accurate images for broad nuclear concepts but fail on specialized engineering prompts](commercial-models-fail-specialized-nuclear-prompts.md) — related
- [Fine-tuning on the 1,000-image nuclear dataset improves image fidelity of SD models, with KID and CMMD decreasing over training steps](fine-tuning-improves-sd-nuclear-image-fidelity.md) — related
- [LoRA fine-tuning of Flux.1 failed to learn nuclear concepts, producing wrong-concept images on all 300 test prompts](lora-flux1-fine-tuning-fails-nuclear-concepts.md) — related

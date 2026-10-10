---
type: design
id: gen-aitecture-comfyui-inpainting-workflow
title: "Gen-AI-tecture: a bespoke, locally run ComfyUI generative-AI image creation and editing workflow for architectural education"
description: A bespoke generative-AI image workflow implemented as a localised ComfyUI environment in which students upload or select images, describe changes in natural language, and receive multiple visual alternatives.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: kapsalis-2026
    resource: "https://orcid.org/0000-0003-1598-6426"
    title: "Kapsalis, T. (2026). Gen-AI-tecture: using generative AI to support architectural students in design tasks. https://orcid.org/0000-0003-1598-6426"
    author: Kapsalis, T
---

# Gen-AI-tecture: a bespoke, locally run ComfyUI generative-AI image creation and editing workflow for architectural education

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
A bespoke generative-AI image workflow implemented as a localised ComfyUI environment in which students upload or select images, describe changes in natural language, and receive multiple visual alternatives. "The workﬂow is powered by the Flux 1 Kontext (dev) diffusion model (Black Forest Labs, 2025), which has been ﬁne-tuned with a curated set of interior-design images" using LoRA adaptation on the InteriorNet dataset. It offers three modes (text-driven, reference-image-driven, hybrid) and edits via in-painting that preserves surrounding context, acting as a visual co-pilot rather than replacing design thinking.

## Design Implications

### Context
#### Requirements
- Runs locally within a ComfyUI node-based environment with the fine-tuned Flux 1 Kontext (dev) model
- Used within scaffolded studio sessions with facilitator demonstration and structured design tasks
#### Constraints
- Fine-tuned for residential interior scenarios (bedroom and living/dining room scenes), so outputs support early design discussions "without claiming the status of resolved architectural drawings" and may not generalise to other design typologies or less supported studio environments

### Target Learners
- Undergraduate architecture students (Levels 3-5)

### Learning Goals
- Architectural design ideation and visualisation
- AI-handling skills for professional practice

### Claims
- [Gen Aitecture Expanded Creative Search Space](../claims/gen-aitecture-expanded-creative-search-space.md) [+M]
- [Gen Aitecture Intensive Engagement Log Data](../claims/gen-aitecture-intensive-engagement-log-data.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Kapsalis, T. (2026). Gen-AI-tecture: using generative AI to support architectural students in design tasks. https://orcid.org/0000-0003-1598-6426

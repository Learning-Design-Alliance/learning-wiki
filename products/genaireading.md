---
type: product
id: genaireading
title: GenAIReading
description: A web application developed by Morita et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# GenAIReading

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
A web application developed by Morita et al. that augments narrative reading with AI-generated stories, summaries, stylistically continuous images, and CLIP-based selection of key summary images.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **GenAIReading pipeline: LLM summaries, DALL-E story images, and CLIP-based Summary Image Selector**: GenAIReading is a web application (React and Node.js) that augments reading with AI-generated materials. A text generation phase uses ChatGPT to create stories from constraint and preference prompts and distill roughly 50-word summaries; an image generation phase uses the diffusion model DALL-E with the preceding image as input for stylistic continuity. Its novel component, the Summary Image Selector, works because "the story and the generated images, which are processed to select five key summary images" using CLIP cosine similarity per story segment. (Ryugo Morita et al. (2025))

### Claims

## Related Products and Programmes
-

## Key Sources
- Ryugo Morita, Ko Watanabe, Jinjia Zhou, Andreas Dengel, and Shoya Ishimaru. (2025). GenAIReading: Augmenting Human Cognition with Interactive Digital Textbooks Using Large Language Models and Image Generation Models. https://arxiv.org/abs/2503.07463

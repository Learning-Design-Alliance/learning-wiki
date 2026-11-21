---
type: product
id: classcomet
title: ClassComet
description: ClassComet is an online educational video platform developed by Ji et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# ClassComet

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
ClassComet is an online educational video platform developed by Ji et al. that overlays automatically generated and learner-authored danmaku comments on course videos to support engagement and learning.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ClassComet, an educational video platform with LMM-driven automatic danmaku generation**: ClassComet is an online educational video platform the authors "designed and developed" that is "empowered by the LMM-driven automated generation of danmaku, aiming to improve viewers' learning outcomes and engagement". Its interface has a video player (controls, danmaku overlay with color highlighting, danmaku input box) and a video sidebar listing course videos. Generated danmaku appears regardless of a video's popularity, and learners can also post their own danmaku with chosen font color and display position. (Zipeng Ji et al. (2025))
- **ClassComet's four-step LMM danmaku-generation pipeline: video understanding, persona creation, structured prompt template, and embedding**: The article proposes "a novel pipeline based on LMMs for generating danmaku that encompasses both content-related and emotion-related danmaku in different types". Step A segments videos with PySceneDetect and uses GPT4o (following MM-VID, 5 frames per minute) plus Azure Video Indexer transcripts to produce clip- and text-level descriptions. Step B uses GPT4o to create six virtual viewer personas with backgrounds and danmaku styles. Step C applies a structured prompt template (system prompt, user prompt, parameters) with in-context examples and calibrated length/frequency/count constraints. Step D embeds the generated danmaku into the video. (Zipeng Ji et al. (2025))

### Claims

## Related Products and Programmes
-

## Key Sources
- Zipeng Ji, Pengcheng An, and Jian Zhao. (2025). ClassComet: Exploring and Designing AI-generated Danmaku in Educational Videos to Enhance Online Learning. https://arxiv.org/abs/2504.18189

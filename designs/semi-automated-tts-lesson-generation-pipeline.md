---
type: design
id: semi-automated-tts-lesson-generation-pipeline
title: Semi-automated three-stage human-in-the-loop pipeline for generating dialogue-based TTS lesson videos
description: "A lesson-video generation workflow with three stages: LLM-based slide generation (Claude 3.5 Sonnet producing Marp Markdown slides), LLM-based TTS-optimized narration generation, and automated speech synthesis and int..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: gendo-kumoi-2026
    resource: "https://arxiv.org/abs/2607.12235"
    title: "Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa. (2026). A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential. Preprint, under review at IEEE Access. https://arxiv.org/abs/2607.12235"
    author: Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa
---

# Semi-automated three-stage human-in-the-loop pipeline for generating dialogue-based TTS lesson videos

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A lesson-video generation workflow with three stages: LLM-based slide generation (Claude 3.5 Sonnet producing Marp Markdown slides), LLM-based TTS-optimized narration generation, and automated speech synthesis and integration via the Gemini TTS API, Marp, Selenium, and MoviePy. The system "was intentionally designed not as a "one-shot" fully automated generation tool but as an interactive and augmentative workflow", positioning educators as retaining final judgment over quality while using AI as an efficient assistant. Educator review occurs after stages 1 and 2; stage 3 is fully automated.

## Design Implications

### Context
#### Requirements
- Educator review between generation and delivery, covering completeness, factual accuracy, provenance, fit to delivery mode and learner, and audio continuity
#### Constraints
- The record covers two lessons produced by the authors, so it describes one team's practice rather than establishing how much review such material needs in general

### Target Learners
- first-year high school students

### Learning Goals
- curriculum lessons delivered as on-demand video (e.g., how generative AI works; a data-driven decision-making framework)

### Claims
- [Educator Review Seven Criteria Caught Contradiction](../claims/educator-review-seven-criteria-caught-contradiction.md) [+M]

## Related Designs

- [Human-supervised AI video production pipeline for personalized instructional videos](ai-personalized-video-production-pipeline.md)

## Examples
-

## Key Sources
- Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma, Manabu Kobayashi, and Shigeichi Hirasawa. (2026). A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential. Preprint, under review at IEEE Access. https://arxiv.org/abs/2607.12235

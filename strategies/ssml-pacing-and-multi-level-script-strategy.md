---
type: strategy
id: ssml-pacing-and-multi-level-script-strategy
title: Control synthetic narration pacing and slide transitions with SSML and generate scripts at multiple detail levels for micro-tuning
description: "The workflow uses Amazon Polly's Speech Synthesis Markup Language to control narration: instructors can set speaking rate (e.g."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: dengsheng-zhang-2025
    resource: "https://arxiv.org/abs/2511.20660"
    title: "Dengsheng Zhang. (2025). Transforming Higher Education with AI-Powered Video Lectures. https://arxiv.org/abs/2511.20660"
    author: Dengsheng Zhang
---

# Control synthetic narration pacing and slide transitions with SSML and generate scripts at multiple detail levels for micro-tuning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The workflow uses Amazon Polly's Speech Synthesis Markup Language to control narration: instructors can set speaking rate (e.g. 85% of usual speed) and insert breaks between slides for transitions. Gemini can also be prompted to produce three script detail levels — normal, elaborated, and in-depth — letting instructors "do micro tuning on lecture topics and slides depending on the importance or do compromise between details and time duration".

## Design Implications

### Context
#### Requirements
- An AWS account and Amazon Polly access
- Scripts sanitised of characters that clash with SSML, or a prompt explicitly excluding dots, ellipses, '/' and '&'
#### Constraints
- 

### Target Learners
- higher education students viewing video lectures

### Target Learning Goals
- manageable information density and pacing in instructional video

## Claims

- [Google Gemini generates accurate, context-sensitive voice scripts for visually rich academic PowerPoint slides from a single-line prompt](../claims/gemini-accurate-scripts-visual-slides.md) [+W]

## Related Strategies

- [Cloud Text-to-Speech API](cloud_text-to-speech_api.md)

## Examples
-

## Key Sources
- Dengsheng Zhang. (2025). Transforming Higher Education with AI-Powered Video Lectures. https://arxiv.org/abs/2511.20660

---
type: design
id: ai-personalized-video-production-pipeline
title: Human-supervised AI video production pipeline for personalized instructional videos
description: "A custom software pipeline produced 300 AI-generated personalized videos (100 topics × three interest variants: business, technology, society/biology) for a large online undergraduate course."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: tomlinson-2026
    resource: "https://doi.org/10.1038/s41598-026-52798-9"
    title: "Tomlinson, B., Black, R.W., Patterson, D.J., van der Hoek, A., Ferguson, J. & Bietz, M.J. (2026). Students prefer personalized, AI-generated educational videos over non-personalized, human-recorded videos. Scientific Reports 16:21804. https://doi.org/10.1038/s41598-026-52798-9"
    author: "Tomlinson, B., Black, R.W., Patterson, D.J., van der Hoek, A., Ferguson, J. & Bietz, M.J"
---

# Human-supervised AI video production pipeline for personalized instructional videos

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 1 study (1 associational), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A custom software pipeline produced 300 AI-generated personalized videos (100 topics × three interest variants: business, technology, society/biology) for a large online undergraduate course. LLMs (GPT-4o, Claude 3.7 Sonnet) drafted five-paragraph scripts from an instructor-defined "ethos" prompt; the instructor and project scientist reviewed and edited all scripts and checked examples for correctness. Videos composited a HeyGen AI avatar built from a recording of the instructor, Unsplash images, bullet points, titles, credits, and music into 3–5 minute videos uploaded to YouTube and embedded in Canvas pages.

## Design Implications

### Context
#### Requirements
- Instructor oversight at multiple stages: script review, correctness checking of examples and images, and final video review
#### Constraints
- Producing and reviewing the scripts "was a time-consuming process, but still quicker than it would have been to write multiple versions of 100 scripts by hand"; numerous iterations were needed to adjust avatar expressiveness, intonation, lighting, and framing

### Target Learners
- undergraduate students in a large online general education course

### Learning Goals
- connections between information technology and global sustainability

### Claims

- [Students preferred AI-generated personalized videos over human-recorded non-personalized videos in direct comparison](../claims/ai-personalized-videos-preferred-over-human-non-personalized.md) [+W]
- [Viewing of the personalized AI videos declined sharply across the quarter, with views of the first week-9 video set suggesting fewer than 10% of the course population was watching voluntarily by the end of the course](../claims/video-views-declined-across-quarter.md) [-W]

## Related Designs

- [Semi-automated three-stage human-in-the-loop pipeline for generating dialogue-based TTS lesson videos](semi-automated-tts-lesson-generation-pipeline.md)
- [Bespoke: a five-stage pipeline that regenerates a complete industry-personalized lecture video from a seed transcript](bespoke-lecture-video-generation-pipeline.md)

## Examples
-

## Key Sources
- Tomlinson, B., Black, R.W., Patterson, D.J., van der Hoek, A., Ferguson, J. & Bietz, M.J. (2026). Students prefer personalized, AI-generated educational videos over non-personalized, human-recorded videos. Scientific Reports 16:21804. https://doi.org/10.1038/s41598-026-52798-9

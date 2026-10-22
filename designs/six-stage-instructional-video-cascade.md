---
type: design
id: six-stage-instructional-video-cascade
title: Six-stage cascade architecture for end-to-end instructional video generation
description: "Nearly all submissions instantiate a six-stage cascade: \"persona parsing and routing, lesson planning, slide and script composition, visual rendering, narration synthesis, and assembly.\" Recurring design choices inclu..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-22
sources:
  - id: lin-2026
    resource: "https://arxiv.org/abs/2608.08852"
    title: "Lin, Yi-Cheng; Guo, Yu-Kai; Chen, Szu-Chi; Feng, Bo-Han; Hsu, Yun-Man; Hsieh, Hsiang; Lin, Yu-Jung; Wu, Yue-Ling; Dong, Jia-Kai; Cheng, An-Yu; Huang, Yu-Han; Ieong, Lok-Lam; Chen, Kuan-Yu; Tchouang, Ming-Douo; Sun, Shao-Hua; Lin, Che; Ding, Jian-Jiun; Lee, Hung-yi. (2026). Findings of the First Teaching Monster Challenge: A Benchmark of Pedagogical Content Knowledge in AI Agents. arXiv. https://arxiv.org/abs/2608.08852"
    author: Lin, Yi-Cheng; Guo, Yu-Kai; Chen, Szu-Chi; Feng, Bo-Han; Hsu, Yun-Man; Hsieh, Hsiang; Lin, Yu-Jung; Wu, Yue-Ling; Dong, Jia-Kai; Cheng, An-Yu; Huang, Yu-Han; Ieong, Lok-Lam; Chen, Kuan-Yu; Tchouang, Ming-Douo; Sun, Shao-Hua; Lin, Che; Ding, Jian-Jiun; Lee, Hung-yi
---

# Six-stage cascade architecture for end-to-end instructional video generation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Nearly all submissions instantiate a six-stage cascade: "persona parsing and routing, lesson planning, slide and script composition, visual rendering, narration synthesis, and assembly." Recurring design choices include structuring the persona as JSON conditioning for every stage, difficulty-based model routing, web-search grounding of lesson plans, Bloom's-taxonomy constraints enforced by closed-loop LLM review, HTML/CSS slide templates with reviewer–fixer loops, split handling of conceptual versus mathematical figures, two-step planning for Manim animation, and word-level forced alignment of narration to animation.

## Design Implications

### Context
#### Requirements
- Each stage consumes artifacts from earlier stages; persona parsing into structured JSON conditions every following stage.
#### Constraints
- Web-search grounding lowers but does not eliminate factual errors in lesson plans; one-shot LLM generation of Manim code fails frequently without a storyboard split.

### Target Learners
- learners described by persona across grade levels and attention spans

### Learning Goals
- persona-adapted instructional video lessons

### Claims

- [Reviewer free-text comments identified synthetic voice, slide–narration reveal timing, and slide layout as the main remaining quality issues](../claims/bespoke-free-text-voice-reveal-layout-issues.md) [~W]

## Related Designs

- [Bespoke: a five-stage pipeline that regenerates a complete industry-personalized lecture video from a seed transcript](bespoke-lecture-video-generation-pipeline.md)
- [Semi-automated three-stage human-in-the-loop pipeline for generating dialogue-based TTS lesson videos](semi-automated-tts-lesson-generation-pipeline.md)

## Examples
-

## Key Sources
- Lin, Yi-Cheng; Guo, Yu-Kai; Chen, Szu-Chi; Feng, Bo-Han; Hsu, Yun-Man; Hsieh, Hsiang; Lin, Yu-Jung; Wu, Yue-Ling; Dong, Jia-Kai; Cheng, An-Yu; Huang, Yu-Han; Ieong, Lok-Lam; Chen, Kuan-Yu; Tchouang, Ming-Douo; Sun, Shao-Hua; Lin, Che; Ding, Jian-Jiun; Lee, Hung-yi. (2026). Findings of the First Teaching Monster Challenge: A Benchmark of Pedagogical Content Knowledge in AI Agents. arXiv. https://arxiv.org/abs/2608.08852

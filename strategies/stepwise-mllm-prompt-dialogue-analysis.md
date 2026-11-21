---
type: strategy
id: stepwise-mllm-prompt-dialogue-analysis
title: "Stepwise prompt-dialogue workflow: start with a comprehensive prompt, then refine through focused interactive dialogue"
description: For AI-assisted analysis of mini-lab data, the article recommends a staged prompting workflow.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: jochen-kuhn-2025
    resource: "https://arxiv.org/abs/2508.16320"
    title: "Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt. (2025). AI-Supported Mini-Labs: Combining Smartphone-Based Experiments and Multimodal AI. https://arxiv.org/abs/2508.16320"
    author: "Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt"
---

# Stepwise prompt-dialogue workflow: start with a comprehensive prompt, then refine through focused interactive dialogue

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
For AI-assisted analysis of mini-lab data, the article recommends a staged prompting workflow. For initial analyses it is "advisable to proceed step by step in dialogue with the model", which lets students understand the analysis process and gain insight into how the AI works; afterwards, more structured, adaptable prompts can be used. In the drag-coefficient example the authors used a middle ground: a comprehensive initial prompt followed by stepwise refining prompts in interactive dialogue (smoothing and regression, computing coefficients, comparing with literature values, explaining anomalies).

## Design Implications

### Context
#### Requirements
- Students need only basic knowledge of prompt engineering, without having to learn additional software tools or complex computational methods
#### Constraints
- 

### Target Learners
- secondary school physics students

### Target Learning Goals
- understanding the data-analysis process and insight into how the AI works while analyzing experimental data

## Claims

- [MLLM-supported analysis offers advantages over conventional methods: time savings, high-quality exportable visualizations, and access to analyses beyond school mathematics](../claims/mllm-analysis-advantages-over-conventional.md) [+W]
- [MLLM-based analysis of smartphone accelerometer data aligns with conventional spreadsheet analysis of the same dataset](../claims/mllm-analysis-matches-spreadsheet-drag-coefficient.md) [+W]
- [MLLMs can analyze alternative experimental data formats, including WAV audio files and video, enabling classroom-scale analyses](../claims/mllm-handles-audio-video-data-formats.md) [+W]

## Related Strategies

- [Three-stage hybrid workflow: API batch review, identification of doubtful cases, focused conversational teacher review](three-stage-hybrid-ai-assessment-workflow.md)
- [Use iterative prompt engineering mirroring human coders' labeling processes to refine LLM classification prompts](iterative-prompt-engineering-mirroring-human-coder-refinement.md)
- [Teachers iteratively refine LLM-simulated student ideas with classroom context before instructional use](iterative-teacher-llm-refinement-strategy.md)
- [Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding](structured-prompts-clear-construct-definitions-llm-labeling.md)

## Examples
-

## Key Sources
- Jochen Kuhn, David J. Rakestraw, Stefan Küchemann & Patrik Vogt. (2025). AI-Supported Mini-Labs: Combining Smartphone-Based Experiments and Multimodal AI. https://arxiv.org/abs/2508.16320

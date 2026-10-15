---
type: design
id: llm-llama-skill-extraction-workflow
title: LLM-based project skill extraction workflow using a fine-tuned Llama 3.2 instruct model
description: "A component that parses sponsor-provided project descriptions and asks an LLM to rate the necessity of each skill on a 0–5 scale, where \"a 5 is given when a skill is realistically indispensable for a project.\" The imp..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: brandon-pardi-2026
    resource: "https://arxiv.org/abs/2606.15572"
    title: "Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572"
    author: Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar
---

# LLM-based project skill extraction workflow using a fine-tuned Llama 3.2 instruct model

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A component that parses sponsor-provided project descriptions and asks an LLM to rate the necessity of each skill on a 0–5 scale, where "a 5 is given when a skill is realistically indispensable for a project." The implementation "uses a preexisting fine-tuned instruct version of Llama 3.2" and produces "a structured JSON list of skills and their rated necessity, that is then manually reviewed and given minor or no corrections." The prompt includes caveats about multiple possible solution paths (e.g., Pytorch or Tensorflow) so the model considers multiple potential solutions.

## Design Implications

### Context
#### Requirements
- The same skill list given to students is sent to the LLM with each project description
- Manual review of the LLM's structured JSON skill ratings
#### Constraints
- The article notes LLM-generated project skills still require manual verification

### Target Learners
- senior-level computer science capstone students

### Learning Goals
- accurate skill-to-project alignment in team formation

### Claims

- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](../claims/score-wise-bias-regression-to-mean-awe.md) [~W]
- [LLaMA's LoRA adaptation compresses its prediction range to roughly 2.0–4.0, while Gemma maintains a broader distribution closer to the ground truth](../claims/llama-prediction-range-compression.md) [~W]

## Related Designs

- [Three-stage methodology combining student surveys, LLM skill extraction, and dynamic preference-aware matching](three-stage-llm-team-formation-methodology.md)

## Examples
-

## Key Sources
- Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572

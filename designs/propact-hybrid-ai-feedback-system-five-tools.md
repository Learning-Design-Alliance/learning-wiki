---
type: design
id: propact-hybrid-ai-feedback-system-five-tools
title: ProPACT Hybrid-AI feedback system with five feedback tools and hierarchical trigger policy
description: "The feedback system is a Hybrid-AI framework that \"combines data-driven forecasting with rule-based pedagogical decision-making\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: anahita-golrang-2026
    resource: "https://arxiv.org/abs/2605.02703"
    title: "Anahita Golrang, Kshitij Sharma, Simon Dehaen, Olga Viberg. (2026). ProPACT: A Proactive AI-Driven Adaptive Collaborative Tutor for Pair Programming. https://arxiv.org/abs/2605.02703"
    author: Anahita Golrang, Kshitij Sharma, Simon Dehaen, Olga Viberg
---

# ProPACT Hybrid-AI feedback system with five feedback tools and hierarchical trigger policy

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The feedback system is a Hybrid-AI framework that "combines data-driven forecasting with rule-based pedagogical decision-making". An XGBoost model predicts JVA, JME, and ME over a 30-second horizon; predictions are discretized against each participant's resting baseline using a ±2SD criterion and mapped against a desired collaboration matrix to predefined trigger conditions. Five feedback tools are integrated: GitHub Copilot autocomplete, dual text selection, a gaze-awareness tool, a dialogue prompt, and a last-resort task-based hint, selected via a top-down hierarchical policy prioritizing minimal intervention.

## Design Implications

### Context
#### Requirements
- A desired collaboration matrix and predefined trigger conditions (e.g., gaze-awareness triggered when JVA = Low, dialogue prompt when JME = Low, task-based hint when both MEs = High)
- Per-participant resting baselines for the ±2SD discretization of predicted states
#### Constraints
- The task-based hint is used only as a last-resort intervention, triggered when less intrusive scaffolds fail and both collaborators exhibit sustained extreme mental-effort levels

### Target Learners
- Undergraduate or master's computer science and engineering students pair programming on debugging tasks

### Learning Goals
- Restoring joint attention and cognitive alignment during collaborative debugging

### Claims
- Propact Dyadic Forecast Driven Adaptivity Framework [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Anahita Golrang, Kshitij Sharma, Simon Dehaen, Olga Viberg. (2026). ProPACT: A Proactive AI-Driven Adaptive Collaborative Tutor for Pair Programming. https://arxiv.org/abs/2605.02703

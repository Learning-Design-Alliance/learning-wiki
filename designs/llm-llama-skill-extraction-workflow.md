---
type: design
id: llm-llama-skill-extraction-workflow
title: LLM-based project skill extraction workflow using a fine-tuned Llama 3.2 instruct model
description: "A component that parses sponsor-provided project descriptions and asks an LLM to rate the necessity of each skill on a 0–5 scale, where \"a 5 is given when a skill is realistically indispensable for a project.\" The imp..."
status: draft
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
> **Evidence** · no claims cited

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
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572

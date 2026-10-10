---
type: design
id: three-stage-llm-team-formation-methodology
title: Three-stage methodology combining student surveys, LLM skill extraction, and dynamic preference-aware matching
description: "The article proposes a data-driven team-formation framework with three stages: \"student surveys to capture detailed and granular skill sets and project preferences; (2) LLM-driven extraction of essential project skill..."
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

# Three-stage methodology combining student surveys, LLM skill extraction, and dynamic preference-aware matching

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a data-driven team-formation framework with three stages: "student surveys to capture detailed and granular skill sets and project preferences; (2) LLM-driven extraction of essential project skills from sponsor-provided descriptions; and (3) a dynamic matching algorithm that iteratively prioritizes currently unfulfilled skills and integrates student preferences during team formation." It is positioned as combining bottom-up student agency with top-down project skill requirements in a single scalable pipeline, addressing gaps in tools like CATME Team-Maker that do not match skills to projects or dynamically integrate preferences.

## Design Implications

### Context
#### Requirements
- Students complete skill and preference surveys at the start of the course, with project summary descriptions available beforehand
- A skill list predetermined from prior and anticipated project requirements
- LLM-generated skill ratings are manually reviewed before use
#### Constraints
- Relies on self-reported skills and preferences, leaving it vulnerable to misrepresentation
- The preference weight parameter requires manual tuning
- LLM-generated project skills still require manual verification

### Target Learners
- senior-level computer science capstone students

### Learning Goals
- effective team formation for project-based learning
- student motivation and agency through preference alignment

### Claims
- [Dynamic Skill Matching Higher Skill Coverage](../claims/dynamic-skill-matching-higher-skill-coverage.md) [+M]
- [Manual Assignment Highest Preference Satisfaction](../claims/manual-assignment-highest-preference-satisfaction.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Brandon Pardi, Garret Castro, Michael Pisman, Avash Adhikari, and Santosh Chandrasekhar. (2026). Improving Capstone Team Outcomes through Dynamic Skill Matching and Preference Alignment. https://arxiv.org/abs/2606.15572

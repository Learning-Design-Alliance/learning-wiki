---
type: design
id: human-in-the-loop-genai-mcq-workflow
title: Eight-stage human-in-the-loop workflow for developing, reviewing, administering, and evaluating GenAI-assisted MCQs
description: "A prespecified workflow described in the article's Table 3 for producing human-edited GenAI-assisted MCQs."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
sources:
  - id: sze-kai-ping-2026
    resource: "https://doi.org/10.2196/100179"
    title: "Sze Kai Ping, Lim Jia Qing, Loke Yng Miin, Ding Teck Yong Gabriel, Wee Wei Chieh, Chen Tongyuan, Wu Jingkai Lawrence, Bansal Vivek, Fong Qi Wei, Chow Minyang. (2026). Human-Edited Generative AI-Assisted Multiple-Choice Questions in Postgraduate Family Medicine: Blinded Cross-Sectional Comparative Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/100179"
    author: Sze Kai Ping, Lim Jia Qing, Loke Yng Miin, Ding Teck Yong Gabriel, Wee Wei Chieh, Chen Tongyuan, Wu Jingkai Lawrence, Bansal Vivek, Fong Qi Wei, Chow Minyang
---

# Eight-stage human-in-the-loop workflow for developing, reviewing, administering, and evaluating GenAI-assisted MCQs

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
A prespecified workflow described in the article's Table 3 for producing human-edited GenAI-assisted MCQs. It runs from educator-defined blueprint and topic selection through structured GenAI prompting of ChatGPT-5.1, draft item generation, educator review and editing, option-set engineering of distractors, blinded trainee administration, empirical item analysis, and an item-bank decision to "Accept, revise, quarantine, or retire items based on expert and empirical evidence." The final items represent a human-in-the-loop workflow rather than raw AI-generated outputs.

## Design Implications

### Context
#### Requirements
- Educator specification of AKT topic, learning objective, and expected reasoning level before prompting
- A structured educator review-and-editing round covering clinical accuracy, local guideline concordance, phrasing, key defensibility, and single-best-answer structure
- Option-set engineering reviewing distractors for authentic misconceptions, common reasoning errors, homogeneity, cueing, and near-miss plausibility
#### Constraints
- Editors were not blinded to item origin during item development; blinding was applied only at the participant-assessment stage

### Target Learners
- Postgraduate family medicine doctors preparing for the FM Applied Knowledge Test

### Learning Goals
- Generation and quality assurance of single-best-answer MCQs for postgraduate applied knowledge assessment

### Claims
- [Genai Mcq Lower Total Scores](../claims/genai-mcq-lower-total-scores.md) [+M]

## Related Designs
- Genai Drafting Adjunct Educator Led Workflow

## Examples
-

## Key Sources
- Sze Kai Ping, Lim Jia Qing, Loke Yng Miin, Ding Teck Yong Gabriel, Wee Wei Chieh, Chen Tongyuan, Wu Jingkai Lawrence, Bansal Vivek, Fong Qi Wei, Chow Minyang. (2026). Human-Edited Generative AI-Assisted Multiple-Choice Questions in Postgraduate Family Medicine: Blinded Cross-Sectional Comparative Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/100179

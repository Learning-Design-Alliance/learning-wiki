---
type: design
id: intelligent-digital-textbook-llm-structured-dialogue
title: Intelligent digital textbook framework with LLM-powered structured dialogue for reading comprehension support
description: The learning engineer collaborators are developing a framework for intelligent digital textbooks augmented with AI capabilities.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: adam-coscia-2026
    resource: "https://arxiv.org/abs/2608.04006"
    title: "Adam Coscia, Sujata Duwal, Langdon Holmes, Scott Crossley, and Alex Endert. (2026). Calibrating Trustworthiness: Co-Designing Metrics and Visualizations for Evaluating LLMs in Education. https://arxiv.org/abs/2608.04006"
    author: Adam Coscia, Sujata Duwal, Langdon Holmes, Scott Crossley, and Alex Endert
---

# Intelligent digital textbook framework with LLM-powered structured dialogue for reading comprehension support

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The learning engineer collaborators are developing a framework for intelligent digital textbooks augmented with AI capabilities. Learners write a summary after reading each page, scored by a finetuned ModernBERT model. If below the passing threshold, a structured dialogue sequence triggers: the learner re-reads a selected passage, then the LLM agent Llama3 generates a self-explanation reading training question, followed by a follow-up question and summary revision advice grounded in the passage and dialogue.

## Design Implications

### Context
#### Requirements
- Smaller, local LLMs are used to enable lower cost, private deployments with protected student data
#### Constraints
- Smaller models often struggle to follow prompt instructions in the same way larger, proprietary models do

### Target Learners
- K-12 and higher education students reading digital textbooks

### Learning Goals
- reading comprehension through self-explanation
- summary writing and revision

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Adam Coscia, Sujata Duwal, Langdon Holmes, Scott Crossley, and Alex Endert. (2026). Calibrating Trustworthiness: Co-Designing Metrics and Visualizations for Evaluating LLMs in Education. https://arxiv.org/abs/2608.04006

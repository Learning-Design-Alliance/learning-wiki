---
type: strategy
id: vibe-coding-rapid-educational-tool-development
title: Use an AI-assisted vibe coding workflow with human pedagogical control to move educational tools from idea to classroom within days
description: The strategy is to develop teacher-facing educational tools through natural-language prompting of an AI app builder (Lovable), with prompts drafted via an LLM (ChatGPT 5.2) and reviewed by a human author who defines i...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: heidi-taveter-and-marina-lepp-2026
    resource: "https://arxiv.org/abs/2607.24757"
    title: "Heidi Taveter and Marina Lepp. (2026). From Idea to Classroom in Days: Using “Vibe Coding” to Create a Programming Process Visualizer from IDE Activity Logs. https://arxiv.org/abs/2607.24757"
    author: Heidi Taveter and Marina Lepp
---

# Use an AI-assisted vibe coding workflow with human pedagogical control to move educational tools from idea to classroom within days

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The strategy is to develop teacher-facing educational tools through natural-language prompting of an AI app builder (Lovable), with prompts drafted via an LLM (ChatGPT 5.2) and reviewed by a human author who defines instructional needs, selects features, evaluates generated functionality, and writes the next prompts. In this workflow "AI assistance lowered the technical barrier and accelerated implementation, while pedagogical reasoning, feature selection, and judgments about usefulness remained under human control." Development proceeded feature by feature, with each new view or component tested before the next was developed.

## Design Implications

### Context
#### Requirements
- A human with pedagogical and programming knowledge who defines instructional needs, evaluates generated functionality, and writes and reviews prompts
- Repeated testing with real data (diverse Thonny log files) and refinement through further prompting and revision
#### Constraints
- Testing generated functionality required more time and additional prompts than producing it; extra effort was needed to account for differences in log structure, such as between older and newer Thonny versions and different operating systems

### Target Learners
- instructors and education-focused teams developing classroom tools

### Target Learning Goals
- rapid operationalization of learning-analytics research into classroom-ready instructional tools

## Related Strategies

- [Teachers iteratively refine LLM-simulated student ideas with classroom context before instructional use](iterative-teacher-llm-refinement-strategy.md)
- [Use generative AI as a no-code development tool so instructors can design laboratory software around their own pedagogical objectives](ai-nocode-lab-software-development.md)
- [Use structured, human-in-the-loop prompting governance (such as NLD-P) with systematic human review to preserve authorship boundaries in AI-assisted research](human-in-control-llm-research-workflow.md)
- [Treat AI-generated lesson plans as drafts requiring teacher evaluation, adaptation, and pedagogical judgment](ai-lesson-plans-as-drafts-requiring-teacher-adaptation.md)
- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)

## Examples
-

## Key Sources
- Heidi Taveter and Marina Lepp. (2026). From Idea to Classroom in Days: Using “Vibe Coding” to Create a Programming Process Visualizer from IDE Activity Logs. https://arxiv.org/abs/2607.24757

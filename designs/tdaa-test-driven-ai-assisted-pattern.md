---
type: design
id: tdaa-test-driven-ai-assisted-pattern
title: "TDAA: high-frequency closed-book tests paired with a human-reviewed AI production harness"
description: "TDAA is a course-level design pattern coupling two cycles: students prepare with aligned materials and face a weekly closed-book gate, while an instructor-side AI harness drafts, reviews, and grades the materials unde..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: jin-guo-liu-2026
    resource: "https://arxiv.org/abs/2606.23315"
    title: "Jin-Guo Liu, Shang-Qi Lu, Xin-Ran Shi, Long-Li Zheng, Wei Wang. (2026). Test-Driven, AI-Assisted Learning: Replacing Lectures with Weekly Closed-Book Tests. https://arxiv.org/abs/2606.23315"
    author: Jin-Guo Liu, Shang-Qi Lu, Xin-Ran Shi, Long-Li Zheng, Wei Wang
---

# TDAA: high-frequency closed-book tests paired with a human-reviewed AI production harness

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
TDAA is a course-level design pattern coupling two cycles: students prepare with aligned materials and face a weekly closed-book gate, while an instructor-side AI harness drafts, reviews, and grades the materials under human approval. The paper states the pairing directly: "high-frequency tests preserve individual accountability, while AI agents make material production and marking scalable." Without the agent layer weekly testing is infeasible for one instructor; without the test gate AI-assisted preparation offers no reliable check on unaided performance.

## Design Implications

### Context
#### Requirements
- A visible preparation path of learning sheets and aligned validation practice so the closed-book tests feel fair rather than arbitrary
- A version-controlled agent workspace with human review before any AI draft reaches students
#### Constraints
- Evidence is limited to one small, proof-heavy course without a control group; transfer to large or non-proof courses is a hypothesis for future offerings, not a result

### Target Learners
- upper-level undergraduate data-science students in a proof-heavy course

### Learning Goals
- unaided problem-solving and proof-writing in theory of computation

### Claims
- [Tdaa Student Acceptance Weekly Gate](../claims/tdaa-student-acceptance-weekly-gate.md) [+W]
- [Ai Answer Keys Mostly Correct Git Audit](../claims/ai-answer-keys-mostly-correct-git-audit.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Jin-Guo Liu, Shang-Qi Lu, Xin-Ran Shi, Long-Li Zheng, Wei Wang. (2026). Test-Driven, AI-Assisted Learning: Replacing Lectures with Weekly Closed-Book Tests. https://arxiv.org/abs/2606.23315

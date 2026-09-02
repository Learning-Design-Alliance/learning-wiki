---
type: strategy
id: failure-driven-scaffolding
title: Failure-Driven Scaffolding
description: Explicit, multi-step scaffolds during a pre-instruction problem attempt that deliberately nudge students toward generating a suboptimal solution representation, so the later instruction phase corrects a concrete, self-generated error rather than an abstract gap.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
sources:
  - id: sinha-2022
    resource: "https://doi.org/10.1080/10508406.2021.1964506"
    title: "Sinha, T. (2022). Enriching problem-solving followed by instruction with explanatory accounts of emotions. Journal of the Learning Sciences, 31(2), 151-198."
    author: "Sinha, T."
---

# Failure-Driven Scaffolding

> **Strategy** · [All strategies](index.md)

## Description
Within a [Problem-Solving Followed by Instruction](../theories/problem-solving-followed-by-instruction.md) design, failure-driven scaffolding presents students with a sequence of increasingly suboptimal representations of a task (e.g., histogram → bar chart → 2D histogram for a comparison task better suited to a scatterplot), inverting the usual assumption that a scaffold should make a task easier. The scaffold's purpose is to reliably provoke a specific, informative kind of failure — not to prevent failure — so the later instruction phase has a concrete misconception to correct. This contrasts with success-driven scaffolding, which shapes the same phase toward an increasingly optimal representation (e.g., a prompt → hint → bottom-out syntax sequence), and with unscaffolded productive failure, where students generate their own range of solutions without any directional pressure.

## Design Implications

### Context
#### Requirements
- A task with a genuine "trap": representations or statistics that appear informative but omit or distort what the canonical method reveals (e.g., matched non-parametric statistics that diverge sharply on parametric ones)
- A subsequent instruction phase that explicitly returns to and resolves the specific representation the scaffold induced
#### Constraints
- Deliberately provoking failure increases negative emotions (shame, in particular) relative to success-driven scaffolding — see the linked claim — so the approach should be paired with a de-stigmatizing framing of the pre-instruction attempt as exploratory, not evaluative
- Evidence is from a single study/domain (data visualization statistics); the specific trap-representation design (histogram → bar chart → 2D histogram) does not generalize mechanically to other content

### Target Learners
- Novices to the target concept who have enough general facility with the domain to attempt a representation, per [Problem-Solving Followed by Instruction](../theories/problem-solving-followed-by-instruction.md)

### Target Learning Goals
- Non-isomorphic conceptual understanding and transfer, more than isomorphic (surface-similar) procedural performance
- [Emotion dynamics during problem-solving predict learning outcomes in a manner that depends on scaffolding design](../claims/emotion-dynamics-during-problem-solving-predict-learning-outcomes-context-dependently.md)

### Instructions
1. Design a task with multiple plausible representations, where at least one increasingly suboptimal path is available for scaffolds to steer toward.
2. During the first problem-solving attempt, give all students identical, minimal scaffolding.
3. During a second attempt, provide failure-driven scaffolds (successively more suboptimal representational prompts) to the experimental group.
4. Follow with direct instruction that explicitly revisits and corrects the representation the scaffolds induced.
5. Assess isomorphic understanding, non-isomorphic understanding, and transfer separately, since failure-driven scaffolding's benefits (where present) concentrate on the latter two.

## Related Strategies
- (none yet linked)

## Examples
- A bivariate data-ranking task (rank companies by "success" using matched non-parametric but divergent parametric statistics) in which failure-driven scaffolds presented histogram → bar chart → 2D histogram representations, compared against success-driven scaffolds (Wikipedia prompt → hint → scatterplot syntax) and unscaffolded productive failure.

## Key Sources
- Sinha, T. (2022). Enriching problem-solving followed by instruction with explanatory accounts of emotions. *Journal of the Learning Sciences, 31*(2), 151-198. [https://doi.org/10.1080/10508406.2021.1964506](https://doi.org/10.1080/10508406.2021.1964506)

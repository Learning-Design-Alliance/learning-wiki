---
type: goal-map
title: "Learning Commons — Fractions Concept Knowledge Graph (Subset)"
description: Flattened goal map of a prerequisite-structured math concept graph covering early fraction understanding.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-30
source:
  framework: "Learning Commons Math Knowledge Graph"
  kind: graph
  version: illustrative
  source_url: null
  license: "Unknown — confirm before real ingest"
nodes:
  - id: math-whole-number-sense
    display_id: "1"
    label: Whole number sense and counting
    competency_framework: "Learning Commons Math KG"
  - id: math-equal-partitioning
    display_id: "2"
    label: Partition a whole into equal-sized parts
    competency_framework: "Learning Commons Math KG"
  - id: math-unit-fractions
    display_id: "3"
    label: Represent a unit fraction as one equal part of a whole
    student_facing_label: Understand what 1/4 means
    competency_framework: "Learning Commons Math KG"
  - id: math-fraction-number-line
    display_id: "4"
    label: Locate a fraction as a point on a number line
    competency_framework: "Learning Commons Math KG"
  - id: math-equivalent-fractions
    display_id: "5"
    label: Generate and recognize equivalent fractions
    competency_framework: "Learning Commons Math KG"
  - id: math-compare-fractions
    display_id: "6"
    label: Compare fractions with unlike denominators
    competency_framework: "Learning Commons Math KG"
  - id: math-add-fractions-like-denom
    display_id: "7"
    label: Add and subtract fractions with like denominators
    competency_framework: "Learning Commons Math KG"
  - id: math-add-fractions-unlike-denom
    display_id: "8"
    label: Add and subtract fractions with unlike denominators
    competency_framework: "Learning Commons Math KG"
    assessment_suggestion: Multi-step word problem requiring a common denominator before combining quantities.
relationships:
  - source: math-whole-number-sense
    target: math-equal-partitioning
    type: prerequisite
  - source: math-equal-partitioning
    target: math-unit-fractions
    type: prerequisite
  - source: math-unit-fractions
    target: math-fraction-number-line
    type: prerequisite
  - source: math-unit-fractions
    target: math-equivalent-fractions
    type: prerequisite
  - source: math-equivalent-fractions
    target: math-compare-fractions
    type: prerequisite
  - source: math-equivalent-fractions
    target: math-add-fractions-like-denom
    type: prerequisite
  - source: math-compare-fractions
    target: math-add-fractions-unlike-denom
    type: prerequisite
  - source: math-add-fractions-like-denom
    target: math-add-fractions-unlike-denom
    type: prerequisite
---

# Learning Commons — Fractions Concept Knowledge Graph (Subset)

> **Illustrative placeholder.** This is a plausible, commonly-taught fraction-learning sequence, not pulled from a specific named "Learning Commons" dataset — substitute the real source's node set and edges once identified.

## Description
An early-fractions concept graph normalized into this wiki's flat goal-map schema. Unlike the ESCO and ExploreSEL examples, this source is almost entirely `prerequisite` edges rather than `default` (hierarchical) ones — a knowledge graph like this describes an acquisition *order* over concepts, not a part-of hierarchy, which is exactly the distinction the two Lazuli relationship types are built to carry.

## Related Wiki Pages
- The strict prerequisite chaining here mirrors [Scaffolding](../elements/scaffolding.md) and [Fading Scaffolding](../elements/fading-scaffolding.md): each node is the load-bearing support for the next.
- Splitting fraction addition into like-denominator before unlike-denominator sub-goals is a direct application of [Chunking Reduces Working Memory Load](../claims/chunking-reduces-working-memory-load.md).
- Concrete instructional sequencing for these nodes should use [Worked Examples](../elements/worked-examples.md).

## Key Sources
- Illustrative only — replace with the actual source dataset's citation once identified.

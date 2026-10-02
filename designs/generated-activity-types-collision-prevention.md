---
type: design
id: generated-activity-types-collision-prevention
title: Automated generation of seven vocabulary activity types with distractor collision prevention
description: During each training session the algorithm selects target words from the P, S, and L sets and generates activities optimizing predicted learning gains.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
sources:
  - id: evgeny-chukharev-hudilainen-and-tatiana-a-klepikova-2016
    resource: "https://doi.org/10.1558/cj.v33i3.26055"
    title: "Evgeny Chukharev-Hudilainen and Tatiana A. Klepikova. (2016). The effectiveness of computer-based spaced repetition in foreign language vocabulary instruction: a double-blind study. calico journal vol 33.3. https://doi.org/10.1558/cj.v33i3.26055"
    author: Evgeny Chukharev-Hudilainen and Tatiana A. Klepikova
---

# Automated generation of seven vocabulary activity types with distractor collision prevention

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
During each training session the algorithm selects target words from the P, S, and L sets and generates activities optimizing predicted learning gains. "At the time of the experiment, the system was capable of generating seven types of activities", including multiple-choice matching in both directions, spelling from an L1 prompt, two listening comprehension tasks, semantic sorting, and fill-in-the-blank sentence completion. A distinctive design feature is collision prevention: "To avoid collisions, WordNet data (Miller, 1995) is used to exclude synonyms and direct hypernyms/hyponyms of the target word from the inventory of possible distractors", while paronyms are given preference to help students distinguish them.

## Design Implications

### Context
#### Requirements
- WordNet data and Levenshtein-distance heuristics over glosses are needed for distractor selection; semantic information must be available for a unit to appear in semantics-dependent activity types, with graceful fallback to simpler types otherwise.
#### Constraints
- The absence of vocabulary production exercises and the limited support for productive use are explained by inherent limitations of automated processing of natural language semantics.

### Target Learners
- EFL students working with automatically generated vocabulary activities

### Target Goals
- Form-meaning mapping, spelling, listening recognition, and semantic classification of target vocabulary

### Claims

- [Posttest scores increase monotonically across the tutoring algorithm's acquisition stages, supporting its stage criteria, though control-group items did not differ from items still in active acquisition](../claims/tutoring-stage-thresholds-validated-by-posttest.md) [+W]
- [Lexical units brought to the 'fully learned' stage by the tutor scored significantly lower on the posttest than units students already knew before introduction](../claims/learned-units-below-previously-known-units.md) [-W]
- [Supplemental computer-based spaced repetition activities nearly triple long-term vocabulary retention in EFL students compared with conventional instruction alone](../claims/spaced-repetition-supplement-triples-vocabulary-retention.md) [+W]

## Related Patterns

- [Five-phase retrieval practice session crossing question format and level of thinking](five-phase-retrieval-practice-session-format-by-level-of-thinking.md)

## Examples
-

## Key Sources
- Evgeny Chukharev-Hudilainen and Tatiana A. Klepikova. (2016). The effectiveness of computer-based spaced repetition in foreign language vocabulary instruction: a double-blind study. calico journal vol 33.3. https://doi.org/10.1558/cj.v33i3.26055

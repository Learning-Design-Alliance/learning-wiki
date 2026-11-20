---
type: product
id: moon
title: MOON
description: MOON is a JupyterLab plugin developed by Christophe Casseau and colleagues that guides students through teacher-authored notebook execution scenarios using visual status cues, navigation controls, and backtracking.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
---

# MOON

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
MOON is a JupyterLab plugin developed by Christophe Casseau and colleagues that guides students through teacher-authored notebook execution scenarios using visual status cues, navigation controls, and backtracking.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **MOON scenario scripting language with three composable execution patterns**: The article introduces a scripting language, built on deterministic finite automata, that lets teachers formalize the expected usage of a notebook's code cells. From an analysis of about one hundred GitHub and Kaggle notebooks with reader instructions, the authors "identified three main patterns for cell execution: i) linear execution, ii) non-linear execution, and iii) optional execution", expressed with parentheses, square brackets and a question-mark operator respectively, which can be composed to express full notebook scenarios. The script is interpreted at runtime to drive the visual assistance. (Christophe Casseau et al. (2023))

### Claims
- [MOON visual assistance increases students' compliance with an educational notebook's intended execution scenario](../claims/moon-increases-notebook-scenario-compliance.md) [+M]
- [MOON does not hinder students' progression through the notebook (no significant completeness difference)](../claims/moon-no-completeness-hindrance.md) [+M]
- [Most surveyed students perceived MOON as useful and reported it helped them follow the execution order](../claims/moon-user-study-perceived-usefulness.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Christophe Casseau, Jean-Rémy Falleri, Thomas Degueule and Xavier Blanc. (2023). MOON: Assisting Students in Completing Educational Notebook Scenarios. https://arxiv.org/abs/2309.16201

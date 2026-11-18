---
type: design
id: acsp-explanation-functionality
title: "ACSP explanation functionality: six dynamically generated why/how explanation pages in a tab-based incremental interface"
description: The explanation functionality is an addition to the ACSP applet that lets students access explanations of the AI-driven adaptive hints.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: cristina-conati-2024
    resource: "https://www.ubc.ca"
    title: "Cristina Conati, Oswald Barral, Vanessa Putnam, Lea Rieger. (2024). Toward Personalized XAI: A Case Study in Intelligent Tutoring Systems. Preprint submitted to the JAI – Special Issue on Explainable Artificial Intelligence. https://www.ubc.ca"
    author: Cristina Conati, Oswald Barral, Vanessa Putnam, Lea Rieger
---

# ACSP explanation functionality: six dynamically generated why/how explanation pages in a tab-based incremental interface

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The explanation functionality is an addition to the ACSP applet that lets students access explanations of the AI-driven adaptive hints. It is structured around three tabs, each providing a self-contained incremental why explanation (WhyHint, WhyLow, WhyRules), with three how pages (HowScore, HowHint, HowRank) reachable from the second tab. Each explanation is "dynamically derived from the current state of the underlying ACSP AI models, as they evolve based on the user's real-time interaction". Users can give feedback via an "I would have liked to know more" button on every page.

## Design Implications

### Context
#### Requirements
- Explanations are triggered by clicking the button "Why am I delivered this hint?" after a hint is delivered
- The design relies on Kulesza et al.'s criteria of iterative, sound, complete, and not overwhelming explanations, prioritizing why over how explanations to avoid excessive complexity
#### Constraints
- The article states the design sacrifices completeness when needed to avoid excessive complexity; the Behavior Discovery algorithms (clustering, rule extraction) are deliberately not explained

### Target Learners
- University students with computer science knowledge sufficient to learn constraint satisfaction problems

### Learning Goals
- Learning the AC-3 algorithm for solving constraint satisfaction problems
- More effective use of the ACSP applet's interactive tools

### Claims
- [Pilot Why Explanations Most Requested](../claims/pilot-why-explanations-most-requested.md) [+M]
- [Acsp Explanation Usage Patterns](../claims/acsp-explanation-usage-patterns.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Cristina Conati, Oswald Barral, Vanessa Putnam, Lea Rieger. (2024). Toward Personalized XAI: A Case Study in Intelligent Tutoring Systems. Preprint submitted to the JAI – Special Issue on Explainable Artificial Intelligence. https://www.ubc.ca

---
type: claim
title: In DKT-simulated curricula on Assistments, blocking outperformed mixing, and deeper lookahead (MDP-8) yielded higher predicted knowledge than blocking
description: In DKT-simulated curricula on Assistments, blocking outperformed mixing, and deeper lookahead (MDP-8) yielded higher predicted knowledge than blocking
id: dkt-curriculum-blocking-mixing-mdp
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-14
evidence_strength: weak
sources:
  - id: chris-piech-2015
    resource: "https://github.com/chrispiech/DeepKnowledgeTracing"
    title: "Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing"
    author: Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein
    q: 2
    i: "?"
    kind: theoretical
    rigour: "?"
  - id: chris-piech-2015-2
    resource: "https://github.com/chrispiech/DeepKnowledgeTracing"
    title: "Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing"
    author: Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# In DKT-simulated curricula on Assistments, blocking outperformed mixing, and deeper lookahead (MDP-8) yielded higher predicted knowledge than blocking

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r?` · `q2`

## Subclaims
`q2 i?` In simulations using a trained DKT model, the blocking curriculum strategy had a notable advantage over mixing on Assistments data. [→ Chris Piech 2015](#chris-piech-2015)
`q2 i?` Choosing exercises with expectimax lookahead eight problems deep (MDP-8) produced curricula where students had higher predicted knowledge after solving fewer problems than blocking. [→ Chris Piech 2015 (2)](#chris-piech-2015-2)

## Evidence

### Chris Piech 2015

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `theoretical · r?`

Curriculum simulation on five Assistments concepts: for each method the DKT model simulated how a student would answer, repeating simulations 500 times and measuring average predicted probability of future correctness after 30 exercises.

> "In the Assistment context the blocking strategy had a notable advantage over mixing. See Figure 3(c)."

### Chris Piech 2015 (2)

Chris Piech, Jonathan Bassen, Jonathan Huang, Surya Ganguli, Mehran Sahami, Leonidas Guibas, Jascha Sohl-Dickstein. (2015). Deep Knowledge Tracing. https://github.com/chrispiech/DeepKnowledgeTracing

`q2 · i?` · `design · r?`

Numerical results shown in Figure 3(c): blocking matched expectimax one exercise deep, but deeper lookahead (MDP-8) produced curricula with higher predicted knowledge after fewer problems. Outcomes are model-predicted, not measured student learning.

> "While blocking performs on par with solving expectimax one exercise deep (MDP-1), if we look further into the future when choosing the next problem we come up with curricula where students have higher predicted knowledge after solving fewer problems (MDP-8)."

## Discussion


## Related Claims
-

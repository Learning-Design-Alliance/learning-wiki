---
type: design
id: unicode-perturbation-soft-barrier-families
title: Unicode perturbation families implemented as system-prompt soft barriers
description: The paper implements soft barriers as a system prompt instructing the model to inject specific Unicode characters into user-defined identifiers during generation, leaving keywords, operators, literals, and built-in na...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: iyiola-e-olatunji-alberick-euraste
    resource: "https://doi.org/10.1145/3832783.3834554"
    title: "Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein, and Tegawendé F. Bissyandé. 2026. Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming. Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26). https://doi.org/10.1145/3832783.3834554"
---

# Unicode perturbation families implemented as system-prompt soft barriers

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The paper implements soft barriers as a system prompt instructing the model to inject specific Unicode characters into user-defined identifiers during generation, leaving keywords, operators, literals, and built-in names unchanged. Four families are evaluated: "Invisible chars" (zero-width characters inside identifiers), "Homoglyphs" (ASCII letters replaced by visually identical Unicode equivalents), "BIDI reordering" (directionality overrides altering internal byte order), and "Deletions" (backspace/delete controls erasing adjacent rendered characters). The mechanism requires no model retraining or environment changes.

## Design Implications

### Context
#### Requirements
- Only a system prompt; no model retraining, decoder change, or execution-environment modification
#### Constraints
- Any real deployment should be institutionally approved, disclosed at the policy level, and accessibility-tested; motivated users can bypass via clean-output requests, text normalizers, or retyping

### Target Learners
- programming students using AI coding assistants

### Learning Goals
- discouraging unexamined transfer of AI-generated code
- promoting reading, editing, and reconstruction of generated code

### Claims
- [Soft Barriers Cpr Model Task Dependent](../claims/soft-barriers-cpr-model-task-dependent.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein, and Tegawendé F. Bissyandé. 2026. Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming. Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26). https://doi.org/10.1145/3832783.3834554

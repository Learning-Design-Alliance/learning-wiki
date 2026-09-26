---
type: element
id: prism-production-system-interpreter
title: "PRISM: a production-system interpreter offering user-selectable options at key architecture choice points"
description: "PRISM (Program for Research Into Self-Modifying Systems), developed by Pat Langley and the author, is a production-system interpreter implemented by augmenting LISP, owing a major debt to Forgy's OPS4."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: neches-1982
    resource: "https://eric.ed.gov/?id=ED217874"
    title: "Neches, Robert. (1982). Simulation Systems for Cognitive Psychology. Learning Research and Development Center, University of Pittsburgh. https://eric.ed.gov/?id=ED217874"
    author: Neches, Robert
---

# PRISM: a production-system interpreter offering user-selectable options at key architecture choice points

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
PRISM (Program for Research Into Self-Modifying Systems), developed by Pat Langley and the author, is a production-system interpreter implemented by augmenting LISP, owing a major debt to Forgy's OPS4. Its design philosophy is that "thereare too many. Unresolvedquestionsabout the detailsofhow a production system. should work," so instead of fixing one architecture it identifies key choice points, offers plausible options, and lets sophisticated users implement alternatives. It expands the traditional data-memory/production-memory recognize-act cycle with user-controlled options such as three spreading-activation schemes (spread-to-depth, spread-to-limit, and directed activation) and split memory-modification operations (add-to-wm, add-to-net, add-connections).

## Design Implications

### Context
#### Requirements
- Users must specify the details of the class of production-system theories they want, selecting options at the architecture's choice points
#### Constraints
- PRISM is not a whole-system simulation of a particular information processing theory; it defines a class of theories

### Target Learners
- cognitive psychology researchers building production-system simulation models

### Target Learning Goals
- implementing and exploring alternative production-system architectures for psychological simulation

## Related Elements
- [Caps Production System Language](caps-production-system-language.md)

## Examples
-

## Key Sources
- Neches, Robert. (1982). Simulation Systems for Cognitive Psychology. Learning Research and Development Center, University of Pittsburgh. https://eric.ed.gov/?id=ED217874

---
type: element
id: caps-production-system-language
title: "CAPS: a LISP-based collaborative activation-based production system for concurrent processing of hypotheses at multiple levels"
description: CAPS (Collaborative Activation-based Production System) is the LISP interpreter Thibadeau built to implement the READER model of reading.
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

# CAPS: a LISP-based collaborative activation-based production system for concurrent processing of hypotheses at multiple levels

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
CAPS (Collaborative Activation-based Production System) is the LISP interpreter Thibadeau built to implement the READER model of reading. Its fundamental processing units are productions, independent condition-action rules; its data objects are node-relation-node propositions with activation levels representing confidence. Productions fire on every cycle while their conditions hold, transmitting activation as a proportion of an evoking proposition's activation, and actions like <REWEIGHT> let the system modify activation flow rates and acceptance thresholds. The paper presents it as "a very general 'processinglanguageforimplementing a large Class of models based on a tommon theoretical'framework."

## Design Implications

### Context
#### Requirements
- Productions specify propositions with threshold activation levels below which they will not execute
#### Constraints
- Activation transmission proportions are multipliers for a global parameter adjustable via <REWEIGHT>

### Target Learners
- cognitive psychology researchers building simulation models of reading and other information-processing tasks

### Target Learning Goals
- modeling hypothesis activation, control processes, and focus of attention in cognitive simulation

## Related Elements
- 

## Examples
-

## Key Sources
- Neches, Robert. (1982). Simulation Systems for Cognitive Psychology. Learning Research and Development Center, University of Pittsburgh. https://eric.ed.gov/?id=ED217874

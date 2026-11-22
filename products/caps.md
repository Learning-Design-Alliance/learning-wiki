---
type: product
id: caps
moved_from: [element/caps-production-system-language]
title: CAPS
description: CAPS is a LISP-based interpreter and production-system software developed by Thibadeau to implement the READER model and related cognitive-processing models.
product_kind: software
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: neches-1982
    resource: "https://eric.ed.gov/?id=ED217874"
    title: "Neches, Robert. (1982). Simulation Systems for Cognitive Psychology. Learning Research and Development Center, University of Pittsburgh. https://eric.ed.gov/?id=ED217874"
    author: Neches, Robert
---

# CAPS

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
CAPS is a LISP-based interpreter and production-system software developed by Thibadeau to implement the READER model and related cognitive-processing models.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Italian adaptation of the CAPS-14 (Child-Adolescent Perfectionism Scale)**: A 14-item Italian self-report adaptation of the Child-Adolescent Perfectionism Scale for assessing perfectionism in young people. The article states "The scale includes fourteen items divided into three subscales: SPP, SOP-Critical and SOP-Striving", each rated on a 5-point Likert scale from 1 (not at all true of me) to 5 (very true of me). Translation used forward and back-translation procedures, and the study reports Cronbach's alphas ranging from .65 to .81 across subscales and groups. (Vecchione Michele (2021))

### Claims
- [The CAPS-14 shows configural and full metric invariance, partial scalar invariance, and structural invariance across middle and high school students](../claims/caps14-measurement-invariance-grade-levels.md) [+M]

## Related Products and Programmes

- [PRISM (Program for Research Into Self-Modifying Systems)](prism-program-for-research-into-self-modifying-systems.md)

## Key Sources
- Neches, Robert. (1982). Simulation Systems for Cognitive Psychology. Learning Research and Development Center, University of Pittsburgh. https://eric.ed.gov/?id=ED217874
<!-- merged 2026-10-10 from elements/caps-production-system-language ("CAPS: a LISP-based collaborative activation-based production system for concurrent processing of hypotheses at multiple levels"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Vecchione Michele, Vacca Mariacarolina. (2021). An Italian adaptation of the Child-Adolescent Perfectionism Scale: Testing measurement invariance across grade levels and exploring associations with academic achievement. PLoS ONE. https://doi.org/10.1371/journal.pone.0255814

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

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- 

## Related Elements

- [PRISM: a production-system interpreter offering user-selectable options at key architecture choice points](prism-program-for-research-into-self-modifying-systems.md)

## Examples
-

## Key Sources
- Neches, Robert. (1982). Simulation Systems for Cognitive Psychology. Learning Research and Development Center, University of Pittsburgh. https://eric.ed.gov/?id=ED217874
-->

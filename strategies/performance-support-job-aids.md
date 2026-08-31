---
type: strategy
title: Performance Support Job Aids
description: Job aids provide just-in-time procedural guidance at the moment of task performance, shifting the instructional burden from memorization to external reference.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Performance Support Job Aids

> **Strategy** · [All strategies](index.md)

## Description
Performance support job aids are external resources — checklists, quick-reference cards, decision trees, embedded tooltips, wizards — that deliver task-relevant information at the moment of need, in the workflow itself. Rather than training learners to memorize infrequently used procedures, the strategy externalizes those procedures so working memory is spent on execution, not recall. Job aids are typically organized around lookup (find the answer fast) rather than instruction (build understanding).

## Design Implications

Job aids exploit the distinction between information needed for *learning* and information needed for *performance*: when a task is performed rarely, is highly procedural, or carries high error cost, externalizing the steps is more efficient and more reliable than training for retention [~S]. Well-designed aids reduce extraneous load at the point of performance by chunking content into scannable units and presenting only what is needed for the immediate step [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. The design risk is the inverse: aids that substitute for all practice can prevent the retrieval practice that builds durable skill, so designers must decide deliberately which tasks should be internalized and which should remain externalized.

### Context
#### Requirements
- Task analysis identifying which steps are error-prone, infrequent, or hard to remember
- A format matched to the use context: laminated card at the workstation, embedded tooltip, searchable decision tree, mobile micro-guide
- Scannable structure: headings, numbered steps, and visuals organized for lookup under time pressure, not prose for reading ([Clear Structure](../principles/clear-structure.md))
- A maintenance process — stale job aids are worse than none, because users follow outdated steps with confidence

#### Constraints
- Over-reliance on aids for tasks that should be automatized blocks the retrieval practice needed for fluency and transfer [-M] — learners never build the internal schema if every step is externally supplied
- Dense, poorly structured aids add search cost and cognitive load at exactly the moment capacity is scarce [Cognitive overload degrades learning and performance.](../claims/cognitive-overload-degrades-learning.md) [-S]
- Aids cannot compensate for missing conceptual understanding; a user who doesn't grasp *why* a step exists cannot troubleshoot when reality diverges from the script [-M]
- Irrelevant decoration or background information on an aid slows lookup [Coherence principle: irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [-M]

#### Implementation Variability
- **Static aids**: checklists, flowcharts, quick-reference cards — cheap, reliable, no infrastructure
- **Embedded support**: tooltips, contextual help, wizards inside the tool itself — lowest retrieval cost because the aid appears in the work context
- **EPSS (Electronic Performance Support Systems)**: integrated systems combining reference, decision support, and data entry
- **Hybrid designs**: job aid for initial performances, faded over time to build internalization ([Fading](../elements/fading.md))

### Target Learners
- New employees performing a procedure for the first few times, before schemas form
- Experienced performers facing rare, complex, or high-stakes variants of a task (even experts use checklists for infrequent steps) [+M]
- Learners in high-turnover environments where full training for every procedure is not economical

### Target Learning Goals
- Procedural accuracy and consistency on well-defined tasks
- Error reduction in high-stakes execution (aviation, medicine, safety-critical operations)
- *Not* suited as the primary vehicle for conceptual understanding or transferable problem solving

### Instructions
1. Conduct a task analysis to identify steps that are infrequent, error-prone, or costly to memorize — these are job aid candidates; steps needed daily for fluency should stay in training ([Practice](../elements/practice.md))
2. Draft the aid in the performer's sequence, one action per line, using [Procedural Information](../elements/procedural-information.md) conventions (imperative verbs, conditional branches made explicit)
3. Chunk and format for scanning: numbered steps, white space, decision points as flowcharts or if/then tables [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]
4. Place the aid in the workflow — embedded in the tool or physically at the point of use — so retrieval cost approaches zero
5. Pilot with actual users under realistic time pressure and revise based on where they hesitate or misread
6. Decide the fade plan: for tasks that should become automatic, transition from aid-dependent to aid-free performance over successive attempts

## Related Strategies
- [Use Worked Examples](use_worked_examples.md) — worked examples build the schema during training; job aids carry the load afterward — the two should be sequenced, not conflated
- [Checklists](checklists.md) — the most common job aid form, with its own evidence base in high-stakes fields
- [Fading](../elements/fading.md) — governs the transition from external support to internalized skill

## Examples
- **WHO Surgical Safety Checklist** (https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery) — a one-page job aid that reduced surgical complications and mortality in multi-site trials by enforcing critical steps at the moment of incision and closure
- **Atlassian's in-product guidance** (https://www.atlassian.com) — embedded tooltips and onboarding checklists that surface features at the point of use rather than in separate training
- **Airline quick-reference handbooks (QRH)** — pilots consult the QRH for abnormal procedures rather than recalling them, an explicit design decision that rare, complex procedures should be externalized

## Key Sources
- Clark, R. C., & Kwinn, A. (2007). *The new virtual classroom: Evidence-based guidelines for synchronous e-learning*. Pfeiffer.
- Rossett, A., & Schafer, L. (2007). *Job aids and performance support: Moving from knowledge in the classroom to knowledge everywhere*. Pfeiffer.
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive load theory*. Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)
- Haynes, A. B., et al. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. *New England Journal of Medicine, 360*(5), 491–499. [doi:10.1056/NEJMsa0810119](https://doi.org/10.1056/NEJMsa0810119)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
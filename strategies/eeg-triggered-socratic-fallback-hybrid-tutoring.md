---
type: strategy
id: eeg-triggered-socratic-fallback-hybrid-tutoring
title: Hybrid Socratic-to-sub-question tutoring with EEG-triggered fallback and progressively concrete hints
description: "The authors propose a design in which \"deployment of Socratic dialogue by default\", but when EEG shows sustained disengagement below the personal baseline, the system temporarily switches to Mode-3-style sub-questions..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: alexandre-clin-deffarges-2026
    resource: "https://arxiv.org/abs/2609.00584"
    title: "Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes. (2026). Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing. arXiv preprint arXiv:2609.00584. https://arxiv.org/abs/2609.00584"
    author: Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes
---

# Hybrid Socratic-to-sub-question tutoring with EEG-triggered fallback and progressively concrete hints

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors propose a design in which "deployment of Socratic dialogue by default", but when EEG shows sustained disengagement below the personal baseline, the system temporarily switches to Mode-3-style sub-questions — the format that kept engagement highest — and then returns to dialogue. When struggle stops being productive (repeated failures, shrinking messages), the system gives progressively more concrete hints instead of indefinite refusal, keeping the learner in the zone of proximal development.

## Design Implications

### Context
#### Requirements
- Real-time EEG engagement measurement with a per-learner baseline (calibration plus EMA-updated baseline as in the study's pipeline)
- A Socratic dialogue mode and a sub-question mode available in the same system
#### Constraints
- The authors state this system design is a suggestion and should be evaluated in a formal study with a delayed post-test

### Target Learners
- Adult learners in independent study sessions with zero prior domain knowledge

### Target Learning Goals
- Factual knowledge acquisition requiring global conceptual understanding

## Related Strategies

- [Design chatbots that begin with guided inquiry and progressively provide explicit guidance when students remain stuck](chatbots-guided-inquiry-then-explicit-guidance.md)
- [Use impasse depth and type as real-time learning-analytics signals to trigger graduated escalation of tutor support](impasse-depth-type-analytics-escalation-signals.md)

## Examples
-

## Key Sources
- Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes. (2026). Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing. arXiv preprint arXiv:2609.00584. https://arxiv.org/abs/2609.00584

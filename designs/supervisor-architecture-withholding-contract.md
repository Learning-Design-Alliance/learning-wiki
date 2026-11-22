---
type: design
id: supervisor-architecture-withholding-contract
title: Supervisor architecture enforcing answer-withholding as a per-turn, machine-checkable contract outside the generating model
description: The architecture surrounds a capable tutor LLM (the actor) with supervisor components that decide what help is allowed each turn, check replies against that decision, and log everything.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: yusuf-pisan-2026
    resource: "https://arxiv.org/abs/2608.12292"
    title: "Yusuf Pisan. (2026). Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior. https://arxiv.org/abs/2608.12292"
    author: Yusuf Pisan
---

# Supervisor architecture enforcing answer-withholding as a per-turn, machine-checkable contract outside the generating model

> **Design** · [All designs](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 associational, 1 design), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The architecture surrounds a capable tutor LLM (the actor) with supervisor components that decide what help is allowed each turn, check replies against that decision, and log everything. As the abstract states, "A non-LLM policy core, reading only trusted learner state, sets a per-turn ceiling on an eight-rung help ladder; a deterministic detector strips solution code; and a separate LLM judge checks each risky reply against the contract." Six principles govern the design, including withhold-by-default, deciding without reading student text, letting deterministic signals outrank model judgments, and preferring revision over refusal.

## Design Implications

### Context
#### Requirements
- The component making the binding withholding decision must be a non-LLM layer fed only trusted signals, never student text
- A single writer component must own all mastery and progress records through typed transitions
- Every turn must log the computed contract, verdicts, help level used, latency, and cost
#### Constraints
- The detector misses split-fence, plain-prose, and cross-language reveals by design, with the judge and execution path as compensating layers
- The goal is not leak-proofness but making the guarded path the path of least resistance

### Target Learners
- undergraduate data structures students

### Learning Goals
- durable learning of programming and data structures through Socratic help rather than answer-giving

### Claims

- [Llm Tutor Full Compliance Four Gates](../claims/llm-tutor-full-compliance-four-gates.md) [+M]
- [Withholding failures of a capable LLM tutor form a descending over-help ladder, from blatant solution leaks to naming the exact bug to over-citing general facts](../claims/over-help-ladder-gross-to-subtle.md) [+W]
- [Half of the apparent ceiling violations in the first run were auditor grounding rejections, not over-help; real ceiling compliance was about 77%](../claims/auditor-artifact-real-compliance-77.md) [+W]
- [The first billed calibration run failed both pedagogy gates badly, with a 43% earnest revise rate and 54% reported hint-ceiling compliance](../claims/first-run-failed-pedagogy-gates.md) [+W]
- [A deployed reflection agent followed its prompt's countable rules but broke its dispositional rules about manner](../claims/agent-followed-countable-not-dispositional-rules.md) [+W]

## Related Designs

- [Uncertainty-based human-in-the-loop dialogue architecture in which a supervisor intervenes when model uncertainty thresholds are met](uncertainty-threshold-supervisor-intervention-architecture.md)

## Examples
-

## Key Sources
- Yusuf Pisan. (2026). Teaching a Large Language Model Tutor to Withhold the Answer: A Supervisor Architecture and an Evidence-Driven Method for Tuning Socratic Behavior. https://arxiv.org/abs/2608.12292

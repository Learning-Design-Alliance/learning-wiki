---
type: design
id: conv-ped-tutor-audit-testbed
title: "Controlled tutor-audit testbed: ConvTutor, PedTutor, and cold baseline over identical frozen weights with a weak simulated student"
description: A within-base testbed in which two tutoring policies are instantiated from identical frozen model weights so that only the policy layer differs.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: shuyi-fan-2026
    resource: "https://arxiv.org/abs/2607.28128"
    title: "Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128"
    author: Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao
---

# Controlled tutor-audit testbed: ConvTutor, PedTutor, and cold baseline over identical frozen weights with a weak simulated student

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A within-base testbed in which two tutoring policies are instantiated from identical frozen model weights so that only the policy layer differs. ConvTutor is a minimal one-call helpful tutor whose answer-giving is emergent; PedTutor is a four-node routed policy with a learner-state tracker and three responders (problem decomposer, answer-deferral gate, hint cascade). All conditions face one deliberately weak simulated student, Llama-3.1-8B-Instruct, with "about11% unaided accuracy", making tutoring load-bearing, plus a no-tutor cold baseline and a frozen 19-problem mixture/weighted-average instrument.

## Design Implications

### Context
#### Requirements
- A weak simulated student so that tutoring is load-bearing and a process contrast is measurable
- Frozen judge, rubrics, metric definitions, and outcome-interpretation table fixed before confirmatory data collection
#### Constraints
- The serving vendor co-varies with the tutor base and Gemini's provider enforces a minimum reasoning setting, so no base is a pure base-model swap
- Results describe one simulated learner on one algebra domain and do not license claims about human learners

### Target Learners
- Simulated weak algebra learners (Llama-3.1-8B-Instruct)

### Learning Goals
- Translating word problems into mixture or weighted-average balance equations

### Claims
- [Leakage Manipulation Check Probe Ceiling](../claims/leakage-manipulation-check-probe-ceiling.md) [+M]
- [Helpfulness Pedagogy Dissociation Primary Base](../claims/helpfulness-pedagogy-dissociation-primary-base.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128

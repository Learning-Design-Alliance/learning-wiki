---
type: design
id: six-setting-scaffold-evaluation-protocol
title: Six-setting evaluation protocol with frozen controller constants and released environment bank materials
description: "The article specifies a complete evaluation protocol: nine settings (six natural, three conflicts) with per-setting scaffolds, learners, context banks of 100 training and 50 held-out contexts (200/100 for MiniGrid and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: siddharth-aphale-2026
    resource: "https://arxiv.org/abs/2607.26417"
    title: "Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. https://arxiv.org/abs/2607.26417"
    author: Siddharth Aphale, Ayushman Singh
---

# Six-setting evaluation protocol with frozen controller constants and released environment bank materials

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article specifies a complete evaluation protocol: nine settings (six natural, three conflicts) with per-setting scaffolds, learners, context banks of 100 training and 50 held-out contexts (200/100 for MiniGrid and the Meta-World conflict), frozen controller constants (Table A.2), and paired seed-bootstrap intervals with 10,000 resamples. "Bank builders, seed IDs, available hashes, and archived exceptions are documented in the release materials." Exact sign tests are reported as descriptive because their six-seed resolution is too coarse for Holm correction.

## Design Implications

### Context
#### Requirements
- Locked software environment (Python 3.12.13, PyTorch 2.12.1, Gymnasium 1.3.0, MuJoCo 3.10.0, among others) with uv.lock pinning the full environment
#### Constraints
- Main-paper natural-setting AUCs are seed medians and comparable only within a task
- The constructed screen overlaps the final seed IDs and is sensitivity/provenance evidence, not an independent test block

### Target Learners
- reinforcement learning researchers evaluating curriculum methods

### Learning Goals
- rigorous comparison of scaffold access and allocation methods

### Claims
- [Scaffold Access Improves Sparse Reward Learning](../claims/scaffold-access-improves-sparse-reward-learning.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Siddharth Aphale, Ayushman Singh. (2026). Per-Context Reverse Curricula for Sparse-Reward Reinforcement Learning. 40th Conference on Neural Information Processing Systems (NeurIPS 2026), Workshop: 8th Robot Learning Workshop. https://arxiv.org/abs/2607.26417

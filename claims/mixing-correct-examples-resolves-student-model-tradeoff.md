---
type: claim
title: "Mixing correct examples into student-model training resolves the misconception-accuracy trade-off, with correct examples as low as 25% preserving both properties"
description: "Mixing correct examples into student-model training resolves the misconception-accuracy trade-off, with correct examples as low as 25% preserving both properties"
id: mixing-correct-examples-resolves-student-model-tradeoff
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: naiming-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2604.00818"
    title: "Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818 [doi:10.48550/arxiv.2604.00818](https://doi.org/10.48550/arxiv.2604.00818)"
    author: Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Mixing correct examples into student-model training resolves the misconception-accuracy trade-off, with correct examples as low as 25% preserving both properties

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Adding correct examples during student-model instruction-tuning recovers CANA while keeping Misconception Accuracy high (90-95%). [→ Naiming Liu 2026](#naiming-liu-2026)

## Evidence

### Naiming Liu 2026

Naiming Liu, Xinghe Chen, Richard Baraniuk, Mrinmaya Sachan, and Shashank Sonkar. (2026). Misconception Acquisition Dynamics in Large Language Models. https://arxiv.org/abs/2604.00818 [doi:10.48550/arxiv.2604.00818](https://doi.org/10.48550/arxiv.2604.00818)

`q2 · i?` · `causal · r2`

Mixed-training experiments (nc/nm in {0.25,0.5,1.0}) on Llama-3.1-8B-Instruct, with similar patterns for Phi-4-4B-Mini and Qwen-3-4B-Instruct; for M8, "MA remained consistently high, increasing from 90.2% at 400 samples to 94.5% at 3200 samples."

> "MA (blue) remains high ( 90-95%) demon- strating successful misconception acquisition, while CAN A (red) rapidly recovers with just 200-400 correct examples."

## Discussion


## Related Claims
- [Instruction-tuning a student model on a single misconception overgeneralizes the error across problems and degrades correct-solving accuracy](student-model-misconception-overgeneralization-degrades-accuracy.md) — related
- [Tutor models trained on ten misconceptions simultaneously learn each misconception while overall correct accuracy remains stable or improves (93% to 98%)](tutor-model-multi-misconception-no-accuracy-tradeoff.md) — related

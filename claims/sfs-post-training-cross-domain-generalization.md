---
type: claim
title: "SFS-aligned post-training generalizes out-of-domain: models trained on one dataset retain substantial SFS gains on the other"
description: "SFS-aligned post-training generalizes out-of-domain: models trained on one dataset retain substantial SFS gains on the other"
id: sfs-post-training-cross-domain-generalization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: heejin-do-2026
    resource: "https://doi.org/10.48550/arxiv.2605.12748"
    title: "Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748 [doi:10.48550/arxiv.2605.12748](https://doi.org/10.48550/arxiv.2605.12748)"
    author: Heejin Do, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# SFS-aligned post-training generalizes out-of-domain: models trained on one dataset retain substantial SFS gains on the other

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models trained under the pipeline on Malrule or EEDI continue to achieve substantial SFS gains when evaluated on the other dataset, despite differences in problem format and misconception structure. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748 [doi:10.48550/arxiv.2605.12748](https://doi.org/10.48550/arxiv.2605.12748)

`q2 · i?` · `causal · r2`

Cross-domain transfer experiment training on one dataset and evaluating on the other (Figure 6); the text reports "substantial SFS gains even in out-of-domain settings," e.g., Malrule-trained models reaching out-of-domain SFS of 0.34–0.41.

> "Figure 6 shows that models trained under the pro- posed pipeline continue to achieve substantial SFS gains even in out-of-domain settings, despite dif- ferences in problem format and misconception structure."

## Discussion


## Related Claims
- [Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators](multi-turn-reflection-does-not-restore-sfs.md) — related
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
- [GRPO with an SFS-aligned reward yields more consistent improvements than DPO, achieving the highest SFS overall](grpo-sfs-reward-beats-dpo.md) — related
- [Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models](tactutor-raises-tactbench-overall-0-629-to-0-832.md) — a narrower finding that bears on this claim
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — related

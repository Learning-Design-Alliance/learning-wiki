---
type: claim
title: GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization
description: GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization
id: par-gains-transfer-to-independent-evaluators
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: heejin-do-2026
    resource: "https://doi.org/10.48550/arxiv.2609.03215"
    title: "Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)"
    author: Heejin Do, Jakub Kontak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GRPO-with-PAR gains over SFT transfer to independent evaluators never used during policy optimization

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Using a DeBERTa-based scorer, GRPO achieves average trait-level QWK of 0.598 versus 0.479 for SFT (+0.119); using an evaluation-only verifier, 0.647 versus 0.501 (+0.146). [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215 [doi:10.48550/arxiv.2609.03215](https://doi.org/10.48550/arxiv.2609.03215)

`q2 · i?` · `causal · r2`

Control analysis on one fold re-scoring all generated essays with two evaluators never involved in RL: an architecturally distinct DeBERTa multi-trait scorer and an evaluation-only ArTS verifier. The paper reports "0.598 compared with 0.479 for SFT (+0.119)".

> "Using the DeBERTa scorer, GRPO achieves an average trait-level QWK of 0.598 compared with 0.479 for SFT (+0.119). Using the evaluation-only verifier, the corresponding scores are 0.647 and 0.501 (+0.146), closely matching the original evaluation (0.618 vs. 0.474, +0.144)."

## Discussion


## Related Claims
- [Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO](data-scarcity-and-length-bottleneck-prompt-8.md) — reports the opposite
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](grpo-par-improves-alignment-across-all-traits.md) — related
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](prompting-collapses-proficiency-variation-toward-idealized-students.md) — related
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [Applying GRPO alone to LLMs for tagging yields significantly lower performance than supervised fine-tuning](grpo-alone-inferior-to-sft-for-tagging.md) — related
- [SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse](no-memorization-or-generation-collapse-in-trained-simulators.md) — related

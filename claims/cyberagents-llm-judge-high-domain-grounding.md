---
type: claim
title: LLM-as-judge evaluation scored CyberAGENTS highest on domain grounding (4.46) and agent role fidelity (4.35)
description: LLM-as-judge evaluation scored CyberAGENTS highest on domain grounding (4.46) and agent role fidelity (4.35)
id: cyberagents-llm-judge-high-domain-grounding
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: hornung-2026
    resource: "https://arxiv.org/abs/2608.07965"
    title: "Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H. (2026). CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity. Preprint. https://arxiv.org/abs/2608.07965"
    author: "Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# LLM-as-judge evaluation scored CyberAGENTS highest on domain grounding (4.46) and agent role fidelity (4.35)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Across 74 recorded student interactions, the LLM-as-judge assigned the highest scores to Domain Relevance and Cybersecurity Grounding (4.46) and Agent Role Fidelity (4.35) on a 1-5 scale. [→ Hornung 2026](#hornung-2026)

## Evidence

### Hornung 2026

Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H. (2026). CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity. Preprint. https://arxiv.org/abs/2608.07965

`q1 · i?` · `design · r2`

LLM-as-judge evaluation of complete transcripts using category-specific rubric prompts, over 74 recorded student interactions for the full system. Scores are on a 1-5 scale; Interaction Coherence and State Tracking was somewhat lower at 3.95, which the rubric labels "Mostly coherent" behavior.

> "The highest scores are obtained in Domain Relevance and Cybersecurity Grounding (4.46) and Agent Role Fidelity (4.35), as seen in Table 3"

## Discussion


## Related Claims
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](ablation-structural-components-lower-judge-scores.md) — related
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related

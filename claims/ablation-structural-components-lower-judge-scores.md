---
type: claim
title: Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding
description: Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding
id: ablation-structural-components-lower-judge-scores
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

# Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Removing the competency map and ontology-based constraints yielded lower scores on all reported LLM-judge dimensions, with the largest degradations in challenge quality, learner intent alignment, and domain grounding. [→ Hornung 2026](#hornung-2026)

## Evidence

### Hornung 2026

Hornung, I., Marasinghe Arachchige, D., Kumarage, T., Agrawal, G., Deng, Y., Chen, Y.-C., & Liu, H. (2026). CyberAGENTS: Structured Autonomy for Agentic Gamified Learning in Cybersecurity. Preprint. https://arxiv.org/abs/2608.07965

`q1 · i?` · `design · r2`

Preliminary ablation comparing the full CyberAGENTS framework (n=74 interactions) against an ablated version (n=26 interactions) without the competency map and ontology-based constraints, scored by the LLM-as-judge. Table 3 shows e.g. Challenge Quality 4.20 vs 3.46 and Domain Relevance 4.46 vs 3.77.

> "Compared with the full system, the ablation yields lower scores on all reported dimensions and the largest degradations appear in challenge quality, learner intent alignment, and domain grounding"

## Discussion


## Related Claims
- [Pipeline components play complementary roles: hierarchical generation has the largest effect, grounding improves specificity and factual accuracy, and cluster-informed TOC planning improves structure and audience fit](pipeline-components-complementary-ablation.md) — related
- [Static Knowledge Grounding and Dynamic Personal Memory are complementary: removing both yields the largest quality degradation](skg-dpm-complementary-ablation-deeptutor.md) — related
- [LLM-as-judge evaluation scored CyberAGENTS highest on domain grounding (4.46) and agent role fidelity (4.35)](cyberagents-llm-judge-high-domain-grounding.md) — related

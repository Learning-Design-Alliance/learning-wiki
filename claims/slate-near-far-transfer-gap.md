---
type: claim
title: "Across all 10 evaluated systems, near-transfer accuracy (31–42%) consistently exceeds far-transfer accuracy (11–16%)"
description: "Across all 10 evaluated systems, near-transfer accuracy (31–42%) consistently exceeds far-transfer accuracy (11–16%)"
id: slate-near-far-transfer-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: jingzhuo-wu-2026
    resource: "https://doi.org/10.48550/arXiv.2609.06212"
    title: "Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)"
    author: Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Across all 10 evaluated systems, near-transfer accuracy (31–42%) consistently exceeds far-transfer accuracy (11–16%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Near-transfer scores (31–42%) consistently exceed far-transfer scores (11–16%) across all systems, indicating decks support pattern reuse more than conceptual generalization. [→ Jingzhuo Wu 2026](#jingzhuo-wu-2026)

## Evidence

### Jingzhuo Wu 2026

Jingzhuo Wu, Jiajun Zhang, Yi Liu, Leqi Zheng, Yuheng Jing, Xinyuan Zhou, Quan Yang. (2026). SLATE: Are AI-Generated Slides Educationally Effective? A Benchmark for Language Teaching Quality and Learner Knowledge Acquisition. arXiv preprint arXiv:2609.06212. [doi:10.48550/arXiv.2609.06212](https://doi.org/10.48550/arXiv.2609.06212)

`q2 · i?` · `design · r2`

D4 evaluation of decks from 10 frontier systems using the Qwen3-VL-8B-Instruct student proxy; Figure 4 shows systems cluster in a high-near / low-far region, with the "20+% gap" persisting for the strongest systems.

> "Across all systems, near-transfer scores (31–42%) consistently exceed far-transfer scores (11–16%), indicating that current decks support pattern reuse more effectively than conceptual generalization."

## Discussion


## Related Claims
- [A recurrent understanding–application gap: physics instructors' conceptual mastery of teaching competences generally exceeds their operational enactment in practice](understanding-application-gap-physics-teaching.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related

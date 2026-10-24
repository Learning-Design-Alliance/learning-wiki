---
type: claim
title: "After PPO optimization, auxiliary feedback semantic similarity (SimCSE) reaches 81.3% and 79.3% for the two policy models, higher than evaluated pretrained baselines"
description: "After PPO optimization, auxiliary feedback semantic similarity (SimCSE) reaches 81.3% and 79.3% for the two policy models, higher than evaluated pretrained baselines"
id: races-auxiliary-feedback-simcse-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhenxin-zhang-2026
    resource: "https://doi.org/10.1186/s41239-026-00607-8"
    title: "Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8"
    author: Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# After PPO optimization, auxiliary feedback semantic similarity (SimCSE) reaches 81.3% and 79.3% for the two policy models, higher than evaluated pretrained baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Auxiliary feedback associated with LLaMA2-7B and Qwen2.5-Instruct-7B reaches maximum SimCSE semantic similarity scores of 81.3% and 79.3% respectively, higher than the evaluated pretrained baselines. [→ Zhenxin Zhang 2026](#zhenxin-zhang-2026)

## Evidence

### Zhenxin Zhang 2026

Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8

`q2 · i?` · `design · r2`

Auxiliary semantic-level analysis (Fig. 5b) using all-MiniLM-L6-v2 embeddings to compare LLM-generated feedback with reference feedback. The article stresses this is "auxiliary evidence for the semantic consistency of proxy feedback signals", not evidence of human-authored feedback quality.

> "the auxiliary feedback associated with LLaMA2-7B and Qwen2.5-Instruct-7B reaches maximum semantic similarity scores of 81.3% and 79.3%, respectively, which are higher than those of the evaluated pretrained baselines"

## Discussion


## Related Claims
- [RACES configurations improve QWK essay-scoring agreement over evaluated pretrained baselines on ASAP 2.0, with LLaMA2-7B-based configurations slightly outperforming Qwen2.5-Instruct-7B-based ones](races-improves-qwk-over-evaluated-baselines.md) — related
- [The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7](ppo-outperforms-random-baseline-reward.md) — related

---
type: claim
title: In user cold-start scenarios, NTKT achieves higher F1 than baselines from the first interaction and personalises rapidly as history grows
description: In user cold-start scenarios, NTKT achieves higher F1 than baselines from the first interaction and personalises rapidly as history grows
id: ntkt-user-cold-start-fast-personalisation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: max-norris-2025
    resource: "https://doi.org/10.48550/arXiv.2511.02599"
    title: "Max Norris, Kobi Gal and Sahan Bulathwela. (2025). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. [doi:10.48550/arXiv.2511.02599](https://doi.org/10.48550/arXiv.2511.02599)"
    author: Max Norris, Kobi Gal and Sahan Bulathwela
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In user cold-start scenarios, NTKT achieves higher F1 than baselines from the first interaction and personalises rapidly as history grows

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On held-out users, NTKT models achieve significantly higher F1 scores than baselines from the very first interaction and continue improving rapidly as additional responses become available. [→ Max Norris 2025](#max-norris-2025)

## Evidence

### Max Norris 2025

Max Norris, Kobi Gal and Sahan Bulathwela. (2025). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. [doi:10.48550/arXiv.2511.02599](https://doi.org/10.48550/arXiv.2511.02599)

`q2 · i?` · `design · r2`

User cold-start experiment (RQ3, Figure 2) computing average F1 at each timestep across held-out users, tracking personalisation as interaction history grows. Baseline models showed "slower and more gradual improvement".

> "NTKT models achieve significantly higher F1 scores than baselines from the very first interaction and continue improving rapidly as additional responses become available."

## Discussion


## Related Claims
- [NTKT maintains stable performance on unseen cold-start questions while baselines show a significant drop between seen and unseen questions](ntkt-question-cold-start-stability.md) — related
- [Modeling knowledge transfer within and across domains alleviates the cold-start problem on unseen concepts](knowledge-transfer-alleviates-cold-start-kt.md) — related
- [Fine-tuned LLaMA NTKT models outperform deep learning KT baselines on the Eedi dataset, exceeding 10 percentage points in AUC over the best baseline](ntkt-outperforms-kt-baselines-edi.md) — related

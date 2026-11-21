---
type: claim
title: "Including full question text yields the best NTKT performance; removing text degrades AUC (ID-only 77.06% vs full text 90.32%)"
description: "Including full question text yields the best NTKT performance; removing text degrades AUC (ID-only 77.06% vs full text 90.32%)"
id: question-text-improves-kt-accuracy
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
    kind: causal
    rigour: 2
---

# Including full question text yields the best NTKT performance; removing text degrades AUC (ID-only 77.06% vs full text 90.32%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the input-representation ablation, full question text outperforms concept-only and ID-only conditions, with AUC dropping from 90.32% to 84.59% for concept-only and 77.06% for ID-only. [→ Max Norris 2025](#max-norris-2025)

## Evidence

### Max Norris 2025

Max Norris, Kobi Gal and Sahan Bulathwela. (2025). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. [doi:10.48550/arXiv.2511.02599](https://doi.org/10.48550/arXiv.2511.02599)

`q2 · i?` · `causal · r2`

Controlled ablation experiment (RQ2, Table 2) comparing three input conditions: ID-only, ID + Concept tags, and Full Question Text, using the LLaMA 3B NTKT configuration. The ID-only condition "exhibits significant AUC degradation (77.06%)".

> "The concept-only configuration, which retains semantic tags but omits full text, leads to a decline across all metrics (e.g., AUC dropping from 90.32% to 84.59%)."

## Discussion


## Related Claims
- [Fine-tuned LLaMA NTKT models outperform deep learning KT baselines on the Eedi dataset, exceeding 10 percentage points in AUC over the best baseline](ntkt-outperforms-kt-baselines-edi.md) — related
- [NTKT maintains stable performance on unseen cold-start questions while baselines show a significant drop between seen and unseen questions](ntkt-question-cold-start-stability.md) — related
- [Both BERT content embeddings and flashcard-level study features contribute to KAR3L's prediction accuracy and calibration](kar3l-ablation-content-and-history-both-help.md) — related
- [Removing any single modality degrades CF–KG only moderately, with text removal causing the largest drop (NDCG 0.625 to 0.593)](cfkg-robust-modality-removal.md) — related

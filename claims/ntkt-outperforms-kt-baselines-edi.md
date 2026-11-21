---
type: claim
title: Fine-tuned LLaMA NTKT models outperform deep learning KT baselines on the Eedi dataset, exceeding 10 percentage points in AUC over the best baseline
description: Fine-tuned LLaMA NTKT models outperform deep learning KT baselines on the Eedi dataset, exceeding 10 percentage points in AUC over the best baseline
id: ntkt-outperforms-kt-baselines-edi
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

# Fine-tuned LLaMA NTKT models outperform deep learning KT baselines on the Eedi dataset, exceeding 10 percentage points in AUC over the best baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the Eedi benchmark, the LLaMA 3B NTKT model achieves the best overall performance (F1 = 85.22%, Accuracy = 78.87%, AUC = 90.32%), surpassing DKT, AKT, AKT-text and DTransformer. [→ Max Norris 2025](#max-norris-2025)

## Evidence

### Max Norris 2025

Max Norris, Kobi Gal and Sahan Bulathwela. (2025). Next Token Knowledge Tracing: Exploiting Pretrained LLM Representations to Decode Student Behaviour. arXiv. [doi:10.48550/arXiv.2511.02599](https://doi.org/10.48550/arXiv.2511.02599)

`q2 · i?` · `design · r2`

Benchmarking experiment (RQ1) on the Eedi dataset with identical data splits across models, results in Table 1 as Mean±SD across 5 runs. NTKT "exceeding 10 percentage points in AUC over the best-performing baseline".

> "Among the evaluated configurations, the LLaMA 3B NTKT model achieves the best overall performance (F1 = 85.22%, Accuracy = 78.87%, AUC = 90.32%), followed by the 1B variant."

## Discussion


## Related Claims
- [Including full question text yields the best NTKT performance; removing text degrades AUC (ID-only 77.06% vs full text 90.32%)](question-text-improves-kt-accuracy.md) — related
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [Frontier LLMs barely exceed a trivial baseline on knowledge tracing, with the best model surpassing always-predict-correct by only about five percentage points](llms-barely-exceed-trivial-baseline-kt.md) — related
- [In user cold-start scenarios, NTKT achieves higher F1 than baselines from the first interaction and personalises rapidly as history grows](ntkt-user-cold-start-fast-personalisation.md) — related

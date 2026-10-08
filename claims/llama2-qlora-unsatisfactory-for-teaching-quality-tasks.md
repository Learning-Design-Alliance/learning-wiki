---
type: claim
title: Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline
description: Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline
id: llama2-qlora-unsatisfactory-for-teaching-quality-tasks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: paiheng-xu-2024
    resource: "https://aclanthology.org/volumes/2024.naacl-long/"
    title: "Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/"
    author: Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Fine-tuning Llama2 with parameter-efficient methods (QLoRA) results in unsatisfactory results in these subject-matter tasks, only marginally improving the majority baseline in most cases. [→ Paiheng Xu 2024](#paiheng-xu-2024)

## Evidence

### Paiheng Xu 2024

Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/

`q2 · i?` · `design · r2`

Model-choice comparison across BERT, DistilBERT, XLNet, RoBERTa, and Llama2-7B fine-tuned with QLoRA in instruction-following style. The authors report Llama2 only marginally improves the majority baseline in most cases (Tables 7 and 11), and that p-tuning and classification-head variants gave similar results.

> "Notably, fine-tuning Llama2 with parameter-efficient methods results in unsatisfactory results in these subject-matter tasks."

## Discussion


## Related Claims
- [Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones](plm-performance-depends-on-pedagogical-expertise-required.md) — related
- [Existing KT methods fail to beat a majority-class baseline on the small CoMTA dialogue dataset but perform significantly better on the larger MathDial dataset.](existing-kt-methods-fail-on-small-comta-but-improve-with-more-data-on-mathdial.md) — related

---
type: claim
title: "Manual quality filtering retained 528 of 2,500 forum question/answer pairs (21%), and an earlier unfiltered fine-tune (FT1) suffered prohibitive quality issues"
description: "Manual quality filtering retained 528 of 2,500 forum question/answer pairs (21%), and an earlier unfiltered fine-tune (FT1) suffered prohibitive quality issues"
id: forum-finetune-manual-filtering-21-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
sources:
  - id: alexandra-vassar-2024
    resource: "https://doi.org/10.48550/arXiv.2411.01765"
    title: Alexandra Vassar 2024
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Manual quality filtering retained 528 of 2,500 forum question/answer pairs (21%), and an earlier unfiltered fine-tune (FT1) suffered prohibitive quality issues

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Five tutors reviewed randomly assigned Q/A pairs against six inclusion criteria, and 528 pairs (21% of the dataset) fit all criteria, yielding the improved FT2 fine-tune. [→ Alexandra Vassar 2024](#alexandra-vassar-2024)

## Evidence

### Alexandra Vassar 2024

Alexandra Vassar, Jake Renzella, Emily Ross, and Andrew Taylor. 2024. Towards Pedagogical LLMs with Supervised Fine Tuning for Computing Education. arXiv:2411.01765. [doi:10.48550/arXiv.2411.01765](https://doi.org/10.48550/arXiv.2411.01765)

`q2 · i?` · `design · r2`

Dataset-curation result from the methodology section: five tutors each reviewed 500 of 2500 randomly assigned Q/A pairs, applying inclusion criteria; the article reports "528 pairs that ﬁt all the criteria" and that filtering produced a far improved fine-tune. No effect size is printed.

> "There were 528 pairs that ﬁt all the criteria described above , constituting 21% of the dataset. While time-consuming, this process was vital in improving the dataset and resulted in a far improved ﬁne-tune (FT2)."

## Discussion


## Related Claims
- [The fine-tuned T5 question-extraction model reached an average training loss of 0.4098, indicating imperfect question extraction](t5-finetuning-average-loss-04098.md) — related
- [A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set](roberta-funneling-focusing-correlation-761.md) — related
- [The unsupervised forwards-range measure correlates negatively with human labels on the UNFILTERED set (ρ = -.130) and positively on the FILTERED set (ρ = .159)](forwards-range-unsupervised-correlations.md) — related

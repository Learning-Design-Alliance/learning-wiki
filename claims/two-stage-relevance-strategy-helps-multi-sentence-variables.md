---
type: claim
title: A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences
description: A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences
id: two-stage-relevance-strategy-helps-multi-sentence-variables
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

# A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The two-stage strategy helps Self-Instruction and Self-Regulation in the three-way setting, despite moderate positive-class F1 in the first-stage relevance prediction. [→ Paiheng Xu 2024](#paiheng-xu-2024)

## Evidence

### Paiheng Xu 2024

Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/

`q2 · i?` · `design · r2`

Experiments on the SimSE subset with sentence-level relevance annotations (199 transcripts). The authors suspect components with multiple relevant sentences per session are less prone to relevance-classifier error, since missing one or two sentences empties the input for Objective and Ending, which have only a few relevant sentences.

> "we find that the two-stage strategy helps Self-Instruction and Self-Regulation in the three-way setting, despite their moderate F1 scores on the relevant (positive) class in the first stage."

## Discussion


## Related Claims
- [Class-weighted loss marginally improves PLM performance on skewed instruction-quality ratings, achieving best performance on 10 of 16 variables in the three-way setting and 9 of 16 in the binary setting](class-weighted-loss-marginal-gain-skewed-teaching-ratings.md) — related
- [Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones](plm-performance-depends-on-pedagogical-expertise-required.md) — related
- [Using only teachers' utterances as input achieves comparable or better PLM performance than including student utterances, even for student-oriented observation variables](teacher-utterances-alone-sufficient-for-classroom-measures.md) — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related

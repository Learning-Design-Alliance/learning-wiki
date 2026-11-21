---
type: claim
title: iRULER produced larger confidence gains than Text-LLM across writing-related skills in both experiments, with mixed advantages over Rubric-LLM
description: iRULER produced larger confidence gains than Text-LLM across writing-related skills in both experiments, with mixed advantages over Rubric-LLM
id: iruler-confidence-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: jingwen-bai-2026
    title: Jingwen Bai 2026
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
  - id: jingwen-bai-2026-2
    title: Jingwen Bai 2026 (2)
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# iRULER produced larger confidence gains than Text-LLM across writing-related skills in both experiments, with mixed advantages over Rubric-LLM

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q3`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` In the writing revision experiment, iRULER significantly outperformed Text-LLM on confidence gains across all skills (all p ≤ .002) but did not differ significantly from Rubric-LLM. [→ Jingwen Bai 2026](#jingwen-bai-2026)
`q3 i?` In the rubric creation experiment, iRULER yielded significantly higher confidence gains than Text-LLM across all four skills (all p ≤ .0005) but surpassed Rubric-LLM only in Designing Rubrics (p = .0012). [→ Jingwen Bai 2026 (2)](#jingwen-bai-2026-2)

## Evidence

### Jingwen Bai 2026

Jingwen Bai, Wei Soon Cheong, Philippe Muller, and Brian Y Lim. 2026. iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790539

`q3 · i?` · `causal · r?`

Change in perceived confidence (ΔConfidence) for Writing, Reviewing, Revising and Rubric Use in the writing revision experiment (N=48); the article notes the Text-LLM condition resulted in a decrease in confidence for some skills.

> "iRULER significantly outperformed Text-LLM across all skills (allp≤ .002) but did not differ significantly from Rubric-LLM."

### Jingwen Bai 2026 (2)

Jingwen Bai, Wei Soon Cheong, Philippe Muller, and Brian Y Lim. 2026. iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790539

`q3 · i?` · `causal · r2`

Confidence gains for Reviewing, Revising, Rubric Use and Designing Rubrics in the rubric creation experiment (N=36); Rubric-LLM also significantly outperformed Text-LLM in Rubric Use (p < .0001).

> "iRULER yielded significantly higher gains than Text-LLM across all four skills (allp≤ .0005), but surpassed the Rubric-LLM group only inDesigning Rubrics(p = .0012)."

## Discussion


## Related Claims
- [Using iRULER in the writing revision task produced larger unaided skill transfer (post-task minus pre-task gains) than Text-LLM feedback](iruler-skill-transfer-unaided-revision.md) — related
- [In the writing revision experiment, iRULER produced larger LLM-judged writing quality improvements than Text-LLM feedback, and larger text-scored improvements than read-only Rubric-LLM feedback](iruler-writing-quality-gains.md) — related
- [In the rubric creation experiment, rubrics designed with iRULER scored significantly higher on both LLM-judged metrics than those from both baselines, with no efficiency advantage](iruler-rubric-creation-quality.md) — related
- [Participants rated iRULER feedback as more helpful and more correct than baseline feedback in writing revision, while sense of control did not differ significantly](iruler-perceived-helpfulness-correctness.md) — related
- [iRULER participants reached satisfactory revisions with fewer iterations than Text-LLM participants, with no difference in task speed](iruler-fewer-revision-iterations.md) — related

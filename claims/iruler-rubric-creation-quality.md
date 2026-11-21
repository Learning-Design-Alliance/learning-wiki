---
type: claim
title: In the rubric creation experiment, rubrics designed with iRULER scored significantly higher on both LLM-judged metrics than those from both baselines, with no efficiency advantage
description: In the rubric creation experiment, rubrics designed with iRULER scored significantly higher on both LLM-judged metrics than those from both baselines, with no efficiency advantage
id: iruler-rubric-creation-quality
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
    rigour: 1
  - id: jingwen-bai-2026-2
    title: Jingwen Bai 2026 (2)
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# In the rubric creation experiment, rubrics designed with iRULER scored significantly higher on both LLM-judged metrics than those from both baselines, with no efficiency advantage

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r1`–`r2` · `q3`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` iRULER-designed rubrics scored significantly higher (Mtext = 83.1, Mrubric = 86.3) than Rubric-LLM (Mtext = 77.4, Mrubric = 79.7) and Text-LLM (Mtext = 76.8, Mrubric = 78.4) rubrics. [→ Jingwen Bai 2026](#jingwen-bai-2026)
`q3 i?` No significant main effect of Feedback Type was found on final criteria subscores, task time, or number of iterations in rubric creation. [→ Jingwen Bai 2026 (2)](#jingwen-bai-2026-2)

## Evidence

### Jingwen Bai 2026

Jingwen Bai, Wei Soon Cheong, Philippe Muller, and Brian Y Lim. 2026. iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790539

`q3 · i?` · `causal · r1`

Between-subjects rubric creation experiment (N=36, 12 per condition) in which participants designed rubrics from scratch; significant effects of Feedback Type on the Text LLM score (p = .0005) and Rubric LLM score (p = .0007).

> "Participants in iRULER (Mtext = 83.1,M rubric = 86.3) scored significantly higher than those in Rubric-LLM (Mtext = 77.4,M rubric =79.7) and Text-LLM (M text =76.8,M rubric =78.4, allp≤.002)."

### Jingwen Bai 2026 (2)

Jingwen Bai, Wei Soon Cheong, Philippe Muller, and Brian Y Lim. 2026. iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790539

`q3 · i?` · `causal · r2`

Secondary analysis of the rubric-of-rubrics criteria subscores (Criteria Alignment, Level Distinction, Descriptive Language) in the same experiment; the article also reports no significant efficiency effects on Task Time or # Iterations, attributing this to the exploratory nature of rubric design.

> "We did not find any significant main effects of Feedback Type on final criteria subscores across all the criteria."

## Discussion


## Related Claims
- [iRULER produced larger confidence gains than Text-LLM across writing-related skills in both experiments, with mixed advantages over Rubric-LLM](iruler-confidence-gains.md) — related
- [iRULER participants reached satisfactory revisions with fewer iterations than Text-LLM participants, with no difference in task speed](iruler-fewer-revision-iterations.md) — related
- [In the writing revision experiment, iRULER produced larger LLM-judged writing quality improvements than Text-LLM feedback, and larger text-scored improvements than read-only Rubric-LLM feedback](iruler-writing-quality-gains.md) — related

---
type: claim
title: In the writing revision experiment, iRULER produced larger LLM-judged writing quality improvements than Text-LLM feedback, and larger text-scored improvements than read-only Rubric-LLM feedback
description: In the writing revision experiment, iRULER produced larger LLM-judged writing quality improvements than Text-LLM feedback, and larger text-scored improvements than read-only Rubric-LLM feedback
id: iruler-writing-quality-gains
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
    rigour: 2
---

# In the writing revision experiment, iRULER produced larger LLM-judged writing quality improvements than Text-LLM feedback, and larger text-scored improvements than read-only Rubric-LLM feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` iRULER's main-task score improvements (Mtext = 26.7, Mrubric = 30.8) were significantly higher than Text-LLM's on both scoring metrics and higher than Rubric-LLM's on the text-based metric only. [→ Jingwen Bai 2026](#jingwen-bai-2026)

## Evidence

### Jingwen Bai 2026

Jingwen Bai, Wei Soon Cheong, Philippe Muller, and Brian Y Lim. 2026. iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790539

`q3 · i?` · `causal · r2`

Between-subjects writing revision experiment (N=48, 16 per condition) scored with LLM-as-a-judge. iRULER's improvements "were significantly higher than in Text-LLM" on both metrics; versus Rubric-LLM the text-based difference was significant (Mtext = 19.2, p = .0003) but the rubric-based one was not (p=n.s.).

> "We found a significant main effect of Feedback Type (p < .0001) on both types of score improvements. iRULER's score improvements (Mtext = 26.7, Mrubric = 30.8) were significantly higher than in Text-LLM (Mtext = 16.1,M rubric = 16.2, bothp < .0001)."

## Discussion


## Related Claims
- [iRULER produced larger confidence gains than Text-LLM across writing-related skills in both experiments, with mixed advantages over Rubric-LLM](iruler-confidence-gains.md) — related
- [iRULER participants reached satisfactory revisions with fewer iterations than Text-LLM participants, with no difference in task speed](iruler-fewer-revision-iterations.md) — related
- [Participants rated iRULER feedback as more helpful and more correct than baseline feedback in writing revision, while sense of control did not differ significantly](iruler-perceived-helpfulness-correctness.md) — related
- [In the rubric creation experiment, rubrics designed with iRULER scored significantly higher on both LLM-judged metrics than those from both baselines, with no efficiency advantage](iruler-rubric-creation-quality.md) — related
- [Using iRULER in the writing revision task produced larger unaided skill transfer (post-task minus pre-task gains) than Text-LLM feedback](iruler-skill-transfer-unaided-revision.md) — related

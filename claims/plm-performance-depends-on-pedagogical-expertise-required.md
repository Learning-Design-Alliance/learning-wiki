---
type: claim
title: Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones
description: Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones
id: plm-performance-depends-on-pedagogical-expertise-required
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: paiheng-xu-2024
    resource: "https://aclanthology.org/volumes/2024.naacl-long/"
    title: "Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/"
    author: Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: paiheng-xu-2024-2
    resource: "https://aclanthology.org/volumes/2024.naacl-long/"
    title: "Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/"
    author: Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` In the SimSE dataset, PLMs achieve Spearman correlations over 0.8 for low-expertise components (Objective, Ending) but notably worse performance for high-expertise components (Unpacking, Self-Instruction, Self-Regulation), though still comparable to human-rater agreement levels. [→ Paiheng Xu 2024](#paiheng-xu-2024)
`q2 i?` In the NCTE dataset, PLMs perform better on MLANG (assessable by lexical usage, Spearman 0.42) than on REMED and LANGIMP, which require further mathematical inference (Spearman 0.28 and 0.20). [→ Paiheng Xu 2024 (2)](#paiheng-xu-2024-2)

## Evidence

### Paiheng Xu 2024

Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/

`q2 · i?` · `design · r2`

Test-set results from fine-tuned PLMs on 1,135 SimSE simulation sessions rated on five metacognitive modeling components. Objective and Ending reached Spearman correlations over 0.8 (three-way) and F1 over 0.9 (binary); the three high-expertise components performed notably worse, though "still obtaining comparable correlation levels as achieved by human raters."

> "In Table 3, Objective and Ending have significant Spearman correlations over 0.8 in the three-way setting and F1 scores over 0.9 in the binary setting. However, components that require higher levels of pedagogical expertise, i.e., Unpacking, Self-Instruction, and Self-Regulation, have notably worse performance"

### Paiheng Xu 2024 (2)

Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/

`q2 · i?` · `design · r2`

Test-set results on 9,886 NCTE classroom segments rated on MQI variables, using teacher text only. MLANG reached Spearman 0.42±0.02 (three-way), while REMED and LANGIMP reached 0.28±0.01 and 0.20±0.04, consistent with the pattern that lexical variables are easier for models.

> "Similarly, in Table 4, LLMs work better for MLANG which can be assessed by lexical usage, while perform worse on REMED and LANGIMP, which require further inferences of mathematical knowledge."

## Discussion


## Related Claims
- [Class-weighted loss marginally improves PLM performance on skewed instruction-quality ratings, achieving best performance on 10 of 16 variables in the three-way setting and 9 of 16 in the binary setting](class-weighted-loss-marginal-gain-skewed-teaching-ratings.md) — related
- [Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline](llama2-qlora-unsatisfactory-for-teaching-quality-tasks.md) — related
- [A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences](two-stage-relevance-strategy-helps-multi-sentence-variables.md) — related
- [Using only teachers' utterances as input achieves comparable or better PLM performance than including student utterances, even for student-oriented observation variables](teacher-utterances-alone-sufficient-for-classroom-measures.md) — related
- [AI is currently not best practice for competency-based micro-credential assessment; human assessors remain indispensable](ai-not-best-practice-competency-based-assessment.md) — related

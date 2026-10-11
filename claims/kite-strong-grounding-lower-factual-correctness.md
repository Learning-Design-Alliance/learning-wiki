---
type: claim
title: "KITE's non-procedural responses show strong retrieval grounding (faithfulness 0.85, context relevance 0.94) and answer similarity 0.76, with lower factual correctness 0.45"
description: "KITE's non-procedural responses show strong retrieval grounding (faithfulness 0.85, context relevance 0.94) and answer similarity 0.76, with lower factual correctness 0.45"
id: kite-strong-grounding-lower-factual-correctness
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: mragisha-jain-2026
    resource: "https://arxiv.org/abs/2605.12988"
    title: "Mragisha Jain, Tirth Bhatt, Griffin Pitts, Aum Pandya, Peter Brusilovsky, Narges Norouzi, Arto Hellas, Juho Leinonen, Bita Akram. (2026). Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education. Proceedings of the 21st Workshop on Innovative Use of NLP for Building Educational Applications (BEA 2026), co-located with ACL 2026. https://arxiv.org/abs/2605.12988"
    author: Mragisha Jain, Tirth Bhatt, Griffin Pitts, Aum Pandya, Peter Brusilovsky, Narges Norouzi, Arto Hellas, Juho Leinonen, Bita Akram
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# KITE's non-procedural responses show strong retrieval grounding (faithfulness 0.85, context relevance 0.94) and answer similarity 0.76, with lower factual correctness 0.45

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On 58 non-procedural questions, KITE scored 0.85 faithfulness, 0.94 context relevance, 0.76 answer relevance, 0.76 answer similarity, 0.45 factual correctness, and 0.64 answer correctness. [→ Mragisha Jain 2026](#mragisha-jain-2026)

## Evidence

### Mragisha Jain 2026

Mragisha Jain, Tirth Bhatt, Griffin Pitts, Aum Pandya, Peter Brusilovsky, Narges Norouzi, Arto Hellas, Juho Leinonen, Bita Akram. (2026). Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education. Proceedings of the 21st Workshop on Innovative Use of NLP for Building Educational Applications (BEA 2026), co-located with ACL 2026. https://arxiv.org/abs/2605.12988

`q2 · i?` · `design · r2`

RAGAs evaluation of KITE's responses on 58 non-procedural questions (42 algorithmic, 16 direct-retrieval) from a university Introduction to AI course, judged by gpt-4o-mini against instructor-authored reference answers. The description reports the printed means: "Faithfulness (0.85)" and "context relevance (0.94)".

> "KITE performs strongly on retrieval and grounding metrics. Faithfulness (0.85) indicates that most answer statements are supported by the retrieved context, while context relevance (0.94) shows that the retrieved passages are highly pertinent to the question."

## Discussion


## Related Claims
- [KITE's feedback led simulated students to improve revised answers in 24 of 27 non-already-correct interactions (88.89%)](kite-feedback-improves-simulated-student-revisions.md) — related
- [Generated answers sometimes added correct background knowledge not explicitly supported by retrieved evidence, an unsupported-answer behavior the authors flag as requiring faithfulness evaluation](answers-add-unsupported-background-knowledge.md) — related

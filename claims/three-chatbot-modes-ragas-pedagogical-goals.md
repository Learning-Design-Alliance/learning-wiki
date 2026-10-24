---
type: claim
title: "The three specialized chatbot modes achieved their distinct pedagogical goals on RAGAS metrics: Quick Mode highest faithfulness (0.92), Deep Understanding near-perfect context recall (0.98) with intentionally low answer relevancy, Exam Coach highest answer relevancy (0.82)"
description: "The three specialized chatbot modes achieved their distinct pedagogical goals on RAGAS metrics: Quick Mode highest faithfulness (0.92), Deep Understanding near-perfect context recall (0.98) with intentionally low answ..."
id: three-chatbot-modes-ragas-pedagogical-goals
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: anna-ostrowska-2026
    resource: "https://doi.org/10.24963/ijcai.2026/984"
    title: "Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr [doi:10.24963/ijcai.2026/984](https://doi.org/10.24963/ijcai.2026/984)"
    author: Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: anna-ostrowska-2026-2
    resource: "https://tinyurl.com/mrytc2dr"
    title: "Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr"
    author: Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: anna-ostrowska-2026-3
    resource: "https://tinyurl.com/mrytc2dr"
    title: "Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr"
    author: Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The three specialized chatbot modes achieved their distinct pedagogical goals on RAGAS metrics: Quick Mode highest faithfulness (0.92), Deep Understanding near-perfect context recall (0.98) with intentionally low answer relevancy, Exam Coach highest answer relevancy (0.82)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Quick Mode achieved the highest faithfulness (0.92), prioritizing direct, factual answers grounded strictly in source materials. [→ Anna Ostrowska 2026](#anna-ostrowska-2026)
`q2 i?` Deep Understanding recorded low answer relevancy by Socratic design yet maintained near-perfect context recall (0.98). [→ Anna Ostrowska 2026 (2)](#anna-ostrowska-2026-2)
`q2 i?` Exam Coach yielded the highest answer relevancy (0.82) through Chain-of-Thought reasoning. [→ Anna Ostrowska 2026 (3)](#anna-ostrowska-2026-3)

## Evidence

### Anna Ostrowska 2026

Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr [doi:10.24963/ijcai.2026/984](https://doi.org/10.24963/ijcai.2026/984)

`q2 · i?` · `design · r2`

RAGAS evaluation of the three specialized interaction modes. The evaluation confirmed Quick Mode reached "the highest faith- fulness (0.92)" among the modes for direct factual answering.

> "The Ragas evaluation of the three specialized interac- tion modes confirmed that they successfully achieved ped- agogical goals:Quick Modeachieved the highest faith- fulness (0.92), prioritizing direct, factual answers grounded strictly in the source materials"

### Anna Ostrowska 2026 (2)

Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr

`q2 · i?` · `design · r2`

The same RAGAS mode evaluation reports Deep Understanding's low answer relevancy as intentional given its Socratic guided-question design, while it "maintained near-perfect context recall (0.98)".

> "Deep Understandingintentionally recorded low answer relevancy because its Socratic design focuses on asking guided questions rather than providing answers, yet it maintained near-perfect context recall (0.98)"

### Anna Ostrowska 2026 (3)

Anna Ostrowska, Michał Kukla, Gabriela Majstrak, Jan Opala, Sebastian Pergała, Jan Skwarek, Anna Wróblewska. (2026). From Surface Learning to Deep Understanding: A Grounded AI Tutoring System for Moodle. https://tinyurl.com/mrytc2dr

`q2 · i?` · `design · r2`

RAGAS evaluation of the interaction modes reports Exam Coach "yielding the highest answer relevancy (0.82)" via Chain-of-Thought reasoning, balancing structured support with accuracy.

> "Exam Coachsuccessfully balanced structured support with accuracy, yielding the highest answer relevancy (0.82) through the use of Chain-of-Thought reasoning"

## Discussion


## Related Claims
- [Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower](rq-higher-relevancy-lower-grounding.md) — related
- [KITE's non-procedural responses show strong retrieval grounding (faithfulness 0.85, context relevance 0.94) and answer similarity 0.76, with lower factual correctness 0.45](kite-strong-grounding-lower-factual-correctness.md) — related
- [AlgoRAG answered all 179 TCS exam-style questions successfully with a mean response time of 38.0 seconds and a pedagogical quality score of 0.7620](algorag-100-success-179-tcs-questions.md) — related
- [Generated answers sometimes added correct background knowledge not explicitly supported by retrieved evidence, an unsupported-answer behavior the authors flag as requiring faithfulness evaluation](answers-add-unsupported-background-knowledge.md) — related

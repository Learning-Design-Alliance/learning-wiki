---
type: claim
title: "Longer student histories do not improve LLM knowledge tracing: FKT AUC-ROC stays near 0.5-0.6 whether models see 50 or 400 prior interactions"
description: "Longer student histories do not improve LLM knowledge tracing: FKT AUC-ROC stays near 0.5-0.6 whether models see 50 or 400 prior interactions"
id: context-length-no-effect-fkt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: eamon-worden-2026
    resource: "https://doi.org/10.48550/arxiv.2602.00070"
    title: "Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)"
    author: Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Longer student histories do not improve LLM knowledge tracing: FKT AUC-ROC stays near 0.5-0.6 whether models see 50 or 400 prior interactions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Context length has essentially no effect on FKT performance; all models hover around AUC-ROC of 0.5-0.6 regardless of history size from 50 to 400 prior interactions. [→ Eamon Worden 2026](#eamon-worden-2026)

## Evidence

### Eamon Worden 2026

Eamon Worden, Cristina Heffernan, Neil Heffernan, and Shashank Sonkar. (2026). FoundationalASSIST: An Educational Dataset for Foundational Knowledge Tracing and Pedagogical Grounding of LLMs. https://arxiv.org/abs/2602.00070 [doi:10.48550/arxiv.2602.00070](https://doi.org/10.48550/arxiv.2602.00070)

`q2 · i?` · `design · r2`

Evaluation of performance across history sizes from 50 to 400 prior interactions, shown in Figure 3 and described in Section 6.1.5. The article quotes that "All models hover around AUC-ROC of 0.5–0.6" at both 50 and 400 interactions.

> "The results show context length has essentially no effect on FKT performance. All models hover around AUC-ROC of 0.5–0.6 regardless of whether they observe 50 or 400 prior student interactions."

## Discussion

## Related Claims

- [LLMKT outperforms existing knowledge tracing methods at predicting student turn correctness in the CoMTA and MathDial tutoring dialogue datasets, and generally outperforms DKT-Sem.](llmkt-outperforms-existing-kt-methods-on-tutoring-dialogues.md) — the general claim this finding bears on, with the studies behind it
- [Extending maximum sequence length from 50 to 100 does not lead to consistent knowledge-tracing performance improvements; negative changes appear more frequently across models and datasets](longer-sequence-length-no-consistent-pkt-gain.md) — related
- A memory-augmented deep learning model improves hint-taking prediction by 12-15 AUC points over a fixed-length history baseline on two datasets — related

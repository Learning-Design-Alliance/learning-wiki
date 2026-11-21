---
type: claim
title: Voyage-based alignment ranking reliably matches expert judgments on LLM-generated resources (0.83 average accuracy)
description: Voyage-based alignment ranking reliably matches expert judgments on LLM-generated resources (0.83 average accuracy)
id: voyage-validated-expert-generated-resources
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: molavi-2025
    resource: "https://doi.org/10.48550/arXiv.2512.13658"
    title: "Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)"
    author: Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Voyage-based alignment ranking reliably matches expert judgments on LLM-generated resources (0.83 average accuracy)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The optimal Voyage model ranked 264 LLM-generated resources such that accepted resources received higher ranks than rejected ones in 0.83 of accepted-rejected pairs, matching two domain experts' consensus evaluations. [→ Molavi 2025](#molavi-2025)

## Evidence

### Molavi 2025

Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)

`q2 · i?` · `causal · r2`

Expert-evaluation study of six LLMs' generated resources across 22 topics in Python Programming and Machine Learning, under two individualization use cases (brevity, cognitive impairment). Experts classified resources by consensus; Voyage achieved "an average ranking accuracy of 0.83" (per-domain 0.80–0.85, Table 3).

> "Similar to the first study, our ranking evaluation score was calculated by analyzing all accepted-rejected pairs and determining the proportion of cases where accepted resources received a higher rank than rejected ones. The results indicated that our optimal solution achieved an average ranking accuracy of 0.83."

## Discussion


## Related Claims
- [LLM-generated resources frequently failed expert acceptance, suggesting LLMs may overlook intended learning outcomes when tailoring resources](llm-generated-resources-fail-expert-acceptance.md) — related
- [The Voyage text-embedding model outperforms other embedding models and the YouTube baseline in ranking educational resources by alignment with intended learning outcomes](voyage-embedding-best-alignment-ranking-accuracy.md) — related

---
type: claim
title: The Voyage text-embedding model outperforms other embedding models and the YouTube baseline in ranking educational resources by alignment with intended learning outcomes
description: The Voyage text-embedding model outperforms other embedding models and the YouTube baseline in ranking educational resources by alignment with intended learning outcomes
id: voyage-embedding-best-alignment-ranking-accuracy
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

# The Voyage text-embedding model outperforms other embedding models and the YouTube baseline in ranking educational resources by alignment with intended learning outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A Friedman test comparing the 8 models and the baseline showed a significant overall difference in performance, with Voyage significantly outperforming every other model after correction except Gemini. [→ Molavi 2025](#molavi-2025)

## Evidence

### Molavi 2025

Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)

`q2 · i?` · `causal · r2`

Omnibus Friedman test across 53 topics comparing the models: "𝜒 2(8)= 142.65, 𝑝<. 001" with Kendall's W=.34. Nemenyi post-hoc comparisons showed Voyage significantly outperformed all but Gemini, where the difference favored Voyage but was not statistically significant.

> "A Friedman test comparing the 8 models and the baseline showed a clear difference in performance (𝜒 2(8)= 142.65, 𝑝<. 001), with a medium effect size (Kendall's W=.34)."

## Discussion


## Related Claims
- [Voyage-based alignment ranking reliably matches expert judgments on LLM-generated resources (0.83 average accuracy)](voyage-validated-expert-generated-resources.md) — related
- [Learners studying top-ranked resources performed significantly better than those studying third-ranked resources](alignment-ranked-resources-predict-learning-performance.md) — related

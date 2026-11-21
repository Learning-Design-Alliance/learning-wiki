---
type: claim
title: LLM-generated resources frequently failed expert acceptance, suggesting LLMs may overlook intended learning outcomes when tailoring resources
description: LLM-generated resources frequently failed expert acceptance, suggesting LLMs may overlook intended learning outcomes when tailoring resources
id: llm-generated-resources-fail-expert-acceptance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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
  - id: molavi-2025-2
    resource: "https://doi.org/10.48550/arXiv.2512.13658"
    title: "Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)"
    author: Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM-generated resources frequently failed expert acceptance, suggesting LLMs may overlook intended learning outcomes when tailoring resources

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Only about half of resources tailored for learners with cognitive impairments were accepted by experts, and acceptance dropped to 45% for brief-content resources. [→ Molavi 2025](#molavi-2025)
`q2 i?` All six LLMs produced both accepted and rejected resources, which the authors cite as highlighting the importance of a verification and ranking system. [→ Molavi 2025 (2)](#molavi-2025-2)

## Evidence

### Molavi 2025

Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)

`q2 · i?` · `causal · r2`

Expert evaluation (Table 3) of 264 generated resources: e.g., 27 of 60 brevity-Python resources accepted. The article reports acceptance of "about half" for cognitive-impairment resources and "45%" for brief content.

> "only about half of the generated resources tailored for learners with cognitive impairments were accepted, and acceptance dropped to 45% for those designed for learners preferring brief content. This suggests that LLMs may overlook some intended learning outcomes when generating resources for different learner needs."

### Molavi 2025 (2)

Molavi, Mohammadreza; Moein, Mohammad; Tavakoli, Mohammadreza; Faraji, Abdolali; Mol, Stefan T.; Kismihók, Gábor. (2025). Embedding-Based Rankings of Educational Resources based on Learning Outcome Alignment: Benchmarking, Expert Validation, and Learner Performance. [doi:10.48550/arXiv.2512.13658](https://doi.org/10.48550/arXiv.2512.13658)

`q2 · i?` · `causal · r2`

The authors' interpretation of the expert-evaluation results across the six LLMs (three ChatGPT and three Gemini models): every model produced both accepted and rejected resources, motivating automated ranking as verification.

> "Notably, all LLMs produced both accepted and rejected resources, highlighting the importance of a reliable verification and ranking system."

## Discussion


## Related Claims
- [Voyage-based alignment ranking reliably matches expert judgments on LLM-generated resources (0.83 average accuracy)](voyage-validated-expert-generated-resources.md) — related
- [Instructors engage LLM-generated suggestions as a controllable refinement process](instructors-use-llm-suggestions-as-controllable-refinement.md) — related

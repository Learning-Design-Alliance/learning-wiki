---
type: claim
title: Providing URLs alone left the MyGPT PHYSBO tutor inaccurate, while uploading official documentation PDFs substantially improved response accuracy
description: Providing URLs alone left the MyGPT PHYSBO tutor inaccurate, while uploading official documentation PDFs substantially improved response accuracy
id: mygpt-pdf-upload-improves-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: takahiro-misawa-2025
    resource: "https://doi.org/10.1080/27660400.2025.2535956"
    title: "Takahiro Misawa, Ai Koizumi, Ryo Tamura, and Kazuyoshi Yoshimi. (2025). Exploring utilization of generative AI for research and education in data-driven materials science. [doi:10.1080/27660400.2025.2535956](https://doi.org/10.1080/27660400.2025.2535956)"
    author: Takahiro Misawa, Ai Koizumi, Ryo Tamura, and Kazuyoshi Yoshimi
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: takahiro-misawa-2025-2
    resource: "https://doi.org/10.1080/27660400.2025.2535956"
    title: "Takahiro Misawa, Ai Koizumi, Ryo Tamura, and Kazuyoshi Yoshimi. (2025). Exploring utilization of generative AI for research and education in data-driven materials science. [doi:10.1080/27660400.2025.2535956](https://doi.org/10.1080/27660400.2025.2535956)"
    author: Takahiro Misawa, Ai Koizumi, Ryo Tamura, and Kazuyoshi Yoshimi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Providing URLs alone left the MyGPT PHYSBO tutor inaccurate, while uploading official documentation PDFs substantially improved response accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MyGPT configured only with URLs produced a plausible but incorrect answer, falsely claiming PHYSBO implements the UCB acquisition function and omitting multi-objective optimization support. [→ Takahiro Misawa 2025](#takahiro-misawa-2025)
`q2 i?` After the official PHYSBO documentation and paper were uploaded as PDFs, MyGPT correctly listed the supported acquisition functions and related usage details. [→ Takahiro Misawa 2025 (2)](#takahiro-misawa-2025-2)

## Evidence

### Takahiro Misawa 2025

Takahiro Misawa, Ai Koizumi, Ryo Tamura, and Kazuyoshi Yoshimi. (2025). Exploring utilization of generative AI for research and education in data-driven materials science. [doi:10.1080/27660400.2025.2535956](https://doi.org/10.1080/27660400.2025.2535956)

`q2 · i?` · `design · r2`

Accuracy test of the AI tutor (Section 3): MyGPT configured with the PHYSBO GitHub repository, official paper, and user manual URLs was asked what acquisition functions PHYSBO supports; it "generated plausible but incorrect information", naming unimplemented UCB. No statistical measure is reported.

> "The results indicate that providing URLs alone was insufficient to ensure accurate responses, since MyGPT generated plausible but incorrect information."

### Takahiro Misawa 2025 (2)

Takahiro Misawa, Ai Koizumi, Ryo Tamura, and Kazuyoshi Yoshimi. (2025). Exploring utilization of generative AI for research and education in data-driven materials science. [doi:10.1080/27660400.2025.2535956](https://doi.org/10.1080/27660400.2025.2535956)

`q2 · i?` · `design · r2`

Same MyGPT evaluation (Section 3): after uploading the official documentation and research paper as PDFs, the repeated query returned correct listings of single- and multi-objective acquisition functions; "uploading structured documents (PDFs) significantly improved response accuracy". The causal explanation is the authors' conjecture.

> "In contrast, uploading structured documents (PDFs) significantly improved response accuracy, probably because the model could directly extract relevant content."

## Discussion


## Related Claims
- [A MyGPT-generated tutorial for PHYSBO-based hyperparameter optimization of a Keras neural network was executable and converged to an accuracy of 0.9742](mygpt-generated-tutorial-executable-keras.md) — related
- [Gen-AI hallucinates sources and values and produces convincing but incorrect explanations, risking student misinformation](genai-hallucination-convincing-incorrect-explanations.md) — a broader claim this one bears on
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related

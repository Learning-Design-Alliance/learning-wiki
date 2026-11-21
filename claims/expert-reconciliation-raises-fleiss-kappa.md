---
type: claim
title: "Expert-based re-annotation with reconciliation raises Fleiss's κ from 0.486 to 0.851, with GPT-4 and PaLM2 near expert reliability and MTurk near random"
description: "Expert-based re-annotation with reconciliation raises Fleiss's κ from 0.486 to 0.851, with GPT-4 and PaLM2 near expert reliability and MTurk near random"
id: expert-reconciliation-raises-fleiss-kappa
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: danielle-r-thomas-2025
    resource: "https://doi.org/10.48550/arXiv.2508.00143"
    title: "Danielle R. Thomas, Conrad Borchers, Kenneth R. Koedinger. (2025). Beyond Agreement: Rethinking Ground Truth in Educational AI. [doi:10.48550/arXiv.2508.00143](https://doi.org/10.48550/arXiv.2508.00143)"
    author: Danielle R. Thomas, Conrad Borchers, Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Expert-based re-annotation with reconciliation raises Fleiss's κ from 0.486 to 0.851, with GPT-4 and PaLM2 near expert reliability and MTurk near random

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` An expert re-annotation protocol with reconciliation across 11 binary-task datasets improved expert Fleiss's κ from 0.486 to 0.851; GPT-4 (0.706) and PaLM2 (0.750) closely matched experts while MTurk workers showed near-random agreement (κ = 0.074). [→ Danielle R. Thomas 2025](#danielle-r-thomas-2025)

## Evidence

### Danielle R. Thomas 2025

Danielle R. Thomas, Conrad Borchers, Kenneth R. Koedinger. (2025). Beyond Agreement: Rethinking Ground Truth in Educational AI. [doi:10.48550/arXiv.2508.00143](https://doi.org/10.48550/arXiv.2508.00143)

`q2 · i?` · `theoretical · r2`

The paper reports, citing Nahum et al. (2024), an expert-based re-annotation protocol with LLM-driven error detection on 11 datasets; reconciliation "significantly enhanced IRR" with κ rising from 0.486 to 0.851. Table 1 additionally reports GPT-4 κ = 0.706, PaLM2 κ = 0.750, MTurk κ = 0.074.

> "This reconciliation improved the quality of annotations and significantly enhanced IRR, with Fleiss’s κ for expert annotations increasing from 0.486 to 0.851 after reconciliation."

## Discussion


## Related Claims
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) — related
- [Some VLMs perform near chance on binary judgments of student correctness, and error-assessment behavior is idiosyncratic across models](binary-correctness-judgments-near-chance.md) — related
- [Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus](moderate-kappa-versus-perceived-consensus-gap.md) — related
- [GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)](llm-communication-grading-insufficient-alignment-ttx.md) — related
- [Rubric scoring of concept image protocols showed inter-rater reliability exceeding acceptable thresholds (Fleiss Kappa 0.60–0.88; Krippendorff's Alpha 0.60–0.88; ICC 0.89–0.98)](concept-image-rubric-inter-rater-reliability.md) — related
- [Human inter-annotator agreement and dataset recall of 75.5 validate the benchmark's coverage of high-quality Socratic utterances](human-ita-dataset-recall-validation.md) — related
- [Mistral 7B shows high ICCs but low Fleiss kappa when scoring summary statements](mistral-7b-high-icc-low-fleiss-kappa.md) — related

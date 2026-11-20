---
type: claim
title: GPTZero, an AI detector built for writing, fails to detect AI-generated code, assigning AI solutions lower suspicion scores than human solutions
description: GPTZero, an AI detector built for writing, fails to detect AI-generated code, assigning AI solutions lower suspicion scores than human solutions
id: gptzero-fails-ai-generated-code
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: kevin-wang-2023
    resource: "https://doi.org/10.1109/csci62032.2023.00268"
    title: "Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)"
    author: Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GPTZero, an AI detector built for writing, fails to detect AI-generated code, assigning AI solutions lower suspicion scores than human solutions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` AI-generated code solutions received very low probability-of-AI scores from GPTZero, below the threshold for identification, and lower than human solutions. [→ Kevin Wang 2023](#kevin-wang-2023)

## Evidence

### Kevin Wang 2023

Kevin Wang, Seth Akins, Abdallah Mohammed, Ramon Lawrence. (2023). Student Mastery or AI Deception? Analyzing ChatGPT's Assessment Proficiency and Evaluating Detection Strategies. arXiv preprint. [doi:10.1109/csci62032.2023.00268](https://doi.org/10.1109/csci62032.2023.00268)

`q2 · i?` · `causal · r1`

AI-detector experiment in which GPTZero was given 24 solutions (14 human, 10 AI) from the CS1/CS2 assignment data set. The study reports "very low probability of AI scores" for AI solutions, with the metrics used to detect AI-generated writing not effective when applied to code solutions.

> "Providing AI solutions to GPTZero [15] resulted in very low probability of AI scores. The AI generated solutions raised less suspicion than human solutions, and overall these percentages are way below the threshold to identify AI generated content."

## Discussion


## Related Claims
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — related
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](light-ai-edits-flagged-at-high-rates.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related
- [Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal](detector-agreement-collapses-after-humanization.md) — related
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related

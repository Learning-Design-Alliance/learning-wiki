---
type: claim
title: "GPTZero misclassified 8 of 50 human-written essays as AI, a 16% false positive rate"
description: "GPTZero misclassified 8 of 50 human-written essays as AI, a 16% false positive rate"
id: gptzero-false-positives-human-essays-16-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: selin-dik-2025
    resource: "https://doi.org/10.48550/arXiv.2506.23517"
    title: "Selin Dik, Osman Erdem, and Mehmet Dik. (2025). Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays. Originally published 2024. [doi:10.48550/arXiv.2506.23517](https://doi.org/10.48550/arXiv.2506.23517)"
    author: Selin Dik, Osman Erdem, and Mehmet Dik
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPTZero misclassified 8 of 50 human-written essays as AI, a 16% false positive rate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Of fifty human-written essays, eight were misclassified as AI, yielding a 16% false positive rate and an overall error rate of 10.3%. [→ Selin Dik 2025](#selin-dik-2025)

## Evidence

### Selin Dik 2025

Selin Dik, Osman Erdem, and Mehmet Dik. (2025). Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays. Originally published 2024. [doi:10.48550/arXiv.2506.23517](https://doi.org/10.48550/arXiv.2506.23517)

`q2 · i?` · `design · r2`

The study's confusion matrix (Table 3) over all 78 submitted essays shows 42 human essays correctly labeled and 8 misclassified as AI; the authors report "GPTZero’s false positive rate was 16%" and an overall error rate of 10.3%.

> "Of the fifty human-written essays, forty-two were accurately labeled as human, while eight were misclassified as AI. GPTZero’s false positive rate was 16% (eight out of fifty human essays), contributing to an overall error rate of 10.3%"

## Discussion


## Related Claims
- [False positives on human essays vary by length: short and long human essays were flagged more often than medium-length ones](essay-length-moderates-gptzero-false-positives.md) — related
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](aggregate-accuracy-group-fairness-detectors.md) — related
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](detectors-insufficient-accuracy-high-stakes.md) — a broader claim this one bears on
- [AI-text detectors misclassify authentic TOEFL essays by non-native English speakers at a mean false-positive rate of 61.3% across seven detectors, far more often than native-speaker essays](detector-61-3-percent-false-positives-non-native-toefl.md) — related
- [In a documented exploratory audit, one human-authored manuscript received materially different classifications from five commercial detectors, spanning 0% human to Human Generated](multi-tool-audit-cross-tool-inconsistency.md) — related
- [Blinded review identified 68% of ChatGPT-generated abstracts as chatbot-produced while 14% of authentic abstracts were misclassified as chatbot-generated](chatgpt-abstract-detection-68-14-percent.md) — related
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](light-ai-edits-flagged-at-high-rates.md) — related
- [GPTZero's assessed AI likelihood for human essays fluctuates across length categories rather than approaching the ideal 0%](gptzero-human-essay-scores-fluctuate.md) — related

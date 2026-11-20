---
type: claim
title: "Among five AI-detection tools, ZeroGPT was most accurate at 98% with precision 1.00 on binary classification"
description: "Among five AI-detection tools, ZeroGPT was most accurate at 98% with precision 1.00 on binary classification"
id: zerogpt-best-ai-detector-98-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: will-yeadon-2024
    resource: "https://doi.org/10.1088/1361-6404/ad669d"
    title: "Will Yeadon, Elise Agra, Oto-obong Inyang, Paul Mackay, Arin Mizouri. (2024). Evaluating AI and Human Authorship Quality in Academic Writing through Physics Essays. [doi:10.1088/1361-6404/ad669d](https://doi.org/10.1088/1361-6404/ad669d)"
    author: Will Yeadon, Elise Agra, Oto-obong Inyang, Paul Mackay, Arin Mizouri
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Among five AI-detection tools, ZeroGPT was most accurate at 98% with precision 1.00 on binary classification

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ZeroGPT achieved 98% accuracy and precision of 1.00, with no false positives and one false negative, outperforming QuillBot, Hive Moderation, Sapling and Radar. [→ Will Yeadon 2024](#will-yeadon-2024)

## Evidence

### Will Yeadon 2024

Will Yeadon, Elise Agra, Oto-obong Inyang, Paul Mackay, Arin Mizouri. (2024). Evaluating AI and Human Authorship Quality in Academic Writing through Physics Essays. [doi:10.1088/1361-6404/ad669d](https://doi.org/10.1088/1361-6404/ad669d)

`q2 · i?` · `design · r2`

Evaluation of all study essays with five commercial detectors (ZeroGPT, QuillBot, Hive Moderation, Sapling, Radar) using confusion matrices. ZeroGPT had "no false positives (FP) and only one false negative (FN)"; Sapling had the most FPs at 18, accuracy 0.70.

> "Applying a confusion matrix to the five AI text detectors, as shown in Table 2, reveals that ‘ZeroGPT’ exhibits the best precision with no false positives (FP) and only one false negative (FN), achieving an accuracy of 98%."

## Discussion


## Related Claims
- [All four detection tools classified 100% of fully human-written papers as true negatives, with false positives nearly absent](all-tools-accurate-on-human-written-papers.md) — related
- [In a documented exploratory audit, one human-authored manuscript received materially different classifications from five commercial detectors, spanning 0% human to Human Generated](multi-tool-audit-cross-tool-inconsistency.md) — related
- [AI language polishing alone can flip human-authored scholarly texts from human-classified to AI-classified](polishing-flips-detector-classification.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](detectors-insufficient-accuracy-high-stakes.md) — related

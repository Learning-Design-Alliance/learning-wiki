---
type: claim
title: Detector accuracy declined significantly as text length increased, with both detectors performing best on short texts
description: Detector accuracy declined significantly as text length increased, with both detectors performing best on short texts
id: detector-accuracy-declines-with-text-length
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: mohammad-hadra-2026
    resource: "https://doi.org/10.1007/s40979-026-00213-1"
    title: "Mohammad Hadra, Karleen Cambridge and Mostefa Mesbah. (2026). Evaluating the accuracy and reliability of AI content detectors in academic contexts. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00213-1"
    author: Mohammad Hadra, Karleen Cambridge and Mostefa Mesbah
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Detector accuracy declined significantly as text length increased, with both detectors performing best on short texts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Both detectors performed best on short texts (300–330 words) with accuracy declining for medium and long texts; the length–accuracy association was statistically significant for both (Turnitin χ²(2)=8.41, p=0.0149; Originality χ²(2)=13.17, p=0.0014). [→ Mohammad Hadra 2026](#mohammad-hadra-2026)

## Evidence

### Mohammad Hadra 2026

Mohammad Hadra, Karleen Cambridge and Mostefa Mesbah. (2026). Evaluating the accuracy and reliability of AI content detectors in academic contexts. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00213-1

`q2 · i?` · `design · r2`

Chi-square tests of independence on classification correctness across three word-count ranges (300–330, 450–550, 900–1,100 words) in the 192-text dataset. Table 3 shows Turnitin accuracy 0.87 for short versus 0.56 for medium texts; the article reports "Turnitin results yielded χ² (2) = 8.41, p = 0.0149".

> "Pearson’s chi-square tests confirmed that these differences were statistically significant for both detectors. Turnitin results yielded χ² (2) = 8.41, p = 0.0149, and for Originality χ² (2) = 13.17, p = 0.0014."

## Discussion


## Related Claims
- [EchoPrompt's AUROC rises with text length, from an average of 75.8% in the shortest 1-40 word bin to 98.9% in the 321-360 bin on DetectRL Length](echoprompt-length-robustness.md) — reports the opposite
- [Originality showed a borderline non-significant trend toward higher accuracy on professional than EFL student writing, while Turnitin showed no significant difference](originality-borderline-efl-accuracy-trend.md) — related

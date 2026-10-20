---
type: claim
title: Both detectors achieved substantially lower accuracy on scientific writing than on humanities texts
description: Both detectors achieved substantially lower accuracy on scientific writing than on humanities texts
id: detectors-lower-accuracy-scientific-writing
status: review
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
    kind: associational
    rigour: 2
---

# Both detectors achieved substantially lower accuracy on scientific writing than on humanities texts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Both detectors showed substantially higher accuracy on humanities than science texts (Turnitin 0.86 vs 0.51; Originality 0.96 vs 0.58), with statistically significant genre associations (Turnitin χ²(1)=19.109, p=0.000; Originality χ²(1)=26.429, p=0.000). [→ Mohammad Hadra 2026](#mohammad-hadra-2026)

## Evidence

### Mohammad Hadra 2026

Mohammad Hadra, Karleen Cambridge and Mostefa Mesbah. (2026). Evaluating the accuracy and reliability of AI content detectors in academic contexts. International Journal for Educational Integrity. https://doi.org/10.1007/s40979-026-00213-1

`q2 · i?` · `associational · r2`

Chi-square analysis of classification correctness across genre (57 humanities, 135 science texts) in the 192-text dataset. Table 4 reports Turnitin accuracy 0.86 humanities vs 0.51 science and Originality 0.96 vs 0.58; the article reports "Turnitin results yielded χ² (1) = 19.109, p = 0.000".

> "Pearson’s Chi-square analyses confirmed that the association between text genre and classification accuracy was statistically significant for both detectors; Turnitin results yielded χ² (1) = 19.109, p = 0.000, and for Originality χ² (1) = 26.429, p = 0.000."

## Discussion


## Related Claims
- [Originality outperformed Turnitin in overall accuracy and macro-average recall on a balanced EFL-relevant dataset, but both showed limited consistency across classes](originality-outperforms-turnitin-accuracy-recall.md) — related
- [Originality showed a borderline non-significant trend toward higher accuracy on professional than EFL student writing, while Turnitin showed no significant difference](originality-borderline-efl-accuracy-trend.md) — related
- [Both detectors performed poorly on hybrid human–AI texts, with Originality showing near-zero recall for the Hybrid class](detectors-fail-hybrid-authorship-texts.md) — related
- [Detector accuracy declined significantly as text length increased, with both detectors performing best on short texts](detector-accuracy-declines-with-text-length.md) — related
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](aggregate-accuracy-group-fairness-detectors.md) — related
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related

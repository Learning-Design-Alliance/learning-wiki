---
type: claim
title: Detector flag rates on 2023–2025 original abstracts vary sharply by domain, with non-STEM rates far above STEM
description: Detector flag rates on 2023–2025 original abstracts vary sharply by domain, with non-STEM rates far above STEM
id: non-stem-abstracts-flagged-more-than-stem
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jonathan-a-karr-jr-2026
    resource: "https://arxiv.org/abs/2608.11256"
    title: "Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256"
    author: Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Detector flag rates on 2023–2025 original abstracts vary sharply by domain, with non-STEM rates far above STEM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Pangram flags 2.1% of chemistry originals versus 26.6% of theology originals in 2023–2025, with GPTZero showing the same ordering (1.1% to 15.2%). [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)
`q2 i?` Non-STEM flag rates exceed STEM rates (p < 0.001). [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)

## Evidence

### Jonathan A. Karr Jr. 2026

Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256

`q2 · i?` · `causal · r2`

Domain-level analysis of 2023–2025 original abstracts (Table 4) scored by Pangram and GPTZero at τ=0.50. The article reports "Pangram flags 2.1% in chemistry versus 26.6% in theology" and states non-STEM rates exceed STEM (p < 0.001).

> "Flag rates on 2023 to 2025 originals vary sharply by domain at the same𝜏 (Table 4): Pangram flags 2.1% in chemistry versus 26.6% in theology; GPTZero shows the same ordering (1.1% to 15.2%)."

## Discussion


## Related Claims
- [Elevated detector scores track long-token and Academic Word List density, with numeric and non-alphabetic token ratios correlating negatively](detector-scores-track-long-token-and-awl-density.md) — related
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](aggregate-accuracy-group-fairness-detectors.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related

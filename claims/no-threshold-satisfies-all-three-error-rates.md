---
type: claim
title: No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low
description: No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low
id: no-threshold-satisfies-all-three-error-rates
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jonathan-a-karr-jr-2026
    resource: "https://doi.org/10.48550/arxiv.2608.11256"
    title: "Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256 [doi:10.48550/arxiv.2608.11256](https://doi.org/10.48550/arxiv.2608.11256)"
    author: Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across τ ∈ {0.4, 0.5, 0.6}, Pangram holds roughly 15% original flags and 80% refine flags, while raising τ from 0.4 to 0.6 slightly increases FNR on AI-labeled rewrites (10.5% to 13.8%). [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)

## Evidence

### Jonathan A. Karr Jr. 2026

Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256 [doi:10.48550/arxiv.2608.11256](https://doi.org/10.48550/arxiv.2608.11256)

`q2 · i?` · `causal · r2`

Threshold sensitivity sweep on the 2023–2025 pre-humanization collection (Table 5 and Appendix K), reporting original flag rate, refine flag rate, and AI-pool FNR at each threshold. The article reports "Pangram holds≈15% original flags and≈80% refine flags across that band."

> "No threshold𝜏∈{ 0.4, 0.5, 0.6} simultaneously keeps original flag rates, refine capture, and AI-pool FNR low (Table 5): Pangram holds≈15% original flags and≈80% refine flags across that band, while raising𝜏 from 0.4 to 0.6 slightlyincreasesFNR on AI-labeled rewrites (10.5% to 13.8%)."

## Discussion


## Related Claims
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — related
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](light-ai-edits-flagged-at-high-rates.md) — related
- [Detector flag rates on 2023–2025 original abstracts vary sharply by domain, with non-STEM rates far above STEM](non-stem-abstracts-flagged-more-than-stem.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related

---
type: claim
title: "Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates"
description: "Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates"
id: light-ai-edits-flagged-at-high-rates
status: review
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

# Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Refine (abstract only) rewrites of human abstracts are flagged at 64.4–80.1% by Pangram and 37.6–48.5% by GPTZero at τ=0.50 under human-source labeling. [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)

## Evidence

### Jonathan A. Karr Jr. 2026

Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256 [doi:10.48550/arxiv.2608.11256](https://doi.org/10.48550/arxiv.2608.11256)

`q2 · i?` · `causal · r2`

Controlled scoring study of 642 OpenAlex abstracts and Gemini 3 Flash rewrites with Pangram 3.2 and GPTZero at τ=0.50. The article reports light-edit flag rates of "Pangram 64.4% (2013–15) and 80.1% (2023–25); GPTZero 37.6% and 48.5%" under human-source labeling.

> "Refine (abstract only)flag rates equal1 −FNR in Table 3 (same scores, opposite proxy labels; Appendix B): Pangram 64.4% (2013–15) and 80.1% (2023–25); GPTZero 37.6% and 48.5%."

## Discussion


## Related Claims
- [Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal](detector-agreement-collapses-after-humanization.md) — related
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — related
- [A detector can achieve high aggregate accuracy while producing materially different over-detection rates across author groups](aggregate-accuracy-group-fairness-detectors.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related
- [Simple paraphrasing and self-editing counter-measures collapse AI detection rates to near-random levels](paraphrasing-defeats-ai-detectors.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — related
- [In a paired exploratory comparison, extensive machine rewriting by a commercial humanizer materially degraded the manuscript while changing the detection score only slightly](humanizer-rewriting-small-score-change.md) — related

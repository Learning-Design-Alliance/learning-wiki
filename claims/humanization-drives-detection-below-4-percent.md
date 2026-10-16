---
type: claim
title: "After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero"
description: "After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero"
id: humanization-drives-detection-below-4-percent
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

# After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Post-humanization false-negative rates exceed 96% for both commercial detectors across both time windows. [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)

## Evidence

### Jonathan A. Karr Jr. 2026

Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256 [doi:10.48550/arxiv.2608.11256](https://doi.org/10.48550/arxiv.2608.11256)

`q2 · i?` · `causal · r2`

Controlled re-scoring of all LLM rewrite variants after Undetectable AI v11 humanization with Pangram 3.2 and GPTZero. The article reports that "fewer than 4% of AI-labeled rewrites remain detectable" (FNR > 96%), with post-humanization Pangram means falling to 0.03–0.04.

> "After humanization, fewer than 4% of AI-labeled rewrites remain detectable for AI detectors (FNR > 96%)."

## Discussion


## Related Claims
- [Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal](detector-agreement-collapses-after-humanization.md) — related
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related
- [Independent evaluation found commercial AI-text detectors neither sufficiently accurate nor sufficiently reliable for high-stakes use](detectors-insufficient-accuracy-high-stakes.md) — a broader claim this one bears on
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](light-ai-edits-flagged-at-high-rates.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related
- [On fully AI-generated papers produced with ChatGPT Deep Research, Pangram achieved 65% strict accuracy while Turnitin, GPTZero and Copyleaks classified essentially all papers as false negatives](pangram-outperforms-tools-fully-ai-generated-deep-research.md) — reports the opposite
- [Simple paraphrasing and self-editing counter-measures collapse AI detection rates to near-random levels](paraphrasing-defeats-ai-detectors.md) — possibly the same claim (merge candidate)

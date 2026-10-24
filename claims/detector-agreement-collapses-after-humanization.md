---
type: claim
title: Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal
description: Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal
id: detector-agreement-collapses-after-humanization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Inter-detector agreement between Pangram and GPTZero collapses after humanization, so a single vendor flag is not a reliable consensus signal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Pangram and GPTZero agree moderately before humanization (Spearman ρ 0.721–0.736) but weakly afterward (ρ 0.100–0.188). [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)

## Evidence

### Jonathan A. Karr Jr. 2026

Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256 [doi:10.48550/arxiv.2608.11256](https://doi.org/10.48550/arxiv.2608.11256)

`q2 · i?` · `causal · r2`

Agreement analysis of paired detector scores (Table 7; n = 1,224 pairs in 2013–15, n = 1,344 in 2023–25). The article reports pre-humanization Spearman ρ of 0.721 and 0.736 falling to 0.100 and 0.188 post-humanization, with Cohen's κ dropping from 0.500–0.539 to 0.200–0.221.

> "Pangram and GPTZero agree moderately before humanization but weakly afterward (Table 7), so a single vendor flag is not a reliable consensus signal after evasion."

## Discussion


## Related Claims
- [Light AI-assisted edits to human-written abstracts are flagged by commercial detectors at 64–80% (Pangram) and 38–49% (GPTZero) rates](light-ai-edits-flagged-at-high-rates.md) — related
- [After humanization with Undetectable AI, fewer than 4% of AI-labeled rewrites remain detectable (FNR > 96%) for Pangram and GPTZero](humanization-drives-detection-below-4-percent.md) — related
- [Applied to 1,163 real master's theses, Pangram flagged 529 (45.5%) as containing AI-generated content, mostly at low-to-moderate levels](pangram-flagged-45-percent-real-theses.md) — related
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related

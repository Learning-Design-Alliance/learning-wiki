---
type: claim
title: Elevated detector scores track long-token and Academic Word List density, with numeric and non-alphabetic token ratios correlating negatively
description: Elevated detector scores track long-token and Academic Word List density, with numeric and non-alphabetic token ratios correlating negatively
id: detector-scores-track-long-token-and-awl-density
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
    i: 2
    kind: causal
    rigour: 2
---

# Elevated detector scores track long-token and Academic Word List density, with numeric and non-alphabetic token ratios correlating negatively

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i2` medium

## Subclaims
`q2 i2` Long-token and AWL ratios correlate positively with 2023–2025 detector scores (ρ ≈ 0.30 to 0.35, p < 0.001); numeric and non-alphabetic ratios correlate negatively. [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)
`q2 i2` After domain centering, long-token and AWL associations strengthen for Pangram (domain-adjusted r > 0.41), indicating response to within-domain stylistic cues. [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)

## Evidence

### Jonathan A. Karr Jr. 2026

Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256 [doi:10.48550/arxiv.2608.11256](https://doi.org/10.48550/arxiv.2608.11256)

`q2 · i2` · `causal · r2`

Correlational analysis (Spearman ρ with Benjamini-Hochberg FDR) of token-level features against Pangram and GPTZero scores on 2023–2025 texts. The article reports "𝜌≈ 0.30to0 .35;𝑝< 0.001" for long-token and AWL ratios, with Pangram AWL ρ = 0.346.

> "Long-token and AWL ratios correlate positively with 2023 to 2025 scores (𝜌≈ 0.30to0 .35;𝑝< 0.001); numeric and non-alphabetic ratios correlate negatively (Table 6; full tests in Appendix H)."

## Discussion


## Related Claims
- [Humanization works by systematically suppressing detector-salient surface cues — long-token ratio, AWL density, and lexical diversity — rather than fragmenting syntax](humanization-suppresses-detector-salient-cues.md) — related
- [Detector flag rates on 2023–2025 original abstracts vary sharply by domain, with non-STEM rates far above STEM](non-stem-abstracts-flagged-more-than-stem.md) — related
- [GPT-assisted writing shows higher lexical diversity, richness, and noun/non-stopword ratios, while independently authored writing shows higher adverb ratio and sentence-length variability](stylometric-feature-differences-gpt-vs-human.md) — related

---
type: claim
title: Humanization works by systematically suppressing detector-salient surface cues — long-token ratio, AWL density, and lexical diversity — rather than fragmenting syntax
description: Humanization works by systematically suppressing detector-salient surface cues — long-token ratio, AWL density, and lexical diversity — rather than fragmenting syntax
id: humanization-suppresses-detector-salient-cues
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
    rigour: 1
---

# Humanization works by systematically suppressing detector-salient surface cues — long-token ratio, AWL density, and lexical diversity — rather than fragmenting syntax

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across 2,568 humanized pairs, long-token ratio, AWL density, and lexical diversity fall systematically (p < 0.001), matching the features that track higher scores. [→ Jonathan A. Karr Jr. 2026](#jonathan-a-karr-jr-2026)

## Evidence

### Jonathan A. Karr Jr. 2026

Jonathan A. Karr Jr., Grigorii Khvatskii, Ting Hua, and Nitesh V. Chawla. (2026). Why AI Detection Fails for Academic Integrity. Proceedings of the ACM AI Leadership Summit (AILS '26). https://arxiv.org/abs/2608.11256 [doi:10.48550/arxiv.2608.11256](https://doi.org/10.48550/arxiv.2608.11256)

`q2 · i?` · `causal · r1`

Paired pre/post feature analysis of Undetectable AI v11 outputs (Appendix M; permutation tests, 5,000 iterations). The article reports long-token ratio fell 0.184 to 0.138 (Δ = −0.045), AWL ratio 0.157 to 0.121, and type-token ratio 0.700 to 0.605, all p < 0.001; word count rose from 180 to 229.

> "Across𝑛= 2,568humanized pairs, long-token ratio, AWL density, and lexical diversity fall systematically (𝑝< 0.001; Table 8), matching the pre-humanization fea-tures that track higher scores—evasion suppresses detector-salient surface cues rather than uniformly fragmenting syntax"

## Discussion


## Related Claims
- [Elevated detector scores track long-token and Academic Word List density, with numeric and non-alphabetic token ratios correlating negatively](detector-scores-track-long-token-and-awl-density.md) — related
- [GPT-assisted writing shows higher lexical diversity, richness, and noun/non-stopword ratios, while independently authored writing shows higher adverb ratio and sentence-length variability](stylometric-feature-differences-gpt-vs-human.md) — related
- [Random Forest using nine interpretable stylometric features detects GPT-assisted student writing with held-out ROC-AUC of 0.870 and F1 of 0.842](stylometric-features-detect-gpt-assisted-writing-rf-auc-0870.md) — related
- [Type-token ratio showed a non-monotonic relationship with predicted difficulty, with both very low and very high lexical diversity increasing predicted text difficulty](ttr-nonmonotonic-difficulty-pattern.md) — related
- [SHAP analysis identifies Hapax Ratio as the most influential stylometric feature in Random Forest predictions, followed by NSR, Noun Ratio, Adverb Ratio, and TTR](shap-hapax-ratio-most-influential-feature.md) — related

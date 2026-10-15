---
type: claim
title: LLM-generated errors received significantly higher plausibility ratings than authentic student errors, explained by a narrower, cleaner error-type distribution
description: LLM-generated errors received significantly higher plausibility ratings than authentic student errors, explained by a narrower, cleaner error-type distribution
id: llm-errors-score-higher-plausibility-than-authentic-student-errors
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ali-keramati-2026
    resource: "https://doi.org/10.48550/arxiv.2606.14113"
    title: "Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113 [doi:10.48550/arxiv.2606.14113](https://doi.org/10.48550/arxiv.2606.14113)"
    author: Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM-generated errors received significantly higher plausibility ratings than authentic student errors, explained by a narrower, cleaner error-type distribution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Synthetic submissions scored higher on a five-point plausibility scale (M=4.27, SD=1.07) than authentic errors (M=3.78, SD=1.11); a Mann-Whitney U test found the difference statistically significant (p<0.001). [→ Ali Keramati 2026](#ali-keramati-2026)
`q2 i?` The pattern is attributed to distribution shape: LLM errors concentrate on Condition Logic (46.4%) and Boundary (21.9%) faults, while 28.3% of authentic submissions fell into the residual Other category. [→ Ali Keramati 2026](#ali-keramati-2026)

## Evidence

### Ali Keramati 2026

Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113 [doi:10.48550/arxiv.2606.14113](https://doi.org/10.48550/arxiv.2606.14113)

`q2 · i?` · `causal · r1`

Blinded expert annotation study rating plausibility of 205 authentic and 196 synthetic submissions on a five-point Likert scale. The authors explain the counterintuitive pattern by error-distribution shape: LLM errors are "clean, single-purpose logical bugs" while authentic code shows a broader, more diffuse distribution.

> "the LLM-generated submissions received a significantly higher mean plausibility score (M= 4.27, SD= 1.07) than authentic student errors (M= 3.78, SD= 1.11). A Mann-Whitney U test confirmed this difference is statistically significant (p <0.001)"

## Discussion


## Related Claims
- [Blinded expert annotators misclassified 83.7% of LLM-generated errors as human-written](blinded-annotators-misclassify-83-7-percent-of-llm-errors-as-human.md) — related
- [BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)](beagle-error-recurrence-novice-envelope.md) — related

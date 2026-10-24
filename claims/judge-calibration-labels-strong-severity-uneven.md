---
type: claim
title: "The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain"
description: "The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain"
id: judge-calibration-labels-strong-severity-uneven
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: yubo-li-2026
    resource: "https://doi.org/10.48550/arxiv.2607.22606"
    title: "Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606 [doi:10.48550/arxiv.2607.22606](https://doi.org/10.48550/arxiv.2607.22606)"
    author: Yubo Li, Rema Padman, Ramayya Krishnan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: yubo-li-2026-2
    resource: "https://arxiv.org/abs/2607.22606"
    title: "Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606"
    author: Yubo Li, Rema Padman, Ramayya Krishnan
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the 146 pairs where both annotators agree, judge agreement is 87.7% (κ = 0.842; macro-F1 0.841). [→ Yubo Li 2026](#yubo-li-2026)
`q2 i?` Severity agreement is less settled: judge agreement is 65.3% with annotator A (κ = 0.385) but 93.9% with annotator B (κ = 0.827), with medium-tier boundaries particularly uncertain. [→ Yubo Li 2026 (2)](#yubo-li-2026-2)

## Evidence

### Yubo Li 2026

Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606 [doi:10.48550/arxiv.2607.22606](https://doi.org/10.48550/arxiv.2607.22606)

`q2 · i?` · `associational · r2`

Human-annotation study of 200 pairs stratified 40 per judge label, independently labelled by two annotators with judge outputs hidden. Inter-annotator agreement is 73.0% (κ = 0.655); the article notes the subset score is unsuitable as population accuracy.

> "On the 146 pairs where A and B agree, judge agreement is 87.7% (κ= 0.842 ; macro-F1 0.841). Per-label F1 on this subset is 1.00 for ABSENT, 0.83 CONSISTENT, 0.70 COMPLEMENTARY, 0.69 DIVERGENT, and 0.99 CONTRADICTORY."

### Yubo Li 2026 (2)

Yubo Li, Rema Padman, Ramayya Krishnan. (2026). Auditing Institutional Heterogeneity for Generative AI in Patient Education: A Large-Scale Study of 102 US Transplant Handbooks. arXiv preprint. https://arxiv.org/abs/2607.22606

`q2 · i?` · `associational · r2`

Severity-calibration subset of the same 200-pair annotation study, summarized in Table 1 showing medium-tier matches are particularly uncertain. The article therefore uses severity only as a review flag, without treating either annotator as an adjudicated clinical reference.

> "Among 49 pairs with shared relationship labels and three available severity ratings, A–B agreement is 67.3% ( κ= 0.425 ); judge agreement is 65.3% with A (κ= 0.385 ) and 93.9% with B (κ= 0.827 )."

## Discussion


## Related Claims

- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md)
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md)
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md)
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md)
- [LLMs agree strongly with their own consensus grades (most ICC > 0.8), far more than with human teachers' grades](llm-high-consensus-agreement-circularity-risk.md)
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md)
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md)
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md)
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md)
- [CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines](clara-highest-human-ranking-agreement.md)
- [LLM-judge evaluation of tutoring sycophancy shows systematic self-judge blind spots and missed sycophancy even under judge consensus](llm-judge-reliability-tutoring-sycophancy.md) — related
- [An automated LLM assessor rates 3E clinical communication skills with agreement comparable to individual human raters](llm-assessor-agrees-with-human-raters-3e.md) — related
- [Feedback givers agree on exact urgency tiers only about a fifth of the time, with most disagreements off by a single tier](low-urgency-rank-agreement.md) — related
- [In Support & Evidence and Claim & Focus, teacher and AES scores agreed at the lowest and highest rubric points but diverged in the middle, with teachers more likely to score a 2 and the AES a 3](teacher-aes-agree-tails-diverge-middle.md) — related

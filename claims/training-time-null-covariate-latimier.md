---
type: claim
title: "The pre/post-testing advantage cannot be attributed to extra training time: training time did not significantly predict final performance"
description: "The pre/post-testing advantage cannot be attributed to extra training time: training time did not significantly predict final performance"
id: training-time-null-covariate-latimier
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2019
sources:
  - id: latimier-2019
    resource: "https://doi.org/10.1038/s41539-019-0053-1"
    title: "Latimier, A., Riegert, A., Peyre, H., Ly, S. T., Casati, R. & Ramus, F. (2019). Does pre-testing promote better retention than post-testing? npj Science of Learning 4:15. https://doi.org/10.1038/s41539-019-0053-1"
    author: "Latimier, A., Riegert, A., Peyre, H., Ly, S. T., Casati, R. & Ramus, F."
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# The pre/post-testing advantage cannot be attributed to extra training time: training time did not significantly predict final performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` In regression models, log(training time) had no significant effect on final test score, and covariance analyses adjusting for training time left results unchanged. [→ Latimier 2019](#latimier-2019)

## Evidence

### Latimier 2019

Latimier, A., Riegert, A., Peyre, H., Ly, S. T., Casati, R. & Ramus, F. (2019). Does pre-testing promote better retention than post-testing? npj Science of Learning 4:15. https://doi.org/10.1038/s41539-019-0053-1

`q3 · i?` · `causal · r2`

Covariate and exploratory regression analyses in the same experiment; the full model added log(training time) as covariate. The article also states it found no correlation between training time and final performance.

> "adding log(training time) had no signiﬁcant effect (F(1,547) = 0.33, p = 0.56, and η2 < 0.001). The main effects of the learning condition and of the question type (trained vs. untrained) remained signiﬁcant"

## Discussion


## Related Claims
- [The post-test advantage of generative AI-supported instruction persists after controlling for pre-test performance (ANCOVA)](genai-geometry-ancova-group-effect.md) — related
- [In-class chat engagement significantly predicts higher test scores in MAIC courses](chat-engagement-predicts-test-scores.md) — related
- [Objective learning gains did not differ significantly by condition in the primary ANCOVA, but KBD showed a significant positive effect on learning gains in exploratory regressions accounting for learner covariates](kbd-objective-learning-gains-ancova-null-exploratory-positive.md) — related
- [Ten extra days of WM training before the second post-test had no significant impact on results](extra-ten-days-training-no-impact.md) — related

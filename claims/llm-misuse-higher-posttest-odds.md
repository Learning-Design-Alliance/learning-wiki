---
type: claim
title: Learners suspected of LLM misuse had significantly higher odds of answering the corresponding posttest MCQ correctly (OR = 2.37, p < .001)
description: Learners suspected of LLM misuse had significantly higher odds of answering the corresponding posttest MCQ correctly (OR = 2.37, p < .001)
id: llm-misuse-higher-posttest-odds
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: bhushan-2025
    resource: "https://doi.org/10.1007/978-3-032-03870-8_4"
    title: "Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. [doi:10.1007/978-3-032-03870-8_4](https://doi.org/10.1007/978-3-032-03870-8_4)"
    author: Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R.
    q: 2
    i: 2
    kind: associational
    rigour: 1
---

# Learners suspected of LLM misuse had significantly higher odds of answering the corresponding posttest MCQ correctly (OR = 2.37, p < .001)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2` · `i2` medium
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i2` In a mixed-effects logistic regression, flagged LLM use on an open-response question predicted significantly higher odds of a correct answer on the corresponding posttest multiple-choice question (OR = 2.37, p < .001), which the authors interpret as a likely bypass of learning rather than genuine gains. [→ Bhushan 2025](#bhushan-2025)

## Evidence

### Bhushan 2025

Bhushan, S., Thomas, D.R., Borchers, C., Raghuvanshi, I., Abboud, R., Gatz, E., Gupta, S., Koedinger, K.R. (2025). Detecting LLM-Generated Short Answers and Effects on Learner Performance. [doi:10.1007/978-3-032-03870-8_4](https://doi.org/10.1007/978-3-032-03870-8_4)

`q2 · i2` · `associational · r1`

Mixed-effects logistic regression (suspected LLM use as fixed effect, students as random intercept, lme4 in R) linking flagged open responses to posttest MCQ accuracy. The article reports "OR = 2.37, p < .001", estimated probabilities of 0.863 (no LLM) versus 0.937 (suspected LLM use), and calls the roughly 137% odds increase substantial.

> "learners who used LLM-generated responses in corresponding open-response questions had significantly higher odds of answering the posttest multiple-choice question correctly (OR = 2.37, p < .001)."

## Discussion


## Related Claims
- [LLM version progression explains about half of the variance in biomedical MCQ accuracy, with GPT‐4o_o1 over six times as likely as GPT‐3/3.5 to answer correctly](llm-version-meta-regression-explains-accuracy-variance.md) — related

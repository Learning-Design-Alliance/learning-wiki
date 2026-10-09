---
type: claim
title: "Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images"
description: "Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback o..."
id: insta-reviewer-four-feedback-deficiencies
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: qinjin-jia-2022
    resource: "https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    title: "Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    author: Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: qinjin-jia-2022-2
    resource: "https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    title: "Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    author: Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` About 15.2% of all statements in generated feedback were non-factual or ambiguous. [→ Qinjin Jia 2022](#qinjin-jia-2022)
`q2 i?` The phrase "the writeup is very/quite readable" appeared in 66% of system-generated feedback, which the authors attribute to 14% of training expert feedback containing the same sentence. [→ Qinjin Jia 2022 (2)](#qinjin-jia-2022-2)

## Evidence

### Qinjin Jia 2022

Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

`q2 · i?` · `design · r2`

Study 2 manually examined all system-generated feedback in the test set (n=50). The article reports the system "may occasionally (≈15.2% of all statements) generate some non-factual or ambiguous statements", which may mislead or confuse students. Descriptive percentage; no effect size.

> "the automated feedback system may occasionally (≈15.2% of all statements) generate some non-factual or ambiguous statements in the feedback"

### Qinjin Jia 2022 (2)

Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

`q2 · i?` · `design · r2`

In Study 2's manual inspection, frequent text pieces were counted across generated feedback: "this phrase was contained in 66% of the system-generated feedback", attributed to an imbalance in the training data. The authors note this repetition is not necessarily a drawback.

> "we found that this phrase was contained in 66% of the system-generated feedback. We speculate that this happens because 14% of the expert feedback that used for training contains the exact same sentence"

## Discussion


## Related Claims
- [Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality](insta-reviewer-near-human-project-report-feedback.md) — related

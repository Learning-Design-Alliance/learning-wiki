---
type: claim
title: Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality
description: Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality
id: insta-reviewer-near-human-project-report-feedback
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

# Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On a test set of 50 reports, system-generated feedback scored higher than expert feedback on the Problems dimension by 6% and on Positive Tone by 2%, while expert feedback outperformed generated feedback by gaps of 6%, 16%, and 15.2% on Readability, Suggestions, and Factuality. [→ Qinjin Jia 2022](#qinjin-jia-2022)
`q2 i?` System-generated feedback was semantically consistent with expert feedback, with ROUGE-1 of 28.54, ROUGE-2 of 6.39, ROUGE-Lsum of 18.21, and BERTScore of 59.18. [→ Qinjin Jia 2022 (2)](#qinjin-jia-2022-2)

## Evidence

### Qinjin Jia 2022

Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

`q2 · i?` · `design · r2`

Study 1 evaluated Insta-Reviewer on the test set (n=50) with human evaluation in five dimensions against instructor feedback as reference. Generated feedback scored 96.0 on Problems and 95.0 on Positive Tone versus expert 90.0 and 93.0; the article notes "our method can outperform human experts by 6% and 2%". No effect size is printed.

> "compared to the expert feedback, we surprisingly find that in terms of “Problems” and “Positive Tone,” our method can outperform human experts by 6% and 2%"

### Qinjin Jia 2022 (2)

Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

`q2 · i?` · `design · r2`

Automatic metrics from Study 1 on the test set (n=50), with expert feedback as ground truth. The article reports these scores "are 28.54, 6.39, 18.21, and 59.18, respectively", implying the generated and expert feedback are basically consistent in semantics. These are similarity scores, not effect sizes.

> "the ROUGE-1 (R1), ROUGE-2 (R2), ROUGE-Lsum (RLsum), and BERTScore (BRTS) for our Insta-Reviewer (“CE + BART” method) are 28.54, 6.39, 18.21, and 59.18, respectively"

## Discussion


## Related Claims
- [Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images](insta-reviewer-four-feedback-deficiencies.md) — related

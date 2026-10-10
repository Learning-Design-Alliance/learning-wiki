---
type: theory
title: Select-then-generate paradigm for feedback generation on overlength documents
description: The select-then-generate paradigm decomposes feedback generation for long documents into two sequential sub-problems.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: qinjin-jia-2022
    resource: "https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    title: "Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    author: Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer
---

# Select-then-generate paradigm for feedback generation on overlength documents

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The select-then-generate paradigm decomposes feedback generation for long documents into two sequential sub-problems. As the article states, it resolves "the issue of overlength input documents: 1) an unsupervised sentence-level extractive summarization task, and 2) a supervised PLM-based text-to-text generation task". An extractive summarizer (cross-entropy extraction optimizing vocabulary diversity plus a length term) produces a summarized report that becomes the input to the generation function implemented by a pre-trained language model (BART).

## Design Implications

### Context
#### Requirements
- An extractive summarizer that retains diverse salient content within the language model's input length limit
- A pre-trained language model fine-tuned on summarized reports paired with reference feedback
#### Constraints
- Summarization may drop sentences that expert suggestions focus on, which the authors speculate contributes to the system's weaker Suggestions performance

### Target Learners
- students submitting long-form project reports

### Target Learning Objectives
- receiving instant textual feedback on complex, open-ended student work

### Claims

- [Project Reports Exceed Bart Token Limit](../claims/project-reports-exceed-bart-token-limit.md) [+M]
- [Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality](../claims/insta-reviewer-near-human-project-report-feedback.md) [+W]
- [Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images](../claims/insta-reviewer-four-feedback-deficiencies.md) [-W]

## Related Theories
- 

## Examples

- [Insta-Reviewer: a select-then-generate system for instant feedback on student project reports](../products/insta-reviewer.md)

## Key Sources
- Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

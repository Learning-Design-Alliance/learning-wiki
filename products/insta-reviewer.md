---
type: product
id: insta-reviewer
title: Insta-Reviewer
description: Insta-Reviewer is a research-developed software system that extracts salient sentences from student project reports and uses a fine-tuned BART model to generate textual feedback.
product_kind: software
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: qinjin-jia-2022
    resource: "https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    title: "Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation"
    author: Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer
---

# Insta-Reviewer

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Insta-Reviewer is a research-developed software system that extracts salient sentences from student project reports and uses a fine-tuned BART model to generate textual feedback.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->

### Claims
- [Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images](../claims/insta-reviewer-four-feedback-deficiencies.md) [-W]
- [Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality](../claims/insta-reviewer-near-human-project-report-feedback.md) [+W]
- [Most student project reports exceed the BART model's 1024-token input limit, motivating a select-then-generate design because truncation can lose critical information](../claims/project-reports-exceed-bart-token-limit.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

<!-- merged 2026-10-10 from elements/insta-reviewer-system ("Insta-Reviewer: a select-then-generate system for instant feedback on student project reports"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Insta-Reviewer: a select-then-generate system for instant feedback on student project reports

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Insta-Reviewer is a data-driven automated feedback system for student project reports. It uses a two-stage pipeline: "an unsupervised sentence-level extractive summarization task, and 2) a supervised PLM-based text-to-text generation task", in which cross-entropy extraction summarizes overlength reports to fit BART's 1024-token input limit, and a fine-tuned BART model with diverse beam search generates the textual feedback. The system was trained on 484 report-review pairs and evaluated with ROUGE, BERTScore, and a five-dimension human evaluation.

## Design Implications

### Context
#### Requirements
- Requires a dataset of student project reports paired with expert textual feedback to fine-tune the generation model
- Requires summarization of input reports to within the 1024-token input limit of the BART model
#### Constraints
- Generation is not always controllable and may produce non-factual or ambiguous statements
- The system takes only report text as input, so it cannot provide feedback on images in project reports

### Target Learners
- graduate students in STEM course projects

### Target Learning Goals
- improving student project reports through timely formative feedback

### Affordances
- [Select Then Generate Paradigm Overlength Documents](../theories/select-then-generate-paradigm-overlength-documents.md)

## Claims

- [Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images](../claims/insta-reviewer-four-feedback-deficiencies.md) [-W]
- [Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality](../claims/insta-reviewer-near-human-project-report-feedback.md) [+W]
- [Most student project reports exceed the BART model's 1024-token input limit, motivating a select-then-generate design because truncation can lose critical information](../claims/project-reports-exceed-bart-token-limit.md) [+W]

## Related Elements

- [Dataset of 484 de-identified student project reports with instructor reviews collected over twelve semesters](../products/dataset-of-484-de-identified-student-project-reports-with-instructor-reviews-collected-ove.md)

## Examples
-

## Key Sources
- Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation
-->

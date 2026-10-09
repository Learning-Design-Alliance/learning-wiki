---
type: element
id: insta-reviewer-project-report-dataset
title: Dataset of 484 de-identified student project reports with instructor reviews collected over twelve semesters
description: "The authors collected \"de-identified students’ project reports and associated textual feedback provided by instructors from twelve semesters between Spring 2015 and Spring 2021\", yielding \"a set of 484 group projects\"."
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

# Dataset of 484 de-identified student project reports with instructor reviews collected over twelve semesters

> **Element** · [All elements](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors collected "de-identified students’ project reports and associated textual feedback provided by instructors from twelve semesters between Spring 2015 and Spring 2021", yielding "a set of 484 group projects". Reports average 1193 words (1643 subword tokens); expert reviews average 55 words (71 tokens). Data came from a graduate-level object-oriented development course, were IRB-approved and FERPA-compliant, and the code is publicly released on GitHub.

## Design Implications

### Context
#### Requirements
- Privacy protection via de-identification: anonymized database identifiers, regular-expression name removal, manual inspection, and secure storage
#### Constraints
- Data come from a single graduate-level course at one public US university, which may limit generalization to other domains

### Target Learners
- graduate students in software development courses

### Target Learning Goals
- supporting research on automated feedback generation for project reports

## Claims

- [Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images](../claims/insta-reviewer-four-feedback-deficiencies.md) [~M]
- [Insta-Reviewer generates near-human-quality feedback on student project reports, outperforming expert feedback on Problems and Positive Tone but trailing it on Readability, Suggestions, and Factuality](../claims/insta-reviewer-near-human-project-report-feedback.md) [+M]
- [Most student project reports exceed the BART model's 1024-token input limit, motivating a select-then-generate design because truncation can lose critical information](../claims/project-reports-exceed-bart-token-limit.md) [~M]

## Related Elements

- [Insta-Reviewer: a select-then-generate system for instant feedback on student project reports](insta-reviewer-system.md)

## Examples
-

## Key Sources
- Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

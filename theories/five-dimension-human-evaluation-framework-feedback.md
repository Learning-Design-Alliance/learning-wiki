---
type: theory
title: Five-dimension framework for manually evaluating system-generated feedback
description: "The article proposes a human-centered evaluation framework for generated feedback, stating \"we manually evaluate generated feedback in five dimensions: Readability, Suggestions, Problems, Positive Tone, and Factuality\"."
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

# Five-dimension framework for manually evaluating system-generated feedback

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes a human-centered evaluation framework for generated feedback, stating "we manually evaluate generated feedback in five dimensions: Readability, Suggestions, Problems, Positive Tone, and Factuality". Readability uses a five-point fluency-and-coherence scale; Suggestions and Problems are binary indicators of at least one valid suggestion or identified issue; Positive Tone is scored 1, 0.5, or 0; and Factuality is the ratio of factually correct statements to total statements. Human evaluation is treated as the gold standard, with ROUGE and BERTScore used to validate it.

## Design Implications

### Context
#### Requirements
- Human evaluators applying task-specific rating criteria
- Complementary automatic metrics (ROUGE, BERTScore) because human evaluations can be inconsistent and subjective
#### Constraints
- The authors state the criteria balance accuracy and cost and are not perfect; the Problems dimension does not account for problem quality and may overestimate generated feedback quality

### Target Learners
- researchers evaluating automated feedback systems

### Target Learning Objectives
- assessing quality of system-generated textual feedback

### Claims

- [Insta Reviewer Near Human Project Report Feedback](../claims/insta-reviewer-near-human-project-report-feedback.md) [+M]
- [Manual inspection of all system-generated feedback reveals four deficiencies: non-factual statements, frequent repeated text, lack of project-specific problem or suggestion statements, and inability to give feedback on images](../claims/insta-reviewer-four-feedback-deficiencies.md) [~W]

## Related Theories
- 

## Examples
-

## Key Sources
- Qinjin Jia, Mitchell Young, Yunkai Xiao, Jialin Cui, Chengyuan Liu, Parvez Rashid, Edward Gehringer. (2022). Automated Feedback Generation for Student Project Reports: A Data-Driven Approach. Journal of Educational Data Mining, Volume 14, No 3. https://github.com/qinjinjia/JEDM22_Automated_Feedback_Generation

---
type: design
id: essay-content-feedback-pipeline
title: Four-component NLP pipeline for essay content scoring and feedback generation
description: A processing pipeline that takes learner-uploaded PDF essays and produces automated content feedback.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: gombert-2024
    resource: "https://doi.org/10.1007/s40593-023-00387-6"
    title: "Gombert, S., Fink, A., Giorgashvili, T., Jivet, I., Di Mitri, D., Yau, J., Frey, A., & Drachsler, H. (2024). From the Automated Assessment of Student Essay Content to Highly Informative Feedback: a Case Study. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00387-6"
    author: "Gombert, S., Fink, A., Giorgashvili, T., Jivet, I., Di Mitri, D., Yau, J., Frey, A., & Drachsler, H"
---

# Four-component NLP pipeline for essay content scoring and feedback generation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A processing pipeline that takes learner-uploaded PDF essays and produces automated content feedback. The article describes "a pipeline composed of four components. These are 1) Preprocessing, 2) Segmentation, 3) Analytic scoring and 4) Feedback generation": text extraction and sentence tokenisation, sentence-level sliding-window classification into learning-tip sections, multilabel prediction of lecture-topic codes per segment against a ground truth table, and rule-triggered feedback texts displayed in a custom Moodle plugin. It was trained on manually labelled essays from a previous cohort and evaluated with a later cohort.

## Design Implications

### Context
#### Requirements
- Manually labelled essays from a previous cohort as training data for both the segmentation and code-prediction steps
- A ground truth table offered by the course instructors mapping correct concept assignments for each learning tip
#### Constraints
- Implemented for one particular task: German-language essays about ten learning tips in an introductory educational psychology lecture

### Target Learners
- German-speaking university teacher students in an introductory educational psychology lecture

### Learning Goals
- Connecting learning tips to lecture concepts such as working memory, metacognition and motivation through argumentative essay writing

### Claims
- 

## Related Designs

- [Learning activity: evaluating ten learning tips from a video in argumentative essays](learning-tips-video-essay-activity.md)

## Examples
-

## Key Sources
- Gombert, S., Fink, A., Giorgashvili, T., Jivet, I., Di Mitri, D., Yau, J., Frey, A., & Drachsler, H. (2024). From the Automated Assessment of Student Essay Content to Highly Informative Feedback: a Case Study. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00387-6

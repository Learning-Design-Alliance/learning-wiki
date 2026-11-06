---
type: strategy
id: gpt4o-case-based-error-analysis-strategy
title: "Use GPT-4o to analyze and reason through students' incorrect answers in case-based teaching with medical images, with human validation of its output"
description: "In exploratory case-based teaching scenarios built on image-based clinical questions, the authors prompted GPT-4o to analyze incorrect responses, and it \"demonstrated its ability to analyze and reason through incorrec..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: xiang-y-2025
    resource: "https://doi.org/10.1186/s12909-025-07752-0"
    title: "Xiang Y, Wei C. (2025). The performance of ChatGPT on medical image-based assessments and implications for medical education. BMC Medical Education. https://doi.org/10.1186/s12909-025-07752-0"
    author: Xiang Y, Wei C
---

# Use GPT-4o to analyze and reason through students' incorrect answers in case-based teaching with medical images, with human validation of its output

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 causal, 1 design), `q2`–`q3` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
In exploratory case-based teaching scenarios built on image-based clinical questions, the authors prompted GPT-4o to analyze incorrect responses, and it "demonstrated its ability to analyze and reason through incorrect answers". The strategy positions the model as a generator of explanatory feedback on wrong answers in medical case teaching, while the article insists that "human validation and correction remain necessary". Detailed prompts are provided in the article's Supplementary Appendix 1.

## Design Implications

### Context
#### Requirements
- Access to GPT-4o via the ChatGPT interface and the prompt engineering approach described in Supplementary Appendix 1
#### Constraints
- The article states human validation and correction remain necessary; errors persist in nuanced clinical contexts involving medical images

### Target Learners
- Medical students preparing for USMLE-style assessments

### Target Learning Goals
- Clinical reasoning about image-based cases
- Understanding and correcting incorrect diagnostic reasoning

## Claims

- [GPT-4o answered image-based USMLE sample items with 89.5% accuracy versus GPT-4's 73.4%, a numerically higher but not statistically significant difference](../claims/gpt4o-89-5-percent-image-usmle-accuracy.md) [+W]
- [All four items GPT-4o answered incorrectly were also answered incorrectly by GPT-4](../claims/gpt4o-errors-subset-of-gpt4-errors.md) [+W]
- [GPT-4 made errors on recall-type image-based questions whereas GPT-4o did not, and both models' error rates were higher on Step 2 CK items](../claims/gpt4-recall-errors-step2ck-higher-error-rate.md) [+W]
- [On 20 image-based items o1-Pro scored 90% versus GPT-4o's 75%, a non-significant difference presented as exploratory](../claims/image-based-items-ukmla-exploratory-null.md) [+W]

## Related Strategies

- [Use LLMs in medical education as support tools requiring human review, not as independent decision-makers or authoritative instructors](llms-as-support-tools-medical-education.md)
- [Use GPT-4o to assist instructors in drafting lesson plans and generating test questions around specific clinical knowledge points, with expert oversight](gpt4o-lesson-plan-and-item-generation-strategy.md)

## Examples
-

## Key Sources
- Xiang Y, Wei C. (2025). The performance of ChatGPT on medical image-based assessments and implications for medical education. BMC Medical Education. https://doi.org/10.1186/s12909-025-07752-0

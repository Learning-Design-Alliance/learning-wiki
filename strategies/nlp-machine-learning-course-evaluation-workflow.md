---
type: strategy
id: nlp-machine-learning-course-evaluation-workflow
title: Use NLP and machine learning (text mining, lexicon sentiment analysis, LDA topic modelling) to evaluate large-scale e-learning course feedback
description: "The article demonstrates a semi-automated evaluation workflow for large volumes of qualitative course feedback: text mining of word frequencies with the tm package, sentiment analysis with the AFINN-111 and syuzhet le..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
sources:
  - id: borakati-aditya-2021
    resource: "https://doi.org/10.1186/s12909-021-02609-8"
    title: "Borakati Aditya. (2021). Evaluation of an international medical E-learning course with natural language processing and machine learning. BMC Medical Education. https://doi.org/10.1186/s12909-021-02609-8"
    author: Borakati Aditya
---

# Use NLP and machine learning (text mining, lexicon sentiment analysis, LDA topic modelling) to evaluate large-scale e-learning course feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article demonstrates a semi-automated evaluation workflow for large volumes of qualitative course feedback: text mining of word frequencies with the tm package, sentiment analysis with the AFINN-111 and syuzhet lexicons with valence shifters handled via sentimentr, and topic modelling with Latent Dirichlet Allocation, followed by consolidated thematic analysis. The author concludes "Natural language processing may be beneficial in analysis of large scale educational courses", offering this as a reproducible, objective proof of concept for medical education evaluation, particularly for MOOCs where manual appraisal is time consuming.

## Design Implications

### Context
#### Requirements
- Analysis scripts and an implementation guide are available in supplementary file 1 and online
- Free-text feedback must be in a single language (English here) for lexicon-based analysis
#### Constraints
- The author states further validation of NLP and machine learning approaches to free-text data in medical education is needed
- Conventional qualitative methods such as interviews and focus groups may yield greater depth of information

### Target Learners
- medical education researchers
- organisers of large-scale online courses

### Target Learning Goals
- evaluating learner satisfaction and course themes at scale

## Claims

- [A massive online e-learning course for clinical study investigators achieved high user satisfaction, with a mean overall rating of 4.56/5 among 1067 feedback respondents](../claims/imagine-elearning-high-satisfaction-4-56.md) [+W]
- [LDA topic modelling of free-text feedback yielded six topics consolidated into themes of ease, assessment, comprehension, interactivity, clarity and summary](../claims/lda-six-topics-course-feedback.md) [+W]
- [Sentiment analysis of all free-text course feedback indicated overall positive sentiment (AFINN +1.54/5; syuzhet +0.287/1)](../claims/nlp-sentiment-positive-feedback-imagine.md) [+W]
- [Text mining of positive-feedback responses found 'easy', 'clear' and 'concise' as the three most common words, while improvement responses most often said 'nothing'](../claims/text-mining-frequent-words-feedback.md) [+W]

## Related Strategies

- [Validate LDA topic-model outcomes by combining thematic analysis with multilevel regression](validate-topics-thematic-analysis-multilevel-regression.md)

## Examples
-

## Key Sources
- Borakati Aditya. (2021). Evaluation of an international medical E-learning course with natural language processing and machine learning. BMC Medical Education. https://doi.org/10.1186/s12909-021-02609-8

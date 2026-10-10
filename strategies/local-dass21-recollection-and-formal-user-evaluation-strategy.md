---
type: strategy
id: local-dass21-recollection-and-formal-user-evaluation-strategy
title: Retrain and evaluate the wellness system on locally collected, clinically validated data, then run a formal user evaluation before wider deployment
description: "The authors' stated forward plan is to move from the public training dataset to primary data: \"Future work will focus on collecting primary data from Pakistani university students using an Urdu-translated and clinical..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: muhammad-fahad-bashir-2026
    resource: "https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    title: "Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    author: Muhammad Fahad Bashir, Muhammad Afzal
---

# Retrain and evaluate the wellness system on locally collected, clinically validated data, then run a formal user evaluation before wider deployment

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors' stated forward plan is to move from the public training dataset to primary data: "Future work will focus on collecting primary data from Pakistani university students using an Urdu-translated and clinically validated DASS -21 instrument to improve the cultural relevance of the classification model", focusing especially on freshmen transitioning from FSc to university life. In parallel, "a formal user evaluation study will be conducted to assess the chatbot's cultural appropriateness, emotional safety, response relevance, and overall user satisfaction". Future versions may also add longitudinal journaling, mobile application support and integration pathways with university counselling services.

## Design Implications

### Context
#### Requirements
- Ethically protected primary data collection with voluntary participation, confidentiality and consent statements presented before survey items
- Access to university counselling services for integration pathways
#### Constraints
- The current classifier evaluation rests on one stratified split, so the authors plan k-fold cross validation for more solid performance estimates with confidence intervals
- The scope of future work is limited by the stated constraints of non-representative training data and lack of formal chatbot evaluation

### Target Learners
- Pakistani university students
- freshman students transitioning from FSc to undergraduate studies

### Target Learning Goals
- Culturally relevant stress classification reflecting locally representative stress patterns
- Verified cultural appropriateness, emotional safety and user satisfaction of chatbot support

## Related Strategies

- [Conduct a smaller sequence of rapid-cycle studies that build on one another instead of planning a single large confirmatory study](sequence-of-smaller-rapid-cycle-dlp-studies.md)
- [Future improvements: real-world user studies, advanced student modeling, and spaced repetition](future-work-user-studies-student-modeling-spaced-repetition.md)

## Examples
-

## Key Sources
- Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students

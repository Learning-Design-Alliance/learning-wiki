---
type: research-method
id: taxonomy-of-student-free-text-evaluation
title: Taxonomy of student free-text evaluation
description: "The survey organises the field of student free-text evaluation — the automatic evaluation of students' free-text production including short answers and essays — along two axes."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Taxonomy of student free-text evaluation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (1 review, 1 qualitative), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The survey organises the field of student free-text evaluation — the automatic evaluation of students' free-text production including short answers and essays — along two axes. By text type, it distinguishes automatic essay evaluation (AEE), where the survey uses "evaluation instead of scoring to emphasise that our survey is not limited to models that predict scores", and automatic short-answer scoring (ASAS). By method, it distinguishes feature-based models, neural architectures (RNN/LSTM, CNN, pre-trained BERT), and hybrid combinations. AEE is further split into holistic essay grading and evaluation of specific aspects of essays; ASAS into evaluation without and based on reference answers. The survey presents state-of-the-art model performance on popular datasets within this structure.

## Accounts
<!-- How each source describes or uses the method -->
- **Taxonomy of student free-text evaluation: automatic essay evaluation (holistic and aspect-based) and automatic short-answer scoring (with or without reference answers)**: The survey organises the field of student free-text evaluation — the automatic evaluation of students' free-text production including short answers and essays — along two axes. By text type, it distinguishes automatic essay evaluation (AEE), where the survey uses "evaluation instead of scoring to emphasise that our survey is not limited to models that predict scores", and automatic short-answer scoring (ASAS). By method, it distinguishes feature-based models, neural architectures (RNN/LSTM, CNN, pre-trained BERT), and hybrid combinations. AEE is further split into holistic essay grading and evaluation of specific aspects of essays; ASAS into evaluation without and based on reference answers. The survey presents state-of-the-art model performance on popular datasets within this structure. (Xiaoyu Bai · Manfred Stede (2023))
- **Nine-category taxonomy of university teaching practices adapted from Smith and Baik (2021)**: The study classifies student testimony using nine categories of teaching practices drawn from a systematic review: Clarity, Investigation, Application, Experience (Experiential), Challenges, Importance (Relevance), Interaction and relationships, Consolidation, and Self-regulation, plus an added category "0" for "none". Each category has stated characteristics; for example, Clarity covers curriculum design, lesson design and delivery, and Interaction and relationships covers collaborative learning, dialogue, student–teacher relationship and peer tutoring. The article uses the taxonomy as the GPT-3 classification rubric so responses can be coded "at a level that can be easily understood by both teachers and students". (Carmen Álvarez-Álvarez et al. (2023))

### Claims
- [Concatenating hand-crafted linguistic features with neural essay representations significantly increases essay scoring performance](../claims/hybrid-features-boost-essay-scoring.md) [+M]
- [Where labelled training data is limited, adding hand-crafted features improves the performance of neural text evaluation models](../claims/handcrafted-features-improve-neural-low-resource.md) [+M]
- [University students most often named teaching practices focused on interaction and relationships and on clarity as the best they had experienced](../claims/students-prefer-clarity-and-interaction-practices.md) [+M]

## Related Research Methods
-

## Key Sources
- Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0
- Carmen Álvarez-Álvarez & Samuel Falcon. (2023). Students' preferences with university teaching practices: analysis of testimonials with artificial intelligence. Education Tech Research Dev. https://doi.org/10.1007/s11423-023-10239-8

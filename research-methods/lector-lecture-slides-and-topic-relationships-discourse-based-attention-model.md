---
type: research-method
id: lector-lecture-slides-and-topic-relationships-discourse-based-attention-model
title: LECTOR (Lecture slides and TOpic Relationships) discourse-based attention model
description: LECTOR (Lecture slides and TOpic Relationships) is an attention-based model that estimates a Matrix of Slide-Topic relationships M from lecture slides.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# LECTOR (Lecture slides and TOpic Relationships) discourse-based attention model

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
LECTOR (Lecture slides and TOpic Relationships) is an attention-based model that estimates a Matrix of Slide-Topic relationships M from lecture slides. "LECTOR extracts a set of topic candidates from the lecture slides and assigns a unique score to each slide-topic pair"; the score is "a linear combination of two scores, one based on the words’ importance (Importance score) and the other on the similarity between the topic and the slide embeddings (Similarity score)". It uses a domain-specific pre-trained BERT model and leverages the hierarchical structure of slides, assuming the main title introduces the main discourse and each slide title introduces the slide's discourse. Multiplying M with slide-wise reading logs yields topic-based reading characteristics such as student topic preferences.

## Accounts
<!-- How each source describes or uses the method -->
- **LECTOR: discourse-based attention model estimating Slide-Topic relationships**: LECTOR (Lecture slides and TOpic Relationships) is an attention-based model that estimates a Matrix of Slide-Topic relationships M from lecture slides. "LECTOR extracts a set of topic candidates from the lecture slides and assigns a unique score to each slide-topic pair"; the score is "a linear combination of two scores, one based on the words’ importance (Importance score) and the other on the similarity between the topic and the slide embeddings (Similarity score)". It uses a domain-specific pre-trained BERT model and leverages the hierarchical structure of slides, assuming the main title introduces the main discourse and each slide title introduces the slide's discourse. Multiplying M with slide-wise reading logs yields topic-based reading characteristics such as student topic preferences. (Erwin Daniel López Zapata et al. (2025))

### Claims
- [LECTOR achieves the highest keyphrase extraction performance among compared models at @15, Best and Mean evaluations on lecture slides](../claims/lector-highest-keyphrase-f1-lecture-slides.md) [+M]
- [Students rated LECTOR-extracted keyphrases as more relevant than TF-IDF-extracted keyphrases in a human evaluation](../claims/lector-human-evaluation-outperforms-tfidf.md) [+M]

## Related Research Methods
-

## Key Sources
- Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

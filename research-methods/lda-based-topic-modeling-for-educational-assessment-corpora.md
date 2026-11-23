---
type: research-method
id: lda-based-topic-modeling-for-educational-assessment-corpora
title: LDA-based topic modeling for educational assessment corpora
description: "A text-mining element in which Latent Dirichlet Allocation distills topics from application essays and aggregates them into moves, defined as \"a functional unit of text, which has an identifiable purpose\"."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-07
---

# LDA-based topic modeling for educational assessment corpora

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (1 associational, 1 qualitative), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
A text-mining element in which Latent Dirichlet Allocation distills topics from application essays and aggregates them into moves, defined as "a functional unit of text, which has an identifiable purpose". Thirty topics were reduced to seven moves (master specific, research skills, prior education, societal impact, interest to learn, city and university, extracurricular); per-essay move probabilities (0–1) served as predictors of master grades. The approach replaces subjective essay ratings, which suffer poor interrater reliability, with probabilistic topic measures.

## Accounts
<!-- How each source describes or uses the method -->
- **LDA-derived seven-move coding of application essays**: A text-mining element in which Latent Dirichlet Allocation distills topics from application essays and aggregates them into moves, defined as "a functional unit of text, which has an identifiable purpose". Thirty topics were reduced to seven moves (master specific, research skills, prior education, societal impact, interest to learn, city and university, extracurricular); per-essay move probabilities (0–1) served as predictors of master grades. The approach replaces subjective essay ratings, which suffer poor interrater reliability, with probabilistic topic measures. (de Boer et al. (2024))
- **Latent Dirichlet Allocation as an unsupervised probabilistic topic model for uncovering thematic structure in large educational text corpora**: Latent Dirichlet Allocation (LDA) is a probabilistic generative model for topic modeling, originally introduced by Blei, Ng, and Jordan in 2003. It is an unsupervised method that discovers patterns in text without manual labeling, assuming each document is a blend of multiple topics characterized by co-occurring word distributions. The article uses LDA within a "bag of words" approach to calculate topic prevalence across decades of physics teaching articles, integrating it with qualitative thematic interpretation to label and track 20 topics over time. (Caramaschi et al. (2024))
- **Latent Dirichlet Allocation as a generative probabilistic topic model**: Latent Dirichlet Allocation is "a generative probabilistic modeling technique that tries to extract the latent or hidden themes from a set of texts or documents". It assumes documents are mixtures of latent topics, each topic a weighted distribution over words, and reverse-engineers topic-word and document-topic distributions from word co-occurrence using a bag-of-words simplification. The article presents LDA as epistemologically similar to simplified toy models in physics, requiring user-specified K and α parameters and multiple levels of validation. (Tor Ole B. Odden et al. (2018))

### Claims
- [Writing more about the specific master program ('master specific' move) predicts higher master grades](../claims/master-specific-move-predicts-higher-grades.md) [+M]
- [Writing more about the interest to learn ('interest to learn' move) predicts higher master grades](../claims/interest-to-learn-move-predicts-higher-grades.md) [+M]
- [Writing more about research skills predicts lower master grades](../claims/research-skills-move-predicts-lower-grades.md) [+M]
- [Writing more about desired societal impact predicts lower master grades](../claims/societal-impact-move-predicts-lower-grades.md) [+M]
- [Writing more about the city and university ('city and university' move) predicts lower master grades](../claims/city-university-move-predicts-lower-grades.md) [+M]
- [The final LDA model for the combined corpus achieved a coherence score of 0.577, selected from 15 averaged models using the elbow method and qualitative inspection.](../claims/lda-model-coherence-0-577-selection.md) [+M]

## Related Research Methods
-

## Key Sources
- de Boer, Van Rijnsoever, de Bresser. (2024). Dear admission committee…: Which moves in application essays predict student master grades? PLoS One. https://doi.org/10.1371/journal.pone.0304394
- Caramaschi, M. and Odden, T. O. B. (2024). Uncovering shifts in the history of Physics education: a systematic, NLP-based, thematic analysis of articles from The Physics Teacher and Physics Education journals (1966 - 2019). https://scholar.google.com/scholar?q=Uncovering+shifts+in+the+history+of+Physics+education
- Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero. (2018). Thematic Analysis of 18 Years of PERC Proceedings using Natural Language Processing. https://github.com/uio-ccse/PERC_TopicModel

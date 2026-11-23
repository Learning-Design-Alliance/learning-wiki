---
type: product
id: perc-proceedings-corpus-and-lda-analysis-pipeline
title: PERC proceedings corpus and LDA analysis pipeline
description: A corpus of PERC proceedings papers paired with preprocessing and Gensim-based LDA analysis code released by Odden et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# PERC proceedings corpus and LDA analysis pipeline

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
A corpus of PERC proceedings papers paired with preprocessing and Gensim-based LDA analysis code released by Odden et al. for quantitative thematic mapping of physics education research.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **PERC proceedings corpus and LDA analysis pipeline (Gensim-based, code released)**: A corpus of all available PERC proceedings PDFs from 2001-2018—"In total, this resulted in 1302 individual papers"—pre-processed with PyPDF2 scraping, stopword removal, part-of-speech-aware lemmatization, and bi-gram detection, leaving 29026 words and bi-grams before filtering. Modeling used Gensim's variational-inference LDA with pandas, NLTK, numpy, scipy, and matplotlib. A selection of code is released at https://github.com/uio-ccse/PERC_TopicModel. (Tor Ole B. Odden et al. (2018))

### Claims

## Related Products and Programmes
-

## Key Sources
- Tor Ole B. Odden, Alessandro Marin, and Marcos D. Caballero. (2018). Thematic Analysis of 18 Years of PERC Proceedings using Natural Language Processing. https://github.com/uio-ccse/PERC_TopicModel

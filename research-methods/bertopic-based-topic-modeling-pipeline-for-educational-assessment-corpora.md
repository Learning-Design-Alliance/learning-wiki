---
type: research-method
id: bertopic-based-topic-modeling-pipeline-for-educational-assessment-corpora
title: BERTopic-based topic modeling pipeline for educational assessment corpora
description: "A six-step NLP pipeline the authors applied to 11,540 NMLE item texts (stems plus answer choices): preprocessing with the MeCab morphological analyzer and the MANBYO medical dictionary, embedding with the Japanese Sentence Transformer model \"sonoisa/sentence-bert-base-ja-mean-tokens-v2\", UMAP dimens"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-05
---

# BERTopic-based topic modeling pipeline for educational assessment corpora

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A six-step NLP pipeline the authors applied to 11,540 NMLE item texts (stems plus answer choices): preprocessing with the MeCab morphological analyzer and the MANBYO medical dictionary, embedding with the Japanese Sentence Transformer model "sonoisa/sentence-bert-base-ja-mean-tokens-v2", UMAP dimensionality reduction, HDBSCAN clustering, CountVectorizer tokenization, and c-TF-IDF weighting. It "effectively classified 10,129 of the 11,540 (88%) items into 25 topics", with topic labels established through focus group consensus. Key parameters (n_neighbors=3, n_components=10, min_cluster_size=20) were tuned via trial and error, and sensitivity checks confirmed main conclusions were stable.

## Accounts
<!-- How each source describes or uses the method -->
- **BERTopic-based topic modeling pipeline for Japanese examination text using MeCab, MANBYO dictionary, and Japanese Sentence-BERT embeddings**: A six-step NLP pipeline the authors applied to 11,540 NMLE item texts (stems plus answer choices): preprocessing with the MeCab morphological analyzer and the MANBYO medical dictionary, embedding with the Japanese Sentence Transformer model "sonoisa/sentence-bert-base-ja-mean-tokens-v2", UMAP dimensionality reduction, HDBSCAN clustering, CountVectorizer tokenization, and c-TF-IDF weighting. It "effectively classified 10,129 of the 11,540 (88%) items into 25 topics", with topic labels established through focus group consensus. Key parameters (n_neighbors=3, n_components=10, min_cluster_size=20) were tuned via trial and error, and sensitivity checks confirmed main conclusions were stable. (Morimoto Y et al. (2025))

### Claims
- [BERTopic topic modeling of 24 NMLE sessions identified 25 topics, of which 10 increased in prominence, including non-organ-specific topics such as accountability and community health care](../claims/nmle-topic-modeling-ten-increasing-topics.md) [+M]

## Related Research Methods
-

## Key Sources
- Morimoto Y, Shikino K, Nomura Y, Ito S. (2025). Trends in the Japanese National Medical Licensing Examination: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/78214

---
type: design
id: etf-forecasting-pipeline-sentiment-dataset
title: Student-built ETF forecasting pipeline with LLM-scored news sentiment dataset
description: "The project's technical artifact is a two-stage predictive system: regression models estimate the magnitude of ETF price deltas and classification models predict direction, with predictions merged by multiplying magni..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: freyaa-chawla-2026
    resource: "https://arxiv.org/abs/2605.05144"
    title: "Freyaa Chawla, Ahan Chawla, Rishi Singh, Joe Germino, Grigorii Khvatskii. (2026). Human-AI Co-Mentorship in Project-Based Learning: A Case Study in Financial Forecasting. arXiv preprint. https://arxiv.org/abs/2605.05144"
    author: Freyaa Chawla, Ahan Chawla, Rishi Singh, Joe Germino, Grigorii Khvatskii
---

# Student-built ETF forecasting pipeline with LLM-scored news sentiment dataset

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The project's technical artifact is a two-stage predictive system: regression models estimate the magnitude of ETF price deltas and classification models predict direction, with predictions merged by multiplying magnitude and sign. The dataset covers "a historical price dataset for 29 exchange-traded funds (ETFs), covering January 2, 2024 through September 23, 2025" harvested via the Yahoo Finance API, plus 260 scraped NASDAQ news articles scored by gpt-5-mini on a -10 to +10 scale with justifications, aggregated daily by sector. Sentiment coverage was sparse and uneven across ETFs, from 0% to 23.16% as shown in Table 1.

## Design Implications

### Context
#### Requirements
- Mentor intervention was needed for rate limiting, error recovery, and anti-bot scraping measures such as dynamic content loading.
#### Constraints
- Sector-level sentiment aggregation may dilute ETF-specific signals; zero-imputation for days without news may introduce bias; LLM scores were not validated against human-coded ground truth.

### Target Learners
- high-school students
- early-undergraduate students

### Learning Goals
- working with APIs and structured financial data
- machine learning model development and validation
- web scraping and data engineering

### Claims
- [Sentiment Features Did Not Improve Etf Forecasting](../claims/sentiment-features-did-not-improve-etf-forecasting.md) [+M]
- [Svm Regressors Outperformed Other Regressors](../claims/svm-regressors-outperformed-other-regressors.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Freyaa Chawla, Ahan Chawla, Rishi Singh, Joe Germino, Grigorii Khvatskii. (2026). Human-AI Co-Mentorship in Project-Based Learning: A Case Study in Financial Forecasting. arXiv preprint. https://arxiv.org/abs/2605.05144

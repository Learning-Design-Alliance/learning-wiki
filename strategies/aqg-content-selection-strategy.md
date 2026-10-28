---
type: strategy
id: aqg-content-selection-strategy
title: "Content selection: identify important sentences or concepts before generating questions"
description: Because the number of questions in examinations is limited, content selection determines important sentences, parts of sentences, or concepts about which to generate questions.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: ghader-kurdi-2020
    resource: "https://doi.org/10.1007/s40593-019-00186-y"
    title: "Ghader Kurdi, Jared Leo, Bijan Parsia, Uli Sattler, Salam Al-Emari. (2020). A Systematic Review of Automatic Question Generation for Educational Purposes. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-019-00186-y"
    author: Ghader Kurdi, Jared Leo, Bijan Parsia, Uli Sattler, Salam Al-Emari
---

# Content selection: identify important sentences or concepts before generating questions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because the number of questions in examinations is limited, content selection determines important sentences, parts of sentences, or concepts about which to generate questions. The review summarises multiple characterisations of importance, including Huang and He's (2016) keyness, completeness, and independence metrics, topic modelling, vector-space similarity to the document, and filtering of sentences insufficient on their own to make valid questions. The majority approach instead generates all possible questions and leaves selection to exam designers, which the review notes is not feasible in self-assessment settings where questions are generated on the fly.

## Design Implications

### Context
#### Requirements
- A criterion for sentence or concept importance, or a setting such as self-assessment where on-the-fly selection is needed
#### Constraints
- Content selection was of interest mainly for text-based approaches; only one study addressed content selection from structured knowledge bases

### Target Learners
- learners in self-assessment, self-study, or examination settings

### Target Learning Goals
- questions targeting the important content of learning material

## Related Strategies

- [Over-generate and rank: generate many questions then filter for quality](overgenerate-and-rank-aqg.md)
- [Text Marking And Highlighting](text-marking-and-highlighting.md)

## Examples
-

## Key Sources
- Ghader Kurdi, Jared Leo, Bijan Parsia, Uli Sattler, Salam Al-Emari. (2020). A Systematic Review of Automatic Question Generation for Educational Purposes. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-019-00186-y

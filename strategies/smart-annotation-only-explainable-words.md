---
type: strategy
id: smart-annotation-only-explainable-words
title: Annotate only words that the knowledge graph can explain, to avoid overwhelming readers with redundant glosses
description: "YAI4Edu's smart annotation mechanism decides which words to underline as clickable glosses."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: sovrano-francesco-2024
    resource: "https://doi.org/10.1007/s40593-024-00399-w"
    title: "Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio. (2024). How to Improve the Explanatory Power of an Intelligent Textbook: a Case Study in Legal Writing. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00399-w"
    author: Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio
---

# Annotate only words that the knowledge graph can explain, to avoid overwhelming readers with redundant glosses

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
YAI4Edu's smart annotation mechanism decides which words to underline as clickable glosses. It checks whether a word is a stop word and, if not, generates its overview via the Intelligent Explanation Generator and annotates the word only when the cumulative pertinence score of the overview's answers exceeds a threshold. The article states this is "intended to remove noisy annotations and distractors so that the reader can focus only on the most central and well-explained concepts," since annotating common-sense words would hinder usability.

## Design Implications

### Context
#### Requirements
- A knowledge graph extracted from the textbook and supplementary texts
- A cumulative pertinence threshold for deciding annotation
#### Constraints
- Only a tiny fraction of the words in a text are helpful to explain; many words have common-sense meanings and should not be annotated

### Target Learners
- Readers of interactive intelligent textbooks

### Target Learning Goals
- Focused exploration of central, well-explained concepts without distraction

### Affordances
- Illocutionary Explanation Theory Archetypal Questions

## Related Strategies
- Yai4Edu Explanatory Textbook Pipeline

## Examples
-

## Key Sources
- Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio. (2024). How to Improve the Explanatory Power of an Intelligent Textbook: a Case Study in Legal Writing. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00399-w

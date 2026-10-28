---
type: strategy
id: filter-summaries-before-automated-scoring
title: Filter student summaries for effort and topicality before automated scoring
description: Before passing student summaries to the LLM scoring models, iTELL applies lightweight filters that reject non-effortful submissions.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: morris-2025
    resource: "https://doi.org/10.1007/s40593-024-00395-0"
    title: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0"
    author: "Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D"
---

# Filter student summaries for effort and topicality before automated scoring

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Before passing student summaries to the LLM scoring models, iTELL applies lightweight filters that reject non-effortful submissions. The article reports that "summaries that heavily borrow from the source text or contain offensive language are rejected without being analyzed by the LLMs," with source borrowing based on overlapping n-grams and offensive language on a word list, alongside a 50–200 word length check and a Doc2Vec topic-similarity check. These filters ensure only effortful summaries reach the models and reduce computational load.

## Design Implications

### Context
#### Requirements
- A source text is available for n-gram overlap and topic-similarity comparison
- A length rule (50–200 words in iTELL) and an offensive word list are configured
#### Constraints
- The article presents the filters as part of the iTELL implementation; it does not report a separate evaluation of the filters' accuracy

### Target Learners
- students writing summaries in intelligent textbooks or online learning platforms

### Target Learning Goals
- authentic summarization practice and accurate automated formative feedback

## Related Strategies

- [Combine data-driven and expert-driven approaches, and add a filter network, to mitigate non-factual output in automated feedback](combine-data-driven-expert-driven-feedback-generation.md)

## Examples
-

## Key Sources
- Morris, W., Crossley, S., Holmes, L., Ou, C., Dascalu, M., & McNamara, D. (2025). Formative Feedback on Student-Authored Summaries in Intelligent Textbooks Using Large Language Models. International Journal of Artificial Intelligence in Education, 35, 1022–1043. https://doi.org/10.1007/s40593-024-00395-0

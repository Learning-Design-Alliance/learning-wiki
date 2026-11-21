---
type: strategy
id: hybrid-llm-pos-vocabulary-level-assignment
title: "Use a hybrid LLM-plus-PoS assignment: LLMs for ambiguous words, PoS-based matching for non-ambiguous words"
description: "Based on the complementary error patterns observed, the authors recommend combining the two systems: LLMs excel where a word has multiple CEFR levels within one part of speech, while deterministic PoS-based matching s..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: stefano-bannò-2025
    resource: "https://arxiv.org/abs/2506.02758"
    title: "Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. https://arxiv.org/abs/2506.02758"
    author: Stefano Bannò, Kate M. Knill, Mark J. F. Gales
---

# Use a hybrid LLM-plus-PoS assignment: LLMs for ambiguous words, PoS-based matching for non-ambiguous words

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Based on the complementary error patterns observed, the authors recommend combining the two systems: LLMs excel where a word has multiple CEFR levels within one part of speech, while deterministic PoS-based matching suffices and even performs best where the EVP lists a single level. The article concludes that "the most effective solution may lie in a hybrid approach, where an LLM is used to handle ambiguous words, while a PoS-based model deals with non-ambiguous ones." This targets automated writing evaluation systems that need word-level vocabulary levels at scale.

## Design Implications

### Context
#### Requirements
- A PoS tagger and EVP lookup for non-ambiguous lemmas; an LLM with EVP options for ambiguous lemmas
#### Constraints
- The PoS-based route misclassifies words used with meanings not covered in the EVP; LLMs were given all options including irrelevant PoS tags, which lowers their non-ambiguous accuracy

### Target Learners
- L2 English learners

### Target Learning Goals
- accurate word-level CEFR vocabulary assessment

## Claims

- [LLMs outperform a PoS-based baseline and a random baseline on word-level CEFR prediction of L2 learner writing, with the largest gains on ambiguous words](../claims/llms-beat-pos-baseline-word-level-cefr.md) [+W]
- [LLMs can identify the intended EVP meaning of polysemous words in context, with accuracy decreasing as the number of candidate meanings increases](../claims/llm-evp-sense-disambiguation-accuracy.md) [+W]
- [Word-level CEFR distributions predicted with an LLM differentiate essay-level proficiency bands better than PoS-based predictions and yield stronger holistic-score correlations on EFCAMDAT](../claims/llm-word-features-essay-proficiency-efcamdat.md) [-W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Stefano Bannò, Kate M. Knill, Mark J. F. Gales. (2025). Exploiting the English Vocabulary Profile for L2 word-level vocabulary assessment with LLMs. arXiv. https://arxiv.org/abs/2506.02758

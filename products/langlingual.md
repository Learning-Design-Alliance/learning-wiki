---
type: product
id: langlingual
title: LangLingual
description: LangLingual is a language-learning software system that estimates and tracks English-learner proficiency using word-bank analytics combined with LLM-based scoring.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# LangLingual

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
LangLingual is a language-learning software system that estimates and tracks English-learner proficiency using word-bank analytics combined with LLM-based scoring.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Hybrid proficiency scoring combining rule-based word-bank levels with LLM-as-judge prediction**: LangLingual estimates learner proficiency with a hybrid scoring approach that combines rule-based and model-based evaluation. Learner input words are lemmatised and checked against the word bank, computing average and median levels for matched words; the same input is also passed to an LLM with a crafted prompt requesting a level prediction between 1-14. The two estimates are combined as Levelcombined = w_wb × Level_wb + w_llm × Level_llm with w_wb = 0.4 and w_llm = 0.6. The authors state this "ensures more accurate proficiency estimation especially because 50,000 words does not sufficiently reflect all possible words in the English Language". (Sammriddh Gupta et al. (2025))

### Claims

## Related Products and Programmes
-

## Key Sources
- Sammriddh Gupta, Sonit Singh, Aditya Joshi, Mira Kim. (2025). LangLingual: A Personalised, Exercise-oriented English Language Learning Tool Leveraging Large Language Models. arXiv preprint. https://arxiv.org/abs/2510.23011

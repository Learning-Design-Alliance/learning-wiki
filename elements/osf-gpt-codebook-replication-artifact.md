---
type: element
id: osf-gpt-codebook-replication-artifact
title: OSF repository of prompts, codebooks, and code for LLM-assisted codebook development
description: "A released replication package hosting the code for the article's codebook development process together with all employed prompts and all codebooks produced by GPT across both studies."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: zambrano-2026
    resource: "https://osf.io/g3z4x"
    title: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x"
    author: "Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C"
---

# OSF repository of prompts, codebooks, and code for LLM-assisted codebook development

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A released replication package hosting the code for the article's codebook development process together with all employed prompts and all codebooks produced by GPT across both studies. The article states: "The code for our codebook development process and all the employed prompts and codebooks produced by GPT are available for replication purposes at: https://osf.io/g3z4x". It supports researchers reproducing or extending the three-step human-AI workflow and the four prompting-strategy comparisons in new theoretical domains or datasets.

## Design Implications

### Context
#### Requirements
- An OpenAI GPT API key to re-run the released prompts
#### Constraints
- 

### Target Learners
- learning scientists and educational data mining researchers conducting qualitative analysis

### Target Learning Goals
- replicable theory-informed qualitative codebook development with LLM assistance

## Claims

- [GPT-4o prompted only with SRL theory references generates a codebook accurately representing most key elements of both foundational SRL theories](../claims/gpt4o-theory-references-codebook-covers-srl-theories.md) [+W]
- [Human review remains essential after GPT-based codebook generation, producing a final refined SRL codebook of eleven constructs](../claims/human-refinement-essential-gpt-codebooks.md) [+W]
- [Fully inductive LLM codebook development risks importing unexamined sensitizing concepts, such as folk theories and scientific misconceptions, from the model's training data](../claims/llm-inductive-coding-sensitizing-concept-risk.md) [+W]
- [In the interest-development context, naming the theory without full references produced the most practical and usable codebook, while supplying full papers enhanced theoretical alignment but reduced applicability](../claims/naming-theory-most-practical-prompting-strategy.md) [+W]
- [Adding think-aloud data to theory prompts improves GPT-4o codebook completeness and alignment with the data](../claims/theory-plus-data-prompting-improves-codebook.md) [+W]

## Related Elements

- [LLM-queries GitHub repository for LLM essay-coding analysis pipeline](llm-queries-github-analysis-code.md)

## Examples

- [Name the target theory in the prompt without supplying full reference papers when practical, usable codebooks are the goal](../strategies/name-theory-without-full-references-prompting.md)
- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](../strategies/zero-shot-prompt-codebook-translation-strategy.md)

## Key Sources
- Zambrano, A.F., Wei, Z., Zhang, J., Baker, R.S., Ocumpaugh, J., Barany, A., Liu, X., Ginger, J., Paquette, L., Zhou, Y., & Borchers, C. (2026). Data Plus Theory Equals Codebook: Leveraging LLMs for Human-AI Codebook Development. Journal of Educational Data Mining, Volume 18, No 1. https://osf.io/g3z4x

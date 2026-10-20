---
type: research-method
id: cpig-the-creative-psychometric-item-generator-framework
moved_from: [design/cpig-multi-stage-prompting-quality-filters]
title: "CPIG: the creative psychometric item generator framework"
description: CPIG is an iterative LLM-based framework for generating and validating creativity test items for the creative problem-solving (CPS) task.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: antonio-laverghetta-jr-2024
    resource: "https://arxiv.org/abs/2409.00202"
    title: "Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202"
    author: Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty
---

# CPIG: the creative psychometric item generator framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
CPIG is an iterative LLM-based framework for generating and validating creativity test items for the creative problem-solving (CPS) task. It uses LLMs as "item generators" to write items, "item response generators" to create human-like solutions under baseline, demographic, or psychometric prompting profiles, and an item scorer (a roberta-base originality model) to select k high-originality items as few-shot exemplars for the next generation round. The article hypothesizes that "items with high quality should enable more creative responses and will tend to elicit better originality scores on average than those that are of lower quality," making originality a proxy for item quality. It extends automated item generation, which has focused on multiple-choice cognitive and non-cognitive items, into the creativity domain.

## Accounts
<!-- How each source describes or uses the method -->
- **CPIG: the creative psychometric item generator framework**: CPIG is an iterative LLM-based framework for generating and validating creativity test items for the creative problem-solving (CPS) task. It uses LLMs as "item generators" to write items, "item response generators" to create human-like solutions under baseline, demographic, or psychometric prompting profiles, and an item scorer (a roberta-base originality model) to select k high-originality items as few-shot exemplars for the next generation round. The article hypothesizes that "items with high quality should enable more creative responses and will tend to elicit better originality scores on average than those that are of lower quality," making originality a proxy for item quality. It extends automated item generation, which has focused on multiple-choice cognitive and non-cognitive items, into the creativity domain. (Antonio Laverghetta Jr. et al. (2024))
- **Multi-stage prompting with rule-based quality filters for item generation**: CPIG's item generation follows a multi-stage prompting pattern: a first LLM produces word lists (three names, a place, and an action) that item-generator LLMs must incorporate, which the authors say helps "maximize diversity in scenario content by using different word lists to ensure no two item generation prompts are the same." Generated scenarios then pass rule-based validity filters: a Flesch reading-ease floor of 45 with a 140-token minimum, a string blacklist targeting priming (e.g., scenarios containing "on the one hand" or "is torn between"), and a required termination string. The pattern is meant to reduce, not replace, human expert review of items.

### Claims

- [CPIG's iterative exemplar selection consistently improves the originality of LLM responses to generated CPS items by the last round of item generation](../claims/cpig-improves-response-originality-over-iterations.md) [+M]
- [Human annotators judge later-round CPIG items as improved in complexity but not in difficulty, with modest rater agreement](../claims/human-review-complexity-improves-difficulty-static.md) [+M]

## Related Research Methods
-

## Key Sources
- Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202

<!-- merged 2026-10-20 from designs/cpig-multi-stage-prompting-quality-filters ("Multi-stage prompting with rule-based quality filters for LLM item generation"), an isolated part of this page (maintainer 2026-10-20: fold approved): its body as it stood. Its bullets this page lacked were added above.

# Multi-stage prompting with rule-based quality filters for LLM item generation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
CPIG's item generation follows a multi-stage prompting pattern: a first LLM produces word lists (three names, a place, and an action) that item-generator LLMs must incorporate, which the authors say helps "maximize diversity in scenario content by using different word lists to ensure no two item generation prompts are the same." Generated scenarios then pass rule-based validity filters: a Flesch reading-ease floor of 45 with a 140-token minimum, a string blacklist targeting priming (e.g., scenarios containing "on the one hand" or "is torn between"), and a required termination string. The pattern is meant to reduce, not replace, human expert review of items.

## Design Implications

### Context
#### Requirements
- Human experts make the final decision on which items to include in a creativity assessment; the filters only eliminate items unlikely to be valid
#### Constraints
- The authors do not claim the priming string list is comprehensive, stating only that it eliminated most priming in generated scenarios

### Target Learners
- human test takers of creativity assessments

### Learning Goals
- generating valid, diverse creative problem-solving test items

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Antonio Laverghetta Jr., Simone Luchini, Averie Linell, Roni Reiter-Palmon and Roger Beaty. (2024). The creative psychometric item generator: a framework for item generation and validation using large language models. CREAI 2024: Workshop on Artificial Intelligence and Creativity. https://arxiv.org/abs/2409.00202
-->

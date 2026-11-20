---
type: strategy
id: prompt-template-catalog-strategy
title: Compile a catalog of evaluated prompt templates for well-defined tasks and use them to teach prompting skills
description: The authors recommend compiling a catalog of evaluated prompt templates for well-defined tasks such as documenting Python functions, which tool vendors could integrate into their tools and educators could use, togethe...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: hans-alexander-kruse-2024
    resource: "https://arxiv.org/abs/2408.00686"
    title: "Hans-Alexander Kruse, Tim Puhlfürß, Walid Maalej. (2024). Can Developers Prompt? A Controlled Experiment for Code Documentation Generation. https://arxiv.org/abs/2408.00686"
    author: Hans-Alexander Kruse, Tim Puhlfürß, Walid Maalej
---

# Compile a catalog of evaluated prompt templates for well-defined tasks and use them to teach prompting skills

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors recommend compiling a catalog of evaluated prompt templates for well-defined tasks such as documenting Python functions, which tool vendors could integrate into their tools and educators could use, together with underlying ideas and hints, to teach prompting skills in schools and universities. Each template could include instructions for the LLM to ask clarifying and contextual questions, e.g., related to the expected documentation style. The authors caution that "Such templates should only provide guidance and should not hinder human creativity in asking out-of-the-box and follow-up questions to an LLM-powered tool."

## Design Implications

### Context
#### Requirements
- Templates must be evaluated for the well-defined task they target
#### Constraints
- Templates should only provide guidance and should not hinder human creativity in asking out-of-the-box and follow-up questions

### Target Learners
- professional software developers
- computer science students

### Target Learning Goals
- effective prompting of LLMs for code documentation

## Claims

- [Developers' successful ad-hoc prompts were short, keyword-based, and never included prompt engineering techniques such as examples or templates](../claims/ad-hoc-prompts-short-keyword-based-no-techniques.md) [-W]
- [Professionals showed no statistically significant rating differences between ad-hoc and predefined prompt tools, partly because some used the Docstring keyword](../claims/professionals-no-significant-prompt-format-differences.md) [+W]
- [Students rated the predefined prompt tool significantly more positive than the ad-hoc prompt tool in five of six UEQ user experience categories](../claims/students-prefer-predefined-prompt-tool-ux.md) [+W]
- [Students rated documentation from a predefined few-shot prompt significantly higher than documentation from ad-hoc prompts on readability, conciseness and usefulness, and on helpfulness for one of two functions](../claims/students-rate-predefined-prompt-documentation-higher.md) [+W]

## Related Strategies


## Examples
-

## Key Sources
- Hans-Alexander Kruse, Tim Puhlfürß, Walid Maalej. (2024). Can Developers Prompt? A Controlled Experiment for Code Documentation Generation. https://arxiv.org/abs/2408.00686

---
type: strategy
id: teler-level2-3-prompt-variable-extraction
title: Use structured TELeR-style prompts (Level 2-3) specifying output format to elicit instructional-goal variables from LLMs
description: "The article's prompting recipes progress from a one-sentence task statement (Level 1) to multi-sentence role-and-task prompts (Level 2) and bulleted sub-task prompts (Level 3) that specify JSON output format for varia..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: effat-farhana-2024
    resource: "https://doi.org/10.1145/3657604.3664695"
    title: "Effat Farhana, Souvika Sarkar, Ralph Knipper, Indrani Dey, Hari Narayanan, Sadhana Puntambekar, and Santu Karmaker. 2024. SimPal: Towards a Meta-Conversational Framework to Understand Teacher's Instructional Goals for K-12 Physics. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3664695"
    author: Effat Farhana, Souvika Sarkar, Ralph Knipper, Indrani Dey, Hari Narayanan, Sadhana Puntambekar, and Santu Karmaker
---

# Use structured TELeR-style prompts (Level 2-3) specifying output format to elicit instructional-goal variables from LLMs

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article's prompting recipes progress from a one-sentence task statement (Level 1) to multi-sentence role-and-task prompts (Level 2) and bulleted sub-task prompts (Level 3) that specify JSON output format for variable names and symbols. The authors conclude that "SimPal can do this task with a high degree of accuracy when provided with a well-defined prompt" and that "the LLM prompting level impacts SimPal's performance", recommending Level 2 and Level 3 prompts for this variable-extraction task.

## Design Implications

### Context
#### Requirements
- Prompts must specify the desired output format (e.g., JSON with variable Name and Symbol keys) and restrict output to relevant variables
#### Constraints
- Level 4 prompting (adding output evaluation criteria and few-shot examples) lowered F1 for all three LLMs in the preliminary experiments

### Target Learners
- K-12 science teachers configuring simulation-based lessons

### Target Learning Goals
- Identifying physical variables relevant to teachers' instructional goals

### Affordances
- [Simpal Meta Conversational Framework](../products/simpal.md)

## Claims

- [ChatGPT-3.5 outperformed PaLM 2 in F1 with Level 3 prompting on both simulation sources](../claims/chatgpt-outperforms-palm2-level3.md) [+W]
- [Level 3 TELeR prompting yielded higher F1 than Level 2 for both LLMs on Golabz simulations](../claims/level3-prompting-beats-level2-golabz.md) [+W]
- [All three evaluated LLMs' F1 scores fell with Level-4 prompting in preliminary experiments](../claims/level4-prompting-lowers-f1-preliminary.md) [+W]
- [SimPal identifies instructional-goal-relevant physics variables with moderate F1 (up to 0.60) across 63 simulations](../claims/simpal-variable-extraction-f1-moderate.md) [+W]
- [Golabz simulations outperformed PhET in F1 score, attributed to content alignment differences](../claims/golabz-outperformed-phet-f1.md) [+W]

## Related Strategies

- [Improve LLM feedback quality via JSON-schema prompts with hidden scoring keys and preprocessing code into structured dictionaries](llm-prompt-schema-and-preprocessing-strategy.md)
- [Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding](structured-prompts-clear-construct-definitions-llm-labeling.md)

## Examples
-

## Key Sources
- Effat Farhana, Souvika Sarkar, Ralph Knipper, Indrani Dey, Hari Narayanan, Sadhana Puntambekar, and Santu Karmaker. 2024. SimPal: Towards a Meta-Conversational Framework to Understand Teacher's Instructional Goals for K-12 Physics. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3664695

---
type: strategy
id: guided-inquiry-scaffolding-for-llm-agents
title: "Apply Guided Inquiry Learning scaffolding — phase-conditioned guidance plus hypothesis verification — to structure LLM agents' inquiry"
description: "A guidance strategy that structures an LLM agent's inquiry cycle by conditioning each generated step on the current inquiry phase and providing phase-specific instructions: during exploration the agent is prompted to..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: marta-knežević-2026
    resource: "https://arxiv.org/abs/2610.21604"
    title: "Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. https://arxiv.org/abs/2610.21604"
    author: Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser
---

# Apply Guided Inquiry Learning scaffolding — phase-conditioned guidance plus hypothesis verification — to structure LLM agents' inquiry

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A guidance strategy that structures an LLM agent's inquiry cycle by conditioning each generated step on the current inquiry phase and providing phase-specific instructions: during exploration the agent is prompted to "modify one variable at a time, following the 'controlling variables' experimentation strategy"; after observations it generates a Thought step analyzing how changes in the dependent variable relate to independent variables; and a verifier provides ground-truth verification of each hypothesis. The article shows this scaffolding, drawn from supports for human inquiry learners, raises strategic exploration and cause–effect reasoning and improves equation-discovery success across most models.

## Design Implications

### Context
#### Requirements
- An IL guide that conditions the model's generation on the current phase of the IL cycle
- A verifier providing ground-truth verification of the hypothesis
- In-context examples further improve outcomes for most models
#### Constraints
- Benefits of step-structure guidance alone are model-dependent; exceptions occurred for Qwen-14B (1-shot) and Vicuna-13B (0-shot)
- Performance gaps remain in the GIL method arising from inherent LLM limitations, including iterative hypothesizing and identifying cause–effect relationships

### Target Learners
- LLM-based agents performing inquiry tasks

### Target Learning Goals
- Systematic exploration of multivariable systems
- Evidence-based hypothesis refinement
- Explicit cause–effect reasoning

## Claims

- [GIL reasoning guidance increases explicit cause–effect relationships in agent reasoning, with cause–effect ratios reaching 1.00 in all GIL conditions](../claims/gil-increases-explicit-cause-effect-reasoning.md) [+W]
- [LLM agents rarely explore strategically without guidance; GIL scaffolding raises the proportion of strategic exploration steps](../claims/gil-raises-strategic-exploration-proportion.md) [+W]
- [Guided Inquiry Learning scaffolding improves LLM agents' equation-discovery success over unguided IL for most models](../claims/gil-scaffolding-improves-llm-equation-discovery.md) [+W]
- [LLM-based agents show limited inherent inquiry capabilities, with low rates of correctly discovered equations that improve with in-context examples](../claims/llm-agents-limited-inherent-inquiry-capabilities.md) [+W]
- [LLM agents repeat prior hypotheses and refine them in model-specific ways, suggesting a confirmation-bias-like tendency](../claims/llm-hypothesis-repetition-confirmation-bias.md) [+W]

## Related Strategies

- [Use proactive GenAI agents that guide students through visualisations with pre-defined scaffolding questions and feedback on responses](proactive-genai-scaffolding-questions-strategy.md)

## Examples
-

## Key Sources
- Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. https://arxiv.org/abs/2610.21604

---
type: strategy
id: match-llm-configuration-to-use-case-constraints
title: "Select LLM prompting configurations by use-case constraints: efficient single-agent prompting for education, multi-agent frameworks for high-stakes complex cases"
description: The article recommends that institutions choose between single-agent and multi-agent LLM configurations based on task complexity, resource constraints, and application setting.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: altermatt-fernando-r-2025
    resource: "https://doi.org/10.1186/s12909-025-07250-3"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J
---

# Select LLM prompting configurations by use-case constraints: efficient single-agent prompting for education, multi-agent frameworks for high-stakes complex cases

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends that institutions choose between single-agent and multi-agent LLM configurations based on task complexity, resource constraints, and application setting. It states that "selecting an appropriate configuration should be guided by use-case constraints": multi-agent frameworks may be justified for high-stakes clinical simulations or policy development, while computationally efficient single-agent strategies such as CoT + few-shot suit medical education and exam preparation without compromising accuracy.

## Design Implications

### Context
#### Requirements
- Access to a capable multilingual LLM (GPT-4o in this study) and an automated scoring pipeline for validation
#### Constraints
- Multi-agent configurations demand high computational resources (e.g., 21.14 API calls and ~192 seconds for MDAGENTS), limiting scalability in low-resource or real-time settings

### Target Learners
- medical students and trainees in Spanish-speaking medical schools

### Target Learning Goals
- clinical reasoning support, case-based learning, and scalable assessment development

## Claims

- [CoT + few-shot prompting delivers high accuracy with minimal computational overhead, offering an efficient alternative to multi-agent frameworks](../claims/cot-few-shot-efficient-alternative.md) [+W]
- [Multi-agent strategies incur substantially higher computational costs than single-agent methods on EUNACOM evaluation](../claims/multiagent-computational-cost-tradeoff.md) [+W]
- [MDAGENTS achieves the highest accuracy on Spanish-language EUNACOM questions, outperforming all other evaluated strategies](../claims/mdagents-highest-accuracy-eunacom.md) [+W]

## Related Strategies

- [Design hybrid instructional chatbot systems that balance breadth and depth via multi-agent architectures or adaptive interaction modes](hybrid-instructional-chatbot-design-strategy.md)
- [Select the variant-generation prompting protocol by deployment threat profile: zero-shot or structured CoT for construct fidelity, few-shot or dimension-preserving generation for surface separation](threat-profile-keyed-generation-protocol.md)

## Examples
-

## Key Sources
- Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3

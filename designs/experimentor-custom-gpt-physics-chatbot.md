---
type: design
id: experimentor-custom-gpt-physics-chatbot
title: "ExperiMentor: a custom GPT-based chatbot that generates and executes Python code for guided physics data analysis"
description: "ExperiMentor is a custom GPT-based chatbot built on the GPT-4o model that \"supports data analysis by automatically generating and executing Python code\"; students received only outputs such as results and visualizatio..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: henze-j-2026
    resource: "https://doi.org/10.3389/feduc.2026.1719670"
    title: "Henze J, Lademann J, Becker-Genschow S and Bresges A (2026). AI-supported data analysis boosts student motivation and reduces stress in physics education. Front. Educ. 11:1719670. https://doi.org/10.3389/feduc.2026.1719670"
    author: Henze J, Lademann J, Becker-Genschow S and Bresges A
---

# ExperiMentor: a custom GPT-based chatbot that generates and executes Python code for guided physics data analysis

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 design, 1 theoretical), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
ExperiMentor is a custom GPT-based chatbot built on the GPT-4o model that "supports data analysis by automatically generating and executing Python code"; students received only outputs such as results and visualizations, with optional code previews, but no direct interaction with the code environment. It was used by student teachers to evaluate thread and spring pendulum experiment data in the study's guided intervention.

## Design Implications

### Context
#### Requirements
- Operates via a system prompt enforcing identification-code authentication, a mentor-not-solver role definition, and a step-by-step interaction flow to manage cognitive load.
#### Constraints
- Implemented using the OpenAI GPT Creator and utilized between June and August 2024; not publicly hosted apart from the OpenAI ChatGPT GPT-Store and developed solely for research purposes without commercial interest.

### Target Learners
- student teachers analyzing physics experiment data

### Learning Goals
- determining gravitational acceleration from thread pendulum data
- calculating the spring constant from spring pendulum data
- data evaluation and interpretation competencies

### Claims

- [Across 28 project contexts, human-in-the-loop and independent peer review identified no conceptual or mathematical hallucinations, and Python visualization scripts executed without compilation errors on the zero-shot attempt.](../claims/no-conceptual-hallucinations-28-contexts.md) [+W]
- [External plugins such as Wolfram and the Advanced Data Analysis mode significantly improve ChatGPT-4's ability to perform calculations that LLMs cannot reliably do alone](../claims/plugins-improve-chatgpt4-calculation-ability.md) [+W]

## Related Designs

- [Custom-built web application integrating an AI chatbot into a three-part diagnostic reasoning case](ai-integrated-diagnostic-reasoning-web-application.md)
- [Jordan Chatbot: a unit-specific GPT-4o pedagogical support agent grounded in constructivist and socio-cultural learning theory](jordan-chatbot-unit-specific-gpt4o-agent.md)
- [Aspen: a prompt-engineered AI chatbot peer mentor for inquiry revision](aspen-ai-chatbot-peer-mentor.md)
- [ChatGPT-assisted Python visualization workflow for hydrogen 2p orbitals](chatgpt-python-2p-orbital-visualization-workflow.md)

## Examples
-

## Key Sources
- Henze J, Lademann J, Becker-Genschow S and Bresges A (2026). AI-supported data analysis boosts student motivation and reduces stress in physics education. Front. Educ. 11:1719670. https://doi.org/10.3389/feduc.2026.1719670

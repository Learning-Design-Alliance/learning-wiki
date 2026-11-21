---
type: strategy
id: multilingual-llm-feedback-design-recommendations
title: Prefer English-only prompts and EN→EN hints by default, but pair native-language instructions with native-language hints and match student model to language resource level
description: The authors distill their 352-setting experiment into design recommendations for LLM-based multilingual tutoring systems.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: junior-cedric-tonga-2025
    resource: "https://arxiv.org/abs/2506.04920"
    title: "Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2025). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. https://arxiv.org/abs/2506.04920"
    author: Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar
---

# Prefer English-only prompts and EN→EN hints by default, but pair native-language instructions with native-language hints and match student model to language resource level

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 2 studies (2 causal), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The authors distill their 352-setting experiment into design recommendations for LLM-based multilingual tutoring systems. They advise that "English hints are generally preferred; however, for HRLs and monolingual student models, native-language hints can be more effective," that EN→EN remains the most preferred hint strategy with a few exceptions, that larger tutor models such as LLaMA-3.3-70B should be preferred, and that monolingual models suit high-resource languages while multilingual models suit low-resource languages.

## Design Implications

### Context
#### Requirements
- A multilingual LLM tutoring setup with a choice of tutor and student models and configurable prompt and hint languages
#### Constraints
- Recommendations derive from LLM-simulated students, not real learners; the authors call for human-in-the-loop evaluations with real students
- With the smaller tutor model, no consistent hint-language patterns emerged

### Target Learners
- grade-school math students in multilingual and low-resource language settings

### Target Learning Goals
- effective multilingual formative feedback and hint generation for math reasoning

## Claims

- [The EN→EN hint generation strategy yields the highest average student gains across setups](../claims/en-to-en-hint-strategy-highest-gains.md) [+W]
- [English-only student prompting generally outperforms multilingual prompting for student gains, except when instructions and hints are both in the native language](../claims/english-only-prompting-beats-multilingual-prompting-llm-tutoring.md) [+W]
- [Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases](../claims/hint-language-impacts-student-gains.md) [+W]
- [A larger tutor model (LLaMA-3.3-70B) yields greater student gains than a smaller one, especially for low-resource languages](../claims/larger-tutor-model-greater-student-gains.md) [+W]
- [Multilingual student models perform better for low-resource languages while monolingual models suit high-resource languages](../claims/multilingual-student-models-lrl-monolingual-hrl.md) [+W]
- [English prompts generally yield better LLM accuracy than language-matched prompts, but top models perform comparably with language-matched prompts](../claims/english-prompt-advantage-top-models-comparable.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2025). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. https://arxiv.org/abs/2506.04920

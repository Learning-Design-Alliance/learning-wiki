---
type: strategy
id: simulated-multiagent-prompting-for-osce-generation
title: Use a simulated multiagent prompt combining role, instruction-based, chain, and few-shot prompting to generate OSCE stations with an LLM
description: "The article's best-performing configuration used a structured prompt simulating a supervised, sequential multiagent system: a supervisor agent coordinated four specialized agents (learning domain, vignette, checklist,..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: zouakia-z-2026
    resource: "https://doi.org/10.2196/82116"
    title: "Zouakia Z, Logak E, Szymczak A, Jais J-P, Burgun A, Tsopra R. (2026). AI-Driven Objective Structured Clinical Examination Generation in Digital Health Education: Comparative Analysis of Three GPT-4o Configurations. JMIR Medical Education. https://doi.org/10.2196/82116"
    author: Zouakia Z, Logak E, Szymczak A, Jais J-P, Burgun A, Tsopra R
---

# Use a simulated multiagent prompt combining role, instruction-based, chain, and few-shot prompting to generate OSCE stations with an LLM

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article's best-performing configuration used a structured prompt simulating a supervised, sequential multiagent system: a supervisor agent coordinated four specialized agents (learning domain, vignette, checklist, and SP script), each activated in sequence and receiving prior outputs. The prompt design "combined multiple prompting strategies": role prompting, instruction-based prompting drawn from the OSCE Vademecum, chain prompting into a sequenced workflow, and few-shot prompting with format illustrations. This configuration produced the most format-compliant, accurate, clear, and usable OSCE stations.

## Design Implications

### Context
#### Requirements
- A reference framework of OSCE construction guidelines to structure agent instructions
- A domain-specific knowledge base (the UPCité reference book) provided to the custom GPT
#### Constraints
- The article notes the prompt worked within an 8000-character limit and did not fully meet all checklist-format requirements

### Target Learners
- Medical and health professions educators designing OSCE assessment stations

### Target Learning Goals
- Production of standardized, usable OSCE stations for competency assessment

## Claims

- [A simulated-agents GPT-4o configuration achieved the highest format compliance of three configurations for generating OSCE stations in digital health](../claims/simulated-agents-gpt-highest-osce-format-compliance.md) [+M]
- [OSCEs from the simulated-agents GPT were significantly more usable and more often ranked first by experts than those from the other configurations](../claims/simulated-agents-gpt-osce-usability-and-expert-ranking.md) [+M]
- [The simulated-agents GPT configuration produced significantly clearer OSCE content than the other two configurations (P=.004)](../claims/simulated-agents-gpt-significantly-clearer-osce-content.md) [+M]
- [The simulated-agents GPT configuration produced significantly more accurate OSCE content than the other two configurations (P=.01)](../claims/simulated-agents-gpt-significantly-more-accurate-osce-content.md) [+M]
- [Experts identified recurring quality problems in LLM-generated OSCEs: leading cues, vignette-script inconsistencies, and overly theoretical content](../claims/expert-identified-quality-problems-llm-generated-osces.md) [~M]

## Related Strategies

- [Use few-shot prompting with chain-of-thought and annotated rubric examples for LLM-based scoring of learner-generated clinical text](few-shot-cot-annotated-rubric-prompting-strategy.md)
- [Development strategies targeting AI virtual patient limitations: expert-reviewed content, iterative prompt engineering, behavioral rules, few-shot prompting, and conversational memory](ai-virtual-patient-mitigation-strategies.md)
- [Configure the LLM simulated patient with behavioral constraints and standardized scripts to ensure consistency](llm-simulated-patient-prompt-constraints-strategy.md)

## Examples
-

## Key Sources
- Zouakia Z, Logak E, Szymczak A, Jais J-P, Burgun A, Tsopra R. (2026). AI-Driven Objective Structured Clinical Examination Generation in Digital Health Education: Comparative Analysis of Three GPT-4o Configurations. JMIR Medical Education. https://doi.org/10.2196/82116

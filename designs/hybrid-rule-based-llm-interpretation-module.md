---
type: design
id: hybrid-rule-based-llm-interpretation-module
title: Hybrid rule-based plus LLM-supported AI interpretation module
description: "The AI module combines \"a rule-based, explainable interpretation engine with optional LLM-supported reformulation when a live connection is available.\" Learners select predefined device-specific findings and optionall..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-04
sources:
  - id: inan-onur-akyüz-ali-2026
    resource: "https://doi.org/10.1186/s12909-026-09952-8"
    title: "İnan Onur; Akyüz Ali. (2026). Simulation- and AI-supported technical troubleshooting training for biomedical device technology students in intensive care equipment education. BMC Medical Education. https://doi.org/10.1186/s12909-026-09952-8"
    author: İnan Onur; Akyüz Ali
---

# Hybrid rule-based plus LLM-supported AI interpretation module

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The AI module combines "a rule-based, explainable interpretation engine with optional LLM-supported reformulation when a live connection is available." Learners select predefined device-specific findings and optionally add free-text notes; the rule engine scores rules against selections and falls back when no live model is available. Outputs comprise a technical summary, possible device-related causes, suggested verification steps and teaching notes, parsed as structured JSON.

## Design Implications

### Context
#### Requirements
- Instructor supervision; structured prompts and predefined knowledge base to keep interpretations grounded in device-specific fault patterns
#### Constraints
- Client-side API key storage is not secure for production environments; the LLM mode is not fully deterministic; output accuracy is not guaranteed

### Target Learners
- biomedical device technology students

### Learning Goals
- organizing observations into structured technical reasoning
- comparing fault hypotheses with structured feedback

### Claims
- 

## Related Designs

- [ProPACT Hybrid-AI feedback system with five feedback tools and hierarchical trigger policy](propact-hybrid-ai-feedback-system-five-tools.md)
- [Scenario-based fault analysis across four device modules with 18 fault patterns](icu-simulator-fault-scenario-set.md)

## Examples
-

## Key Sources
- İnan Onur; Akyüz Ali. (2026). Simulation- and AI-supported technical troubleshooting training for biomedical device technology students in intensive care equipment education. BMC Medical Education. https://doi.org/10.1186/s12909-026-09952-8

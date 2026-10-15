---
type: design
id: stepped-care-tiered-response-architecture-chatbot
title: "Stepped Care Model response architecture: chatbot tone, language and support intensity escalate proportionally with detected stress severity"
description: "The article applies the Stepped Care Model, described as \"a well recognised framework for a clinical approach of escalating intensity, tone and type of support in accordance with the level of stress detected\", as the..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: muhammad-fahad-bashir-2026
    resource: "https://doi.org/10.48550/arxiv.2609.11199"
    title: "Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://doi.org/10.48550/arxiv.2609.11199"
    author: Muhammad Fahad Bashir, Muhammad Afzal
---

# Stepped Care Model response architecture: chatbot tone, language and support intensity escalate proportionally with detected stress severity

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article applies the Stepped Care Model, described as "a well recognised framework for a clinical approach of escalating intensity, tone and type of support in accordance with the level of stress detected", as the logic governing how Sukoon generates responses. The chatbot module maps each classification output to one of three pre-defined response tiers (low, moderate, high), ranging "from a warm and encouraging approach at low stress to a grounding, calm, non -judgemental support at high stress". This framework determines both the opening wellness message served after classification and the tone of subsequent LLM-generated turns.

## Design Implications

### Context
#### Requirements
- A stress-severity classification output that can be mapped to one of three pre-defined tiers of responses
#### Constraints
- The article frames the model as a clinical approach whose application here is to escalate support with detected severity; response quality at each tier was checked only in a preliminary functional assessment

### Target Learners
- Pakistani university students classified at low, moderate or high stress levels

### Learning Goals
- Stress-level-appropriate wellness support whose intensity, tone and type match detected severity

### Claims

## Related Designs
- 

## Examples
-

## Key Sources
- Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://doi.org/10.48550/arxiv.2609.11199

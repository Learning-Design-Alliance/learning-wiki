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
    resource: "https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    title: "Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students"
    author: Muhammad Fahad Bashir, Muhammad Afzal
---

# Stepped Care Model response architecture: chatbot tone, language and support intensity escalate proportionally with detected stress severity

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

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
- [Preliminary Chatbot Evaluation Simulated Inputs Three Tiers](../claims/preliminary-chatbot-evaluation-simulated-inputs-three-tiers.md) [+M]
- [Confusion Matrix Low To Moderate Misclassification Safe Direction](../claims/confusion-matrix-low-to-moderate-misclassification-safe-direction.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Muhammad Fahad Bashir, Muhammad Afzal. (2026). An AI-Powered Culturally Aware Chatbot for Stress Detection and Wellness Support among Pakistani University Students Using NLP and Machine Learning. https://scholar.google.com/scholar?q=An+AI-Powered+Culturally+Aware+Chatbot+for+Stress+Detection+and+Wellness+Support+among+Pakistani+University+Students

---
type: element
id: cba-middle-school-math-chat-log-corpus
title: Conversation-based assessment (CBA) chat log corpus for middle school mathematics
description: A chat log dataset of over 10,000 student turns (human coder 1 coded N = 10,919 turns) collected from 107 middle school students classified as English learners (mean age 12.4 years) interacting with a conversation-bas...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: ober-2026
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F"
---

# Conversation-based assessment (CBA) chat log corpus for middle school mathematics

> **Element** · [All elements](index.md)
> **Evidence** · 7 claims (6 for, 1 against) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 7 claims rest on one study

## Description
A chat log dataset of over 10,000 student turns (human coder 1 coded N = 10,919 turns) collected from 107 middle school students classified as English learners (mean age 12.4 years) interacting with a conversation-based assessment for middle school mathematics. The CBA comprised "a sequence of six structured, interactive conversations between the student and three pedagogical agents, a teacher agent and two peer agents," designed to simulate small-group mathematical problem solving with NLP-based dialogue adaptation. Students completed up to seven tasks targeting six competencies including proportional reasoning.

## Design Implications

### Context
#### Requirements
- The system uses NLP to analyze student input and adjust the dialogue path based on characteristics of the student input, using a match score system
#### Constraints
- Participation varied between the human student and the pedagogical agents, with students producing fewer turns on average (mean = 24.55, SD = 8.28) and shorter responses (~7 words per turn) than the pedagogical agents

### Target Learners
- middle school students classified as English learners

### Target Learning Goals
- upper elementary and middle school math competencies including ratios, proportions, and proportional reasoning

## Claims

- [Constructs with higher operational clarity show higher overall coder agreement, and low clarity harms human coder agreement more than LLM agreement](../claims/construct-clarity-predicts-coding-agreement.md) [+W]
- [Human-human agreement (average κ = 0.644) was lower than the best LLM-LLM agreement (average κ = 0.856) across constructs](../claims/human-human-agreement-lower-than-llm-llm.md) [+W]
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](../claims/human-llm-agreement-low-construct-varying.md) [-W]
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](../claims/llm-pairwise-agreement-model-type-temperature.md) [+W]
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](../claims/llm-within-configuration-reliability-high.md) [+W]
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](../claims/temperature-construct-type-interaction-coding.md) [+W]
- [LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531)](../claims/llm-classification-agreement-varies-by-construct.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

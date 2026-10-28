---
type: design
id: eca-jack-restaurant-l2-agent
title: Embodied conversational agent Jack for restaurant-context English conversation practice
description: "The system is an embodied conversational agent, personified as Jack, implemented with the Unity game engine front-end and Node.js back-end, built on the authors' previous work."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: emmanuel-ayedoun-2018
    resource: "https://doi.org/10.1007/s40593-018-0171-6"
    title: "Emmanuel Ayedoun, Yuki Hayashi, Kazuhisa Seta. (2018). Adding Communicative and Affective Strategies to an Embodied Conversational Agent to Enhance Second Language Learners' Willingness to Communicate. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-018-0171-6"
    author: Emmanuel Ayedoun, Yuki Hayashi, Kazuhisa Seta
---

# Embodied conversational agent Jack for restaurant-context English conversation practice

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The system is an embodied conversational agent, personified as Jack, implemented with the Unity game engine front-end and Node.js back-end, built on the authors' previous work. It supports spoken dialogues in a restaurant context where learners are welcomed, guided to a table, order drinks and dishes, and request the bill. Speech recognition is performed by external services (Wit.ai and Dialogflow) that turn utterances into intents and entities with confidence scores. Jack also uses non-verbal backchannels like gaze, head nods, smiles, and blinking.

## Design Implications

### Context
#### Requirements
- Intents for the conversation domain must be defined beforehand on the Wit.ai or Dialogflow platform so they can be identified from learner utterances
#### Constraints
- The conversation is domain-specific (restaurant scenario); the dialogue script is written in XML and can be modified to target a different conversation context

### Target Learners
- Japanese EFL learners at a university

### Learning Goals
- Practicing daily English conversation and increasing willingness to communicate in L2

### Claims
- 

## Related Designs

- [Conversational pedagogical agent with AI-driven dialogue, lip-synchronised audio and conversation memory](ai-conversational-pedagogical-agent-system.md)
- [DiMaCA: a dialogue management model combining communication strategies and affective backchannels to foster WTC-friendly agent conversations](dimaca-dialogue-management-model.md)
- [Phoenix: a voice-based, non-embodied LLM conversational peer agent for group learning](phoenix-voice-llm-peer-agent-group-learning.md)

## Examples
-

## Key Sources
- Emmanuel Ayedoun, Yuki Hayashi, Kazuhisa Seta. (2018). Adding Communicative and Affective Strategies to an Embodied Conversational Agent to Enhance Second Language Learners' Willingness to Communicate. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-018-0171-6

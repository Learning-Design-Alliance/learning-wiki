---
type: design
id: dimaca-dialogue-management-model
title: "DiMaCA: a dialogue management model combining communication strategies and affective backchannels to foster WTC-friendly agent conversations"
description: DiMaCA is a dialogue management model specifying rules for when an embodied conversational agent deploys communication strategies (CS) and affective backchannels (AB) during L2 conversations.
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

# DiMaCA: a dialogue management model combining communication strategies and affective backchannels to foster WTC-friendly agent conversations

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
DiMaCA is a dialogue management model specifying rules for when an embodied conversational agent deploys communication strategies (CS) and affective backchannels (AB) during L2 conversations. Its rationale is 'increasing L2 learners' confidence via CSs and reducing their level of anxiety towards communication via ABs', in line with MacIntyre's WTC model. The model is implemented as a strategies management module that detects six conversation states (e.g., learner silent, learner NUNA, agent NUNA) and triggers adapted CS and AB accordingly, with CS chosen in a heuristically predefined order and AB chosen stochastically.

## Design Implications

### Context
#### Requirements
- A dialogue script defining the conversation domain, intent detection via external speech recognition services, and databases of CS and AB options per conversation state
#### Constraints
- The Guessing strategy is only an approximation: the agent does not perform dynamic reasoning about learner intention from a wide range of possibilities but relies on a narrow range of expected answers specified in advance in the dialogue script

### Target Learners
- Japanese undergraduate and graduate EFL learners

### Learning Goals
- Willingness to communicate in English as a second language

### Claims
- 

## Related Designs

- [Nine communication strategies and four categories of affective backchannels implemented in DiMaCA](dimaca-cs-ab-strategy-sets.md)
- [Embodied conversational agent Jack for restaurant-context English conversation practice](eca-jack-restaurant-l2-agent.md)

## Examples
-

## Key Sources
- Emmanuel Ayedoun, Yuki Hayashi, Kazuhisa Seta. (2018). Adding Communicative and Affective Strategies to an Embodied Conversational Agent to Enhance Second Language Learners' Willingness to Communicate. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-018-0171-6

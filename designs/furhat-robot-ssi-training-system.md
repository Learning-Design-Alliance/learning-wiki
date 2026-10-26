---
type: design
id: furhat-robot-ssi-training-system
title: Furhat robot-assisted speech training system with simulated social interaction
description: "The system uses the social robot Furhat, which \"can be programmed to interact with autistic children and provide effective training\", with cloud-based speech recognition (Google ASR and Microsoft Azure Cognitive Servi..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
sources:
  - id: chen-2026
    resource: "https://doi.org/10.1038/s41539-026-00425-7"
    title: "Chen, S., Wang, B.X., Cheung, J.C.-W. et al. (2026). Lab perceptual training and robot-assisted training in improving speech prosody of autistic children. npj Science of Learning. https://doi.org/10.1038/s41539-026-00425-7"
    author: Chen, S., Wang, B.X., Cheung, J.C.-W. et al
---

# Furhat robot-assisted speech training system with simulated social interaction

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The system uses the social robot Furhat, which "can be programmed to interact with autistic children and provide effective training", with cloud-based speech recognition (Google ASR and Microsoft Azure Cognitive Services) and speech synthesis (Amazon Polly and Acapela TTS), a back-projected face with synchronized lip movements, and face tracking. A web-application architecture (Raspberry Pi 4B web server in Golang, React.js GUI with participant and instructor modes) synchronizes image display, audio and the robot's facial expressions. Children ask the robot questions and judge whether its answers match the elicited focus type and position.

## Design Implications

### Context
#### Requirements
- A Furhat robot with cloud-based ASR and TTS services, a slim client with an internet browser, and the custom web server and GUI system for interaction control and synchronization
#### Constraints
- Training materials were limited to six sentences with subject-verb-object structure; the study's sentences were limited to five-syllable subject-verb-object structures

### Target Learners
- Cantonese-speaking autistic children

### Learning Goals
- Using prosodic cues (duration, f0, intensity) to mark broad, narrow and contrastive focus in speech production

### Claims
- [Robot Ssi Training Improves Duration And Post Focus F0](../claims/robot-ssi-training-improves-duration-and-post-focus-f0.md) [+M]
- [Robot Training Effects Limited To Contrastive Focus](../claims/robot-training-effects-limited-to-contrastive-focus.md) [~M]

## Related Designs
- 

## Examples
-

## Key Sources
- Chen, S., Wang, B.X., Cheung, J.C.-W. et al. (2026). Lab perceptual training and robot-assisted training in improving speech prosody of autistic children. npj Science of Learning. https://doi.org/10.1038/s41539-026-00425-7

---
type: design
id: speech-to-sign-translation-three-module-architecture
title: Three-module speech-to-sign-language translation architecture with a rule-based translation core
description: "The article describes a pipeline for translating spoken or text language to sign language comprising three modules: \"First speech recognizer as input if dealing with spoken language, the translation system that conver..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: wanzare-2024
    resource: "https://ai4d.africa/"
    title: "Wanzare, L., Okutoyi, J., Kang'ahi, M., & Ayere, M. (2024). Kenyan Sign Language (KSL) Dataset: Using Artificial Intelligence (AI) in Bridging Communication Barrier among the Deaf Learners. https://ai4d.africa/"
    author: "Wanzare, L., Okutoyi, J., Kang'ahi, M., & Ayere, M"
---

# Three-module speech-to-sign-language translation architecture with a rule-based translation core

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article describes a pipeline for translating spoken or text language to sign language comprising three modules: "First speech recognizer as input if dealing with spoken language, the translation system that converts the text to sign language and finally a graphical avatar as output". Because there are no large KSL datasets for training statistical or deep learning models, the project follows a rule-based approach, which the article notes has been popular and appropriate for text-to-sign-language systems. HamNoSys serves as the language-independent phonetic notation, convertible to SiGML for avatar animation rendering.

## Design Implications

### Context
#### Requirements
- a sign writing notation (HamNoSys) representing signs digitally
- conversion of HamNoSys to SiGML as input to the animation module
- a graphical avatar for rendering output signs
#### Constraints
- rule-based systems were preferred because large training datasets for KSL do not exist
- HamNoSys itself does not have a representation for ease of rendering

### Target Learners
- deaf learners in integrated Kenyan classrooms

### Learning Goals
- real-time translation of spoken and written English into Kenyan Sign Language during classroom interactions

### Claims
- [Ai4Ksl 4000 Words Hamnosys Transcription](../claims/ai4ksl-4000-words-hamnosys-transcription.md) [+M]

## Related Designs

- [Four-module architecture for language-driven robot control in educational simulation](edusim-llm-four-module-architecture.md)
- [Uncertainty-based human-in-the-loop dialogue architecture in which a supervisor intervenes when model uncertainty thresholds are met](uncertainty-threshold-supervisor-intervention-architecture.md)
- [Intelligent practice teaching platform with three core modules](intelligent-practice-teaching-platform-obgyn.md)

## Examples
-

## Key Sources
- Wanzare, L., Okutoyi, J., Kang'ahi, M., & Ayere, M. (2024). Kenyan Sign Language (KSL) Dataset: Using Artificial Intelligence (AI) in Bridging Communication Barrier among the Deaf Learners. https://ai4d.africa/

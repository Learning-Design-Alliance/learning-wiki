---
type: design
id: phoenix-voice-llm-peer-agent-group-learning
title: "Phoenix: a voice-based, non-embodied LLM conversational peer agent for group learning"
description: "Phoenix is a \"voice-based, non-embodied conversational agent that joins real-time group discussions through spoken dialogue with multiple participants\", positioned as an equal peer supporting knowledge co-construction..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: ravi-2026
    resource: "https://arxiv.org/abs/2606.12805"
    title: "Ravi, P., Stevens, C., Hurt, B., Hanks, B., Lin, G., and Anderson, E. (2026). Exploring How Agent Voice Accents Shape Human-AI Collaboration in K-12 Group Learning. https://arxiv.org/abs/2606.12805"
    author: Ravi, P., Stevens, C., Hurt, B., Hanks, B., Lin, G., and Anderson, E
---

# Phoenix: a voice-based, non-embodied LLM conversational peer agent for group learning

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Phoenix is a "voice-based, non-embodied conversational agent that joins real-time group discussions through spoken dialogue with multiple participants", positioned as an equal peer supporting knowledge co-construction rather than an authoritative tutor. Its architecture integrates Google speech-to-text, Microsoft Azure text-to-speech, and OpenAI's GPT-4.1-mini on a Django backend, with a GPT-4.1-mini-based gatekeeping classifier analyzing the eight most recent dialogue turns to decide when Phoenix should respond. Phoenix was implemented with Indian, British, and African American accents while keeping the LLM prompt and tasks constant.

## Design Implications

### Context
#### Requirements
- Runs on a shared laptop at the group table with a web interface displaying spoken output alongside a live transcript
- A gatekeeping classifier that analyzes the eight most recent dialogue turns to determine when the agent should respond
- The LLM generating responses is not informed of the synthesized accent type, to prevent accent-related cultural biases in outputs
#### Constraints
- Designed for one-off, lab-based workshop interactions in this study rather than longitudinal classroom use
- Technical constraints, including latency and limited model transparency, affected interaction flow and trust

### Target Learners
- K-12 teachers in small-group problem-solving tasks

### Learning Goals
- Collaborative problem-solving and consensus building
- Equitable, human-led participation in group discussion

### Claims
- [Accent Shapes Drawn Agent Form Human Vs Technology](../claims/accent-shapes-drawn-agent-form-human-vs-technology.md) [+M]
- [British Accent Agent Framed As Technological Helper](../claims/british-accent-agent-framed-as-technological-helper.md) [+M]
- [Indian Accent Agent Integrated As Trusted Peer](../claims/indian-accent-agent-integrated-as-trusted-peer.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ravi, P., Stevens, C., Hurt, B., Hanks, B., Lin, G., and Anderson, E. (2026). Exploring How Agent Voice Accents Shape Human-AI Collaboration in K-12 Group Learning. https://arxiv.org/abs/2606.12805

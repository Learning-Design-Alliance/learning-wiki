---
type: design
id: dpt-five-agent-simulated-classroom
title: Five-agent DPT simulated classroom on a static-friction problem
description: "A simulated class of five AI students, each embodying a distinct point of failure in the reasoning process: Davide (Hazards A+B), Elena (Hazard C), Tommaso (Hazard D), Chiara (in transition) and Andrea (a near-expert..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: eugenio-tufino-2026
    resource: "https://huggingface.co/spaces"
    title: "Eugenio Tufino. (2026). A multi-agent AI classroom based on dual-process reasoning hazards: a pilot with prospective physics teachers. https://huggingface.co/spaces"
    author: Eugenio Tufino
---

# Five-agent DPT simulated classroom on a static-friction problem

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A simulated class of five AI students, each embodying a distinct point of failure in the reasoning process: Davide (Hazards A+B), Elena (Hazard C), Tommaso (Hazard D), Chiara (in transition) and Andrea (a near-expert peer). It runs on an LLM via a Gradio application on Hugging Face Spaces, with personas defined entirely in the system prompt, session reset and one-click export of the anonymised conversation log. Named agents respond, with roughly 30% probability a second agent intervenes, and an open question draws two to four responses.

## Design Implications

### Context
#### Requirements
- Requires a valid API key from a supported LLM provider, supplied by the user; no specialised infrastructure or model training is needed.
#### Constraints
- The hazards are reified into stable characters — a deliberate pedagogical simplification the framework itself warns against.
- Participants noted the environment's limits as a proxy for real classrooms: "real students do not ask all those questions".

### Target Learners
- prospective physics teachers in MSc programs

### Learning Goals
- responding in real time to student reasoning with differentiated questioning strategies

### Claims

## Related Designs

- [Practice-based clinical mastery through progressively challenging simulated encounters](residencyrl-practice-based-clinical-mastery.md)
- [Dual-process reasoning hazards framework with hazard-matched questioning strategies](dpt-hazards-framework-and-matched-questioning.md)

## Examples
-

## Key Sources
- Eugenio Tufino. (2026). A multi-agent AI classroom based on dual-process reasoning hazards: a pilot with prospective physics teachers. https://huggingface.co/spaces

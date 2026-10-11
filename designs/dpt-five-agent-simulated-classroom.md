---
type: design
id: dpt-five-agent-simulated-classroom
title: Five-agent DPT simulated classroom on a static-friction problem
description: "A simulated class of five AI students, each embodying a distinct point of failure in the reasoning process: Davide (Hazards A+B), Elena (Hazard C), Tommaso (Hazard D), Chiara (in transition) and Andrea (a near-expert..."
status: draft
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
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 2 claims rest on one study

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
- [Knowing Doing Gap In Live Questioning](../claims/knowing-doing-gap-in-live-questioning.md) [+M]
- [Residual Doubt Marker Signals Convergence](../claims/residual-doubt-marker-signals-convergence.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Eugenio Tufino. (2026). A multi-agent AI classroom based on dual-process reasoning hazards: a pilot with prospective physics teachers. https://huggingface.co/spaces

---
type: strategy
id: tiered-routing-hesitation-and-complexity-triggers
title: Use latency-hesitation triggers and heuristic complexity filtering to route difficult queries to a higher-reasoning tier
description: The article proposes two practical principles for autonomous tiered routing of LLM queries in medical education.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
sources:
  - id: kirchberger-michael-constantin-md-mavragani-amaryllis-2026
    resource: "https://doi.org/10.2196/86999"
    title: "Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999"
    author: Kirchberger Michael Constantin MD; Mavragani Amaryllis
---

# Use latency-hesitation triggers and heuristic complexity filtering to route difficult queries to a higher-reasoning tier

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 1 study (1 design), `q3` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article proposes two practical principles for autonomous tiered routing of LLM queries in medical education. First, systems can use internal model metrics as escalation triggers: "systems can leverage internal model metrics, such as confidence scores or real-time processing latency," with GPT-5 Instant's significant hesitation on incorrect answers (P=.002) cited as evidence that algorithmic hesitation is a viable real-time trigger for T2 escalation. Second, routing mechanisms can analyze structural prompt characteristics such as word count or the presence of multistep clinical vignettes to bypass T1 for highly complex queries. This operationalizes the validated 2-tiered rescue framework for clinical practice.

## Design Implications

### Context
#### Requirements
- A deployed T1 model whose latency or confidence metrics can be monitored in real time, plus a more computationally intensive T2 reasoning model available for escalation
#### Constraints
- The hesitation trigger was demonstrated only for GPT-5 Instant; Gemini 2.5 Flash showed no latency difference between correct and incorrect answers (P=.81)
- The routing principles are proposed on the basis of the study's findings and have not themselves been tested in deployment

### Target Learners
- medical students preparing for the German M2 examination
- developers of AI tools for medical education and clinical practice

### Target Learning Goals
- safe and reliable use of LLMs for answering challenging medical examination questions

## Claims

- [The relationship between question difficulty and response latency is absent for Gemini Flash and weakly positive for GPT-5 Instant](../claims/difficulty-latency-correlation-model-specific.md) [~M]
- [GPT-5 Instant takes significantly longer on items it answers incorrectly while Gemini 2.5 Flash shows no such hesitation](../claims/gpt5-instant-hesitation-on-incorrect-answers.md) [+M]
- [The 2-tiered rescue protocol corrects roughly one-third to one-half of T1 errors, raising final accuracy to 94.3% (Gemini) and 95.6% (GPT-5) with no significant system difference](../claims/two-tier-rescue-raises-final-accuracy.md) [+M]

## Related Strategies
- 

## Examples
-

## Key Sources
- Kirchberger Michael Constantin MD; Mavragani Amaryllis. (2026). A 2-Tiered Rescue Protocol to Mitigate Difficulty-Based Failures of ChatGPT (GPT-5) and Gemini on the German M2 Medical Examination: Evaluation Study. JMIR Formative Research. https://doi.org/10.2196/86999

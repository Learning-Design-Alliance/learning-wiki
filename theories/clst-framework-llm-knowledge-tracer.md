---
type: theory
title: "CLST: framing knowledge tracing as language processing so a generative LLM can serve as a student's knowledge tracer"
description: CLST is a framework that aligns a generative LLM to knowledge tracing by converting problem-solving histories into natural-language prompt sequences, a process the authors call knowledge tracing as language processing...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: heeseok-jung-2025
    resource: "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    title: "Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    author: Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang
---

# CLST: framing knowledge tracing as language processing so a generative LLM can serve as a student's knowledge tracer

> **Theory** · [All theories](index.md)
> **Evidence** · no claims cited

## Description
CLST is a framework that aligns a generative LLM to knowledge tracing by converting problem-solving histories into natural-language prompt sequences, a process the authors call knowledge tracing as language processing (KTLP) formatting. Each exercise is rendered as a textual description (e.g., KC name), interactions are tuples connected by the '→' symbol, and the binary label becomes a yes/no answer word; prediction is read from a bi-dimensional softmax over the logits of the two answer words. The model is adapted with LoRA low-rank fine-tuning so that "the original parameters can be preserved in a frozen state while additional information in the fine-tuning dataset is efficiently incorporated by training smaller matrices." The framework targets system cold-start scenarios where new institutions lack interaction data.

## Design Implications

### Context
#### Requirements
- A KTLP-formatted dataset expressing exercise descriptions and response correctness in natural language
- An accessible instruction-tuned generative LLM whose weights can be fine-tuned (the article selected Mistral-7B partly for weight access and data-security concerns about third-party APIs)
- LoRA low-rank adaptation to avoid resource-intensive full-parameter fine-tuning
#### Constraints
- The article notes fine-tuning with a small amount of data may narrow the range of output values, affecting calibration plots
- Experiments were limited to the first 50 interactions per student and training sets of 8-64 students in cold-start tests

### Target Learners
- K-12 students in mathematics, social studies, and science on online learning platforms

### Target Learning Objectives
- Estimating students' current knowledge states and mastery of knowledge components to support personalized learning and content recommendation in intelligent tutoring systems

### Claims


## Related Theories
- 

## Examples
-

## Key Sources
- Heeseok Jung, Yohaan Yoon, Jaesang Yoo, Yeonju Jang. (2025). CLST: Cold-Start Mitigation in Knowledge Tracing by Aligning a Generative Language Model as a Students' Knowledge Tracer. Journal of Educational Data Mining, Volume 17, No 2. https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

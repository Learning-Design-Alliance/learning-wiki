---
type: strategy
id: improve-llm-reasoning-under-uncertainty-ai-tutors
title: "Improve LLMs' scientific and mathematical reasoning under uncertainty to enable AI tutors for science and maths learning"
description: "The authors propose that the benchmark's findings motivate targeted improvement of LLMs on scientific and mathematical reasoning in contexts of uncertainty, where answers must be given from incomplete, progressively r..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: george-boateng-2026
    resource: "https://arxiv.org/abs/2605.07051"
    title: "George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051"
    author: George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol
---

# Improve LLMs' scientific and mathematical reasoning under uncertainty to enable AI tutors for science and maths learning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The authors propose that the benchmark's findings motivate targeted improvement of LLMs on scientific and mathematical reasoning in contexts of uncertainty, where answers must be given from incomplete, progressively revealed clues. They state that "these findings point to the need for efforts to improve LLMs on this type of scientific and mathematical reasoning in the context of uncertainty" and that such capabilities "could enable the use of LLMs to power AI tutors to better support students' science and maths learning". The strategy is grounded in the real-time proxy evaluation showing performance drops when clues are incomplete.

## Design Implications

### Context
#### Requirements
- LLMs capable of deciding when to answer from partial clue information, as operationalized in the real-time proxy prompt requiring an answer plus a confidence of sure or not sure
#### Constraints
- The article notes real-world deployment performance would be affected by audio chunk length, transcription errors, and latency

### Target Learners
- senior secondary school students in science and mathematics

### Target Learning Goals
- science and maths learning supported by AI tutors

## Claims

- [LLM performance drops from offline to real-time proxy evaluation when clues arrive incrementally](../claims/performance-drops-realtime-proxy-nsmq.md) [+W]
- [Answering early on few clues correlates with worse real-time proxy performance](../claims/early-answering-correlates-worse-realtime-performance.md) [+W]
- [LLMs struggle most with Chemistry riddles, with best EM accuracy at or below 75% versus above 90% in other subjects](../claims/llms-struggle-most-chemistry-nsmq-riddles.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- George Boateng, Naafi Dasana Ibrahim, Samuel John, Philemon Badu, Patrick Agyeman-Budu, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor, Andrew Kojo Mensah-Onumah, Nana Sam Yeboah, and Victor Kumbol. (2026). NSMQ Riddles: A Benchmark of Scientific and Mathematical Riddles for Quizzing Large Language Models. arXiv preprint. https://arxiv.org/abs/2605.07051

---
type: claim
title: The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text
description: The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator...
id: ai-feedback-response-time-and-authoring-efficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: chloe-qianhui-zhao-2026
    resource: "https://doi.org/10.48550/arxiv.2601.15280"
    title: "Chloe Qianhui Zhao, Jie Cao, Jionghao Lin, and Kenneth R. Koedinger. (2026). LLM-based Multimodal Feedback Produces Equivalent Learning and Better Student Perceptions than Educator Feedback. LAK 2026. https://arxiv.org/abs/2601.15280 [doi:10.48550/arxiv.2601.15280](https://doi.org/10.48550/arxiv.2601.15280)"
    author: Chloe Qianhui Zhao, Jie Cao, Jionghao Lin, and Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: chloe-qianhui-zhao-2026-2
    resource: "https://arxiv.org/abs/2601.15280"
    title: "Chloe Qianhui Zhao, Jie Cao, Jionghao Lin, and Kenneth R. Koedinger. (2026). LLM-based Multimodal Feedback Produces Equivalent Learning and Better Student Perceptions than Educator Feedback. LAK 2026. https://arxiv.org/abs/2601.15280"
    author: Chloe Qianhui Zhao, Jie Cao, Jionghao Lin, and Kenneth R. Koedinger
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q1`–`q2`

## Subclaims
`q2 i?` Median system response time was 0.299 seconds for MCQs and 6.23 seconds for open-ended questions. [→ Chloe Qianhui Zhao 2026](#chloe-qianhui-zhao-2026)
`q1 i?` By word-count proxy, the system is approximately 2.77 times more time-efficient than authoring equivalent human text feedback. [→ Chloe Qianhui Zhao 2026 (2)](#chloe-qianhui-zhao-2026-2)

## Evidence

### Chloe Qianhui Zhao 2026

Chloe Qianhui Zhao, Jie Cao, Jionghao Lin, and Kenneth R. Koedinger. (2026). LLM-based Multimodal Feedback Produces Equivalent Learning and Better Student Perceptions than Educator Feedback. LAK 2026. https://arxiv.org/abs/2601.15280 [doi:10.48550/arxiv.2601.15280](https://doi.org/10.48550/arxiv.2601.15280)

`q2 · i?` · `causal · r2`

System response-time calculation in RQ1.2, covering total time to return structured text feedback and the slide reference for each question type. Descriptive statistics only; no comparison test.

> "For multiple choice questions, the median of system response time is 0.299 seconds (𝑀𝑒𝑎𝑛= 0.700,𝑆𝐷= 1.457); for open-ended questions, the median of system response time is 6.23 seconds (𝑀𝑒𝑎𝑛=7.210,𝑆𝐷=3.389)."

### Chloe Qianhui Zhao 2026 (2)

Chloe Qianhui Zhao, Jie Cao, Jionghao Lin, and Kenneth R. Koedinger. (2026). LLM-based Multimodal Feedback Produces Equivalent Learning and Better Student Perceptions than Educator Feedback. LAK 2026. https://arxiv.org/abs/2601.15280

`q1 · i?` · `causal · r2`

A proxy comparison of word counts: the prompt template contained 356 words versus 985 words of human-authored feedback across 8 MCQs (26 options) and 5 OEQs. The authors state educator time writing the feedback was not recorded, so this is an assumption-based estimate.

> "Assuming com- parable effort per word for preparing a set of reusable feedback, the system is approximately985/356≈ 2.77× more time-efficient than authoring equivalent human text feedback."

## Discussion


## Related Claims
- [Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant](hdr-human-scoring-time-burden.md) — related
- [On the live single-node deployment, short-answer rounds take ≈32 s (≈$0.015/round) while multiple-choice rounds are ≈4× faster (≈7.6 s, ≈$0.005/round) because grading is deterministic](collearn-latency-cost-efficiency.md) — related
- [Feedback type shifts engagement by question type: educator feedback yields more MCQ submissions while AI feedback trends toward more open-ended revisions, with no overall difference](feedback-type-shifts-engagement-by-question-type.md) — related
- [Prebuilt quiz banks of 435 questions across 65 modules decouple practice from live generation, with warm practice-request medians of 4.8 and 5.8 ms](prebuilt-quiz-banks-decouple-practice.md) — related
- [LLM-generated retrieval practice was practical to deploy and well received, but high correctness rates (about 70% of items at p=1.0) restricted score variance](llm-generated-retrieval-practice-deployable-but-high-accuracy-limits-variance.md) — related
- [Under a simulated load of 100 concurrent users, Taklif.AI averaged 30 seconds end-to-end response time per request](load-test-100-concurrent-users-30-second-response.md) — related
- [LearnLens reduces teacher feedback time, with half of teachers previously spending 10–30 minutes per assignment versus a median below 5 minutes with the system](learnlens-reduces-teacher-feedback-time.md) — related

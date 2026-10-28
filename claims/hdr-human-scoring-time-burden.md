---
type: claim
title: Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant
description: Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant
id: hdr-human-scoring-time-burden
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: satoshi-takahashi-2026
    resource: "https://doi.org/10.48550/arxiv.2609.25790"
    title: "Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790 [doi:10.48550/arxiv.2609.25790](https://doi.org/10.48550/arxiv.2609.25790)"
    author: Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Human scoring and feedback for HDR takes approximately 11 minutes and 30 seconds per learner; for 100 learners it would take approximately 17 hours and 8 minutes, whereas GPT-based scoring and feedback can be completed almost instantly. [→ Satoshi Takahashi 2026](#satoshi-takahashi-2026)

## Evidence

### Satoshi Takahashi 2026

Satoshi Takahashi, Atsushi Yoshikawa, Megumi Kose, Kenichi Suzuki, Chieko Inoue, Yumi Watanabe, and Mari Sawada. (2026). Automating Constructive Assessment with Large Language Models: Toward Scalable and Repeated Evaluation of Practical Competence. arXiv. https://arxiv.org/abs/2609.25790 [doi:10.48550/arxiv.2609.25790](https://doi.org/10.48550/arxiv.2609.25790)

`q3 · i?` · `design · r2`

Time analysis (Table 8): five graders spent 138 minutes scoring 117 responses plus 30 minutes consensus; feedback preparation, creation, and re-check took 860 minutes for 117 questions, versus a few seconds for LLM generation.

> "when humans provide scoring and feedback for HDR, it takes approximately 11 minutes and 30 seconds per learner. If 100 learners were assessed, it would take approximately 17 hours and 8 minutes."

## Discussion


## Related Claims
- [Automated HDR problem generation makes repeated and longitudinal assessment feasible by producing structurally equivalent cases with different contexts](automated-generation-enables-longitudinal-hdr-assessment.md) — related
- [Automated marking reduced assessment turnaround from 11.2 days to 0.1 days and enabled intervention students to complete 4.1 times the practice volume of controls](automated-marking-turnaround-and-practice-volume.md) — related
- In a real academic pilot, AISSA processed 90 presentations reliably at 1–3 minutes per submission and an estimated cost of $0.06–0.07 USD per evaluation — related
- [A page-by-page, rubric-guided multimodal LLM workflow graded an authentic handwritten exam in about three hours at roughly $100 in token costs, versus about $3,500 in TA time](ai-grading-workflow-feasibility-cost.md) — related
- [The AI feedback system returns responses in under a second for MCQs and about six seconds for open-ended questions, and its reusable prompt is roughly 2.77 times more time-efficient to prepare than equivalent educator text](ai-feedback-response-time-and-authoring-efficiency.md) — related
- [GPT-4 generated detailed per-response feedback that was useful for identifying scoring errors and could support personalized student feedback](gpt4-feedback-useful-for-error-identification.md) — related
- [LearnLens reduces teacher feedback time, with half of teachers previously spending 10–30 minutes per assignment versus a median below 5 minutes with the system](learnlens-reduces-teacher-feedback-time.md) — a narrower finding that bears on this claim
- [GPT-generated feedback passes simulated-student helpfulness evaluations only about 35% of the time on real student data](gpt-feedback-passes-automated-helpfulness-35-percent.md) — related
- [LLMs can deliver scalable, personalized, interactive feedback almost instantly, reducing dependency on teacher availability and supporting self-regulated learning in large courses](llms-scalable-personalized-feedback-large-courses.md) — a broader claim this one bears on
- [Simulated Human-in-the-Loop workflow reduces required full human scoring of written productions by at least 50%](hitl-workflow-reduces-human-scoring-workload-50-percent.md) — related
- [Under a simulated load of 100 concurrent users, Taklif.AI averaged 30 seconds end-to-end response time per request](load-test-100-concurrent-users-30-second-response.md) — related
- [Early adopters report time savings from ChatGPT automation, including a Wharton professor's exam-writing productivity increase of 100%](chatgpt-automation-time-savings-educators.md) — related
- [LLM-based extraction of three variables from 156 meta-analyses cost about $50 in computing fees, far less than estimated human-assistant labor costs](llm-extraction-cost-time-savings.md) — related
- [The short form saves about eleven hours of giving and scoring time per class of thirty pupils compared with the long scales](survey-test-saves-eleven-hours-per-class.md) — related
- [Machine-learning-supported grading with complete manual review of all classifier output reduced total exam grading time by 74% (or 64% under a conservative estimate) compared with fully manual grading](ml-supported-grading-cuts-exam-workload-64-74-percent.md) — related
- [Six expert teachers completed grading tasks in ASYST with 100% effectiveness, median 2:15 minutes, and an average SUS score of 88.8](asyst-usability-study-high-sus.md) — related
- [AI feedback after sessions can provide on average eight qualified comments aligned with expert feedback per 30-min lesson](ai-feedback-eight-comments-per-lesson.md) — related

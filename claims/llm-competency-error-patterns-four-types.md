---
type: claim
title: "Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response"
description: "Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response"
id: llm-competency-error-patterns-four-types
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: zhen-xu-2026
    resource: "https://doi.org//10.18608/jla.2026.9127"
    title: "Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127"
    author: Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: zhen-xu-2026-2
    resource: "https://doi.org//10.18608/jla.2026.9127"
    title: "Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127"
    author: Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Zhen Xu 2026 (2): no comparison group (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` Over-interpretation occurred across all models and document types, e.g., defaulting to the assumption that exams are writing-based. [→ Zhen Xu 2026](#zhen-xu-2026)
`q2 i?` Failure to detect relevant information is common in lengthy learning activity content, and hallucination is more common in concise descriptions and instructional schedules. [→ Zhen Xu 2026 (2)](#zhen-xu-2026-2)

## Evidence

### Zhen Xu 2026

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Manual error analysis of cases where LLM predictions diverged from human annotations; the article identifies over-interpretation as occurring "across all models and all curriculum document types we evaluated".

> "In contrast, LLMs tend to default to the assumption that exams are writing based, leading them to confidently infer writing competencies, which reflects biased reasoning."

### Zhen Xu 2026 (2)

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Manual error analysis found missed nuanced evidence mainly in long learning activity documents, while hallucination was "more common in concise course descriptions and instructional schedule data"; failure to respond occurred predominantly in smaller models such as Llama3-8B.

> "This error pattern is common in lengthy curriculum document types such as learning activity content, where dense information makes it difficult for LLMs to capture and interpret key details accurately."

## Discussion


## Related Claims

- [Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage](llm-accuracy-regression-overestimation-bias.md) — related
- LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — a narrower finding that bears on this claim
- [Generative AI generates responses based on probability and pattern prediction, not reasoning or understanding](genai-probabilistic-prediction-not-reasoning.md) — related
- [Phase VI AI-enabled systems face six documented challenges: explainability, hallucination risk, prompt sensitivity, computational cost, validation complexity, and limited large-scale evidence](phase-vi-ai-systems-six-challenges.md) — related
- [The most reported risks of AI tools in science and chemistry education are ethical issues, including gender and racial bias, hallucinations, copyright infringement, and plagiarism](ethical-issues-most-reported-ai-risk.md) — related
- ML-based scoring approaches more often overestimated expert-assigned scores, whereas LLM-based approaches more often underestimated them — related
- [An LLM debugging assistant correctly interprets brief, informal natural-language prompts describing circuits](llm-handles-natural-language-circuit-prompts.md) — related
- [Recurring risks of GenAI in STEAM education include hallucination, bias, superficial completion strategies, and compromised assessment validity](genai-steam-risks-hallucination-bias.md) — related
- [Three recurring AI failure modes arose in this project-based learning context: plausible-but-incorrect code, missing specialized knowledge, and limited long-term context](three-ai-failure-modes-project-based-learning.md) — related
- [Gen-AI hallucinates sources and values and produces convincing but incorrect explanations, risking student misinformation](genai-hallucination-convincing-incorrect-explanations.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [Current LLMs misalign instructional-strategy sensitivity with pedagogical relevance, including hallucinated relevance of irrelevant traits](llm-relevance-impact-misalignment-learner-characteristics.md) — a narrower finding that bears on this claim
- [Dominant logical fallacies in LLM mathematical explanations shift from family to family and across prompting modes](llm-math-explanation-fallacies-vary-by-family.md) — related
- [Vision-assisted extraction identified chart type in all sampled images but showed ±5–10% numeric estimation error and two failure modes correctable via mandatory review](llm-chart-extraction-accuracy-failure-modes.md) — related
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [GenAI novices develop prompting strategies through trial and error, starting from zero-shot prompts and refining them after unsatisfactory outputs](novices-refine-prompts-trial-and-error.md) — related
- [Leading LLMs hallucinated legal authorities in 58%-88% of tested cases while failing to recognise incorrect legal assumptions in prompts](llms-hallucinate-legal-authorities-58-88.md)
- [Human experts and LLMs show qualitatively different error patterns in outcome prediction](expert-llm-error-patterns-differ.md) — related
- [Switching from reference-based to contextual evaluation prompts improved GenAI grading accuracy](contextual-evaluation-prompt-improvement.md) — related
- [Manual error analysis finds incomplete retrieval is the most frequent failure category, ahead of code-semantics limits, bilingual retrieval gaps, and over-conservative refusals](eduguard-failure-analysis-incomplete-retrieval.md) — related
- [Retrieval-augmented generation reduces but does not eliminate hallucinations in AI-assisted verification](rag-reduces-not-eliminates-hallucinations.md) — related
- [LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs](llm-hallucination-rate-education.md) — related

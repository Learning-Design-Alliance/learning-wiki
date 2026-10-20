---
type: claim
title: Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance
description: Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance
id: curricular-cot-improves-accuracy-larger-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
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

# Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Curricular CoT improves prediction accuracy over the zero-shot baseline across all granularity levels, more apparently in GPT-4o and Llama3-70B. [→ Zhen Xu 2026](#zhen-xu-2026)
`q2 i?` The definition-based (DEF) strategy does not improve performance and can even reduce accuracy. [→ Zhen Xu 2026 (2)](#zhen-xu-2026-2)

## Evidence

### Zhen Xu 2026

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Experiment comparing five prompting strategies (DEF, CQA, CQ, QA, A) against the zero-shot baseline across four models and four granularity levels; the article describes the gains as modest but consistent, particularly in binary tasks.

> "Overall, we find that curricular CoT improves prediction accuracy over the zero-shot baseline across all levels of task granularity. However, these improvements are more apparent in larger and more advanced models, such as GPT-4o and Llama3-70B."

### Zhen Xu 2026 (2)

Zhen Xu, Xin Guan, Chenxi Shi, Qinhao Chen, Renzhe Yu. (2026). Evaluating 21st-Century Competencies in Postsecondary Curricula with Large Language Models: Performance Benchmarking and Reasoning-Based Prompting Strategies. Journal of Learning Analytics 13(1), 7–30. https://doi.org//10.18608/jla.2026.9127

`q2 · i?` · `causal · r2`

Same prompting-strategy comparison: providing competency definitions from human annotator notes failed to help and in some cells lowered accuracy relative to the zero-shot baseline.

> "In contrast, the definition-based (DEF) strategy, which provides the model with human-annotated notes for each competency, does not improve performance and can even reduce accuracy."

## Discussion


## Related Claims
- [Curriculum document type and competency framework significantly predict LLM prediction accuracy, and zero-shot LLMs systematically overestimate competency coverage](llm-accuracy-regression-overestimation-bias.md) — related
- [Zero-shot LLMs perform only marginally above random in five-class competency classification but exceed 70% accuracy on binary classification](zero-shot-llm-granularity-competency-classification.md) — related
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related
- Prompt type interacts with coding dimension in error rates: definitions and instructions can impair detection of listing — related
- Zero-shot prompt type has minimal impact on LLM-human coding concordance — related
- Agentic frameworks built on GPT-3.5 and GPT-4 show significant performance gains on the HumanEval benchmark over zero-shot baselines — related
- Chain-of-thought prompting improved LLM multistep reasoning, operationalized via decomposition and interleaved planning approaches — related
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — related
- [Reasoning-capable model variants and chain-of-thought prompting yield no measurable improvement in either alignment axis for classroom evaluation](reasoning-variants-no-alignment-improvement.md) — reports the opposite
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [High self-consistency between a simulator's reasoning and its own generated code does not imply alignment with real student reasoning or behavior](self-consistency-does-not-imply-student-alignment.md) — related
- [A construction-focused correctness rubric underperformed behavior-focused and undefined prompts for LLM scoring of code explanations](construction-rubric-underperformed-llm-scoring.md) — related
- [Enforcing an explicit multi-step reasoning structure yields no significant improvement for the two studied models, which already self-organize an effective reasoning structure](enforced-structure-no-gain-self-organized-reasoning.md) — reports the opposite
- [In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner](icl-does-not-unlock-beyond-k5-reasoning.md) — related
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Chain-of-Thought rationale quality shows no direct correlation with the accuracy of simulated student responses](cot-rationale-quality-no-correlation-simulated-accuracy.md) — related
- [Self-refinement gains depend on model strength and on behavior-prediction quality](self-refinement-gains-depend-on-model-and-prediction-quality.md) — a broader claim this one bears on
- [The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)](varia-ablation-null-effects.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — related
- [Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution](few-shot-prompting-no-f1-gain-reduces-overattribution.md) — related
- [The framework generalizes under automatically generated Q-matrices without requiring expert annotation](automatic-qmatrix-extraction-generalization.md) — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related

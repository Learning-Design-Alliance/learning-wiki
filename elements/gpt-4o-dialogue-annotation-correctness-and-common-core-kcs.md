---
type: element
id: gpt-4o-dialogue-annotation-correctness-and-common-core-kcs
title: GPT-4o Automated Dialogue Annotation with Recursive Common Core Tagging
description: The article annotates each student turn with correctness and KC labels using GPT-4o via simple, zero-shot chain-of-thought prompting, instructing it to summarize turns before labeling.
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
---

# GPT-4o Automated Dialogue Annotation with Recursive Common Core Tagging

> **Element** · [All elements](index.md)
> **Evidence** · 11 claims (6 for, 4 mixed, 1 against) · 7 studies (6 design, 1 causal), `q2` · 0 of 7 report an effect size · 11 claims rest on one study

## Description
The article annotates each student turn with correctness and KC labels using GPT-4o via simple, zero-shot chain-of-thought prompting, instructing it to summarize turns before labeling. "For KC annotation, we adapt the recursive tagging algorithm from [34], which tags math word problems with Common Core math standards": the model selects domains, then clusters, then turn-level standards from the Achieve the Core coherence map. The two tasks are run separately because "doing so leads to improved accuracy compared to combining them".

## Design Implications

### Context
#### Requirements
- The full dialogue as input, and the hierarchically organized Common Core standards (domains, clusters, standards) from the Achieve the Core coherence map.
- Separate prompts for correctness annotation and KC annotation.
#### Constraints
- Annotating a full dialogue with a single prompt makes real-time KT impossible; annotating one turn at a time is costly and is left for future work.
- Several dialogues are not covered by Common Core standards, so it may be necessary to augment the standards with other sources or defer to humans for labeling.

### Target Learners
- Students in one-on-one math tutoring dialogues with human or LLM-powered tutors (the article uses the CoMTA and MathDial datasets)

### Target Learning Goals
- Labeling student response correctness and the math knowledge components involved in each tutoring dialogue turn

### Affordances
- [Dialogue Knowledge Tracing Framework](../theories/dialogue-knowledge-tracing-framework.md)

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](../claims/gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) [+M]
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](../claims/expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) [+M]
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](../claims/gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) [+W]
- [Prompting with category information or few-shot examples yields limited improvement in distribution alignment, with zero-shot closest for most models](../claims/prompting-strategies-limited-alignment-gain.md) [+W]
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](../claims/cot-effect-varies-model-stage-kc-planning.md) [~W]
- [CLARA annotations align with blinded educator judgments, with 0.81 pairwise agreement and highest-rated educational interpretability](../claims/clara-educator-agreement-interpretability.md) [~W]
- [Given sufficient prompt context, GPT-4 describes student errors in a College Algebra ITS with 87.8% accuracy](../claims/gpt4-diagnoses-its-errors-87-8-accuracy.md) [+W]
- [The framework is robust to 15% ASR transcription noise and retains 99.6% of its ICS under zero-shot cross-domain transfer to EdNet-Math](../claims/framework-robust-asr-noise-cross-domain-transfer.md) [~W]
- [GPT-4o shows more consistent performance than Llama 3 70B across topics and metrics, while Llama 3 70B falls below 60% on the unit metric for three advanced topics](../claims/gpt4o-consistency-vs-llama3-unit-weakness.md) [+W]
- [Llama 3 70B outperforms GPT-4o on completeness and method metrics due to its leniency, but performs significantly worse on the unit metric](../claims/llama3-lenient-gpt4o-rigor-tradeoff.md) [~W]
- [GPT-4o frequently makes characteristic errors in homework assessment, including failing to recognize unit and numeric equivalences, marking complete solutions incomplete, and mishandling alternative methods and notations](../claims/gpt4o-characteristic-assessment-error-types.md) [-W]

## The evidence by question
- *Can a large language model label whether students' responses are correct, and which skills they show, accurately enough to stand in for human annotators?* [GPT-4o's final-turn correctness labeling on CoMTA is only slightly less accurate than expert human annotators, which the authors read as close to human-level performance on a challenging task.](../claims/gpt-4o-final-turn-correctness-labeling-is-close-to-human-level.md) [+M]

## Related Elements
- [Annotating](../principles/annotating.md)

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490

---
type: claim
title: Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none
description: Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none
id: human-llm-agreement-low-construct-varying
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ober-2026
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ober-2026-2
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ober-2026-3
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Human-LLM alignment remained low across all constructs and configurations, with κ ranging from 0.000 to 0.419. [→ Ober 2026](#ober-2026)
`q2 i?` Every human-LLM comparison for Prior KSAs yielded κ = 0 despite percent agreement of 52.22% to 83.96%, reflecting different evidence standards for prior knowledge. [→ Ober 2026 (2)](#ober-2026-2)
`q2 i?` Self-efficacy demonstrated the best human-LLM alignment (κ = 0.138 to 0.418), and non-mini models consistently outperformed mini models in human alignment for self-efficacy. [→ Ober 2026 (3)](#ober-2026-3)

## Evidence

### Ober 2026

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Human-LLM agreement analysis comparing LLM outputs against codes from two trained human coders with over five years of assessment development experience. The article reports human-LLM alignment "remained low (κ ranging from 0.000 to 0.419)."

> "In contrast, while LLMs achieved high inter-model agreement for certain configurations, human-LLM alignment remained low (κ ranging from 0.000 to 0.419)"

### Ober 2026 (2)

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Human-LLM comparisons for Prior KSAs across all configurations. LLMs coded explicit knowledge statements such as answers to questions, while human coders relied on subtle indicators like domain-specific vocabulary or references to past experiences, which were largely absent in the dataset.

> "The most striking finding was the lack of alignment in identifying Prior KSA s, where every human -LLM comparison yielded κ = 0 despite agreement ranging from 52.22% to 83.96%"

### Ober 2026 (3)

Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck

`q2 · i?` · `design · r2`

Human-LLM agreement for self-efficacy across configurations. Non-mini models outperformed mini models: human2 vs. ChatGPT4o/temperature=0 achieved κ = 0.418, while human2 vs. ChatGPT4o-mini/temperature=0 reached only κ = 0.192. Even the best alignment was poor to fair by conventional standards.

> "Self-efficacy demonstrated the best human-LLM alignment among all constructs, with κ values ranging from 0.138 to 0.418. However, this “best” performance still represents poor to fair agreement by conventional standards"

## Discussion


## Related Claims

- Constructs with higher operational clarity show higher overall coder agreement, and low clarity harms human coder agreement more than LLM agreement — related
- [Human-human agreement (average κ = 0.644) was lower than the best LLM-LLM agreement (average κ = 0.856) across constructs](human-human-agreement-lower-than-llm-llm.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — reports the opposite
- LLM-based transcript classifications agreed highly with human judgment for explicit questions (κ = .778) and math talk (κ = .722), but only moderately for need for help (κ = .562) and confusion (κ = .531) — reports the opposite
- [LLM configurations show high within-configuration reliability when re-coding the same chat log dataset, with ChatGPT4o/temperature=0 highest](llm-within-configuration-reliability-high.md) — related
- Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts — related
- LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — reports the opposite
- LLMs align better with human coding on concise theories with discrete concepts than on more complex ones — related
- Multi-agent essay scoring system (MASS) reportedly achieves increased consistency and reliability compared to stand-alone LLMs — related
- [Human-LLM agreement is moderated by code properties, multi-model consensus, and model-reported confidence](agreement-moderators-tiers-consensus-confidence.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy](anvil-llm-judge-analogy-screening.md) — related
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](hint-prompts-raise-llm-scoring-agreement.md) — related
- [LLM-human factor-structure similarity is consistently lower than human-human similarity on both assessments](llm-human-factor-congruence-lower-than-human-human.md) — related
- [Some LLMs exhibit a selection bias against selecting option D on multiple-choice pedagogy questions](llm-selection-bias-against-option-d.md) — related
- [Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items](ca-selective-best-average-agreement-drawings.md) — related
- [CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines](clara-highest-human-ranking-agreement.md) — related
- [Anchored judge prompts restore score discrimination and raise the reward's agreement with independent human ratings (Spearman ρ 0.672→0.741)](judge-anchoring-raises-human-agreement.md) — related
- [LLM and human written 7C analyses show no overall difference in behavioral alignment or evidence correspondence, but align less on Communication and Constructive dimensions](llm-7c-analytical-alignment-mixed.md) — related
- [Adding a cross-model agreement filter improves performance for the top three LLM annotators](cross-model-agreement-filter-improves-top-annotators.md) — related
- [LLM-judge evaluation of tutoring sycophancy shows systematic self-judge blind spots and missed sycophancy even under judge consensus](llm-judge-reliability-tutoring-sycophancy.md) — related
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — related
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — reports the opposite
- [LLM alignment with expert teaching ratings does not predict, and is often negatively associated with, alignment with student learning gains](proxy-alignment-not-impact-alignment-llm-classroom.md) — related
- [A multimodal LLM achieves moderate-to-substantial agreement with human consensus on well-defined CT practices but lower agreement on multi-component constructs like Physics Correctness and Systems Thinking](llm-human-agreement-ct-practices.md) — related
- [Hierarchical Acceptance Rate aligns with expert acceptance decisions better than single-dimension and holistic LLM judges](har-outperforms-llm-judge-acceptance-alignment.md) — related
- LLM-generated replies were consistently not similar to human replies, though including chat history slightly improved alignment — related
- [Rank-based metrics can be misleading for analytic assessment: systems prompted for holistic scoring achieve strong, sometimes stronger, correlations with analytic scores than when prompted for those aspects](rank-based-metrics-misleading-analytic-assessment.md) — related
- [LLM graders show model-specific precision/recall trade-offs, so a single metric is insufficient to judge grading quality](llm-grader-precision-recall-tradeoffs-single-metric-insufficient.md) — related
- [Students engaged deeply with LLM feedback, with coded evidence of reflection, rebuttal, and acceptance in the large majority of responses](deep-engagement-llm-feedback-reflection-rebuttal-acceptance.md) — related
- [Even the best LLM grader reaches only moderate agreement with human teachers, below the threshold for good reliability](llm-grading-moderate-human-agreement-icc.md) — related
- [The LLM judge agrees with human annotators at 87.7% (κ = 0.842) on consensus pairs, but severity-rating agreement is uneven and medium-tier boundaries are uncertain](judge-calibration-labels-strong-severity-uneven.md)
- [GPT models achieved high polarity agreement with instructors only for positive feedback on the Topic aspect, and could not reliably assess the other rubric aspects](gpt-polarity-agreement-low-except-topic.md) — related
- [Peer marks and grades show acceptably high reliability with teachers' marks in most comparison studies, but a substantial minority report low reliability](peer-assessment-adequate-reliability-most-studies.md) — related
- [Pedagogical agents significantly improve learners' self-efficacy expectations (g = 0.29), with effects moderated by grade level, facial expressions, and reliability reporting](pa-improve-self-efficacy-expectations.md) — related
- [Validator agent reliability is highest for realism and lowest for authenticity in human evaluation](validator-reliability-highest-realism-lowest-authenticity.md) — related
- [Systematic prompting of an LLM can generate cognitively activating formative feedback aligned with research-based scaffold types (demonstrated, not yet empirically validated)](leap-prompt-design-generates-cognitively-activating-feedback.md) — reports the opposite
- [Prior non-LLM automated coding approaches yielded variable and often lower agreement with human coders on teacher knowledge measures, especially PCK](prior-automated-coding-variable-lower-agreement-pck.md) — related
- [Humans are more certain when judging that facilitation is not needed than when judging it is](humans-certain-when-not-facilitating.md) — related
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](llm-judge-pipeline-validated-against-human-raters.md) — related
- [GPT-4 demonstrated higher reliability of feedback than GPT-3.5, with higher F1 agreement with instructors on most assessment aspects](gpt4-higher-polarity-reliability-than-gpt35.md) — related
- [Human expert review is the most credible but slowest and most resource-intensive evaluation method](human-expert-review-most-credible-slowest.md) — related
- [Across 468 data points, human coders, LLMs, and both standards agreed on the same value in 280 cases (59.8%)](coder-agreement-patterns-upset-468.md) — related
- [Multi-label classification of open-ended course feedback was challenging even for expert human annotators who developed the label set, with average inter-rater Jaccard similarity of 81.24%](multi-label-survey-classification-challenging-expert-annotators.md) — related
- [Card sorting of GenAI-brainstormed concepts showed best agreement for the Refreshing Stimulus category and under-70% agreement for some concepts](genai-card-sorting-concept-agreement.md) — related
- [LLMs prompted with diverse strategies can analyze educational survey feedback and generate corrective tutor feedback at or above expert human performance in specific scenarios](llm-prompting-human-level-educational-feedback.md) — reports the opposite

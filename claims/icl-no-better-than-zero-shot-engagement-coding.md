---
type: claim
title: In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding
description: In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding
id: icl-no-better-than-zero-shot-engagement-coding
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: lan-anh-do-2026
    resource: "https://doi.org/10.48550/arxiv.2607.28651"
    title: "Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas. (2026). Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents. https://arxiv.org/abs/2607.28651 [doi:10.48550/arxiv.2607.28651](https://doi.org/10.48550/arxiv.2607.28651)"
    author: Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across criteria versions and models, ICL and zero-shot prompting produced similar agreement, and zero-shot sometimes slightly outperformed ICL. [→ Lan Anh Do 2026](#lan-anh-do-2026)

## Evidence

### Lan Anh Do 2026

Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas. (2026). Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents. https://arxiv.org/abs/2607.28651 [doi:10.48550/arxiv.2607.28651](https://doi.org/10.48550/arxiv.2607.28651)

`q2 · i?` · `causal · r2`

Null comparison within the same annotation study: for GPT-5.2 and GPT-4o under human-refined criteria, ICL and zero-shot QWK values were closely matched (e.g., GPT-5.2 Cri-V1 overall 0.631 ICL vs 0.629 zero-shot), a null result with no printed effect size.

> "Differences between ICL and zero-shot prompting were also modest and sometimes favored zero-shot, indicating that few-shot prompting with human examples did not consistently improve human–machine reliability on this task."

## Discussion


## Related Claims
- [Agent-refined frameworks improved cross-model agreement but remained below the human-refined framework and varied across foundation models](agent-refined-frameworks-below-human-refined.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Adding regex-based rules to few-shot LLM labeling improves agreement with human annotation (0.818 to 0.852 overall)](regex-rules-improve-fewshot-llm-labeling-accuracy.md) — related
- Zero-shot prompt type has minimal impact on LLM-human coding concordance — related
- [Machine–machine agreement exceeds human–machine agreement but remains below human–human agreement](machine-machine-above-human-machine-below-human-human.md) — related
- [Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution](few-shot-prompting-no-f1-gain-reduces-overattribution.md) — related
- [Gemini 2.0 Flash validated as a reliable LLM annotator of feedback focus types](gemini-flash-reliable-feedback-focus-annotator.md) — related
- [Few-shot prompting does not uniformly improve LLM performance and can degrade subskill mastery estimates, most notably for phonology](few-shot-prompting-degrades-phonology-mastery.md) — a narrower finding that bears on this claim

---
type: claim
title: Current LLMs misalign instructional-strategy sensitivity with pedagogical relevance, including hallucinated relevance of irrelevant traits
description: Current LLMs misalign instructional-strategy sensitivity with pedagogical relevance, including hallucinated relevance of irrelevant traits
id: llm-relevance-impact-misalignment-learner-characteristics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: naiming-liu-2025
    resource: "https://doi.org/10.48550/arxiv.2512.24362"
    title: "Naiming Liu, Brittany Bradford, Johaun Hatchett, Gabriel Diaz, Lorenzo Luzi, Zichao Wang, Debshila Basu Mallick, Richard Baraniuk. (2025). Learning Context: A Unified Framework and Roadmap for Context-Aware AI in Education. https://arxiv.org/abs/2512.24362 [doi:10.48550/arxiv.2512.24362](https://doi.org/10.48550/arxiv.2512.24362)"
    author: Naiming Liu, Brittany Bradford, Johaun Hatchett, Gabriel Diaz, Lorenzo Luzi, Zichao Wang, Debshila Basu Mallick, Richard Baraniuk
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# Current LLMs misalign instructional-strategy sensitivity with pedagogical relevance, including hallucinated relevance of irrelevant traits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In leave-one-out analyses, an LLM assigned a meaningless distractor (favorite hobby) a higher impact weight (TVD: 0.273) than nearly all pedagogical traits, and failed to attend to effort regulation (TVD: 0.080). [→ Naiming Liu 2025](#naiming-liu-2025)

## Evidence

### Naiming Liu 2025

Naiming Liu, Brittany Bradford, Johaun Hatchett, Gabriel Diaz, Lorenzo Luzi, Zichao Wang, Debshila Basu Mallick, Richard Baraniuk. (2025). Learning Context: A Unified Framework and Roadmap for Context-Aware AI in Education. https://arxiv.org/abs/2512.24362 [doi:10.48550/arxiv.2512.24362](https://doi.org/10.48550/arxiv.2512.24362)

`q1 · i?` · `theoretical · r2`

Leave-one-out (LOO) analysis measuring Total Variation Distance between full-context and LOO-context strategy distributions, shown in Figure 3; ground-truth characteristics sourced from the MSLQ, distractors synthetically generated.

> "While the model correctly prioritizes impactful traits like the learner's perceived value of the task (TVD: 0.287) and self-efficacy (TVD: 0.207), it fails to attend to other vital factors such as the learner's ability to regulate their effort (TVD: 0.080), treating them as effectively invisible."

## Discussion


## Related Claims
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — a broader claim this one bears on
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](chatgpt-zero-shot-relevance-extraction-unreliable.md) — related
- LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers — related
- [Recurring risks of GenAI in STEAM education include hallucination, bias, superficial completion strategies, and compromised assessment validity](genai-steam-risks-hallucination-bias.md) — a broader claim this one bears on
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — a broader claim this one bears on
- [LLMs in educational applications hallucinate in 15–25% of responses and can amplify bias against non-native language inputs](llm-hallucination-rate-education.md) — a broader claim this one bears on

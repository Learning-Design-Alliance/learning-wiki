---
type: claim
title: Machine–machine agreement exceeds human–machine agreement but remains below human–human agreement
description: Machine–machine agreement exceeds human–machine agreement but remains below human–human agreement
id: machine-machine-above-human-machine-below-human-human
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: lan-anh-do-2026
    resource: "https://doi.org/10.48550/arxiv.2607.28651"
    title: "Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas. (2026). Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents. https://arxiv.org/abs/2607.28651 [doi:10.48550/arxiv.2607.28651](https://doi.org/10.48550/arxiv.2607.28651)"
    author: Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Machine–machine agreement exceeds human–machine agreement but remains below human–human agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under ICL, GPT-4o vs GPT-5.2 QWK was 0.882 (Cri-V1) and 0.851 (Cri-V2), higher than human–machine QWK (about 0.58–0.66) but below human–human QWK (0.974). [→ Lan Anh Do 2026](#lan-anh-do-2026)

## Evidence

### Lan Anh Do 2026

Lan Anh Do, Hanling Jiang, Shuchin Aeron, Ayanna K. Thomas. (2026). Measuring Cognitive Engagement in Collaborative Discourse with an Extended ICAP Framework: Comparing Human Annotation, In-Context Learning, and Reflective LLM Agents. https://arxiv.org/abs/2607.28651 [doi:10.48550/arxiv.2607.28651](https://doi.org/10.48550/arxiv.2607.28651)

`q2 · i?` · `design · r3`

Reliability comparison across the three annotation dyads in the same 42-group dataset: machine–machine QWK of 0.851–0.894 across prompting conditions, human–machine around 0.575–0.655, human–human 0.974. Zero-shot with the human-refined framework "produced slightly higher agreement (QWK = 0.894 and 0.874)".

> "Machine–machine reliability was higher than human–machine reliability but remained lower than human–human agreement. Under the ICL setting, QWK was 0.882 for Criteria Version 1 and 0.851 for Version 2, with corresponding Krippendorff’sαvalues of 0.847 and 0.810, respectively."

## Discussion


## Related Claims
- [Agent-refined frameworks improved cross-model agreement but remained below the human-refined framework and varied across foundation models](agent-refined-frameworks-below-human-refined.md) — related
- Trained human annotators reach near-perfect agreement on the 7-point engagement scale, improving across refinement stages — related
- [The human-refined framework improved human agreement substantially but produced only modest gains for ICL-based LLM annotation](human-refined-framework-gains-humans-not-llms.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [LLM ratings of classroom transcripts are more correlated with each other than with expert human ratings, across the same and different tasks](llm-llm-agreement-exceeds-llm-human-classroom-ratings.md) — possibly the same claim (merge candidate)
- [Developmental representations remain relatively stable across translated bilingual narratives](clara-bilingual-translation-consistency.md) — related
- [Lower model performance on Prompt 2 tracks poor inter-annotator agreement (QWK 0.560 vs 0.758)](prompt2-low-performance-tracks-annotator-agreement.md) — related

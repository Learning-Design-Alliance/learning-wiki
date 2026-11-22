---
type: claim
title: Including the rubric description and training with justifications yields the best scoring performance, improving F1 from 0.158 to 0.353 over omitting both
description: Including the rubric description and training with justifications yields the best scoring performance, improving F1 from 0.158 to 0.353 over omitting both
id: rubric-description-and-justification-ablation-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: nischal-ashok-kumar-2026
    resource: "https://doi.org/10.48550/arXiv.2607.13433"
    title: "Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. [doi:10.48550/arXiv.2607.13433](https://doi.org/10.48550/arXiv.2607.13433)"
    author: Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Including the rubric description and training with justifications yields the best scoring performance, improving F1 from 0.158 to 0.353 over omitting both

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The With Description, With Justification configuration improves accuracy from 0.226 to 0.399, F1 from 0.158 to 0.353, and alpha from 0.019 to 0.346 compared to Without Description, Without Justification. [→ Nischal Ashok Kumar 2026](#nischal-ashok-kumar-2026)

## Evidence

### Nischal Ashok Kumar 2026

Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. [doi:10.48550/arXiv.2607.13433](https://doi.org/10.48550/arXiv.2607.13433)

`q2 · i?` · `causal · r2`

Ablation experiments (Appendix A.5, Table 5) over rubric description and justification variants in the fine-tuning framework; the article reports the With Description, With Justification setting achieving the highest performance across all metrics and uses it for all main experiments.

> "Compared to the setting with “Without Description” and “Without Justification”, this configuration improves accuracy from 0.226 to 0.399 (+17.3%), F1 from 0.158 to 0.353 (+19.5%), and 𝛼 from 0.019 to 0.346 (+32.7%)."

## Discussion


## Related Claims
- [Predicting rubric-agnostic trait values as outputs improves cross-rubric essay scoring in the No Labels setting, improving macro F1 by 5.0% over a no-traits baseline](trait-output-supervision-improves-no-labels-cross-rubric-scoring.md) — related
- [Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353](fine-tuning-beats-zero-shot-prompting-same-model.md) — related
- [The best fine-tuned open-source model outperforms GPT-5-mini prompting by 2.1% macro F1 and trails GPT-5 by 1.9% macro F1 on unseen rubrics](fine-tuned-open-source-competitive-with-proprietary-llms.md) — related

---
type: claim
title: "The best fine-tuned open-source model outperforms GPT-5-mini prompting by 2.1% macro F1 and trails GPT-5 by 1.9% macro F1 on unseen rubrics"
description: "The best fine-tuned open-source model outperforms GPT-5-mini prompting by 2.1% macro F1 and trails GPT-5 by 1.9% macro F1 on unseen rubrics"
id: fine-tuned-open-source-competitive-with-proprietary-llms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: nischal-ashok-kumar-2026
    resource: "https://doi.org/10.48550/arXiv.2607.13433"
    title: "Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. [doi:10.48550/arXiv.2607.13433](https://doi.org/10.48550/arXiv.2607.13433)"
    author: Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The best fine-tuned open-source model outperforms GPT-5-mini prompting by 2.1% macro F1 and trails GPT-5 by 1.9% macro F1 on unseen rubrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The best fine-tuned model (Gold Labels) achieves F1 of 0.431 versus GPT-5-mini's 0.410 (+2.1%) and alpha of 0.412 versus 0.388, while achieving lower accuracy (0.470 vs 0.492) and trailing GPT-5 (F1 0.450, accuracy 0.532, alpha 0.476). [→ Nischal Ashok Kumar 2026](#nischal-ashok-kumar-2026)

## Evidence

### Nischal Ashok Kumar 2026

Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. [doi:10.48550/arXiv.2607.13433](https://doi.org/10.48550/arXiv.2607.13433)

`q2 · i?` · `design · r2`

Comparison of the best fine-tuned open-source Llama-based model against zero-shot prompting of proprietary GPT-5-mini and GPT-5 on unseen rubrics; the article reports comparable F1 to GPT-5 (0.431 vs 0.450) but lower accuracy and alpha.

> "Compared to GPT-5-mini, our model achieves slightly higher F1 from 0.410 to 0.431 (+2.1%) and 𝛼 from 0.388 to 0.412 (+2.4%), while accuracy changes from 0.492 to 0.470."

## Discussion


## Related Claims
- [Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353](fine-tuning-beats-zero-shot-prompting-same-model.md) — related
- [Increasing target-essay supervision from No Labels to Pseudo Labels to Gold Labels consistently improves cross-rubric scoring, with Gold Labels providing the strongest and statistically significant gains](target-essay-supervision-improves-cross-rubric-scoring.md) — related
- [Fine-tuned Llama-3.1-8B model outperforms GPT-4o and Claude-3.5-Sonnet at rating the four resistance-response mechanisms](finetuned-llama-outperforms-baselines-resistance-mechanisms.md) — related
- [Predicting rubric-agnostic trait values as outputs improves cross-rubric essay scoring in the No Labels setting, improving macro F1 by 5.0% over a no-traits baseline](trait-output-supervision-improves-no-labels-cross-rubric-scoring.md) — related
- [The benefit of trait-based representations diminishes when target-essay supervision is available, with traits not consistently outperforming no-traits baselines under Pseudo or Gold Labels](trait-benefit-diminishes-with-target-essay-supervision.md) — related
- [Including the rubric description and training with justifications yields the best scoring performance, improving F1 from 0.158 to 0.353 over omitting both](rubric-description-and-justification-ablation-gains.md) — related

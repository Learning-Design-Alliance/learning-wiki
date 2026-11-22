---
type: claim
title: Increasing target-essay supervision from No Labels to Pseudo Labels to Gold Labels consistently improves cross-rubric scoring, with Gold Labels providing the strongest and statistically significant gains
description: Increasing target-essay supervision from No Labels to Pseudo Labels to Gold Labels consistently improves cross-rubric scoring, with Gold Labels providing the strongest and statistically significant gains
id: target-essay-supervision-improves-cross-rubric-scoring
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
    kind: causal
    rigour: 2
---

# Increasing target-essay supervision from No Labels to Pseudo Labels to Gold Labels consistently improves cross-rubric scoring, with Gold Labels providing the strongest and statistically significant gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Moving from No Labels to Gold Labels improves accuracy from 0.399 to 0.470, F1 from 0.353 to 0.431 (p<0.01), and alpha from 0.346 to 0.412; the Pseudo Labels gain (F1 0.353 to 0.376, p=0.109) is consistent but not significant. [→ Nischal Ashok Kumar 2026](#nischal-ashok-kumar-2026)

## Evidence

### Nischal Ashok Kumar 2026

Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. [doi:10.48550/arXiv.2607.13433](https://doi.org/10.48550/arXiv.2607.13433)

`q2 · i?` · `causal · r2`

Fine-tuning experiments comparing supervision levels in the No Traits configuration on the six-rubric critical thinking dataset; the article reports the Gold Labels gain reaching statistical significance (𝑝<0.01) while the Pseudo Labels gain remains modest (𝑝=0.109).

> "Moving from No Labels to Gold Labels improves accuracy from 0.399 to 0.470 (+7.1%), F1 from 0.353 to 0.431 (+7.8%, 𝑝<0.01), and 𝛼 from 0.346 to 0.412 (+6.6%)."

## Discussion


## Related Claims
- [The best fine-tuned open-source model outperforms GPT-5-mini prompting by 2.1% macro F1 and trails GPT-5 by 1.9% macro F1 on unseen rubrics](fine-tuned-open-source-competitive-with-proprietary-llms.md) — related
- [The benefit of trait-based representations diminishes when target-essay supervision is available, with traits not consistently outperforming no-traits baselines under Pseudo or Gold Labels](trait-benefit-diminishes-with-target-essay-supervision.md) — related
- [Predicting rubric-agnostic trait values as outputs improves cross-rubric essay scoring in the No Labels setting, improving macro F1 by 5.0% over a no-traits baseline](trait-output-supervision-improves-no-labels-cross-rubric-scoring.md) — related
- [Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353](fine-tuning-beats-zero-shot-prompting-same-model.md) — related

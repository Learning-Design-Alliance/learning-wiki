---
type: claim
title: Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353
description: Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353
id: fine-tuning-beats-zero-shot-prompting-same-model
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

# Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Moving from zero-shot prompting to the fine-tuning baseline improves F1 from 0.222 to 0.353 (+13.1%, p<0.001), accuracy from 0.372 to 0.399, and alpha from 0.251 to 0.346 for Llama 3.1 8B Instruct. [→ Nischal Ashok Kumar 2026](#nischal-ashok-kumar-2026)

## Evidence

### Nischal Ashok Kumar 2026

Nischal Ashok Kumar, Payu Wittawatolarn, Sana Kang, Marisa C. Peczuh, Blair Lehman, Ryan Baker, Caitlin Mills, Sherry Lachman, Ruochen Sun and Andrew Lan. (2026). When Rubrics Change: Cross-Rubric Generalization for Critical Thinking Essay Scoring. AI for Education Day, SIGKDD 2026. [doi:10.48550/arXiv.2607.13433](https://doi.org/10.48550/arXiv.2607.13433)

`q2 · i?` · `design · r2`

Comparison of Llama 3.1 8B Instruct zero-shot prompting against the fine-tuning baseline (No Labels, No Traits) on the six-rubric dataset; the article attributes zero-shot weakness to concentration on frequent proficiency levels, collapsing recall on minority labels.

> "Moving from zero-shot prompting to the fine-tuning baseline most notably improves F1 from 0.222 to 0.353 (+13.1%, 𝑝<0.001), with additional gains in accuracy from 0.372 to 0.399 (+2.7%) and 𝛼 from 0.251 to 0.346 (+9.5%)."

## Discussion


## Related Claims
- [The best fine-tuned open-source model outperforms GPT-5-mini prompting by 2.1% macro F1 and trails GPT-5 by 1.9% macro F1 on unseen rubrics](fine-tuned-open-source-competitive-with-proprietary-llms.md) — related
- [Predicting rubric-agnostic trait values as outputs improves cross-rubric essay scoring in the No Labels setting, improving macro F1 by 5.0% over a no-traits baseline](trait-output-supervision-improves-no-labels-cross-rubric-scoring.md) — related
- [Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.](sft-ineffective-reference-metrics-unreliable.md) — reports the opposite
- [A fine-tuned 8B model outperforms a zero-shot LLaMA-70B baseline on context-dependent components like Evidence and Conclusion, though the 70B excels on self-contained components like Position](fine-tuned-8b-outperforms-70b-on-context-dependent-components.md) — related
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — related
- [Including the rubric description and training with justifications yields the best scoring performance, improving F1 from 0.158 to 0.353 over omitting both](rubric-description-and-justification-ablation-gains.md) — related
- [Fine-tuned Llama-3.1-8B model outperforms GPT-4o and Claude-3.5-Sonnet at rating the four resistance-response mechanisms](finetuned-llama-outperforms-baselines-resistance-mechanisms.md) — related
- [Increasing target-essay supervision from No Labels to Pseudo Labels to Gold Labels consistently improves cross-rubric scoring, with Gold Labels providing the strongest and statistically significant gains](target-essay-supervision-improves-cross-rubric-scoring.md) — related

---
type: claim
title: The best-scoring prompt-engineered approaches did not match the fine-tuned models on emotion detection and Gibbs cycle tasks
description: The best-scoring prompt-engineered approaches did not match the fine-tuned models on emotion detection and Gibbs cycle tasks
id: papagai-finetuned-outperforms-gpt3-davinci
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: solopova-2023
    resource: "https://doi.org/10.1007/978-3-031-42608-7_16"
    title: "Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)"
    author: Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: solopova-2023-2
    resource: "https://doi.org/10.1007/978-3-031-42608-7_16"
    title: "Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)"
    author: Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: solopova-2023-3
    resource: "https://doi.org/10.1007/978-3-031-42608-7_16"
    title: "Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)"
    author: Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The best-scoring prompt-engineered approaches did not match the fine-tuned models on emotion detection and Gibbs cycle tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On a held-out subset, the fine-tuned models reached 0.81 on the custom emotion metric and 0.98 for the Gibbs cycle, performances the best-scoring prompt-engineered Davinci approaches did not offer. [→ Solopova 2023 (2)](#solopova-2023-2)
`q2 i?` Few-shot prompting with three examples per label raised Davinci only to 0.49 for emotions and 0.87 for the Gibbs cycle, still below the fine-tuned models. [→ Solopova 2023 (3)](#solopova-2023-3)

## Evidence

### Solopova 2023

Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)

`q2 · i?` · `design · r2`

Comparison evaluation in the results section: the fine-tuned RoBERTa and ELECTRA models were compared against the prompt-engineered generative model Davinci under zero-, one- and few-shot prompting on a held-out subset of samples.

> "We compared our emotions detection (fine-tuned RoBERTa) and Gibbs cycle model (fine-tuned Electra) with the prompt-engineered state-of-the-art generative model Davinci [4] on the same task."

### Solopova 2023 (2)

Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)

`q2 · i?` · `design · r2`

Held-out comparison against prompt-engineered Davinci: the article reports the best-scoring prompted approaches "did not offer a comparable performance to our fine-tuned models", which scored 0.81 on the custom emotion metric and 0.98 for the Gibbs cycle.

> "However, the best-scoring approaches did not offer a comparable performance to our fine-tuned models on these specific tasks with 0.81 on the same custom metric for emotion detection and 0.98 for the Gibbs cycle."

### Solopova 2023 (3)

Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)

`q2 · i?` · `design · r2`

Few-shot condition of the same comparison: the article reports that three examples per label produced "a slight improvement of 3% (0.49) for emotions, and 7% (0.87) for the Gibbs cycle" for the prompted generative model.

> "Increasing the number of examples to three resulted in a slight improvement of 3% (0.49) for emotions, and 7% (0.87) for the Gibbs cycle."

## Discussion


## Related Claims
- [Fine-tuned ELECTRA classifies Gibbs cycle phases in reflective sentences, with top-3 predictions reaching up to 98% F1](papagai-electra-gibbs-cycle-top3-f1-098.md) — possibly the same claim (merge candidate)
- [Adaptation through prompt injection avoids fine-tuning, so the system works with any OpenAI-compatible LLM and its logic is transparent to educators](prompt-engineering-adaptation-transparency-tradeoff.md) — related
- [Fine-tuned RoBERTa detects sentence-level emotions in reflective essays with a micro F1 of 0.70](papagai-roberta-emotion-detection-f1-070.md) — related
- [Prompt customization introduces at least three types of prompting bias: majority label, recency, and common token bias](prompting-bias-three-types.md) — related
- Fine-tuned GPT3-DaVinci is the most accurate classifier of acceptable clue-answer pairs at 79.88% — related

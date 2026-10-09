---
type: claim
title: "NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward"
description: "NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward"
id: nlp-la-performance-kappa-accuracy-benchmarks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: rafael-ferreira-mello-2024
    resource: "https://doi.org/10.18608/jla.2024.8403"
    title: "Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403"
    author: Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević
    q: 3
    i: "?"
    kind: quant-synthesis
    rigour: 2
  - id: rafael-ferreira-mello-2024-2
    resource: "https://doi.org/10.18608/jla.2024.8403"
    title: "Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403"
    author: Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević
    q: 3
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · quant-synthesis `r2` · `q3`

## Subclaims
`q3 i?` Across reviewed studies reporting metrics, mean performance reached 0.54 in kappa and 0.79 in accuracy. [→ Rafael Ferreira Mello 2024](#rafael-ferreira-mello-2024)
`q3 i?` From 2021 onward, deep learning models (LSTM, DNN, BERT) outperformed others in the majority of recent studies. [→ Rafael Ferreira Mello 2024 (2)](#rafael-ferreira-mello-2024-2)

## Evidence

### Rafael Ferreira Mello 2024

Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403

`q3 · i?` · `quant-synthesis · r2`

Synthesis of Cohen's kappa and accuracy across reviewed studies (Table 4, RQ7): overall kappa mean 0.54 (SD 0.19, 28 papers) and accuracy mean 0.79 (SD 0.10, 45 papers). The review notes a kappa of 0.54 denotes moderate agreement and 0.79 accuracy a strong indicator of good performance.

> "However, the mean performance metrics observed in the field significantly exceed these thresholds, typically reaching 0.54 in kappa and 0.79 in accuracy."

### Rafael Ferreira Mello 2024 (2)

Rafael Ferreira Mello, Elyda Freitas, Luciano Cabral, Filipe Dwan Pereira, Luiz Rodrigues, Mladen Rakovic, Jackson Raniel, Dragan Gašević. (2024). Words of Wisdom: A Journey through the Realm of Natural Language Processing for Learning Analytics—A Systematic Literature Review. Journal of Learning Analytics, 11(3), 82–105. https://doi.org/10.18608/jla.2024.8403

`q3 · i?` · `quant-synthesis · r2`

Year-by-year analysis of the best-performing algorithm per study (Figure 8, RQ7). Random Forest predominated in earlier years, peaking in 2020; from 2021 onward deep learning models led in the majority of recent studies. The review cautions that dataset and other factors influence outcomes, so results are not a definitive benchmark.

> "In contrast, if we focus exclusively on research from 2021 onward, it becomes evident that deep learning models, namely LSTM, DNN (Deep Neural Networks) (Canale et al., 2021), and BERT, have outperformed others in the majority of recent studies."

## Discussion


## Related Claims
- [The fine-tuned BERT model generalizes to an external dataset collected by a different research team, maintaining almost perfect agreement with human coders](bert-generalizes-external-self-affirmation-dataset.md) — a narrower finding that bears on this claim
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
- [Collaborative learning is the most prominent educational task addressed with NLP in learning analytics research, followed by assessment and feedback](nlp-la-collaborative-learning-most-prominent-task.md) — related
- [NLP-for-LA research is heavily biased toward English-language texts and small datasets, with almost no open datasets](nlp-la-english-small-dataset-bias.md) — related
- [Most NLP-for-LA studies (89.10%) never apply their models in real educational settings, revealing a gap between model development and practical use](nlp-la-gap-model-development-practical-use.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related

---
type: claim
title: "NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward"
description: "NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward"
id: nlp-la-performance-kappa-accuracy-benchmarks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
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
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

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
- Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021 — related
- Collaborative learning is the most prominent educational task addressed with NLP in learning analytics research, followed by assessment and feedback — related
- NLP-for-LA research is heavily biased toward English-language texts and small datasets, with almost no open datasets — related
- Most NLP-for-LA studies (89.10%) never apply their models in real educational settings, revealing a gap between model development and practical use — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- The review's evidence base comprises 42 peer-reviewed publications selected from 922 records with high inter-rater agreement (Cohen's kappa = 0.88) — related
- [Inter-annotator agreement was moderate (combined mean Fleiss's κ of 0.62 across 23 groups), yet most students reported having reached consensus](moderate-kappa-versus-perceived-consensus-gap.md) — a narrower finding that bears on this claim
- An independent human second coder reached moderate agreement (kappa = 0.395) with the AI-assisted primary coding on the five-category outcome — a narrower finding that bears on this claim
- [Transformer-based NLP models achieve automated essay scoring with correlations to human grading exceeding 0.85](bert-essay-scoring-correlation-085.md) — a narrower finding that bears on this claim
- [Benchmarking shows NLP-based automated essay scoring achieves grading times up to 80% faster than human graders while maintaining comparable accuracy](nlp-grading-80-percent-faster-benchmark.md) — related
- [NLP-based feedback generation for textual student answers in large courses reduced grading effort by up to 85% with high precision (reported from Bernius et al.)](nlp-feedback-reduced-grading-effort-85-percent.md) — related
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [Essays within each tool group showed consistent homogeneity across named entities, n-grams, and topic ontology](nlp-homogeneity-ner-ngrams-ontology-within-groups.md) — related
- [The rule-based recipe annotation system reaches near-perfect inter-annotator agreement (Cohen's Kappa 0.85) and average accuracy 0.95 in a validation on sampled recipe segments.](relex-annotation-validation-kappa-accuracy.md) — a narrower finding that bears on this claim
- [Machine learning detects five of eight reflective-writing categories with substantial or almost perfect reliability and three with moderate reliability (Cohen's κ .53–.85)](ml-detects-reflection-categories-kappa-053-085.md) — related
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — a narrower finding that bears on this claim
- [Predictive LA research neglects interpretability, explainability, and prescriptive analytics, with course-level prediction dominating over programme-level](la-interpretability-prescriptive-gap.md) — related
- [The introduction reports that deep learning and NLP techniques predicted fine-grained rubric scores of student essays with success well beyond the agreement level between two human raters](deep-learning-essay-scoring-beyond-human-rater-agreement.md) — related
- [ML scoring models for scientific argumentation items achieved good to almost perfect agreement with human consensus scores (mean Cohen's kappa = 0.60)](ml-scoring-argumentation-mean-kappa-060.md) — a narrower finding that bears on this claim
- [Sentence-to-learning-tip segmentation coding by three trained coders reached an average Cohen's Kappa of 0.96](segmentation-coding-kappa-096.md) — a narrower finding that bears on this claim
- [Learning-tip-to-lecture-topic coding by seven coders reached an overall agreement of 0.87 (Cohen's Kappa)](topic-coding-agreement-087.md) — related
- [A non-fine-tuned pre-trained sentiment analysis model achieves moderate agreement with human coders of student open-ended answers](pretrained-sa-moderate-agreement.md) — a narrower finding that bears on this claim

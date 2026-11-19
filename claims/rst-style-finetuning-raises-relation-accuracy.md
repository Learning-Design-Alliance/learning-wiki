---
type: claim
title: "Fine-tuning the discourse classifier on RST-DT-style segments reconciles the PDTB–RST framework mismatch and raises accuracy from 65.7% to 81.1%"
description: "Fine-tuning the discourse classifier on RST-DT-style segments reconciles the PDTB–RST framework mismatch and raises accuracy from 65.7% to 81.1%"
id: rst-style-finetuning-raises-relation-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: matt-grenander-2021
    resource: "https://doi.org/10.1609/aaai.v35i17.17829"
    title: "Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)"
    author: Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning the discourse classifier on RST-DT-style segments reconciles the PDTB–RST framework mismatch and raises accuracy from 65.7% to 81.1%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On 103 hand-annotated student solution attempt samples, the discourse classifier improved from 65.7% accuracy before fine-tuning to 81.1% after fine-tuning on RST-DT-style EDUs with PDTB-style relations. [→ Matt Grenander 2021](#matt-grenander-2021)

## Evidence

### Matt Grenander 2021

Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)

`q2 · i?` · `design · r2`

Model assessment on 103 hand-annotated student solution attempt samples after building a bridging dataset in which 40% of relations came from shared EDU boundaries, 50% from cue word heuristics, and 10% from manual annotation. Accuracy rose from 65.7% to 81.1% after fine-tuning.

> "We assess the ﬁne-tuned model on 103 hand-annotated student solution attempt samples. We ﬁnd that before ﬁne-tuning on RST-DT-style EDUs, the model reaches 65.7% accuracy. After ﬁne-tuning, the resulting classiﬁer achieves 81.1% accuracy"

## Discussion


## Related Claims
- [A RoBERTa-based discourse segmentation model outperforms prior LSTM- and BERT-based segmenters on the RST-DT test set](roberta-segmenter-outperforms-rst-dt.md) — related
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [A RoBERTa-based discourse relation classifier achieves strong implicit relation results on PDTB 2.0 while also handling explicit relations](roberta-discourse-classifier-pdtb-implicit-sota.md) — related

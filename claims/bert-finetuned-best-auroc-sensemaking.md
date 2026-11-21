---
type: claim
title: A fine-tuned BERT encoder achieves the best agreement with human coding (AUROC 0.916) among three encoder variants on held-out student responses to the same four problems
description: A fine-tuned BERT encoder achieves the best agreement with human coding (AUROC 0.916) among three encoder variants on held-out student responses to the same four problems
id: bert-finetuned-best-auroc-sensemaking
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: gili-2025
    resource: "https://doi.org/10.1103/v6gw-lv4c"
    title: "Gili, Heuton, Shah, Hammer, and Hughes. (2025). Combining physics education and machine learning research to measure evidence of students' mechanistic sensemaking. arXiv. [doi:10.1103/v6gw-lv4c](https://doi.org/10.1103/v6gw-lv4c)"
    author: Gili, Heuton, Shah, Hammer, and Hughes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A fine-tuned BERT encoder achieves the best agreement with human coding (AUROC 0.916) among three encoder variants on held-out student responses to the same four problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On a held-out test set of responses from 15 new students, the BERTfinetuned model achieved an average AUROC of 0.916, outperforming BERTfrozen and BoW on most sensemaking domains. [→ Gili 2025](#gili-2025)

## Evidence

### Gili 2025

Gili, Heuton, Shah, Hammer, and Hughes. (2025). Combining physics education and machine learning research to measure evidence of students' mechanistic sensemaking. arXiv. [doi:10.1103/v6gw-lv4c](https://doi.org/10.1103/v6gw-lv4c)

`q2 · i?` · `design · r2`

Held-out test evaluation of the multi-label classification models on 60 responses from 15 randomly selected students, stratified by student to prevent leakage. The article reports "an AUROC score of 0.916" for BERTfinetuned, best on four named domains, with 160 minutes training time.

> "BERTfinetunedachieves an AUROC score of 0.916. It performs the best for influences, spatial organization, movement activities, and interactions. It takes significant time to train, 160 minutes."

## Discussion


## Related Claims
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [Fine-tuning several pre-trained LLMs with class balancing, data augmentation, and tailored input modification reaches near human-level automated scoring accuracy on most extended-response mathematics assessment items](fine-tuned-llms-near-human-math-scoring.md) — related
- [Classification performance varies across the seven sensemaking domains, and no AUROC could be reported for the properties domain because its positive examples were too rare](per-domain-auroc-varies-properties-undefined.md) — related
- [The fine-tuned model generalized to out-of-domain lessons with 77% overall accuracy](fine-tuned-model-out-of-domain-77.md) — related

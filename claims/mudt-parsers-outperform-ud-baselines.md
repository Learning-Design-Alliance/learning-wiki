---
type: claim
title: Parsers trained on MUDT outperform UD-trained baselines in-domain, and cross-domain transfer is asymmetric with performance degrading sharply when UD-trained models are applied to MUDT data
description: Parsers trained on MUDT outperform UD-trained baselines in-domain, and cross-domain transfer is asymmetric with performance degrading sharply when UD-trained models are applied to MUDT data
id: mudt-parsers-outperform-ud-baselines
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: jiaxin-zuo-2025
    resource: "https://doi.org/10.48550/arXiv.2507.21536"
    title: "Jiaxin Zuo, Yiquan Wang, Yuan Pan, and Xiadiya Yibulayin. (2025). Construction and educational application of a linguistically grounded dependency treebank for Uyghur. [doi:10.48550/arXiv.2507.21536](https://doi.org/10.48550/arXiv.2507.21536)"
    author: Jiaxin Zuo, Yiquan Wang, Yuan Pan, and Xiadiya Yibulayin
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jiaxin-zuo-2025-2
    resource: "https://doi.org/10.48550/arXiv.2507.21536"
    title: "Jiaxin Zuo, Yiquan Wang, Yuan Pan, and Xiadiya Yibulayin. (2025). Construction and educational application of a linguistically grounded dependency treebank for Uyghur. [doi:10.48550/arXiv.2507.21536](https://doi.org/10.48550/arXiv.2507.21536)"
    author: Jiaxin Zuo, Yiquan Wang, Yuan Pan, and Xiadiya Yibulayin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Parsers trained on MUDT outperform UD-trained baselines in-domain, and cross-domain transfer is asymmetric with performance degrading sharply when UD-trained models are applied to MUDT data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In-domain, the Stanza model trained on MUDT achieved a UAS of 0.655 versus 0.572 for the UD-trained model. [→ Jiaxin Zuo 2025](#jiaxin-zuo-2025)
`q2 i?` Cross-domain, UD-trained models applied to MUDT data degraded sharply, with LAS dropping to as low as 0.158 in the Stanza experiment. [→ Jiaxin Zuo 2025 (2)](#jiaxin-zuo-2025-2)

## Evidence

### Jiaxin Zuo 2025

Jiaxin Zuo, Yiquan Wang, Yuan Pan, and Xiadiya Yibulayin. (2025). Construction and educational application of a linguistically grounded dependency treebank for Uyghur. [doi:10.48550/arXiv.2507.21536](https://doi.org/10.48550/arXiv.2507.21536)

`q2 · i?` · `design · r2`

Extrinsic parsing experiments using UDPipe, Stanza, and DiaParser, reported in Table 4. The article reports the MUDT-trained Stanza model's "Unlabeled Attachment Score of 0.655" versus 0.572 for the UD-trained model, and DiaParser reached UAS 0.8050 and LAS 0.6675.

> "the Stanza model trained on MUDT achieved an Unlabeled Attachment Score of 0.655, significantly higher than the 0.572 achieved by the model trained on UD."

### Jiaxin Zuo 2025 (2)

Jiaxin Zuo, Yiquan Wang, Yuan Pan, and Xiadiya Yibulayin. (2025). Construction and educational application of a linguistically grounded dependency treebank for Uyghur. [doi:10.48550/arXiv.2507.21536](https://doi.org/10.48550/arXiv.2507.21536)

`q2 · i?` · `design · r2`

Cross-domain evaluation in the extrinsic parsing section, reported in Table 4. The article describes the asymmetric compatibility between schemes, with LAS "dropping to as low as 0.158" for UD-trained models on MUDT data, and interprets MUDT as a superset of linguistic knowledge.

> "when the model trained on UD was applied to MUDT data, performance degraded sharply, with the Labeled Attachment Score dropping to as low as 0.158 in the Stanza experiment."

## Discussion


## Related Claims
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — a broader claim this one bears on
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — related
- [All pretrained transformer models showed a significant performance drop of about 20% between IID and OOD data, and OOD performance correlated linearly with IID performance](pretrained-transformers-twenty-percent-ood-drop.md) — a broader claim this one bears on
- [Novice L2 learners using MUDT-Tutor syntax-aware feedback achieved significantly higher learning gains (13.73 points) than a no-feedback control group (7.88 points), t(29)=2.51, p=0.018, d=0.90](mudt-tutor-syntax-aware-feedback-higher-gains.md) — related

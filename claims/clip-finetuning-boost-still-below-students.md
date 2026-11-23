---
type: claim
title: Finetuning CLIP substantially boosts performance (+30 points on science and math) yet remains far below average elementary students
description: Finetuning CLIP substantially boosts performance (+30 points on science and math) yet remains far below average elementary students
id: clip-finetuning-boost-still-below-students
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: jianhao-shen-2024
    resource: "https://doi.org/10.48550/arXiv.2402.17205"
    title: "Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang, Chenguang Wang. (2024). MEASURING VISION-LANGUAGE STEM SKILLS OF NEURAL MODELS. Published as a conference paper at ICLR 2024. [doi:10.48550/arXiv.2402.17205](https://doi.org/10.48550/arXiv.2402.17205)"
    author: Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang, Chenguang Wang
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Finetuning CLIP substantially boosts performance (+30 points on science and math) yet remains far below average elementary students

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Finetuning CLIP ViT-L/14@336px raises science and math accuracy by an average of 30 percentage points over zero-shot, reaching 76.3 average, but stays far behind elementary students. [→ Jianhao Shen 2024](#jianhao-shen-2024)

## Evidence

### Jianhao Shen 2024

Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang, Chenguang Wang. (2024). MEASURING VISION-LANGUAGE STEM SKILLS OF NEURAL MODELS. Published as a conference paper at ICLR 2024. [doi:10.48550/arXiv.2402.17205](https://doi.org/10.48550/arXiv.2402.17205)

`q3 · i?` · `causal · r1`

Finetuning experiment training CLIP ViT-L/14@336px on each subject's entire training set with model selection on the validation set (Table 2, Table 4). Zero-shot 54.4 average rises to 76.3 finetuned, still far below the human-level performance presented in Sec. 3.3.

> "finetuning CLIP ViT-L/14@336px is able to significantly boost the performance on science and math by averaging 30% points over its zero-shot setting. The performance improvements on other subjects are 7.9% points, which is much smaller."

## Discussion


## Related Claims
- Zero-shot CLIP accuracy improves with model size but saturates, indicating scaling alone is insufficient — related
- [CLIP-RN50x64 is the best zero-shot model on STEM, outperforming GPT-3.5-Turbo by 5.9 percentage points, but math improves only marginally](clip-best-zero-shot-math-hardest.md) — related
- [State-of-the-art foundation models remain well below average elementary students on STEM, mastering only 2.5% of third-grade skills](foundation-models-below-elementary-students-stem.md) — a broader claim this one bears on
- Zero-shot CLIP is overconfident and poorly calibrated; finetuning improves calibration — related

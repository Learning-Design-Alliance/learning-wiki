---
type: claim
title: RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction
description: RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction
id: roberta-classifiers-discourse-moves-moderate-high-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: dorottya-demszky-and-heather-hill-2023
    resource: "https://doi.org/10.18653/v1/2023.bea-1.44"
    title: "Dorottya Demszky and Heather Hill. (2023). The NCTE Transcripts: A Dataset of Elementary Math Classroom Transcripts. Originally published 2022. [doi:10.18653/v1/2023.bea-1.44](https://doi.org/10.18653/v1/2023.bea-1.44)"
    author: Dorottya Demszky and Heather Hill
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` RoBERTa models fine-tuned on turn-level annotations classify each discourse feature with moderate to high accuracy, performing best on on vs off task instruction (F1 = .942 for student and .923 for teacher utterances) and moderately on higher-inference moves. [→ Dorottya Demszky and Heather Hill 2023](#dorottya-demszky-and-heather-hill-2023)

## Evidence

### Dorottya Demszky and Heather Hill 2023

Dorottya Demszky and Heather Hill. (2023). The NCTE Transcripts: A Dataset of Elementary Math Classroom Transcripts. Originally published 2022. [doi:10.18653/v1/2023.bea-1.44](https://doi.org/10.18653/v1/2023.bea-1.44)

`q2 · i?` · `design · r2`

Supervised classification of NCTE transcripts, averaged across five-fold cross validation (Table 4). The article reports "F1 score (har- monic mean of precision and recall) is .942 and .923" for on-task detection, with Focusing Questions lowest at F1 = .501.

> "The model performs best on classify- ing on vs off task instruction — F1 score (har- monic mean of precision and recall) is .942 and .923 for student and teacher utterances, respec- tively."

## Discussion


## Related Claims
- [All classifier-predicted discourse features correlate significantly with classroom observation scores measuring instruction quality and classroom climate](discourse-features-correlate-observation-scores.md) — related
- [Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set](roberta-funneling-focusing-correlation-761.md) — related
- [GPT-3 achieves higher precision than RoBERTa for every talk-move classifier, with gains of at least 5 and up to 21 points](gpt3-higher-precision-than-roberta-talk-moves.md) — related
- [GPT-3's recall varies significantly across talk moves, performing far worse than RoBERTa for Connecting](gpt3-recall-varies-connecting-worst.md) — related
- [Unadjusted foundation models achieve only moderate agreement (Cohen's κ = 0.38–0.58) with expert annotations when classifying instructional moves in authentic classroom transcripts](llm-baseline-moderate-kappa-talk-moves.md) — related

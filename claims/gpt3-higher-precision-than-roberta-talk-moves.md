---
type: claim
title: GPT-3 achieves higher precision than RoBERTa for every talk-move classifier, with gains of at least 5 and up to 21 points
description: GPT-3 achieves higher precision than RoBERTa for every talk-move classifier, with gains of at least 5 and up to 21 points
id: gpt3-higher-precision-than-roberta-talk-moves
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: ashlee-kupor-2023
    resource: "https://doi.org/10.48550/arXiv.2311.10749"
    title: "Ashlee Kupor, Candice Morgan, Dorottya Demszky. (2023). Measuring Five Accountable Talk Moves to Improve Instruction at Scale. arXiv. [doi:10.48550/arXiv.2311.10749](https://doi.org/10.48550/arXiv.2311.10749)"
    author: Ashlee Kupor, Candice Morgan, Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-3 achieves higher precision than RoBERTa for every talk-move classifier, with gains of at least 5 and up to 21 points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across the five binary talk-move classifiers, GPT-3's precision exceeds RoBERTa's for every talk move, by at least 5 points and up to 21 points (Probing). [→ Ashlee Kupor 2023](#ashlee-kupor-2023)

## Evidence

### Ashlee Kupor 2023

Ashlee Kupor, Candice Morgan, Dorottya Demszky. (2023). Measuring Five Accountable Talk Moves to Improve Instruction at Scale. arXiv. [doi:10.48550/arXiv.2311.10749](https://doi.org/10.48550/arXiv.2311.10749)

`q2 · i?` · `design · r2`

Model comparison on a held-out 20% split of 2,503 annotated instructor utterances from Code in Place 2021; Table 2 reports precision per talk move. The article finds GPT-3 "at least 5 points higher and sometimes as much as 21 points more" than RoBERTa in precision.

> "In terms of precision, GPT-3 has a higher score for every talk move, being at least 5 points higher and sometimes as much as 21 points more."

## Discussion


## Related Claims
- [GPT-3's recall varies significantly across talk moves, performing far worse than RoBERTa for Connecting](gpt3-recall-varies-connecting-worst.md) — related
- [RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction](roberta-classifiers-discourse-moves-moderate-high-accuracy.md) — related
- [Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — reports the opposite

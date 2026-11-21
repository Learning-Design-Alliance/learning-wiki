---
type: claim
title: "GPT-3's recall varies significantly across talk moves, performing far worse than RoBERTa for Connecting"
description: "GPT-3's recall varies significantly across talk moves, performing far worse than RoBERTa for Connecting"
id: gpt3-recall-varies-connecting-worst
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

# GPT-3's recall varies significantly across talk moves, performing far worse than RoBERTa for Connecting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-3's recall matches RoBERTa for Probing and Revoicing, is 10 points better for Eliciting, and up to 47 points worse for Connecting; its F1 is over 20 points worse for Connecting. [→ Ashlee Kupor 2023](#ashlee-kupor-2023)

## Evidence

### Ashlee Kupor 2023

Ashlee Kupor, Candice Morgan, Dorottya Demszky. (2023). Measuring Five Accountable Talk Moves to Improve Instruction at Scale. arXiv. [doi:10.48550/arXiv.2311.10749](https://doi.org/10.48550/arXiv.2311.10749)

`q2 · i?` · `design · r2`

Evaluation on the same held-out split as the precision comparison (Table 2). The article reports GPT-3 F1 better by 3-12 points for most moves but "over 20 points worse" for Connecting, and recall up to 47 points worse for Connecting.

> "GPT-3 F1's score is better for all talk moves with improvements ranging between 3-12 points compared to RoBERTa, except forConnecting where it performs over 20 points worse."

## Discussion


## Related Claims
- [GPT-3 achieves higher precision than RoBERTa for every talk-move classifier, with gains of at least 5 and up to 21 points](gpt3-higher-precision-than-roberta-talk-moves.md) — related
- [Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction](roberta-classifiers-discourse-moves-moderate-high-accuracy.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [LLMs classifying Talk Moves show higher recall than precision, overproducing labels at a high false-positive rate](llm-talk-move-labeling-high-false-positives.md) — related

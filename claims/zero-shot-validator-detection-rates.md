---
type: claim
title: "Zero-shot validation filters identified 56.76% (Italian prompts) and 69.72% (English prompts) of unacceptable clue-answer pairs"
description: "Zero-shot validation filters identified 56.76% (Italian prompts) and 69.72% (English prompts) of unacceptable clue-answer pairs"
id: zero-shot-validator-detection-rates
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: kamyar-zeinalipour-2023
    resource: "https://doi.org/10.48550/arXiv.2311.15723"
    title: "Kamyar Zeinalipour, Tommaso Iaquinta, Asya Zanollo, Giovanni Angelini, Leonardo Rigutini, Marco Maggini, Marco Gori. (2023). Italian Crossword Generator: Enhancing Education through Interactive Word Puzzles. arXiv preprint. [doi:10.48550/arXiv.2311.15723](https://doi.org/10.48550/arXiv.2311.15723)"
    author: Kamyar Zeinalipour, Tommaso Iaquinta, Asya Zanollo, Giovanni Angelini, Leonardo Rigutini, Marco Maggini, Marco Gori
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Zero-shot validation filters identified 56.76% (Italian prompts) and 69.72% (English prompts) of unacceptable clue-answer pairs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The multi-stage validation process identified unacceptable clue-answer pairs at rates of 56.76% with Italian prompts and 69.72% with English prompts. [→ Kamyar Zeinalipour 2023](#kamyar-zeinalipour-2023)

## Evidence

### Kamyar Zeinalipour 2023

Kamyar Zeinalipour, Tommaso Iaquinta, Asya Zanollo, Giovanni Angelini, Leonardo Rigutini, Marco Maggini, Marco Gori. (2023). Italian Crossword Generator: Enhancing Education through Interactive Word Puzzles. arXiv preprint. [doi:10.48550/arXiv.2311.15723](https://doi.org/10.48550/arXiv.2311.15723)

`q2 · i?` · `design · r2`

Human-supervised evaluation of the validation stage of the text path on 50 Wikipedia paragraphs. The authors report the validator "identified 56.76% and 69.72% of the unacceptable clue-answer pairs" for Italian and English prompts. No effect size is printed.

> "Through this validation, we were able to identify 56.76% and 69.72% of the unacceptable clue-answer pairs generated using the Italian and English prompts, respectively."

## Discussion


## Related Claims
- English prompts outperform Italian prompts when generating Italian crossword clues from Italian text — related
- [Text-based clue generation achieves 79.73% acceptable keywords and 76.70% acceptable clues with English prompts](text-path-clue-generation-accuracy.md) — related
- Fine-tuned GPT3-DaVinci is the most accurate classifier of acceptable clue-answer pairs at 79.88% — related

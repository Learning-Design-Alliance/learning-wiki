---
type: claim
title: "Text-based clue generation achieves 79.73% acceptable keywords and 76.70% acceptable clues with English prompts"
description: "Text-based clue generation achieves 79.73% acceptable keywords and 76.70% acceptable clues with English prompts"
id: text-path-clue-generation-accuracy
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

# Text-based clue generation achieves 79.73% acceptable keywords and 76.70% acceptable clues with English prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On 50 Wikipedia paragraphs evaluated with human supervision, keyword extraction reached 79.73% (Italian prompts) and 75.60% (English prompts) accuracy, and 68.34% (Italian) and 76.70% (English) of generated clues were judged acceptable. [→ Kamyar Zeinalipour 2023](#kamyar-zeinalipour-2023)

## Evidence

### Kamyar Zeinalipour 2023

Kamyar Zeinalipour, Tommaso Iaquinta, Asya Zanollo, Giovanni Angelini, Leonardo Rigutini, Marco Maggini, Marco Gori. (2023). Italian Crossword Generator: Enhancing Education through Interactive Word Puzzles. arXiv preprint. [doi:10.48550/arXiv.2311.15723](https://doi.org/10.48550/arXiv.2311.15723)

`q2 · i?` · `design · r2`

Human-supervised evaluation of the zero/few-shot text path on 50 Wikipedia paragraphs, comparing Italian and English prompts. The evaluation found "79.73% and 75.60% accuracy in generating suitable keywords" and acceptable-clue rates of 68.34% and 76.70%. No effect size is reported.

> "we obtained 79.73% and 75.60% accuracy in generating suitable keywords for crossword clues using Italian and English prompts, respectively. Subsequently, we subjected the clue-generation process to human evaluation and found that, with Italian and English prompts, 68.34% and 76.70% of the generated clues were considered acceptable"

## Discussion


## Related Claims
- Fine-tuned GPT3-DaVinci outperformed GPT3-Curie in keyword-based clue generation (60.1% vs 34.9% acceptable) — related
- English prompts outperform Italian prompts when generating Italian crossword clues from Italian text — possibly the same claim (merge candidate)
- [Zero-shot validation filters identified 56.76% (Italian prompts) and 69.72% (English prompts) of unacceptable clue-answer pairs](zero-shot-validator-detection-rates.md) — related

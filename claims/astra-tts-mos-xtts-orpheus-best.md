---
type: claim
title: XTTS and Orpheus achieve the highest human-rated MOS for Singaporean-accented ATC speech synthesis (3.71 and 3.70), with female voices preferred across models
description: XTTS and Orpheus achieve the highest human-rated MOS for Singaporean-accented ATC speech synthesis (3.71 and 3.70), with female voices preferred across models
id: astra-tts-mos-xtts-orpheus-best
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: ethan-chew-2026
    resource: "https://arxiv.org/abs/2606.18319"
    title: "Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319"
    author: Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# XTTS and Orpheus achieve the highest human-rated MOS for Singaporean-accented ATC speech synthesis (3.71 and 3.70), with female voices preferred across models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In human MOS ratings, XTTS and Orpheus achieve the highest overall scores (3.71 and 3.70) while CSM trails across all dimensions due to truncations and incomplete utterance endings. [→ Ethan Chew 2026](#ethan-chew-2026)
`q2 i?` LLM-based scores follow the same ranking but diverge from human judgment, with XTTS showing the largest human-LLM gap (3.71 vs 3.37), and gender accuracy exceeds 96% for all models. [→ Ethan Chew 2026](#ethan-chew-2026)

## Evidence

### Ethan Chew 2026

Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319

`q2 · i?` · `design · r2`

Perceptual MOS evaluation of three fine-tuned TTS models on five dimensions, rated by 21 aviation personnel familiar with ICAO radiotelephony plus an automated LLM evaluator (Gemini 2.5 Flash); each human rater evaluated 9 clips. The paper notes "CSMtrails both mod- els across all dimensions".

> "As shown in Table 3,XTTSandOrpheusachieve the highest overall human MOS scores (3.71 and 3.70 respectively)."

## Discussion


## Related Claims
- [In pairwise A/B preference tests, raters preferred XTTS and Orpheus over CSM, and preferred female voices across all models](astra-ab-preference-xtts-orpheus-over-csm.md) — related

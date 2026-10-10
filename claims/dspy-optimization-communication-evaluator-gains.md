---
type: claim
title: "DSPy prompt optimization improves all radiotelephony evaluators, with the largest gain in accuracy (+7.9%)"
description: "DSPy prompt optimization improves all radiotelephony evaluators, with the largest gain in accuracy (+7.9%)"
id: dspy-optimization-communication-evaluator-gains
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ethan-chew-2026
    resource: "https://arxiv.org/abs/2606.18319"
    title: "Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319"
    author: Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ethan-chew-2026-2
    resource: "https://arxiv.org/abs/2606.18319"
    title: "Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319"
    author: Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DSPy prompt optimization improves all radiotelephony evaluators, with the largest gain in accuracy (+7.9%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` After DSPy optimization, evaluator performance improved for accuracy (83.8 to 91.7%), brevity (85.5 to 89.7%), and completeness (81.5 to 88.1%), measured by inverted MAE on held-out sets. [→ Ethan Chew 2026](#ethan-chew-2026)
`q2 i?` FewShot+RS achieved the peak score for accuracy (91.7%) while MIPROv2 yielded the best results for brevity (89.7%) and completeness (88.1%). [→ Ethan Chew 2026 (2)](#ethan-chew-2026-2)

## Evidence

### Ethan Chew 2026

Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319

`q2 · i?` · `design · r2`

Experiments on three communication evaluators (accuracy, brevity, completeness), each DSPy-optimized and trained on labeled examples, evaluated on held-out development sets using inverted MAE; BERTScore F1 was additionally used for brevity. The paper reports compiled scores of 91.7, 89.7, and 88.1%.

> "Table 5 shows prompt optimization improved performance across all evaluators, with the largest gain observed inaccuracy(+7.9%)."

### Ethan Chew 2026 (2)

Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim, Ranen Sim, Brandon Koh, Kaleb Nim, Caden Toh, Wei Dong Soin, Darius Koh, Galen Tay, Prannaya Gupta, Jonathan Koong, Yong Zhi Lim. (2026). ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots. https://arxiv.org/abs/2606.18319

`q2 · i?` · `design · r2`

Comparison of DSPy optimization strategies (Table 6): FewShot, FewShot with Random Search, and MIPROv2. The authors suggest instruction-aware optimization particularly benefits stylistic and multi-parameter assessments, whereas random search excels at calibrating phraseology-based scoring.

> "While RS achieved the peak score foraccuracy,MIPROv2yielded the best re- sults forbrevityandcompleteness."

## Discussion


## Related Claims
-

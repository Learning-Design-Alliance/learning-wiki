---
type: claim
title: In well-trained DNN+HMM face-recognition models, an eyes-focused eye movement pattern yields higher recognition accuracy than a nose-focused pattern
description: In well-trained DNN+HMM face-recognition models, an eyes-focused eye movement pattern yields higher recognition accuracy than a nose-focused pattern
id: well-trained-model-eyes-focused-pattern-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: hsiao-2022
    resource: "https://doi.org/10.1038/s41539-022-00139-6"
    title: "Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B. (2022). Understanding the role of eye movement consistency in face recognition and autism through integrating deep neural networks and hidden Markov models. npj Science of Learning 7:28. https://doi.org/10.1038/s41539-022-00139-6"
    author: "Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B."
    q: 2
    i: 2
    kind: design
    rigour: 2
---

# In well-trained DNN+HMM face-recognition models, an eyes-focused eye movement pattern yields higher recognition accuracy than a nose-focused pattern

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i2` medium
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i2` Well-trained DNN+HMM models with the eyes-focused pattern showed higher face recognition accuracy than nose-focused models (effect size d = 0.75). [→ Hsiao 2022](#hsiao-2022)

## Evidence

### Hsiao 2022

Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B. (2022). Understanding the role of eye movement consistency in face recognition and autism through integrating deep neural networks and hidden Markov models. npj Science of Learning 7:28. https://doi.org/10.1038/s41539-022-00139-6

`q2 · i2` · `design · r2`

Simulation of 80 trained DNN+HMM models on the LFW-a face dataset; representative eye movement patterns were derived by EMHMM clustering. Well-trained (epoch 500) eyes-focused models outperformed nose-focused ones, with printed effect size d = 0.75 and "MA = 0.534, MB = 0.500".

> "In the well-trained models, those with pattern A (eye-focused) exhibited higher accuracy than pattern B (nose-focused), t(78) = 3.33, p = 0.001, d = 0.75, MA = 0.534, MB = 0.500"

## Discussion


## Related Claims
- [In partially trained DNN+HMM models simulating children, eye movement consistency (lower entropy) predicts recognition accuracy but eye movement pattern does not](partially-trained-model-consistency-predicts-accuracy.md) — related
- [In typically developing children aged 6–11, face recognition performance is predicted by eye movement consistency but not by eye movement pattern](children-consistency-not-pattern-predicts-recognition.md) — related
- [A more eyes-focused scanning pattern and higher eye movement consistency are each correlated with better face recognition performance](eyes-focused-pattern-consistency-correlate-better-recognition.md) — related
- [In adults, face recognition performance is predicted by eye movement pattern, with eye movement consistency adding no additional variance](adults-pattern-not-consistency-predicts-recognition.md) — related

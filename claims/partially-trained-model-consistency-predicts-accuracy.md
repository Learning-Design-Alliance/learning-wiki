---
type: claim
title: In partially trained DNN+HMM models simulating children, eye movement consistency (lower entropy) predicts recognition accuracy but eye movement pattern does not
description: In partially trained DNN+HMM models simulating children, eye movement consistency (lower entropy) predicts recognition accuracy but eye movement pattern does not
id: partially-trained-model-consistency-predicts-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: hsiao-2022
    resource: "https://doi.org/10.1038/s41539-022-00139-6"
    title: "Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B. (2022). Understanding the role of eye movement consistency in face recognition and autism through integrating deep neural networks and hidden Markov models. npj Science of Learning 7:28. https://doi.org/10.1038/s41539-022-00139-6"
    author: "Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: hsiao-2022-2
    resource: "https://doi.org/10.1038/s41539-022-00139-6"
    title: "Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B. (2022). Understanding the role of eye movement consistency in face recognition and autism through integrating deep neural networks and hidden Markov models. npj Science of Learning 7:28. https://doi.org/10.1038/s41539-022-00139-6"
    author: "Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In partially trained DNN+HMM models simulating children, eye movement consistency (lower entropy) predicts recognition accuracy but eye movement pattern does not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In partially trained (epoch 100) models, lower HMM entropy was negatively correlated with recognition accuracy. [→ Hsiao 2022](#hsiao-2022)
`q2 i?` In partially trained models, the eyes- vs nose-focused patterns did not differ in validation accuracy and AB scale was not correlated with accuracy. [→ Hsiao 2022 (2)](#hsiao-2022-2)

## Evidence

### Hsiao 2022

Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B. (2022). Understanding the role of eye movement consistency in face recognition and autism through integrating deep neural networks and hidden Markov models. npj Science of Learning 7:28. https://doi.org/10.1038/s41539-022-00139-6

`q2 · i?` · `associational · r2`

Simulation result: among 80 partially trained DNN+HMM models, entropy (a consistency measure) correlated negatively with accuracy; the article prints "p < 0.001 R2 = 0.205" but no standardised effect size.

> "The entropy of partially trained models was negatively correlated with accuracy, p < 0.001 R2 = 0.205"

### Hsiao 2022 (2)

Hsiao, J. H., An, J., Hui, V. K. S., Zheng, Y. & Chan, A. B. (2022). Understanding the role of eye movement consistency in face recognition and autism through integrating deep neural networks and hidden Markov models. npj Science of Learning 7:28. https://doi.org/10.1038/s41539-022-00139-6

`q2 · i?` · `associational · r2`

Simulation: at epoch 100, eyes- and nose-focused representative patterns showed no accuracy difference (d = 0.16, MA = 0.464 vs MB = 0.457); equivalence was not tested. The article also reports "the AB scale was not correlated with accuracy".

> "the patterns A and B of partially trained models did not differ in accuracy on the validation data, t(78) = 0.72, p = 0.475, d = 0.16, MA = 0.464, MB = 0.457"

## Discussion


## Related Claims
- [In typically developing children aged 6–11, face recognition performance is predicted by eye movement consistency but not by eye movement pattern](children-consistency-not-pattern-predicts-recognition.md) — related
- [Children's eye movement consistency is associated with selective attention and executive function, whereas eye movement pattern relates to working memory](eye-movement-consistency-executive-function-children.md) — related
- [A less eyes-focused pattern and lower eye movement consistency jointly predict poorer recognition beyond age and cognitive abilities](eye-movement-pattern-consistency-predict-recognition-beyond-age.md) — related
- [A more eyes-focused scanning pattern and higher eye movement consistency are each correlated with better face recognition performance](eyes-focused-pattern-consistency-correlate-better-recognition.md) — related
- [In adults, face recognition performance is predicted by eye movement pattern, with eye movement consistency adding no additional variance](adults-pattern-not-consistency-predicts-recognition.md) — related
- [In well-trained DNN+HMM face-recognition models, an eyes-focused eye movement pattern yields higher recognition accuracy than a nose-focused pattern](well-trained-model-eyes-focused-pattern-advantage.md) — related

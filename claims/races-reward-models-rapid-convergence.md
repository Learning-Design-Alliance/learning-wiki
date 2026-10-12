---
type: claim
title: "Both reward models converge rapidly, reaching stable Hit@k performance around 200–250 training steps and above-baseline Hit@3 within about 50 steps"
description: "Both reward models converge rapidly, reaching stable Hit@k performance around 200–250 training steps and above-baseline Hit@3 within about 50 steps"
id: races-reward-models-rapid-convergence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: zhenxin-zhang-2026
    resource: "https://doi.org/10.1186/s41239-026-00607-8"
    title: "Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8"
    author: Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Both reward models converge rapidly, reaching stable Hit@k performance around 200–250 training steps and above-baseline Hit@3 within about 50 steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Both reward models reached relatively stable performance around 200–250 training steps, and both obtained relatively high Hit@3 accuracy within approximately 50 training steps, exceeding the random baseline of 50%. [→ Zhenxin Zhang 2026](#zhenxin-zhang-2026)

## Evidence

### Zhenxin Zhang 2026

Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8

`q2 · i?` · `design · r2`

Numerical analysis of Hit@1, Hit@2, and Hit@3 accuracy curves across training iterations (Fig. 3) for the two reward models in the RACES framework, showing convergence "with a limited number of training iterations".

> "both models obtained relatively high Hit@3 accuracy within approximately 50 training steps, exceeding the random baseline of 50%. These results suggest that both reward models converge under the constructed evaluation setting"

## Discussion


## Related Claims
- [Mistral-7B reward model outperforms GPT2-XL on Hit@k ranking and Pairwise Accuracy for proxy preference discrimination, at higher computational cost](mistral-reward-model-beats-gpt2-xl.md) — related

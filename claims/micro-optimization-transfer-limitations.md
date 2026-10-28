---
type: claim
title: Micro-optimization models currently transfer poorly across tasks and contexts, and tight fitting to interface or content creates versioning and transferability issues
description: Micro-optimization models currently transfer poorly across tasks and contexts, and tight fitting to interface or content creates versioning and transferability issues
id: micro-optimization-transfer-limitations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2016
sources:
  - id: nye-2016
    resource: "https://doi.org/10.1007/s40593-016-0098-8"
    title: "Nye, B. D. (2016). ITS, The End of the World as We Know It: Transitioning AIED into a Service-Oriented Ecosystem. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0098-8"
    author: Nye, B. D.
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
  - id: nye-2016-2
    resource: "https://doi.org/10.1007/s40593-016-0098-8"
    title: "Nye, B. D. (2016). ITS, The End of the World as We Know It: Transitioning AIED into a Service-Oriented Ecosystem. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0098-8"
    author: Nye, B. D.
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# Micro-optimization models currently transfer poorly across tasks and contexts, and tight fitting to interface or content creates versioning and transferability issues

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r2`–`r3` · `q1`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The article states that many models for micro-optimization, such as reinforcement learning, have not transferred well to new tasks or contexts, even for the same domain. [→ Nye 2016](#nye-2016)
`q1 i?` Micro-level optimization tightly fits a specific user interface or content and will likely suffer from versioning issues (small problem-element changes potentially invalidating prior data and policies) and transferability issues across contexts such as desktop versus mobile. [→ Nye 2016 (2)](#nye-2016-2)

## Evidence

### Nye 2016

Nye, B. D. (2016). ITS, The End of the World as We Know It: Transitioning AIED into a Service-Oriented Ecosystem. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0098-8

`q1 · i?` · `theoretical · r2`

The author's stated limitation on micro-optimization in the Micro-Adaptation section: such models "have not transferred well to new tasks or contexts," attributed to Chi et al. (2014). This is an interpretive statement about the state of the field, offered without new data.

> "At present, many models for micro-optimization (e.g., reinforcement learning) have not transferred well to new tasks or contexts, even for the same domain (Chi et al., 2014)."

### Nye 2016 (2)

Nye, B. D. (2016). ITS, The End of the World as We Know It: Transitioning AIED into a Service-Oriented Ecosystem. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-016-0098-8

`q1 · i?` · `theoretical · r3`

The author's argument that micro-level optimization "will likely suffer from versioning issues" and transferability issues such as an optimized case "not transferring well from a desktop to a mobile context." The article offers this as a reasoned prediction, not an empirical result.

> "However, micro-level optimization will likely suffer from versioning issues (e.g., changes to small problem elements potentially invalidating prior data and policies) and also transferability issues (e.g., an optimized case not transferring well from a desktop to a mobile context)."

## Discussion


## Related Claims
- [Reinforcement learning used for micro-adaptation showed potential learning gains of up to 1 sigma over poorly-optimized dialog or no dialog (per the article, citing Chi et al. 2014)](reinforcement-learning-micro-adaptation-gains.md) — related
- [An analytical chapter identifies reward hacking, engagement optimization over learning, and scaffolding dependency as risks of RL policies with poorly specified rewards](rl-reward-misalignment-failure-modes.md) — related
- [Help-seeking skill models built from ITS practice data were not transferable across Costa Rican, Philippine, and US contexts (reported by Ogan et al., 2014)](help-seeking-models-not-transferable-across-cultures.md) — a narrower finding that bears on this claim
- [Help-seeking models transfer above chance across sites but perform poorly on the Costa Rican data](help-seeking-model-transfer-mixed.md) — related
- [Automated detectors of disengaged behaviors inferred from interaction-log data alone reached AUC over 0.8 for gaming and correlated 0.55 with observed off-task behavior](sensor-free-disengagement-detectors-accuracy.md) — related

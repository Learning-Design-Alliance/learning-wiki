---
type: claim
title: A micro curriculum with GAN-generated goals solves hard Fetch push, slide and pick-and-place variants on which HER fails to learn, without resetting to arbitrary states or using expert actions
description: A micro curriculum with GAN-generated goals solves hard Fetch push, slide and pick-and-place variants on which HER fails to learn, without resetting to arbitrary states or using expert actions
id: micmic-micro-curriculum-solves-hard-fetch-tasks-her-fails
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2019
sources:
  - id: manan-tomar-2019
    resource: "https://doi.org/10.1609/aaai.v33i01.330110053"
    title: "Manan Tomar, Akhil Sathuluri, Balaraman Ravindran. (2019). MaMiC: Macro and Micro Curriculum for Robotic Reinforcement Learning. Proc. of the 18th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2019). [doi:10.1609/aaai.v33i01.330110053](https://doi.org/10.1609/aaai.v33i01.330110053)"
    author: Manan Tomar, Akhil Sathuluri, Balaraman Ravindran
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A micro curriculum with GAN-generated goals solves hard Fetch push, slide and pick-and-place variants on which HER fails to learn, without resetting to arbitrary states or using expert actions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On push-hard and slide-hard Fetch tasks, HER is unable to even learn to reach the object, while the micro scheme gradually learns to reach and push/slide to generated goals and then to target goals. [→ Manan Tomar 2019](#manan-tomar-2019)
`q2 i?` The micro scheme learns optimal policies for all three Fetch tasks considered (push-hard, slide-hard, pick-and-place). [→ Manan Tomar 2019](#manan-tomar-2019)

## Evidence

### Manan Tomar 2019

Manan Tomar, Akhil Sathuluri, Balaraman Ravindran. (2019). MaMiC: Macro and Micro Curriculum for Robotic Reinforcement Learning. Proc. of the 18th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2019). [doi:10.1609/aaai.v33i01.330110053](https://doi.org/10.1609/aaai.v33i01.330110053)

`q2 · i?` · `causal · r2`

Simulation study on Mujoco Fetch environments (Fig. 3) comparing the micro curriculum against HER, the state-of-the-art algorithm on these domains, with no episode starting from a solved state. The paper reports: "For push-hard and slide-hard tasks, HER is unable to even learn to reach the object as shown in Fig 3."

> "On the other hand, following the micro scheme, we are able to gradually start learning to reach and push / slide the object to nearby generated goals and then gain expertise with respect to the target goals."

## Discussion


## Related Claims
-

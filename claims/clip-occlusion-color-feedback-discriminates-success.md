---
type: claim
title: "Clip-occlusion simulation distinguishes failed partial occlusion, where the dilation's fluid changes color, from complete occlusion, where the fluid inside stays blue"
description: "Clip-occlusion simulation distinguishes failed partial occlusion, where the dilation's fluid changes color, from complete occlusion, where the fluid inside stays blue"
id: clip-occlusion-color-feedback-discriminates-success
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-09
evidence_strength: moderate
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: liu-yu-2017
    resource: "https://doi.org/10.1038/srep44301"
    title: "Liu Yu, Gao Qing, Du Song, Chen ZiChen, Fu JianZhong, Chen Bing, Liu ZhenJie, He Yong. (2017). Fabrication of cerebral aneurysm simulator with a desktop 3D printer. Scientific Reports 7, 44301. https://doi.org/10.1038/srep44301"
    author: Liu Yu, Gao Qing, Du Song, Chen ZiChen, Fu JianZhong, Chen Bing, Liu ZhenJie, He Yong
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: liu-yu-2017-2
    resource: "https://doi.org/10.1038/srep44301"
    title: "Liu Yu, Gao Qing, Du Song, Chen ZiChen, Fu JianZhong, Chen Bing, Liu ZhenJie, He Yong. (2017). Fabrication of cerebral aneurysm simulator with a desktop 3D printer. Scientific Reports 7, 44301. https://doi.org/10.1038/srep44301"
    author: Liu Yu, Gao Qing, Du Song, Chen ZiChen, Fu JianZhong, Chen Bing, Liu ZhenJie, He Yong
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Clip-occlusion simulation distinguishes failed partial occlusion, where the dilation's fluid changes color, from complete occlusion, where the fluid inside stays blue

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Deliberately clipping only two thirds of the dilation, leaving a small hole, lets the fluid inside change color, which the article labels the failing case. [→ Liu Yu 2017](#liu-yu-2017)
`q2 i?` Clipping the whole blister-like dilation keeps the fluid inside it blue while the surrounding vascular fluid changes color, which the article labels the successful case. [→ Liu Yu 2017 (2)](#liu-yu-2017-2)

## Evidence

### Liu Yu 2017

Liu Yu, Gao Qing, Du Song, Chen ZiChen, Fu JianZhong, Chen Bing, Liu ZhenJie, He Yong. (2017). Fabrication of cerebral aneurysm simulator with a desktop 3D printer. Scientific Reports 7, 44301. https://doi.org/10.1038/srep44301

`q2 · i?` · `design · r2`

Deliberate failed-occlusion trial in the Results section: clips occlude 'two thirds of the blister-like dilation, leaving a small hole', the fluid inside 'changes colors from blue to green and then yellow', and the article labels this 'the failing case'.

> "We also can observe that the fluid of the blister-like dilation's inside changes colors from blue to green and then yellow. The simulation of the second group shows the failing case that applied aneurysm clips to occlude the blister-like dilation."

### Liu Yu 2017 (2)

Liu Yu, Gao Qing, Du Song, Chen ZiChen, Fu JianZhong, Chen Bing, Liu ZhenJie, He Yong. (2017). Fabrication of cerebral aneurysm simulator with a desktop 3D printer. Scientific Reports 7, 44301. https://doi.org/10.1038/srep44301

`q2 · i?` · `design · r2`

Results-section demonstration: yellow fluid perfuses the vascular model — 'The fluid of the vascular inside changes colors from blue to green and then yellow' — while 'the blister-like dilation's inside don't change the color which is blue', marking the successful complete occlusion.

> "The fluid of the vascular inside changes colors from blue to green and then yellow. But the fluid of the blister-like dilation's inside don't change the color which is blue."

## Discussion


## Related Claims
- [Existing aneurysm clipping training methods are heterogeneous and do not realistically simulate the complete microsurgical workflow](simulation-methods-incomplete-microsurgical-workflow.md) — related

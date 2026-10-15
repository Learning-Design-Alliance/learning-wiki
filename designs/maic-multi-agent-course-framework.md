---
type: design
id: maic-multi-agent-course-framework
title: "MAIC: an LLM-driven multi-agent online course framework balancing scalability and adaptivity"
description: MAIC (Massive AI-empowered Course) is a proposed form of online education in which instructors upload slides and LLM-driven agents prepare structured lecture resources, then deliver classes through a teacher agent, te...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: jifan-yu-2024
    resource: "https://arxiv.org/abs/2409.03512"
    title: "Jifan Yu, Zheyuan Zhang, Daniel Zhang-li, Shangqing Tu, Zhanxin Hao, Ruimiao Li, Haoxuan Li, Yuanchun Wang, Hanming Li, Linlu Gong, Jie Cao, Jiayin Lin, Jinchang Zhou, Fei Qin, Haohua Wang, Jianxiao Jiang, Lijun Deng, Yisi Zhan, Chaojun Xiao, Xusheng Dai, Xuan Yan, Nianyi Lin, Nan Zhang, Ruixin Ni, Yang Dang, Lei Hou, Yu Zhang, Xu Han, Manli Li, Juanzi Li, Zhiyuan Liu, Huiqin Liu, Maosong Sun. (2024). From MOOC to MAIC: Reshaping Online Teaching and Learning through LLM-driven Agents. Preprint. Under review. https://arxiv.org/abs/2409.03512"
    author: Jifan Yu, Zheyuan Zhang, Daniel Zhang-li, Shangqing Tu, Zhanxin Hao, Ruimiao Li, Haoxuan Li, Yuanchun Wang, Hanming Li, Linlu Gong, Jie Cao, Jiayin Lin, Jinchang Zhou, Fei Qin, Haohua Wang, Jianxiao Jiang, Lijun Deng, Yisi Zhan, Chaojun Xiao, Xusheng Dai, Xuan Yan, Nianyi Lin, Nan Zhang, Ruixin Ni, Yang Dang, Lei Hou, Yu Zhang, Xu Han, Manli Li, Juanzi Li, Zhiyuan Liu, Huiqin Liu, Maosong Sun
---

# MAIC: an LLM-driven multi-agent online course framework balancing scalability and adaptivity

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
MAIC (Massive AI-empowered Course) is a proposed form of online education in which instructors upload slides and LLM-driven agents prepare structured lecture resources, then deliver classes through a teacher agent, teaching assistant agent, and customizable classmate agents. The article frames it as balancing the scalability of MOOCs with adaptivity: 'a new form of online education that leverages LLM-driven multi-agent systems to construct an AI-augmented classroom, balancing scalability with adaptivity.' Classroom interactions are organized around four behavior categories — Teaching and Initiation, In-depth Discussion, Emotional Companionship, and Classroom Management — orchestrated by a Session Controller with a Class State Receptor and Manager Agent.

## Design Implications

### Context
#### Requirements
- Instructors must upload course slides and proofread and refine generated scripts and agents before class
#### Constraints
- The authors state the reported assessments 'provide only an initial view of specific aspects of MAIC rather than its overall effectiveness'

### Target Learners
- university students in online courses

### Learning Goals
- domain knowledge acquisition
- personalized adaptive learning
- student engagement

### Claims

- [Students in MAIC tend to prefer the passive continuous mode over interactive mode](../claims/students-prefer-continuous-mode.md) [+W]
- [Students reported significant perceived gains in abstract and critical thinking, with other higher-order thinking effects ambiguous](../claims/perceived-higher-order-thinking-gains.md) [+W]
- [MAIC's script generation function outscores baseline and human script generation on five Likert-rated dimensions](../claims/maic-funcgen-outperforms-baselines.md) [+W]

## Related Designs

- [Multi-agent teacher-in-the-loop architecture for context personalization](multi-agent-teacher-in-the-loop-architecture.md)

## Examples
-

## Key Sources
- Jifan Yu, Zheyuan Zhang, Daniel Zhang-li, Shangqing Tu, Zhanxin Hao, Ruimiao Li, Haoxuan Li, Yuanchun Wang, Hanming Li, Linlu Gong, Jie Cao, Jiayin Lin, Jinchang Zhou, Fei Qin, Haohua Wang, Jianxiao Jiang, Lijun Deng, Yisi Zhan, Chaojun Xiao, Xusheng Dai, Xuan Yan, Nianyi Lin, Nan Zhang, Ruixin Ni, Yang Dang, Lei Hou, Yu Zhang, Xu Han, Manli Li, Juanzi Li, Zhiyuan Liu, Huiqin Liu, Maosong Sun. (2024). From MOOC to MAIC: Reshaping Online Teaching and Learning through LLM-driven Agents. Preprint. Under review. https://arxiv.org/abs/2409.03512

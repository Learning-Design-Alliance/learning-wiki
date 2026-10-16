---
type: design
id: domain-grounded-mediation-llm-vr-instruction
title: Domain-grounded mediation framework for LLM-assisted VR instruction
description: "The article frames LLM-assisted VR instruction as a mediation process connecting three layers: expert expression, executable operations, and learner-facing representations."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: danxuan-liang-2026
    resource: "https://arxiv.org/abs/2609.17335"
    title: "Danxuan Liang, Chun Yin Li, Zheng Wei, Xian Xu, Meng Xia, Huamin Qu, Wai Tong. (2026). LumiNote: LLM-Assisted Multimodal Instruction for VR Stage Lighting Education. https://arxiv.org/abs/2609.17335"
    author: Danxuan Liang, Chun Yin Li, Zheng Wei, Xian Xu, Meng Xia, Huamin Qu, Wai Tong
---

# Domain-grounded mediation framework for LLM-assisted VR instruction

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article frames LLM-assisted VR instruction as a mediation process connecting three layers: expert expression, executable operations, and learner-facing representations. The authors state that their findings characterize LLM-assisted VR instruction as a "domain-grounded mediation process among expert expression, executable operations, and learner-facing representations." In this framework, an instructor's high-level pedagogical intent must be translated into concrete scene manipulations while simultaneously being made understandable to learners. Technical executability alone is insufficient because generated actions must remain inspectable and controllable by the instructor.

## Design Implications

### Context
#### Requirements
- An instructor-facing system that translates pedagogical intent into executable actions within a domain-specific VR environment
- Domain knowledge integration into LLM prompting to constrain generation to valid operations
#### Constraints
- Focused on instructor-facing live concept delivery rather than dynamic student interaction
- Generated actions require instructor review and approval before execution

### Target Learners
- Stage lighting instructors
- Beginner-level technical theater arts students

### Learning Goals
- Understanding spatial lighting relationships
- Connecting technical operations with visual effects
- Acquiring domain-specific terminology

### Claims

- [LLM assistance shifts instructor effort from manual setup toward pedagogical expression](../claims/llm-assistance-shifts-effort-toward-pedagogical-expression.md) [+W]
- [Representation-alignment tension between expert externalization and novice comprehension](../claims/representation-alignment-tension-expert-novice.md) [~W]

## Related Designs

- [Three pedagogical expression strategies for VR lighting instruction](three-pedagogical-expression-strategies-vr-lighting.md)

## Examples
-

## Key Sources
- Danxuan Liang, Chun Yin Li, Zheng Wei, Xian Xu, Meng Xia, Huamin Qu, Wai Tong. (2026). LumiNote: LLM-Assisted Multimodal Instruction for VR Stage Lighting Education. https://arxiv.org/abs/2609.17335

---
type: product
id: adapt
title: AdaPT
description: AdaPT is a Vue.js and TypeScript NestJS web application developed by Yanjie Zhang and colleagues that structures existing lesson plans, analyzes student learning profiles, and supports teacher-in-the-loop adaptation for differentiated K–12 instruction.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# AdaPT

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
AdaPT is a Vue.js and TypeScript NestJS web application developed by Yanjie Zhang and colleagues that structures existing lesson plans, analyzes student learning profiles, and supports teacher-in-the-loop adaptation for differentiated K–12 instruction.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Multi-agent backend with LessonPlan Agent and LearningProfile Analysis Agent providing traceable transformations**: AdaPT's backend is a multi-agent system in which each agent encapsulates distinct reasoning responsibilities. The LessonPlan Agent parses uploaded plans into schema-conformant components (using RAG over a tree-structured knowledge graph of national curriculum standards) and transforms them by recalibrating objectives and iteratively adjusting tasks. The LearningProfile Analysis Agent generates structured profiles from teacher natural-language descriptions, optionally retrieving knowledge readiness from the school's LMS via tool-calling. The authors state "The backend of AdaPT is designed as a multi-agent system (Figure 5), where each agent encapsulates distinct reasoning responsibilities aligned with the design requirements." Outputs are schema-validated JSON with references and localized reasons for traceability. (Yanjie Zhang et al. (2026))

### Claims
- [A formative study with six teachers and two experts identified five core challenges in lesson plan adaptation, including lack of systematic student profile data and fragmented refinement workflows](../claims/five-challenges-lesson-plan-adaptation.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Yanjie Zhang, Jiajun Zhu, Minyu Wu, Huamin Qu, and Sicheng Song. (2026). AdaPT: Adaptive Lesson Plan Transformer for Cross-Regional and Differentiated Instruction. https://arxiv.org/abs/2606.17633

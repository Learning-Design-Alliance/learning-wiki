---
type: product
id: kite-knowledge-informed-tutoring-engine
title: KITE (Knowledge-Informed Tutoring Engine)
description: KITE is a course-grounded intelligent tutoring system developed by Mragisha Jain et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# KITE (Knowledge-Informed Tutoring Engine)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
KITE is a course-grounded intelligent tutoring system developed by Mragisha Jain et al. that combines multi-stage retrieval with intent-routed pedagogical response strategies for algorithmic reasoning instruction.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **KITE: an intent-aware RAG tutoring architecture combining multi-stage retrieval with pedagogical response strategies**: KITE (Knowledge-Informed Tutoring Engine) is a RAG-based intelligent tutoring system for course-grounded dialogue on algorithmic reasoning and problem-solving. As the article states, "the system includes five components: document preprocessing, embedding generation, multi-stage retrieval, intent-aware response generation, and session management." Each query is classified by pedagogical intent, and the classified intent determines the response strategy: grounded explanations for direct and conceptual questions, Socratic assessment for validation, diagnostic hint progressions for debugging, and step-by-step state-tracing for algorithm tracing. Retrieval combines dense bi-encoder search, hybrid scoring (70% dense, 30% BM25), MMR with λ = 0.7, cross-encoder reranking, and source-based boosting, passing the top eight chunks to GPT-5. (Mragisha Jain et al. (2026))

### Claims

- [KITE's non-procedural responses show strong retrieval grounding (faithfulness 0.85, context relevance 0.94) and answer similarity 0.76, with lower factual correctness 0.45](../claims/kite-strong-grounding-lower-factual-correctness.md) [+M]
- [KITE's feedback led simulated students to improve revised answers in 24 of 27 non-already-correct interactions (88.89%)](../claims/kite-feedback-improves-simulated-student-revisions.md) [+M]
- [Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient](../claims/evidence-tracing-114-claims-retrieval-limit.md) [~W]
- [Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower](../claims/rq-higher-relevancy-lower-grounding.md) [~W]

## Related Products and Programmes
-

## Key Sources
- Mragisha Jain, Tirth Bhatt, Griffin Pitts, Aum Pandya, Peter Brusilovsky, Narges Norouzi, Arto Hellas, Juho Leinonen, Bita Akram. (2026). Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education. Proceedings of the 21st Workshop on Innovative Use of NLP for Building Educational Applications (BEA 2026), co-located with ACL 2026. https://arxiv.org/abs/2605.12988

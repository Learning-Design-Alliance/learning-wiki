---
type: claim
title: Learned question embeddings capture question difficulty rather than clustering exercises by concept
description: Learned question embeddings capture question difficulty rather than clustering exercises by concept
id: question-embeddings-capture-difficulty-not-concepts
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: weak
sources:
  - id: ritwick-chaudhry-2017
    resource: "https://educationaldatamining.org/"
    title: "Ritwick Chaudhry, Harvineet Singh, Pradeep Dogga, and Shiv Kumar Saini. (2017). Modeling Hint-Taking Behavior and Knowledge State of Students with Multi-Task Learning. Proceedings of the 11th International Conference on Educational Data Mining. https://educationaldatamining.org/"
    author: Ritwick Chaudhry, Harvineet Singh, Pradeep Dogga, and Shiv Kumar Saini
    q: 2
    i: "?"
---

# Learned question embeddings capture question difficulty rather than clustering exercises by concept

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` t-SNE visualization of Junyi question representations shows a difficulty gradient but no clustering by concept. [→ Ritwick Chaudhry 2017](#ritwick-chaudhry-2017)

## Evidence

### Ritwick Chaudhry 2017

Ritwick Chaudhry, Harvineet Singh, Pradeep Dogga, and Shiv Kumar Saini. (2017). Modeling Hint-Taking Behavior and Knowledge State of Students with Multi-Task Learning. Proceedings of the 11th International Conference on Educational Data Mining. https://educationaldatamining.org/

`q2 · i?`

t-SNE visualization analysis of question representations for the Junyi dataset (Figure 4a/4b), colored by difficulty and by concept. The text reports exercise tags within a concept "do not cluster together" and seem randomly scattered.

> "On the other hand the color of the exercise tags in Figure 4a shows a deﬁnite pattern with the easiest question tags towards the left and the most diﬃcult ones towards the right. This shows that the question representation vectors tend to capture the diﬃculty level of an exercise tag."

## Discussion


## Related Claims
- [The learned question embedding aligns with manually labeled skill categories, showing clear clustering of questions by skill in a multidimensional scaling visualization](dynemb-question-embedding-clusters-by-skill.md) — reports the opposite
- [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags](dynemb-tracks-knowledge-without-skill-tags.md) — related

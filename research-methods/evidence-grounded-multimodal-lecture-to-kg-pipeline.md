---
type: research-method
id: evidence-grounded-multimodal-lecture-to-kg-pipeline
title: Evidence-grounded multimodal lecture-to-KG pipeline
description: "An end-to-end pipeline combining \"timestamped automatic speech recognition (ASR), high-recall anchor selection, OCR, grounded vision-language extraction, validation, canonicalization, KG construction, and GraphRAG-style retrieval.\" Its design constraint is that \"a concept or relationship is promoted"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Evidence-grounded multimodal lecture-to-KG pipeline

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An end-to-end pipeline combining "timestamped automatic speech recognition (ASR), high-recall anchor selection, OCR, grounded vision-language extraction, validation, canonicalization, KG construction, and GraphRAG-style retrieval." Its design constraint is that "a concept or relationship is promoted only when tied to lecture evidence." Unlike slide- or transcript-only educational KG pipelines, it treats video frames, OCR output, and transcript segments as three simultaneous evidence sources for the same anchor, capturing diagram- and equation-only content. The output is a NetworkX MultiDiGraph whose edges carry relation type, lecture, timestamp, anchor, evidence quotation, and confidence.

## Accounts
<!-- How each source describes or uses the method -->
- **Evidence-grounded multimodal lecture-to-KG pipeline**: An end-to-end pipeline combining "timestamped automatic speech recognition (ASR), high-recall anchor selection, OCR, grounded vision-language extraction, validation, canonicalization, KG construction, and GraphRAG-style retrieval." Its design constraint is that "a concept or relationship is promoted only when tied to lecture evidence." Unlike slide- or transcript-only educational KG pipelines, it treats video frames, OCR output, and transcript segments as three simultaneous evidence sources for the same anchor, capturing diagram- and equation-only content. The output is a NetworkX MultiDiGraph whose edges carry relation type, lecture, timestamp, anchor, evidence quotation, and confidence. (Sahil Al Farib et al. (2026))

### Claims
- [Across three neural-network lectures, evidence and confidence checks retained 1,022 of 1,155 raw concept mentions (88.48%) and 312 of 400 raw relationship mentions (78.00%), yielding 172 canonical concepts and 282 graph relationships with 90.38% endpoint coverage](../claims/evidence-grounded-kg-extraction-yield-three-lectures.md) [+M]
- [On a preliminary three-question retrieval sanity check, all seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00](../claims/three-seed-retrieval-sanity-check-perfect.md) [+M]

## Related Research Methods

- [Evidence-grounding extraction schema for auditable educational knowledge graphs](evidence-grounding-extraction-schema-for-auditable-educational-knowledge-graphs.md)

## Key Sources
- Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, and Md. Tanvir Raihan. (2026). Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning. https://arxiv.org/abs/2608.03161

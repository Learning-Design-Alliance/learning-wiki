---
type: design
id: psychologically-aware-multimodal-conversational-agent
title: Psychologically-aware multimodal conversational agent (Falcon-7B + KG-BERT + BiLSTM-attention fusion)
description: An educational conversational agent that fuses LLM-based semantic reasoning with knowledge-graph contextualization and prosodic emotion detection to monitor four student states (engagement, stress, motivation, concept...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: ben-chaabene-2026
    resource: "https://arxiv.org/abs/2512.10441"
    title: "Ben Chaabene, N.E.H., Hammami, H., Kahloul, L. (2026). Decoding Student Minds: Leveraging Conversational Agents for Psychological and Learning Analysis. arXiv preprint. https://arxiv.org/abs/2512.10441"
    author: Ben Chaabene, N.E.H., Hammami, H., Kahloul, L
---

# Psychologically-aware multimodal conversational agent (Falcon-7B + KG-BERT + BiLSTM-attention fusion)

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An educational conversational agent that fuses LLM-based semantic reasoning with knowledge-graph contextualization and prosodic emotion detection to monitor four student states (engagement, stress, motivation, conceptual understanding) in real time. Falcon-7B encodes utterances; KG-BERT scores triples from a 486-node, 1,240-edge course knowledge graph and converts top-ranked triples into structured prompts reintegrated into Falcon-7B's prompt window; a two-layer BiLSTM with additive attention performs early fusion of text and prosodic features. The article describes it as enabling "joint reasoning across symbolic (graph-based) and sub-symbolic (embedding-based) representations".

## Design Implications

### Context
#### Requirements
- Weekly psychometric self-reports (PSS, STAI, AMS) plus trained-assistant behavioral annotation to supply ground-truth labels
- A domain-specific knowledge graph scoped to the target curriculum, semi-automatically built and manually validated
#### Constraints
- Only 30% of pilot interactions included spoken input, limiting prosodic generalization
- Pilot deployment was single-course, single-institution with N=45

### Target Learners
- undergraduate students in an introductory programming course

### Learning Goals
- monitoring and supporting engagement, stress regulation, motivation, and conceptual understanding during learning

### Claims
- [Multimodal Fusion Outperforms Unimodal Baselines](../claims/multimodal-fusion-outperforms-unimodal-baselines.md) [+M]
- [Kg Bert Ablation Gain](../claims/kg-bert-ablation-gain.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ben Chaabene, N.E.H., Hammami, H., Kahloul, L. (2026). Decoding Student Minds: Leveraging Conversational Agents for Psychological and Learning Analysis. arXiv preprint. https://arxiv.org/abs/2512.10441

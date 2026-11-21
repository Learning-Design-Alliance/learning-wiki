---
type: strategy
id: human-llm-collaborative-annotation-framework-t-med
title: Six-step human-LLM collaborative annotation framework for large-scale emotion dataset construction
description: "The article describes \"a novel human-machine collaboration annotation collaborative framework\" that \"integrates iterative model refinement and expert oversight across six sequential steps\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: zhiyi-duan-2025
    resource: "https://arxiv.org/abs/2512.20548"
    title: "Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2025). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. https://arxiv.org/abs/2512.20548"
    author: Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing
---

# Six-step human-LLM collaborative annotation framework for large-scale emotion dataset construction

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article describes "a novel human-machine collaboration annotation collaborative framework" that "integrates iterative model refinement and expert oversight across six sequential steps". A small pilot subset (10% of the corpus) is pre-labeled by a pre-trained model, corrected by three experts to build a seed set, used to fine-tune the model, which then labels the full corpus, and a final independent panel of five experts reviews all annotations under a strict voting criterion. This reduces manual annotation burden while maintaining label reliability.

## Design Implications

### Context
#### Requirements
- Access to a pre-trained emotion model (emotion2vec-large) for pilot annotation and fine-tuning
- Expert panels for pilot correction and independent final review
#### Constraints
- Data failing the voting criterion (fewer than four experts confirming a label) is discarded

### Target Learners
- Researchers constructing educational affect datasets from classroom recordings

### Target Learning Goals
- Accurate and efficient labeling of teacher emotions at scale

## Claims

- [The human-refined framework improved human agreement substantially but produced only modest gains for ICL-based LLM annotation](../claims/human-refined-framework-gains-humans-not-llms.md) [+W]
- [Agent-refined frameworks improved cross-model agreement but remained below the human-refined framework and varied across foundation models](../claims/agent-refined-frameworks-below-human-refined.md) [~W]
- [Machine–machine agreement exceeds human–machine agreement but remains below human–human agreement](../claims/machine-machine-above-human-machine-below-human-human.md) [~W]

## Related Strategies

- T Med Teacher Multimodal Sentiment Dataset
- [Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling](instruction-guided-llm-annotation-interaction-labels.md)
- [Use iterative prompt engineering mirroring human coders' labeling processes to refine LLM classification prompts](iterative-prompt-engineering-mirroring-human-coder-refinement.md)
- [Future directions: fine-tuning on human-refined frameworks and hybrid human–LLM or multi-agent annotation systems](future-hybrid-human-llm-annotation-systems.md)

## Examples
-

## Key Sources
- Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2025). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. https://arxiv.org/abs/2512.20548

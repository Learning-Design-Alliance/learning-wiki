---
type: strategy
id: hybrid-ai-generation-expert-calibration-strategy
title: Implement hybrid AI-generation with expert calibration for examination production
description: "The article recommends immediate adoption of hybrid \"AI-generation/expert-calibration\" models in dental education assessment, bridging formative feedback enabled by AI efficiency with summative rigor supplied by human..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
sources:
  - id: ma-xiang-2025
    resource: "https://doi.org/10.1186/s12909-025-07706-6"
    title: "Ma Xiang, Pan Wei, Yu Xiao-ning. (2025). Evaluating AI-generated examination papers in periodontology: a comparative study with human-designed counterparts. BMC Medical Education. https://doi.org/10.1186/s12909-025-07706-6"
    author: Ma Xiang, Pan Wei, Yu Xiao-ning
---

# Implement hybrid AI-generation with expert calibration for examination production

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (3 for, 3 against) · 2 studies (1 causal, 1 design), `q3` · 1 of 2 report an effect size · 5 claims rest on one study

## Description
The article recommends immediate adoption of hybrid "AI-generation/expert-calibration" models in dental education assessment, bridging formative feedback enabled by AI efficiency with summative rigor supplied by human expertise. Future work should develop AI pre-screening followed by expert refinement with knowledge graph-enhanced distractor complexity, and constrain item parameters during generation. The strategy directly targets the study's findings on breadth gains and discrimination shortfalls.

## Design Implications

### Context
#### Requirements
- expert refinement step after AI pre-screening of generated items
- knowledge graph augmentation to optimize item generation algorithms
#### Constraints
- the study's sample came from a single medical school in a simulated test environment, which may not reflect high-stakes assessment performance
- AI item design must balance cognitive friendliness with clinical authenticity

### Target Learners
- undergraduate dental students in periodontology courses

### Target Learning Goals
- foundational knowledge testing and clinical reasoning assessment in periodontology

### Affordances
- [Hybrid Ai Human Collaborative Generation Framework](../designs/hybrid-ai-human-collaborative-generation-framework.md)

## Claims

- [The AI-generated and human-designed examinations showed comparable split-half reliability and difficulty distributions](../claims/ai-exam-comparable-reliability-difficulty.md) [+W]
- [A GPT-4-generated periodontology examination achieved higher syllabus content coverage than a human-designed examination (81.3% vs. 72.4%)](../claims/ai-exam-higher-content-coverage-periodontology.md) [+W]
- [Students scored significantly higher on the AI-generated examination than on the human-designed examination, with a narrower score range](../claims/ai-exam-higher-total-scores.md) [+W]
- [AI-generated examination questions showed significantly lower item discrimination than human-designed ones in two studies (0.35 vs 0.49; 0.28 vs 0.42)](../claims/ai-exam-lower-discrimination.md) [-W]
- [AI-generated X-type questions were easier than human-designed X-type questions (difficulty 0.77 vs. 0.62)](../claims/ai-x-type-questions-easier.md) [-W]
- [Students rated the AI-generated examination significantly lower on difficulty adaptability, knowledge coverage, and learning inspiration](../claims/students-rate-ai-exam-lower-feedback.md) [-W]

## Related Strategies

- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)
- [Use AI-based assessment periodically for formative feedback while avoiding AI in summative assessment](ai-formative-not-summative-assessment-strategy.md)
- [Use LLMs in supervised settings to generate formative question variants and structured self-assessments for surgical trainees, while guarding against knowledge miscalibration.](supervised-llm-formative-question-generation-surgical-training.md)
- [Phased implementation of AI assessment starting with root opportunities in low-stakes settings](phased-ai-assessment-implementation-roadmap.md)
- [Use LLMs as faculty-supervised adjuncts for automated MCQ pretesting and formative feedback](llm-faculty-supervised-mcq-pretesting-feedback.md)

## Examples
-

## Key Sources
- Ma Xiang, Pan Wei, Yu Xiao-ning. (2025). Evaluating AI-generated examination papers in periodontology: a comparative study with human-designed counterparts. BMC Medical Education. https://doi.org/10.1186/s12909-025-07706-6

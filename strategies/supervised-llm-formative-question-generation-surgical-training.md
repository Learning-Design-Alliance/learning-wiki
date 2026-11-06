---
type: strategy
id: supervised-llm-formative-question-generation-surgical-training
title: Use LLMs in supervised settings to generate formative question variants and structured self-assessments for surgical trainees, while guarding against knowledge miscalibration.
description: "The article supports a cautious educational role for LLMs in postgraduate surgical training: \"models with stable behaviour may be used in supervised settings to generate formative question variants or structured self-..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
sources:
  - id: güler-ibrahim-2026
    resource: "https://doi.org/10.1177/17531934261436305"
    title: "Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305"
    author: Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik
---

# Use LLMs in supervised settings to generate formative question variants and structured self-assessments for surgical trainees, while guarding against knowledge miscalibration.

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article supports a cautious educational role for LLMs in postgraduate surgical training: "models with stable behaviour may be used in supervised settings to generate formative question variants or structured self-assessments". However, it warns that high accuracy on fundamental concepts combined with systematic deficits in subspecialty depth may lead trainees to overestimate both model reliability and their own level of understanding, particularly when LLMs are perceived as surrogate supervisors rather than supplementary learning tools.

## Design Implications

### Context
#### Requirements
- Supervised settings with specialist review of LLM-generated formative materials
- Framing LLMs as supplementary learning tools rather than surrogate supervisors to avoid trainee knowledge miscalibration
#### Constraints
- High accuracy on fundamental concepts combined with systematic deficits in subspecialty depth may lead trainees to overestimate both model reliability and their own level of understanding
- The increasing use of LLMs for clinical documentation introduces additional medico-legal considerations requiring cautious integration and continued expert review

### Target Learners
- Postgraduate surgical trainees preparing for specialty certification examinations
- Medical educators designing formative assessment materials

### Target Learning Goals
- Knowledge consolidation and question validation in hand surgery training
- Accurate self-assessment and confidence calibration in trainees using AI-assisted learning

## Claims

- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](../claims/llm-ebhs-exam-accuracy-range-72-85-percent.md) [+W]
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](../claims/llm-ebhs-inter-run-reliability-high-kappa-0821.md) [+W]
- [A small subset of EBHS examination questions produced incorrect responses across most or all LLMs, concentrated in specialized domains including rare congenital anomalies, European-specific practice patterns, historical terminology and eponyms, and complex reconstructions.](../claims/llm-ebhs-persistent-subspecialty-knowledge-gaps.md) [~W]
- [Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.](../claims/proprietary-llms-outperform-open-source-ebhs.md) [+W]

## Related Strategies

- [Augment LLMs with retrieval-augmented generation using authoritative subspecialty resources to address remaining knowledge gaps on board-style examinations.](rag-subspecialty-resources-llm-knowledge-gaps.md)
- [Use LLMs cautiously as supplementary learning tools in dental education, with output verification and professional supervision](cautious-llm-supplementary-tools-dental-education.md)
- [Frame LLM use in biomedical education around low‐stakes formative tasks with expert‐guided verification and rationale requests](llm-low-stakes-formative-use-expert-verification-strategy.md)
- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)
- [Future work should evaluate LLM performance on Part B, viva-style and clinical scenario assessments and study effects on trainee learning outcomes](future-llm-evaluation-part-b-viva-learning-outcomes.md)
- [Integrate AI chatbots into dental education as supervised supplementary tools for exam preparation and formative self-assessment](supervised-chatbot-supplementary-dental-education.md)
- [Use LLMs as faculty-supervised adjuncts for automated MCQ pretesting and formative feedback](llm-faculty-supervised-mcq-pretesting-feedback.md)
- [Implement hybrid AI-generation with expert calibration for examination production](hybrid-ai-generation-expert-calibration-strategy.md)

## Examples
-

## Key Sources
- Güler Ibrahim, Muir Lindsay, Grieb Gerrit, Moog Philipp, Kraus Armin, Stelling Henrik. (2026). Performance and reliability of large language models on the European Board of Hand Surgery examination: a multi-model evaluation study. The Journal of Hand Surgery, European Volume. https://doi.org/10.1177/17531934261436305

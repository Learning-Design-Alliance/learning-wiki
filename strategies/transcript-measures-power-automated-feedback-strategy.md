---
type: strategy
id: transcript-measures-power-automated-feedback-strategy
title: Use transcript-based discourse measures to power automated teacher feedback and professional development improvements
description: "The article recommends applying measures built on the NCTE data to improve instruction: \"Measures built on this data can power automated feedback tools and enable empirically-driven improvements to widely used profess..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: dorottya-demszky-and-heather-hill-2022
    resource: "https://arxiv.org/abs/2211.11772"
    title: "Dorottya Demszky and Heather Hill. (2022). The NCTE Transcripts: A Dataset of Elementary Math Classroom Transcripts. https://arxiv.org/abs/2211.11772"
    author: Dorottya Demszky and Heather Hill
---

# Use transcript-based discourse measures to power automated teacher feedback and professional development improvements

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 against) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The article recommends applying measures built on the NCTE data to improve instruction: "Measures built on this data can power automated feedback tools and enable empirically-driven improvements to widely used professional development frameworks". The authors also suggest randomly assigning teachers to learning opportunities that improve their discourse moves and examining downstream impacts on student outcomes, and building new NLP measures incorporating lesson-level metadata and broader context.

## Design Implications

### Context
#### Requirements
- Measures must be validated on new domains to ensure representativeness of the target population
#### Constraints
- Experimental validation of the discourse-move to outcome link in a K-12 context has not yet been done

### Target Learners
- K-12 mathematics teachers

### Target Learning Goals
- Improving dialogic instructional practices and addressing pandemic learning loss and equity gaps

## Claims

- [Dialogic discourse moves (uptake, focusing questions, student reasoning) correlate positively with teachers' value-added scores](../claims/dialogic-moves-correlate-value-added.md) [+W]
- [All classifier-predicted discourse features correlate significantly with classroom observation scores measuring instruction quality and classroom climate](../claims/discourse-features-correlate-observation-scores.md) [+W]
- [RoBERTa classifiers detect annotated discourse moves in math classroom transcripts with moderate to high accuracy, best for on vs off task instruction](../claims/roberta-classifiers-discourse-moves-moderate-high-accuracy.md) [+W]
- [Baseline student talk ratios do not correlate with observation scores or value-added scores, with student word percentage correlating with instructional dialogue as the exception](../claims/student-talk-ratios-null-correlation.md) [-W]
- [RoBERTa model outputs correlate significantly with math instruction quality scores and with teacher value-added scores](../claims/roberta-measure-correlates-educational-outcomes.md) [+W]

## Related Strategies

- [Use MET video feedback with novice-led think-aloud discourse in teacher education, prompting trainees to also identify positive aspects of their teaching](met-feedback-novice-led-discourse-strategy.md)
- [Triangulate LLM-based discourse measures with multiple methods and seek input from participating communities](triangulate-llm-discourse-measures-with-community-input.md)
- [Deliver scalable automated talk-move feedback to online instructors as a complement to professional development](automated-talk-move-feedback-strategy.md)
- [Use audio-only recording (with transcription) for privacy-preserving automated discourse assessment](audio-only-privacy-preserving-discourse-assessment.md)

## Examples
-

## Key Sources
- Dorottya Demszky and Heather Hill. (2022). The NCTE Transcripts: A Dataset of Elementary Math Classroom Transcripts. https://arxiv.org/abs/2211.11772

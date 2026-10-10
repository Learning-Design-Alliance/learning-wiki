---
type: product
id: simse
title: SimSE
description: SimSE is a dataset of 1,135 simulated five-minute teaching sessions by pre-service teachers, annotated for metacognitive modeling components and collected through the TeachSim platform by Xu and colleagues.
product_kind: dataset
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: paiheng-xu-2024
    resource: "https://aclanthology.org/volumes/2024.naacl-long/"
    title: "Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/"
    author: Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai
---

# SimSE

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
SimSE is a dataset of 1,135 simulated five-minute teaching sessions by pre-service teachers, annotated for metacognitive modeling components and collected through the TeachSim platform by Xu and colleagues.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **SimSE dataset of simulated teaching sessions for pre-service teachers rated on metacognitive modeling components**: The SimSE dataset was collected as part of TeachSim, "a teaching simulation platform for pre-service teachers," from Fall 2022 to Spring 2023. It contains 1,135 five-minute transcribed teaching sessions (teachers' talk only), each annotated with five metacognitive modeling components — Unpacking, Self-Instruction, Self-Regulation, Objective, and Ending — scored 1 to 3 by experts. The sessions focus on teaching metacognitive modeling while unpacking a word problem, a practice the authors describe as critical for supporting students with special needs in general math education. (Paiheng Xu et al. (2024))

### Claims
- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](../claims/chatgpt-zero-shot-relevance-extraction-unreliable.md) [+W]
- [Class-weighted loss marginally improves PLM performance on skewed instruction-quality ratings, achieving best performance on 10 of 16 variables in the three-way setting and 9 of 16 in the binary setting](../claims/class-weighted-loss-marginal-gain-skewed-teaching-ratings.md) [+W]
- [Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline](../claims/llama2-qlora-unsatisfactory-for-teaching-quality-tasks.md) [+W]
- [Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones](../claims/plm-performance-depends-on-pedagogical-expertise-required.md) [+W]
- [Using only teachers' utterances as input achieves comparable or better PLM performance than including student utterances, even for student-oriented observation variables](../claims/teacher-utterances-alone-sufficient-for-classroom-measures.md) [+W]
- [A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences](../claims/two-stage-relevance-strategy-helps-multi-sentence-variables.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/

<!-- merged 2026-10-10 from elements/simse-metacognitive-modeling-dataset ("SimSE dataset of simulated teaching sessions for pre-service teachers rated on metacognitive modeling components"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# SimSE dataset of simulated teaching sessions for pre-service teachers rated on metacognitive modeling components

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The SimSE dataset was collected as part of TeachSim, "a teaching simulation platform for pre-service teachers," from Fall 2022 to Spring 2023. It contains 1,135 five-minute transcribed teaching sessions (teachers' talk only), each annotated with five metacognitive modeling components — Unpacking, Self-Instruction, Self-Regulation, Objective, and Ending — scored 1 to 3 by experts. The sessions focus on teaching metacognitive modeling while unpacking a word problem, a practice the authors describe as critical for supporting students with special needs in general math education.

## Design Implications

### Context
#### Requirements
- Well-defined rubrics that delineate each category unambiguously, given the high cost of annotation
#### Constraints
- Label distributions are highly skewed towards low ratings, which may account for up to 80% of samples for some components
- Sessions comprise teacher utterances only, making it a simpler context than in-person classrooms

### Target Learners
- Pre-service teachers in teaching simulation sessions; students with special needs in general math classrooms as the instructional target

### Target Learning Goals
- Metacognitive modeling: narrating actions, decisions, and thought processes while demonstrating metacognitive strategies

## Claims

- [ChatGPT zero-shot relevance extraction for instruction-quality assessment retrieves mostly irrelevant utterances and overestimates instruction quality](../claims/chatgpt-zero-shot-relevance-extraction-unreliable.md) [+W]
- [Class-weighted loss marginally improves PLM performance on skewed instruction-quality ratings, achieving best performance on 10 of 16 variables in the three-way setting and 9 of 16 in the binary setting](../claims/class-weighted-loss-marginal-gain-skewed-teaching-ratings.md) [+W]
- [Fine-tuning Llama2-7B with parameter-efficient methods yields unsatisfactory results for measuring subject-matter teaching practices, only marginally improving the majority baseline](../claims/llama2-qlora-unsatisfactory-for-teaching-quality-tasks.md) [+W]
- [Fine-tuned PLMs measure high-inference teaching practices better when the variable requires less pedagogical expertise, matching human-rater agreement on lexical variables but degrading on inference-heavy ones](../claims/plm-performance-depends-on-pedagogical-expertise-required.md) [+W]
- [Using only teachers' utterances as input achieves comparable or better PLM performance than including student utterances, even for student-oriented observation variables](../claims/teacher-utterances-alone-sufficient-for-classroom-measures.md) [+W]
- [A two-stage relevance-then-classification strategy improves PLM scoring of metacognitive modeling components whose assessment relies on multiple relevant sentences](../claims/two-stage-relevance-strategy-helps-multi-sentence-variables.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Paiheng Xu, Jing Liu, Nathan Jones, Julie Cohen, and Wei Ai. (2024). The Promises and Pitfalls of Using Language Models to Measure Instruction Quality in Education. Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). https://aclanthology.org/volumes/2024.naacl-long/
-->

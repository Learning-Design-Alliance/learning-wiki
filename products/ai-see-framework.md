---
type: product
id: ai-see-framework
moved_from: [design/ai-see-framework]
title: AI-SEE framework
description: The AI-SEE framework proposed by Feng Liu et al.
product_kind: framework
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: feng-liu-2026
    resource: "https://doi.org/10.3390/su18042124"
    title: "Feng Liu, Hua Wang, Yuntao Guo, Tianpei Tang. (2026). Enhancing Sustainability Consciousness in Higher Education: Impacts of Artificial Intelligence-Integrated Sustainable Engineering Education. Sustainability 18, 2124. https://doi.org/10.3390/su18042124"
    author: Feng Liu, Hua Wang, Yuntao Guo, Tianpei Tang
---

# AI-SEE framework

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 2 studies (1 causal, 1 qualitative), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The AI-SEE framework proposed by Feng Liu et al. organizes application-oriented engineering curricula around intelligence-driven, green-empowered, responsibility-leading, and practice-integrated learning.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Four-pillar curriculum pattern: intelligence-driven, green-empowered, responsibility-leading, and practice-integrated learning**: The AI-SEE framework organizes the curriculum as four mutually reinforcing pillars. The intelligence-driven pillar embeds AI for data acquisition, modeling, feedback, and simulation; the green-empowered pillar embeds lifecycle assessment and carbon accounting as decision criteria; the responsibility-leading pillar makes engineering ethics a required component; the practice-integrated pillar connects classrooms with industry and communities. The article states that "AI-SEE therefore emphasizes that learning tasks should culminate in action within real contexts," and that the pillars "together form a dynamic system for cultivating the competencies required of sustainable engineering professionals in the AI era." (Feng Liu et al. (2026))
- **Publicly released SEE and instruction optimization prompts (StanfordAI4HI/ed-expert-simulator)**: The article releases its prompt materials as a public artifact: "Our prompts are publicly available at https://github.com/StanfordAI4HI/ed-expert-simulator." These include the evaluation prompts for simulated expert evaluations (student persona, instruction, test question, and scoring task) and the optimization prompts pairing worksheets with their post-test scores, enabling replication of the SEE procedure and the instruction optimization algorithm. (Joy He-Yueya et al. (2024))
- **Simulated Expert Evaluation (SEE): an LM evaluator predicts a student persona's post-test performance given instructional content**: SEE is an evaluation procedure in which an evaluator LM takes a student persona, an instruction, and test questions, and predicts the probability the student solves each test problem, averaged into a post-test score. Unlike simulating a student, an SEE "only predicts the post-test scores without actually simulating the student's responses". The authors use SEEs over populations of personas to estimate the aggregate impact of instructions and as the reward function in instruction optimization. (Joy He-Yueya et al. (2024))

### Claims
- [Pilot students reported structural limitations of AI-SEE: AI-tool entry barriers, limited hands-on time, and partial disconnection between ethics instruction and routine engineering decisions](../claims/ai-see-reported-structural-limitations.md) [-W]
- [LM-based simulated expert evaluations replicate the Expertise Reversal Effect: low-expertise learners benefit more from worked examples than practice, with no such difference among high-expertise learners](../claims/see-replicates-expertise-reversal-effect.md) [+M]
- [LM-based simulated expert evaluations replicate the Variability Effect: high variability enhances performance in worked-example conditions but has no effect in practice conditions](../claims/see-replicates-variability-effect.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Feng Liu, Hua Wang, Yuntao Guo, Tianpei Tang. (2026). Enhancing Sustainability Consciousness in Higher Education: Impacts of Artificial Intelligence-Integrated Sustainable Engineering Education. Sustainability 18, 2124. https://doi.org/10.3390/su18042124
<!-- merged 2026-10-20 from designs/ai-see-framework ("AI-SEE: a pedagogical framework integrating AI across the engineering curriculum as a cognitive scaffold and system-optimization resource"), misfiled as a design and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.
- Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. https://arxiv.org/abs/2403.02795

# AI-SEE: a pedagogical framework integrating AI across the engineering curriculum as a cognitive scaffold and system-optimization resource

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
AI-SEE (Artificial Intelligence-Integrated Sustainable Engineering Education) is a pedagogical framework structured around an input-process-output logic, in which institutional conditions, learner characteristics, and external contexts feed a pedagogical process of four pillars whose intended outputs are sustainability-related knowledge, attitudes, and behavioral orientations. The article states that "The core pedagogical process is operationalized through four mutually reinforcing pillars—intelligence-driven, green-empowered, responsibility-leading, and practice-integrated—which together constitute an integrated learning system." AI is positioned not merely as an instructional aid but as a cognitive augmentation platform and scenario simulation engine supporting systems thinking, ethical trade-off analysis, and knowledge-to-action translation.

## Design Implications

### Context
#### Requirements
- AI embedded across the educational lifecycle to support data-rich learning, iterative feedback, and adaptive instruction
- human-AI collaboration positioning engineers and students as accountable agents of judgment rather than passive recipients of algorithmic outputs
#### Constraints
- designed for feasibility, scalability, and sustainability within resource-constrained, practice-oriented higher education contexts
- tailored to application-oriented undergraduate institutions in China

### Target Learners
- application-oriented undergraduate engineering students

### Learning Goals
- sustainability consciousness (knowledge, attitudes, behavioral orientations)
- systems thinking and ethical trade-off analysis in engineering decision-making

### Claims
- 

## Related Designs

- [Evolving-artifact course organization: each module's output becomes the next module's input](../designs/evolving-artifact-module-chain.md)

## Examples
-

## Key Sources
- Feng Liu, Hua Wang, Yuntao Guo, Tianpei Tang. (2026). Enhancing Sustainability Consciousness in Higher Education: Impacts of Artificial Intelligence-Integrated Sustainable Engineering Education. Sustainability 18, 2124. https://doi.org/10.3390/su18042124
-->

---
type: research-method
id: dynemb-knowledge-tracing-framework
title: DynEmb knowledge tracing framework
description: "DynEmb is a knowledge tracing framework with two independently trained components: QuestionEmb, which learns a static d-dimensional question embedding via regularized biased matrix factorization from student-question interactions, and StudentDyn, an RNN (an LSTM by default) whose hidden state serves"
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: liangbei-xu-and-mark-a-davenport-2020
    resource: "https://educationaldatamining.org"
    title: "Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org"
    author: Liangbei Xu and Mark A. Davenport
---

# DynEmb knowledge tracing framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
DynEmb is a knowledge tracing framework with two independently trained components: QuestionEmb, which learns a static d-dimensional question embedding via regularized biased matrix factorization from student-question interactions, and StudentDyn, an RNN (an LSTM by default) whose hidden state serves as a dynamic student embedding. The predicted probability of a correct response combines the question embedding and the dynamic student embedding through an inner product with a per-question bias and sigmoid activation. The article argues this hybrid "can harness the advantages from both static and sequential models in a way that outperforms both", and that the framework is flexible, accommodatin

## Accounts
<!-- How each source describes or uses the method -->
- **DynEmb: a hybrid knowledge tracing framework combining static matrix-factorization question embeddings with an RNN that tracks dynamic student knowledge states**: DynEmb is a knowledge tracing framework with two independently trained components: QuestionEmb, which learns a static d-dimensional question embedding via regularized biased matrix factorization from student-question interactions, and StudentDyn, an RNN (an LSTM by default) whose hidden state serves as a dynamic student embedding. The predicted probability of a correct response combines the question embedding and the dynamic student embedding through an inner product with a per-question bias and sigmoid activation. The article argues this hybrid "can harness the advantages from both static and sequential models in a way that outperforms both", and that the framework is flexible, accommodatin (Liangbei Xu et al. (2020))

### Claims
- [DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting](../claims/dynemb-outperforms-dkt-and-bmf-baselines.md) [+M]
- [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVMN performance, while DynEmb tracks knowledge using pretrained question embeddings instead of tags](../claims/dynemb-tracks-knowledge-without-skill-tags.md) [+M]

## Related Research Methods
-

## Key Sources
- Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org

<!-- merged 2026-10-10 from theories/dynemb-framework ("DynEmb: a hybrid knowledge tracing framework combining static matrix-factorization question embeddings with an RNN that tracks dynamic student knowledge states"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# DynEmb: a hybrid knowledge tracing framework combining static matrix-factorization question embeddings with an RNN that tracks dynamic student knowledge states

> **Theory** · [All theories](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
DynEmb is a knowledge tracing framework with two independently trained components: QuestionEmb, which learns a static d-dimensional question embedding via regularized biased matrix factorization from student-question interactions, and StudentDyn, an RNN (an LSTM by default) whose hidden state serves as a dynamic student embedding. The predicted probability of a correct response combines the question embedding and the dynamic student embedding through an inner product with a per-question bias and sigmoid activation. The article argues this hybrid "can harness the advantages from both static and sequential models in a way that outperforms both", and that the framework is flexible, accommodating various sequential models and optional tag or other feature information.

## Design Implications

### Context
#### Requirements
- A sequence of student-question-response interactions from an ensemble of students; the question embedding must be pretrained and held fixed while training the sequential component.
#### Constraints
- The paper focuses mainly on binary correct/incorrect responses, though the framework is stated to extend to numerical scores; online deployment requires additional algorithmic improvement.

### Target Learners
- students interacting with computer-based learning systems and intelligent tutoring systems

### Target Learning Objectives
- estimating and tracking student knowledge or proficiency over time to enable personalized learning

### Claims
- [Dynemb Outperforms Dkt And Bmf Baselines](../claims/dynemb-outperforms-dkt-and-bmf-baselines.md) [+M]
- [Dynemb Tracks Knowledge Without Skill Tags](../claims/dynemb-tracks-knowledge-without-skill-tags.md) [+M]

## Related Theories
- 

## Examples

- [Skill tag integration scheme: concatenating matrix-factorization question embeddings with one-hot skill tag embeddings, with l1-regularized tag-based initialization](../elements/dynemb-skill-tag-concatenation-integration.md)

## Key Sources
- Liangbei Xu and Mark A. Davenport. (2020). Dynamic Knowledge Embedding and Tracing. Proceedings of The 13th International Conference on Educational Data Mining (EDM 2020). https://educationaldatamining.org
-->

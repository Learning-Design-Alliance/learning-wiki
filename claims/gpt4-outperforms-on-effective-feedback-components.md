---
type: claim
title: GPT-4 outperformed GPT-3.5 and human instructors in producing feedback containing effective feedback components such as feeding-up and process-level information
description: GPT-4 outperformed GPT-3.5 and human instructors in producing feedback containing effective feedback components such as feeding-up and process-level information
id: gpt4-outperforms-on-effective-feedback-components
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-15
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: dai-2024
    resource: "https://doi.org/10.1016/j.caeai.2024.100299"
    title: "Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299"
    author: Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: dai-2024-2
    resource: "https://doi.org/10.1016/j.caeai.2024.100299"
    title: "Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299"
    author: Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 outperformed GPT-3.5 and human instructors in producing feedback containing effective feedback components such as feeding-up and process-level information

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 generated feeding-up information in 94.17% of feedback versus 5.83% for instructors and 0% for GPT-3.5, and process-level information in 97.09% versus 80% and 55%. [→ Dai 2024](#dai-2024)
`q2 i?` Neither GPT model produced self-level feedback, which appeared in 25 pieces of instructor feedback. [→ Dai 2024 (2)](#dai-2024-2)

## Evidence

### Dai 2024

Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299

`q2 · i?` · `design · r2`

Expert annotation of 309 feedback pieces (103 per generator) against Hattie and Timperley's framework, blind to source. Table 7: feeding-up 5.83% instructor, 0% GPT-3.5, 94.17% GPT-4; process 80%, 55%, 97.09%; "GPT-4 gen- erated feeding-up information in almost every piece of feed- back (94.17%)".

> "GPT-3.5 did not o ffer any of this information in its generated feedback. In contrast, GPT-4 gen- erated feeding-up information in almost every piece of feed- back (94.17%)."

### Dai 2024 (2)

Wei Dai, Yi-Shan Tsai, Jionghao Lin, Ahmad Aldino, Hua Jin, Tongguang Li, Dragan Gašević, Guanliang Chen. (2024). Assessing the Proficiency of Large Language Models in Automatic Feedback Generation: An Evaluation Study. Computers and Education: Artificial Intelligence, 7, 100299. Preprint submitted to Elsevier. https://doi.org/10.1016/j.caeai.2024.100299

`q2 · i?` · `design · r2`

Same annotation study: self-level information absent from all GPT-generated feedback while present in 25 of 103 instructor pieces; the article notes self-level feedback "can be an important feedback element to motivate students".

> "Finally, the self level information was detected in 25 pieces of human feedback, but not in GPT-3.5 or GPT-4 generated feedback at all."

## Discussion


## Related Claims
- [A human assessor agreed with the majority of GPT-generated feedback comments on assessment aspects that instructors had not commented on](human-assessor-agrees-with-gpt-feedback-on-uncommented-aspects.md) — related
- [Students receiving instructor feedback showed significantly greater improvements in lab assignment scores than students receiving AI-generated feedback, after controlling for initial knowledge](instructor-feedback-greater-lab-score-improvements-than-ai-feedback.md) — related

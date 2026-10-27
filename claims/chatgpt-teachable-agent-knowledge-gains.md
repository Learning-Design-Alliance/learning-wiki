---
type: claim
title: Students who teach a ChatGPT teachable agent in natural language achieve greater knowledge gains than students who learn the same material from online videos
description: Students who teach a ChatGPT teachable agent in natural language achieve greater knowledge gains than students who learn the same material from online videos
id: chatgpt-teachable-agent-knowledge-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2024
source_checked: 2026-10-17
sources:
  - id: angxuan-chen-2024
    resource: "https://doi.org/10.48550/arxiv.2412.15226"
    title: "Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226 [doi:10.48550/arxiv.2412.15226](https://doi.org/10.48550/arxiv.2412.15226)"
    author: Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang
    q: 2
    i: 3
    kind: causal
    rigour: 1
---

# Students who teach a ChatGPT teachable agent in natural language achieve greater knowledge gains than students who learn the same material from online videos

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2` · `i3` large
> **Currency** · newest study 2024 · checked against its sources 2026-10-17 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i3` In a controlled experiment on the eight queens puzzle, the experimental group that taught a ChatGPT agent scored significantly higher on the knowledge post-test than the video-only control group (adjusted means 11.86 vs 10.53, η2 = 0.74). [→ Angxuan Chen 2024](#angxuan-chen-2024)

## Evidence

### Angxuan Chen 2024

Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226 [doi:10.48550/arxiv.2412.15226](https://doi.org/10.48550/arxiv.2412.15226)

`q2 · i3` · `causal · r1`

ANCOVA with pre-test scores as covariate compared students who taught a gpt-4 teachable agent with students who learned from online videos; the experimental group "had a higher adjusted average score than CG (11.86 > 10.53)", with F = 35.54 and η2 = 0.74. Checked against the arXiv full text on 2026-10-15: Table 2 prints η2 = 0.74 for this two-group contrast (EG n = 20, CG n = 21), but it does not square with the paper's own figures. F = 35.54 on 1 and 38 degrees of freedom implies a partial η2 of about 0.48, and the unadjusted means and SDs (11.90, SD 2.09, against 10.76, SD 1.02) imply a d of about 0.7. So the effect is probably large or medium-to-large, but the printed 0.74 overstates it.

> "The ANCOV A results showed that the three groups were significantly different in knowledge test scores (F = 35.54, p < 0.05, η2 = 0.74) (as shown in Table 2) that EG had a higher adjusted average score than CG (11.86 > 10.53)."

## Discussion

## Related Claims

- [Learning By Teaching Improves Tutor Learning](learning-by-teaching-improves-tutor-learning.md) — the general claim this finding bears on, with the studies behind it

- [Discussion promotes more active thinking than lecture, though lecture is no worse for transmitting information](discussion-promotes-more-active-thought-than-lecture.md) — the general claim this finding bears on, with the studies behind it
- [Teaching a ChatGPT agent yields significantly higher code clearness and readability scores than learning from online videos, but not higher code correctness](chatgpt-teachable-agent-code-clearness-readability.md) — related
- [Students teaching the ChatGPT agent passed the online judge with fewer code submission attempts than control students](chatgpt-teachable-agent-fewer-submission-attempts.md) — related
- [Teaching a ChatGPT agent does not significantly improve code correctness compared with writing code independently from videos](chatgpt-teachable-agent-no-correctness-gain.md) — related
- [Teaching a ChatGPT agent improves students' self-regulated learning, specifically self-efficacy and use of cognitive strategies](chatgpt-teaching-self-efficacy-cognitive-strategies.md) — related
- [Teaching a ChatGPT agent does not significantly change students' test anxiety](chatgpt-teaching-test-anxiety-no-difference.md) — related
- [Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment](chatgpt-hints-significant-gains-versus-control.md) — related
- Eleventh-grade students with ChatGPT access scored significantly higher than traditionally taught controls on the electronic magnetism post-test, with large effect sizes — related
- [Adding a teachable agent to the standard science curriculum improved fourth-graders' learning gains on both curriculum tests and researcher-designed hierarchical reasoning tests](ta-improves-basic-and-added-value-gains-fourth-grade.md) — a narrower finding that bears on this claim
- [TAIA produced higher adjusted post-test scientific achievement than worksheet-supported inquiry, controlling for pre-test and ICT competency](taia-higher-posttest-achievement-rural.md) — related
- [Conversational-agent prompts improve student dialogue outcomes at both individual and dyad levels](conversational-agent-prompts-improve-individual-and-dyad-outcomes.md) — related
- [Flipped classroom teaching with structured interaction improves learning outcomes more than lecture-based teaching and a video-lecture control](structured-interaction-flipped-classroom-improves-learning.md) — related

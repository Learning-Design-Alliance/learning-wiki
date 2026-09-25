---
type: claim
title: Peer Feedback Accuracy Depends On Expertise
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: peer-feedback-accuracy-depends-on-expertise
evidence_strength: weak
sources:
  - id: wu-schunn-2023
    resource: "https://doi.org/10.1037/edu0000768"
    title: "Wu, Y., & Schunn, C. D. (2023). Assessor writing performance on peer feedback: Exploring the relation between assessor writing performance, problem identification accuracy, and helpfulness of peer feedback. *Journal of Educational Psychology, 115*(1), 118–142. [doi:10.1037/edu0000768](https://doi.org/10.1037/edu0000768)"
    author: "Wu, Y., & Schunn, C. D."
    q: 2
    i: "?"
    n: 234 assessors (1,921 individual comments), 234 secondary/high-school students in a U.S. writing course
  - id: schunn-et-al-2016
    resource: "https://doi.org/10.1002/jaal.525"
    title: "Schunn, C., Godley, A., & DeMartino, S. (2016). The reliability and validity of peer review of writing in high school AP English classes. *Journal of Adolescent & Adult Literacy, 60*(1), 13–23. [doi:10.1002/jaal.525](https://doi.org/10.1002/jaal.525)"
    author: "Schunn, C., Godley, A., & DeMartino, S."
    q: 2
    i: "?"
    n: 1,215 students across 26 U.S. schools (12 states); 489 essays independently rated by teachers and trained AP scorers
---

# Peer Feedback Accuracy Depends On Expertise

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

The accuracy and usefulness of feedback that learners give to one another depends on the feedback-giver's domain expertise: novices often misdiagnose problems and endorse flawed work. The claim concerns the *accuracy* of the feedback given, not the *benefit* of receiving or producing it — those can diverge.

## Subclaims

`q2 i?` Among secondary-school peer assessors, writer/assessor performance level was unrelated to whether they correctly identified a genuine problem in a peer's draft, but it strongly predicted whether their comments were rated helpful — so "expertise" tracks the usefulness of feedback more reliably than its diagnostic accuracy. [→ Wu & Schunn 2023](#wu-schunn-2023)

`q2 i?` Among AP English students using a structured, well-specified rubric, agreement between peer ratings and teacher/expert AP scores did not differ significantly between higher- and lower-performing schools, qualifying a simple novice-vs-expert accuracy story when reviewers are given strong scaffolding. [→ Schunn et al. 2016](#schunn-et-al-2016)

## Evidence

### Wu & Schunn 2023

Wu, Y., & Schunn, C. D. (2023). Assessor writing performance on peer feedback: Exploring the relation between assessor writing performance, problem identification accuracy, and helpfulness of peer feedback. *Journal of Educational Psychology, 115*(1), 118–142. [doi:10.1037/edu0000768](https://doi.org/10.1037/edu0000768)

`q2 · observational/correlational study with regression controls (not an experimental manipulation of expertise)` · `i? · no d/r-scale effect size reported; findings expressed as odds ratios and null regression coefficients` · `n=234 assessors (1,921 individual comments), 234 secondary/high-school students in a U.S. writing course`

234 high-school assessors' own writing performance was measured at three grain sizes (genre, rubric dimension, specific problem topic) and related to (a) whether they correctly flagged real problems in a peer's essay and (b) whether their comments were rated helpful. Multiple regression showed assessor writing performance was **not** related to problem-identification accuracy at any grain size — lower-performing assessors even flagged *more* problems (not fewer) on several topics, with directionally higher false-alarm rates that were not statistically significant. By contrast, assessor performance on specific topics and dimensions consistently and substantially predicted [feedback helpfulness](../elements/rubrics.md) (topic-level performance more than doubled the odds of helpful feedback; dimensional performance raised it by ~25%), even though lower-performing assessors rarely gave outright incorrect advice.

### Schunn et al. 2016

Schunn, C., Godley, A., & DeMartino, S. (2016). The reliability and validity of peer review of writing in high school AP English classes. *Journal of Adolescent & Adult Literacy, 60*(1), 13–23. [doi:10.1002/jaal.525](https://doi.org/10.1002/jaal.525)

`q2 · observational/correlational classroom study, no experimental manipulation of reviewer ability` · `i? · reported as correlations (r ≈ .4–.7) and a non-significant moderation test, not a d-scale effect for the expertise comparison` · `n=1,215 students across 26 U.S. schools (12 states); 489 essays independently rated by teachers and trained AP scorers`

1,215 AP English students anonymously rated five classmates' rhetorical-analysis essays each with a task-specific [rubric](../elements/rubrics.md); their mean ratings were compared to their teachers' and to trained AP expert scorers' ratings of the same 489 essays. Correlations between mean student ratings and both teacher and expert scores were moderate-to-high (roughly .4–.7, approaching .7 for the overall essay score) and, notably, students' averaged ratings correlated with expert scores slightly *more* strongly than individual teachers' ratings did. Critically for this claim, reliability and validity did **not** differ significantly between higher- and lower-performing schools on any rubric criterion, suggesting that — at least when reviewers use a carefully designed, well-specified rubric — peer-assessment accuracy does not simply track the reviewers' own academic performance level.

## Discussion

**The evidence below does not support the claim as stated.** Wu & Schunn (2023) found assessor expertise predicted how *helpful* feedback was but was unrelated to how *accurately* it identified problems, and Schunn et al. (2016) found peer ratings about as reliable in lower- as in higher-performing schools once a well-designed rubric was used. Read the title as a hypothesis the current evidence does not bear out, at least where assessment is structured.

**Why expertise matters.** Accurate peer feedback requires the same knowledge that accurate self-assessment requires: a mental model of what quality looks like and the ability to detect deviations from it. Novices lack this model, so their comments tend to be generic ("good introduction") or wrong (praising fluent but incorrect reasoning). This is closely tied to the [expertise reversal effect](../theories/expertise-reversal-effect.md) — the same knowledge gap that makes [worked examples](../theories/cognitive-load-theory.md) valuable for novices makes them unreliable evaluators of others' work. Under [cognitive load theory](../theories/cognitive-load-theory.md), evaluating a peer's work demands comparing it against internal standards for quality; without those schemas, novices default to surface features.

**Moderators and boundary conditions.** The claim is directional, not absolute. Peer feedback can still be valuable for novices when (a) the task is well-structured with explicit criteria or [rubrics](../elements/rubrics.md) that substitute for missing internal standards, (b) feedback is exchanged at a surface level (clarity, organization) rather than deep conceptual correctness, or (c) peers collectively catch errors that individuals miss. Conversely, the higher the domain-specificity of the judgment required, the more accuracy depends on expertise — a constraint that worsens as tasks become more open or conceptually demanding. This mirrors the broader finding that feedback improves achievement mainly when it tells the learner where they stand relative to goals and how to close the gap ([Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md)) [+M] — a function novice peers are poorly positioned to serve on conceptually demanding work.

**Design implications.** Where peer feedback is used with novices, designers should treat it as a supplement to, not a substitute for, instructor or expert feedback, and should scaffold the judgment itself: rubrics, annotated exemplars contrasting strong and weak work, and training in applying criteria. Receiving peer feedback may still benefit the receiver even when the giver's comments are imperfect — the act of reviewing can activate criteria in the giver as well — but designers should not assume accuracy scales with participation. Note also that simply adding evaluation checklists does not by itself produce accurate judgments online ([Checklist evaluation is ineffective online](checklist-evaluation-ineffective-online.md)) [~M]; the scaffolds must build genuine criterion knowledge, not just prompt surface checks. Where criterion knowledge is genuinely weak, pairing peer review with [worked examples](../theories/cognitive-load-theory.md) or annotated models of strong and weak work is a more promising route than procedural supports alone. Structured peer-review protocols that distribute judgment across a group (e.g., calibrated peer review with exemplar comparison before rating) partially mitigate the problem, but they substitute external criteria for internal ones rather than eliminating the expertise dependence.

**Open questions.** Most of the literature contrasts novices with more advanced peers or instructors; the expertise threshold at which peer feedback becomes reliably accurate is not well established, and evidence is needed across domains before strong design prescriptions can be made. Until that evidence is added to this page, the claim should be treated as a well-motivated theoretical expectation rather than an empirically established effect.

## Related Claims

- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — the same knowledge asymmetry governs when scaffolds and peer evaluation help or hurt.
- [Cognitive load theory](../theories/cognitive-load-theory.md) — explains why novices lack the schemas needed to evaluate work accurately.
- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — feedback only helps when it accurately locates work relative to criteria, which is exactly what novice peers struggle to do.
- [Checklist evaluation is ineffective online](checklist-evaluation-ineffective-online.md) — surface-level evaluation supports do not compensate for missing criterion knowledge.
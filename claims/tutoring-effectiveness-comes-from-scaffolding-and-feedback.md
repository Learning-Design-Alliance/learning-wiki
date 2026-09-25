---
type: claim
title: Tutoring Effectiveness Comes From Scaffolding And Feedback
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: tutoring-effectiveness-comes-from-scaffolding-and-feedback
evidence_strength:
sources:
  - id: chi-et-al-2001
    resource: "https://doi.org/10.1207/s15516709cog2504_1"
    title: "Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G. (2001). Learning from human tutoring. *Cognitive Science, 25*(4), 471–533. [doi:10.1207/s15516709cog2504_1](https://doi.org/10.1207/s15516709cog2504_1)"
    author: "Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G."
    q: 2
    i: "?"
    n: 11 tutor–student dyads (Study 1), 11 dyads (Study 2)
  - id: vanlehn-2011
    resource: "https://doi.org/10.1080/00461520.2011.611369"
    title: "VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)"
    author: VanLehn, K.
    q: 3
    i: 2
    n: "not stated in the abstract (full text is paywalled; abstract reports \"6 figures, 11 tables\" of synthesized comparisons but not a pooled study/effect count)"
---

# Tutoring Effectiveness Comes From Scaffolding And Feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2`–`q3` · `i2` medium

The learning benefits of tutoring are attributed to the tutor's ability to scaffold tasks within the learner's zone of proximal development and to provide immediate, adaptive feedback — not merely to one-on-one attention.

## Subclaims

`q2 i?` In naturalistic human tutoring of 8th-graders, tutor explanations and students' scaffolded responses each correlated with shallow learning gains beyond prior knowledge and reading ability, but suppressing tutor feedback and explanations in favor of pure scaffolding prompts did not reduce learning — students learned just as well from scaffolding-only tutoring. [→ Chi et al. 2001](#chi-et-al-2001)

`q3 i2` Across the tutoring-research literature, human tutoring produces a medium-sized learning advantage over no-tutoring instruction (d = 0.79), a substantially smaller benchmark than the often-cited two-sigma (d = 2.0) figure, and close in magnitude to the best intelligent tutoring systems (d = 0.76). [→ VanLehn 2011](#vanlehn-2011)

## Evidence

### Chi et al. 2001

Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G. (2001). Learning from human tutoring. *Cognitive Science, 25*(4), 471–533. [doi:10.1207/s15516709cog2504_1](https://doi.org/10.1207/s15516709cog2504_1)

`q2 · quasi-experimental / naturalistic tutoring study with a follow-up manipulation` · `i? · no standardized effect size (d/g/r/OR) reported; findings reported as regression R² changes and correlations` · `n=11 tutor–student dyads (Study 1), 11 dyads (Study 2)`

Two studies of one-to-one human tutoring on the human circulatory system with 8th-graders and unskilled college-student tutors. Study 1 coded naturalistic tutoring dialogues and used step-wise regression to show that, beyond prior knowledge and reading ability, tutors' explanations predicted shallow learning and students' scaffolded (elicited) responses and reflective comments predicted shallow and deep learning respectively. Study 2 then manipulated tutoring style: tutors were instructed to suppress explanations and feedback entirely and instead use content-free prompts to elicit student construction (pure [scaffolding](../elements/demonstration.md)-style prompting). Students in this feedback-suppressed condition learned just as well as students in Study 1's ordinary explanation-and-feedback tutoring, which the authors attribute to deeper and more frequent scaffolding-elicited construction and greater self-directed reading.

### VanLehn 2011

VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)

`q3 · systematic review synthesizing effect sizes across tutoring experiments` · `i2 · medium effect, d=0.79 (human tutoring vs. no tutoring)` · `n=not stated in the abstract (full text is paywalled; abstract reports "6 figures, 11 tables" of synthesized comparisons but not a pooled study/effect count)`

A review of experiments comparing human tutoring, several classes of computer tutoring systems (answer-based, step-based, substep-based), and no-tutoring instruction on the same content. Contrary to the widely repeated belief that human tutoring produces very large gains (d = 2.0, per Bloom's two-sigma figure) far beyond intelligent tutoring systems (believed d = 1.0), the review found human tutoring's actual effect size relative to no tutoring was much lower (d = 0.79) and that intelligent tutoring systems (d = 0.76) were nearly as effective. Read from the publisher/ERIC abstract only, since the full text sits behind a paywall with no open-access copy found via Unpaywall.

## Discussion

**The recorded evidence complicates the title.** In Chi et al. (2001), when tutors were told to withhold feedback and explanations and only prompt, students learned as much, which the authors attribute to the students' own construction rather than to tutor feedback. So the evidence recorded here supports scaffolding more than feedback as the source of tutoring's effect.

**Why tutoring works.** The dominant explanation for tutoring's large learning gains is process-based: effective tutors continuously diagnose the learner's understanding, adjust task difficulty and hints accordingly (scaffolding), and deliver feedback that is immediate, specific, and contingent on the learner's current performance. Bloom's (1984) "two sigma" observation — that one-on-one tutoring combined with mastery learning produced achievement roughly two standard deviations above conventional instruction — framed tutoring as a benchmark, and subsequent work has sought to decompose *which* tutor behaviors drive the effect rather than treating tutoring as an undifferentiated treatment. Scaffolding and contingent feedback are the two most consistently cited candidate mechanisms, and both are independently supported in the broader literature (see [Cognitive load management](../principles/cognitive-load-management.md) and [Feedback improves learning](feedback-improves-learning.md)).

**Boundary conditions.** The claim is about *effective* tutoring. Human tutors vary enormously in quality, and observational studies of naturalistic tutoring show that many tutors do relatively little scaffolding — much tutor talk is didactic telling rather than contingent responding. The claim therefore does not imply that any one-on-one arrangement produces gains; the mechanism is the instructional moves, not the staffing ratio. Similarly, computer-based tutoring systems (e.g., intelligent tutoring systems) capture some of the benefit by modeling learner knowledge and adapting hints and feedback, but typically fall short of expert human tutors on measures of deep conceptual change.

**Interaction with mastery learning.** Bloom's original two-sigma result combined tutoring with mastery learning, so the canonical benchmark conflates two active ingredients. Any claim that tutoring *alone* produces two-sigma gains overstates the evidence; the tutoring-plus-mastery combination is the well-documented configuration (see [Mastery learning improves outcomes](mastery-learning-improves-outcomes.md)).

**Scaffolding implies fading.** Scaffolding is not permanent support: the construct, from Wood, Bruner, and Ross's original formulation, requires that assistance be withdrawn as competence grows. Tutoring that maintains a fixed level of hinting indefinitely risks fostering dependence rather than independence — the same expertise-reversal logic that applies to [worked examples](../elements/demonstration.md) applies to tutor-provided hints (see [Expertise reversal effect](../theories/expertise-reversal-effect.md)). Effective tutoring is therefore defined by *contingent shifting*: more support when the learner struggles, less as performance stabilizes.

**Open questions.** The relative contribution of scaffolding versus feedback within tutoring is not well established, and the two interact: feedback is most effective when it is contingent on a diagnosis, which is itself a scaffolding act. Disentangling these mechanisms requires component-manipulation studies that are currently underrepresented in the evidence base.

## Related Claims

- [Feedback improves learning.](feedback-improves-learning.md) — feedback is one of the two proposed active ingredients of tutoring
- [Mastery learning improves outcomes.](mastery-learning-improves-outcomes.md) — mastery learning was combined with tutoring in Bloom's original two-sigma work
- [Adaptive learning improves outcomes.](adaptive-learning-improves-outcomes.md) — machine-adaptive systems attempt to replicate the contingency of human tutoring
- [Cognitive load theory.](../theories/cognitive-load-theory.md) — scaffolding manages working-memory load during guided practice
- [Cognitive apprenticeship.](../patterns/cognitive-apprenticeship.md) — a broader instructional pattern built on modeling, coaching (scaffolding), and fading
- [Expertise reversal effect.](../theories/expertise-reversal-effect.md) — sustained tutor support can become counterproductive as competence grows
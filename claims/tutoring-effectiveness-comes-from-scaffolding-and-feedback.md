---
type: claim
title: "Human tutoring has a medium effect over no tutoring, and in one small study students learned as well when tutors only prompted them as when tutors also explained and gave feedback"
status: review
generated:
  by: claude/unspecified
  at: 2026-09-25
id: tutoring-effectiveness-comes-from-scaffolding-and-feedback
evidence_strength:
newest_evidence: 2011
sources:
  - id: chi-et-al-2001
    resource: "https://doi.org/10.1207/s15516709cog2504_1"
    title: "Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G. (2001). Learning from human tutoring. *Cognitive Science, 25*(4), 471–533. [doi:10.1207/s15516709cog2504_1](https://doi.org/10.1207/s15516709cog2504_1)"
    author: "Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G."
    q: 2
    i: "?"
    n: 11 tutor–student dyads (Study 1), 11 dyads (Study 2)
    kind: causal
    rigour: 1
  - id: vanlehn-2011
    resource: "https://doi.org/10.1080/00461520.2011.611369"
    title: "VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)"
    author: VanLehn, K.
    q: 3
    i: 2
    n: not stated in the abstract (full text is paywalled; the abstract gives no study or effect count)
    kind: quant-synthesis
    rigour: "?"
---

# Human tutoring has a medium effect over no tutoring, and in one small study students learned as well when tutors only prompted them as when tutors also explained and gave feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r1`, 1 quant-synthesis `r?` · `q2`–`q3` · `i2` medium
> **Currency** · newest study 2011 · not yet checked against its sources · not reviewed by a person
<!-- deprecated title (2026-10-05, overstated its evidence): Tutoring Effectiveness Comes From Scaffolding And Feedback -->

<!-- deprecated (2026-10-05, overstated its evidence): The learning benefits of tutoring are attributed to the tutor's ability to scaffold tasks within the learner's zone of proximal development and to provide immediate, adaptive feedback — not merely to one-on-one attention. -->

The two studies recorded here show that human tutoring outperforms no tutoring by a medium amount (VanLehn 2011), and that in one small study of 8th-graders students learned as well when tutors were told to withhold explanations and feedback and only prompt as when tutors explained and gave feedback (Chi et al. 2001). Neither study shows that tutor feedback is a source of tutoring's effect; the Chi et al. result points to scaffolded student construction instead.

## Subclaims

`q2 i?` In naturalistic human tutoring of 8th-graders, tutor explanations and students' scaffolded responses each correlated with shallow learning gains beyond prior knowledge and reading ability, but suppressing tutor feedback and explanations in favor of pure scaffolding prompts did not reduce learning — students learned just as well from scaffolding-only tutoring. [→ Chi et al. 2001](#chi-et-al-2001)

`q3 i2` Across the tutoring-research literature, human tutoring produces a medium-sized learning advantage over no-tutoring instruction (d = 0.79), a substantially smaller benchmark than the often-cited two-sigma (d = 2.0) figure, and close in magnitude to intelligent tutoring systems (d = 0.76). [→ VanLehn 2011](#vanlehn-2011)

## Evidence

### Chi et al. 2001

Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G. (2001). Learning from human tutoring. *Cognitive Science, 25*(4), 471–533. [doi:10.1207/s15516709cog2504_1](https://doi.org/10.1207/s15516709cog2504_1)

`q2 · quasi-experimental / naturalistic tutoring study with a follow-up manipulation` · `i? · no standardized effect size (d/g/r/OR) reported; findings reported as regression R² changes and correlations` · `n=11 tutor–student dyads (Study 1), 11 dyads (Study 2)` · `causal · r1`

Two studies of one-to-one human tutoring on the human circulatory system with 8th-graders and unskilled college-student tutors. Study 1 coded naturalistic tutoring dialogues and used step-wise regression to show that, beyond prior knowledge and reading ability, tutors' explanations predicted shallow learning and students' scaffolded (elicited) responses and reflective comments predicted shallow and deep learning respectively. Study 2 then manipulated tutoring style: tutors were instructed to suppress explanations and feedback entirely and instead use content-free prompts to elicit student construction (pure [scaffolding](../elements/demonstration.md)-style prompting). Students in this feedback-suppressed condition learned just as well as students in Study 1's ordinary explanation-and-feedback tutoring, which the authors attribute to deeper and more frequent scaffolding-elicited construction and greater self-directed reading.

### VanLehn 2011

VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)

`q3 · systematic review synthesizing effect sizes across tutoring experiments` · `i2 · medium effect, d=0.79 (human tutoring vs. no tutoring)` · `n=not stated in the abstract (full text is paywalled; the abstract gives no study or effect count)` · `quant-synthesis · r?`

A review of experiments comparing human tutoring, several classes of computer tutoring systems (answer-based, step-based, substep-based), and no-tutoring instruction on the same content. Contrary to the widely repeated belief that human tutoring produces very large gains (d = 2.0, per Bloom's two-sigma figure) far beyond intelligent tutoring systems (believed d = 1.0), the review found human tutoring's actual effect size relative to no tutoring was much lower (d = 0.79) and that intelligent tutoring systems (d = 0.76) were nearly as effective. Read from the publisher/ERIC abstract only, since the full text sits behind a paywall with no open-access copy found via Unpaywall.

## Studies bearing on this claim

<!-- synthesis:start -->
*What should support during practice do: explain and give feedback, prompt the learner to construct the step, or respond contingently to each attempt?* This table gathers the studies behind this claim and the 2 narrower claims that bear on it: **7 distinct studies** (3 causal, 2 quant-synthesis, 1 review, 1 qualitative), `q2`–`q4`, 1 of 7 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Chi et al. 2001](https://doi.org/10.1207/s15516709cog2504_1) | q2 · causal · r1 | i? | this claim; [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [VanLehn 2011](https://doi.org/10.1080/00461520.2011.611369) | q3 · quant-synthesis · r? | i2 · medium effect, d=0.79 (human tutoring vs. no tutoring) | this claim |
| [Pratt and Savoy-Levine 1998](<https://doi.org/10.1016/s0193-3973(99)80041-0>) | q3 · causal · r? | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [Swanson and Lussier 2001](https://doi.org/10.3102/00346543071002321) | q4 · quant-synthesis · r? | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [van de Pol et al. 2010](https://doi.org/10.1007/s10648-010-9127-6) | q3 · review · r2 | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [Wood et al. 1976](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x) | q3 · qualitative · r? | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [Tsvetomila Mihaylova 2026](https://doi.org/10.48550/arxiv.2605.16933) | q2 · causal · r2 | i? | [All three LLM feedback types credibly reduced attempts to success relative to the baseline](llm-feedback-fewer-attempts.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

**What the recorded evidence supports.** In Chi et al. (2001), when tutors were told to withhold feedback and explanations and only prompt, students learned as much, which the authors attribute to the students' own construction rather than to tutor feedback. So the evidence recorded here supports scaffolding more than feedback as the source of tutoring's effect; the page's former title, which named both, overstated it. The paragraphs below describe the wider literature's proposed mechanisms, which no entry here tests.

**Why tutoring works.** The dominant explanation for tutoring's large learning gains is process-based: effective tutors continuously diagnose the learner's understanding, adjust task difficulty and hints accordingly (scaffolding), and deliver feedback that is immediate, specific, and contingent on the learner's current performance. Bloom's (1984) "two sigma" observation — that one-on-one tutoring combined with mastery learning produced achievement roughly two standard deviations above conventional instruction — framed tutoring as a benchmark, and subsequent work has sought to decompose *which* tutor behaviors drive the effect rather than treating tutoring as an undifferentiated treatment. Scaffolding and contingent feedback are the two most consistently cited candidate mechanisms, and both are independently supported in the broader literature (see [Cognitive load management](../principles/cognitive-load-management.md) and [Feedback improves learning](feedback-improves-learning.md)).

**Boundary conditions.** The claim is about *effective* tutoring. Human tutors vary enormously in quality, and observational studies of naturalistic tutoring show that many tutors do relatively little scaffolding — much tutor talk is didactic telling rather than contingent responding. The claim therefore does not imply that any one-on-one arrangement produces gains; the mechanism is the instructional moves, not the staffing ratio. Similarly, computer-based tutoring systems (e.g., intelligent tutoring systems) capture some of the benefit by modeling learner knowledge and adapting hints and feedback, but typically fall short of expert human tutors on measures of deep conceptual change.

**Interaction with mastery learning.** Bloom's original two-sigma result combined tutoring with mastery learning, so the canonical benchmark conflates two active ingredients. Any claim that tutoring *alone* produces two-sigma gains overstates the evidence; the tutoring-plus-mastery combination is the well-documented configuration (see [Mastery learning improves outcomes](mastery-learning-improves-outcomes.md)).

**Scaffolding implies fading.** Scaffolding is not permanent support: the construct, from Wood, Bruner, and Ross's original formulation, requires that assistance be withdrawn as competence grows. Tutoring that maintains a fixed level of hinting indefinitely risks fostering dependence rather than independence — the same expertise-reversal logic that applies to [worked examples](../elements/demonstration.md) applies to tutor-provided hints (see [Expertise reversal effect](../theories/expertise-reversal-effect.md)). Effective tutoring is therefore defined by *contingent shifting*: more support when the learner struggles, less as performance stabilizes.

**Open questions.** The relative contribution of scaffolding versus feedback within tutoring is not well established, and the two interact: feedback is most effective when it is contingent on a diagnosis, which is itself a scaffolding act. Disentangling these mechanisms requires component-manipulation studies that are currently underrepresented in the evidence base.

## Related Claims

- [Scaffolding improves learning](scaffolding-improves-learning.md) — the general claim this finding bears on, with the studies behind it

- [Feedback improves learning.](feedback-improves-learning.md) — feedback is one of the two proposed active ingredients of tutoring
- [Mastery learning improves outcomes.](mastery-learning-improves-outcomes.md) — mastery learning was combined with tutoring in Bloom's original two-sigma work
- [Adaptive learning improves outcomes.](adaptive-learning-improves-outcomes.md) — machine-adaptive systems attempt to replicate the contingency of human tutoring
- [Cognitive load theory.](../theories/cognitive-load-theory.md) — scaffolding manages working-memory load during guided practice
- [Cognitive apprenticeship.](../patterns/cognitive-apprenticeship.md) — a broader instructional pattern built on modeling, coaching (scaffolding), and fading
- [Expertise reversal effect.](../theories/expertise-reversal-effect.md) — sustained tutor support can become counterproductive as competence grows
- [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) — related
- The FTS proposes that fading distinguishes expert from non-expert peers via a game-progress threshold, and peer-tutoring collaboration is expected to improve non-expert game progress and knowledge gained — related
- [PAIR-C scaffolding shows mixed evidence for deep understanding and reduced misconceptions in emergent-phenomena instruction](pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) — related
- Productive difficulty at the edge of mastery, with high expectations, fosters deeper learning — related
- [Scaffold use correlated significantly with mastery of attributes 1, 3, and 4, but not attributes 2 and 5](scaffolding-correlates-mastery-three-of-five-attributes.md) — related
- [Standalone LLM tutors replicate Phase II's profile: strong single-interaction intelligence without systematic control over the learning trajectory](standalone-llm-tutors-lack-trajectory-control.md) — related
- [AI's key contribution in STEM education is intelligent scaffolding that lowers the threshold for understanding knowledge, driving a shift from knowledge transmission to capability development](ai-intelligent-scaffolding-lowers-knowledge-threshold.md) — related
- [Intelligent tutoring systems can improve learning outcomes, particularly with immediate actionable feedback](its-improve-learning-outcomes-with-actionable-feedback.md) — related
- [One-to-one human tutoring lifts an ordinary student well beyond the average classroom with an effect of about d = 0.79 (VanLehn, 2011, as reported)](human-tutoring-effect-d-079.md) — related
- [The AI's nonjudgmental conversational tone and adaptive prompting fostered risk-taking and productive struggle in a psychologically safe environment](nonjudgmental-ai-tone-risk-taking.md) — related
- [In a large-scale RCT, real-time LLM-generated pedagogical suggestions for human tutors raised student knowledge-component mastery by 4 percentage points on average, with larger effects for lower-performing or less-experienced tutors](tutor-copilot-raises-exit-ticket-mastery-4pp.md) — related
- [Theory-guided five-step prompting of AI interaction improves open-ended explanation performance in construction education review, while unprompted AI access alone does not](structured-prompting-improves-open-ended-ai-learning.md) — related
- [SPED-adaptive prompting shifts tutor behavior toward We-Do scaffolding, naturalistic language support, and participation-affirming feedback across three codebooks](sped-adaptive-shifts-tutor-behavior-codebooks.md) — related
- [Within sociocultural theory, teacher feedback and AI-assisted peer feedback function as heterogeneous scaffolds with distinct natures and complementary advantages](heterogeneous-scaffolds-sct-framework.md) — related
- [Tutors with Tutor CoPilot access use more understanding-fostering strategies (e.g., prompting students to explain) and rely less on giving away answers than control tutors](tutor-copilot-shifts-tutors-toward-understanding-fostering-strategies.md) — a narrower finding that bears on this claim
- [The effectiveness of some types of peer tutoring is already well established but under-disseminated to practitioners](peer-tutoring-effectiveness-known-but-undisseminated.md) — a broader claim this one bears on
- [Learning benefits of Cognitive Tutor interactivity are supported to varying extents by a growing body of experimental studies](cognitive-tutor-interactivity-benefits-varying-extents.md) — related
- [Teacher and researcher coaches both used a cognitive apprenticeship approach but differed in scaffolding style](bioworld-coaching-styles-cognitive-apprenticeship.md) — related
- [Students who discussed the prompts answered them more often and gave more domain-related answers, and domain-relatedness predicted learning gain](domain-related-prompt-answers-predict-learning-gain.md) — related
- [Pedagogical experts tutoring in biology generated less deep learning than less pedagogically expert, more interactive tutors](pedagogical-experts-less-deep-learning-tutoring.md) — related
- [Tutoring is highly effective, and hiring older peers as tutors supports learning gains for both older and younger students](tutoring-and-cross-age-peer-tutors-effective.md) — related
- [Contingency is not treated as a necessary condition of scaffolding in bilingual education research, unlike broader educational research](contingency-not-necessary-condition-bilingual-education-scaffolding.md) — related
- [Expert modeling, feedback, hints, and multiple strategies improve cognitive outcomes, but question prompts show no evident difference from control](scaffolding-strategy-moderator-question-prompts-null.md) — related
- [Feedback features shift with age: scaffolds (prompts, audio, physical demonstrations) cluster in ages 3-7 while written and paper-based feedback appears only from age 8](feedback-features-tailored-by-age.md) — related
- [In the LeActiveMaths knowledge-elicitation studies, tutors' feedback became more positive, more elaborate, and more targeted to situational diagnoses over successive interactions](leam-ke-improved-tutor-feedback.md) — related
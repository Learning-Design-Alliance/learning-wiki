---
type: claim
title: Cooperative Learning Improves Achievement
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: cooperative-learning-improves-achievement
aliases: [cooperative-learning-outperforms-competitive-individualistic]
evidence_strength: moderate
sources:
  - id: roseth-et-al-2008
    resource: "https://doi.org/10.1037/0033-2909.134.2.223"
    title: "Roseth, C. J., Johnson, D. W., & Johnson, R. T. (2008). Promoting early adolescents' achievement and peer relationships: The effects of cooperative, competitive, and individualistic goal structures. *Psychological Bulletin, 134*(2), 223–246. [doi:10.1037/0033-2909.134.2.223](https://doi.org/10.1037/0033-2909.134.2.223)"
    author: "Roseth, C. J., Johnson, D. W., & Johnson, R. T."
    q: 4
    i: "?"
    n: "148 studies, >17,000 early adolescents"
  - id: johnson-johnson-stanne-2000
    title: "Johnson, D. W., Johnson, R. T., & Stanne, M. B. (2000). *Cooperative learning methods: A meta-analysis.* University of Minnesota, Minneapolis: Cooperative Learning Center. No DOI found (unpublished technical report, not indexed by Crossref); URL used below."
    author: "Johnson, D. W., Johnson, R. T., & Stanne, M. B."
    q: 2
    i: 3
    n: 164 studies, 194 independent effect sizes
---

# Cooperative Learning Improves Achievement

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2`–`q4` · `i3` large

Structured cooperative learning — small groups working interdependently toward shared goals with individual accountability — raises achievement relative to individualistic or purely competitive formats.

## Subclaims

`q4 i?` A meta-analysis of 148 studies (17,000+ early adolescents, 11 countries) found cooperative goal structures associated with higher achievement than competitive or individualistic goal structures. [→ Roseth et al. 2008](#roseth-et-al-2008)

`q2 i3` Across 164 studies of the Learning Together method, cooperative learning outperformed individualistic learning on achievement (weighted d=0.91, k=56) and competitive learning (weighted d=0.70, k=25). [→ Johnson, Johnson & Stanne 2000](#johnson-johnson-stanne-2000)

## Evidence

### Roseth et al. 2008

Roseth, C. J., Johnson, D. W., & Johnson, R. T. (2008). Promoting early adolescents' achievement and peer relationships: The effects of cooperative, competitive, and individualistic goal structures. *Psychological Bulletin, 134*(2), 223–246. [doi:10.1037/0033-2909.134.2.223](https://doi.org/10.1037/0033-2909.134.2.223)

`q4 · peer-reviewed meta-analysis` · `i? · no effect-size figure in the abstract text read` · `n=148 studies, >17,000 early adolescents`

Meta-analysis of 148 independent studies (over 8 decades of research, 11 countries and 4 multinational samples) comparing cooperative, competitive, and individualistic goal structures for early adolescents. Higher achievement and more positive peer relationships were both associated with cooperative rather than competitive or individualistic goal structures, and cooperative goal structures were associated with a positive relation between achievement and peer relationships — consistent with social interdependence theory. Only the PubMed abstract was read (the publisher page and an author-repository copy were both blocked to automated access), so no numeric effect size from this record can be verified here; treat the direction of effect, not a magnitude, as established by this entry.

### Johnson, Johnson & Stanne 2000

Johnson, D. W., Johnson, R. T., & Stanne, M. B. (2000). *Cooperative learning methods: A meta-analysis.* University of Minnesota, Minneapolis: Cooperative Learning Center. No DOI found (unpublished technical report, not indexed by Crossref); URL used below.

`q2 · meta-analysis, unpublished technical report (not peer-reviewed)` · `i3 · large effect, weighted d=0.91 (vs. individualistic)` · `n=164 studies, 194 independent effect sizes`

A search identified 164 studies (194 independent effect sizes) testing eight named cooperative-learning methods against competitive or individualistic conditions; all eight methods showed a significant positive effect on achievement. For the most-studied method, Learning Together (positive interdependence plus individual accountability, i.e. the same design elements this claim's page defines as "structured" cooperative learning), the weighted mean effect size was d=0.70 (SE=0.06, k=25 comparisons) against competitive conditions and d=0.91 (SE=0.04, k=56 comparisons) against individualistic conditions. Most studies used random assignment of participants or groups (70%), spanned all school levels, and about half ran 30 or more sessions.

## Related note

Both studies converge on direction (cooperative > competitive/individualistic for achievement) but the two available numeric anchors — d≈0.70–0.91 for Learning Together specifically — should not be read as the effect size for "cooperative learning" generically; Roseth et al. (2008), the larger and peer-reviewed meta-analysis, is the better-powered source for the overall claim but its magnitude could not be verified from the text read here.

## Discussion

The claim is best read as conditional on design quality. The classic cooperative-learning literature identifies five mediating conditions — positive interdependence, individual accountability, promotive interaction, social skills, and group processing — and effects are consistently larger when at least interdependence and accountability are present than when students are merely seated in groups [~M]. Without individual accountability, groups are vulnerable to free-riding and status-based participation inequalities, which can erase or reverse achievement gains for lower-status members [-M].

Moderators to watch: group composition (heterogeneous groups tend to outperform homogeneous ones for peer tutoring benefits [~M]), task type (open-ended, discussion-worthy tasks suit cooperation better than routine practice, which individual learners often complete faster alone [~M]), and duration (benefits typically emerge after groups have learned to work together, so short one-off group activities may show weak effects [~W]). The distinction between cooperative learning (structured interdependence) and unstructured [collaborative learning](../patterns/collaborative-learning.md) matters for interpreting mixed findings in the literature.

Boundary conditions for designers: cooperative formats can impose extraneous load on novices, who may lack the prior knowledge needed to give and receive elaborated peer explanations [~M] — see [cognitive load theory](../theories/cognitive-load-theory.md) and [cognitive load management](../principles/cognitive-load-management.md). Group processing (structured reflection on how the group worked) is the most frequently omitted element in practice, yet it is what converts repeated group work into improving group work [~W].

Open questions include how effects scale in online and hybrid settings, where informal accountability mechanisms are weaker, and how cooperative learning interacts with [assessment](../elements/assessment.md) structures that may re-individualize incentives.

*Merged from “Cooperative learning outperforms competitive and individualistic goal structures” (cooperative-learning-outperforms-competitive-individualistic):* **Goal-structure theory.** The claim derives from Deutsch's theory of cooperation and competition, operationalized by Johnson and Johnson: cooperative structures create "promotive interaction" (peers encourage and facilitate each other's efforts), whereas competitive structures create oppositional interaction and individualistic structures leave learners without peer support [+M]. The five elements of effective cooperative learning — positive interdependence, individual accountability, promotive interaction, social skills, and group processing — are the proposed moderators: groups lacking individual accountability or interdependence tend to collapse into parallel individual work, eroding the advantage [~M]. This connects to the broader pattern described in [Cooperative learning](../patterns/cooperative-learning.md) and to [Collaborative learning improves outcomes.](collaborative-learning-improves-outcomes.md), of which goal structure is one moderator.

**Boundary conditions.** The advantage is not automatic. Poorly structured group work can produce free-riding, status-based participation gaps, and off-task interaction [-M]; competitive structures may still motivate simple, well-practiced tasks or learners high in performance-approach orientation [~W]. The claim should be read as "well-designed cooperative learning outperforms competitive and individualistic structures," not "any group activity is better than none." Designers should attend to group composition, task design, and accountability mechanisms — see [Collaborative learning](../patterns/collaborative-learning.md) for the less-structured variant and how it differs.

**Open questions.** Most supporting evidence comes from K–12 and undergraduate settings in Western contexts; effects in adult professional training and across cultures with different norms around group vs. individual achievement remain less well established [~W]. The relative weight of achievement vs. relational outcomes (peer support, intergroup relations) also varies across studies, and the mechanisms linking promotive interaction to achievement — elaboration, peer explanation, mutual regulation — are consistent with [Social learning theory](../theories/social-learning-theory.md) and [Constructivism](../theories/constructivism.md) but have not been fully disentangled experimentally.

## Related Claims

- [Collaborative learning improves outcomes.](collaborative-learning-improves-outcomes.md) — the broader claim that group-based learning formats raise achievement, of which cooperative learning is the structured variant
- [Active learning improves exam performance.](active-learning-improves-exam-performance.md) — cooperative structures are one of the most common active-learning implementations
- [Assessment for learning improves achievement.](assessment-for-learning-improves-achievement.md) — individual accountability within cooperative groups is typically operationalized through formative assessment
- [Cooperative learning](../patterns/cooperative-learning.md) — the pattern page describing the design elements (interdependence, accountability, group processing) this claim depends on
- [Social learning theory](../theories/social-learning-theory.md) — theoretical grounding for learning through observation of and interaction with peers
- [Collaborative learning](../patterns/collaborative-learning.md) — related pattern; cooperative learning adds structured interdependence and accountability
- [Constructivism](../theories/constructivism.md) — situates cooperative learning within socially constructed knowledge-building
- [After the IDEAS academy, both studied teachers' classrooms moved toward more student-centered methods, with inquiry and collaborative learning emerging](academy-shift-toward-student-centered-methods.md) — a narrower finding that bears on this claim
- [Active and collaborative approaches promote higher-order thinking and complex reasoning (review attribution)](active-collaborative-approaches-higher-order-thinking.md) — related
- [Competitive (norm-referenced) grading pits students against one another and discourages cooperation, according to the author's argument](competitive-grading-pits-students-against-each-other.md) — related
- [Cooperation compared with individualistic efforts typically results in higher achievement, greater retention, and greater social competence and self-esteem](cooperation-versus-individualistic-effort-outcomes.md) — a broader claim this one bears on
- [Group rewards combined with individual accountability make cooperative learning effective](cooperative-learning-group-rewards-and-individual-accountability.md) — a narrower finding that bears on this claim
- [Meta-analyses by Johnson and Johnson find cooperative learning promotes higher achievement than competition or individual work across ages, subjects, and tasks](johnson-meta-analysis-cooperative-achievement.md) — a broader claim this one bears on
- [SEL Programs Improve Behavior And Achievement](sel-programs-improve-behavior-and-achievement.md) — related
- [Cooperative learning produces significantly greater achievement than traditional instruction in most long-duration controlled comparisons](cooperative-learning-achievement-synthesis-slavin.md) — related
- [Collaborative concept mapping enhances learning more than individual concept mapping, supporting Interactive over Constructive engagement](interactive-beats-constructive-concept-mapping.md) — related
- [Small Group Learning Improves STEM Achievement](small-group-learning-improves-stem-achievement.md) — related

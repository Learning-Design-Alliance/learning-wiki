---
type: claim
title: Civic Online Reasoning Instruction Improves Evaluation
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: civic-online-reasoning-instruction-improves-evaluation
aliases: [lateral-reading-improves-source-evaluation]
evidence_strength: weak
sources:
  - id: wineburg-et-al-2022
    resource: "https://doi.org/10.1037/edu0000740"
    title: "Wineburg, S., Breakstone, J., McGrew, S., Smith, M. D., & Ortega, T. (2022). Lateral reading on the open Internet: A district-wide field study in high school government classes. *Journal of Educational Psychology, 114*(5), 893–909. [doi:10.1037/edu0000740](https://doi.org/10.1037/edu0000740)"
    author: "Wineburg, S., Breakstone, J., McGrew, S., Smith, M. D., & Ortega, T."
    q: 2
    i: "?"
    n: 499 students (271 treatment, 228 control)
    kind: causal
    rigour: "?"
  - id: mcgrew-et-al-2019
    resource: "https://doi.org/10.1111/bjep.12279"
    title: "McGrew, S., Smith, M., Breakstone, J., Ortega, T., & Wineburg, S. (2019). Improving university students' web savvy: An intervention study. *British Journal of Educational Psychology, 89*(3), 485–500. [doi:10.1111/bjep.12279](https://doi.org/10.1111/bjep.12279)"
    author: "McGrew, S., Smith, M., Breakstone, J., Ortega, T., & Wineburg, S."
    q: 3
    i: "?"
    n: 67 students (29 treatment, 38 control)
    kind: causal
    rigour: 2
  - id: mcgrew-2020
    resource: "https://doi.org/10.1016/j.compedu.2019.103711"
    title: "McGrew, S. (2020). Learning to evaluate: An intervention in civic online reasoning. *Computers & Education, 145*, 103711. [doi:10.1016/j.compedu.2019.103711](https://doi.org/10.1016/j.compedu.2019.103711)"
    author: McGrew, S.
    q: 2
    i: "?"
    n: 68 students
    kind: causal
    rigour: "?"
---

# Civic Online Reasoning Instruction Improves Evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 3 studies · 3 causal `r2` · `q2`–`q3`

Explicit instruction in evaluating online information — including lateral reading, source checking, and attention to evidence — improves learners' ability to judge the credibility of web content.

## Subclaims

`q2 i?` In a district-wide field study, high school government students taught lateral reading in six 50-minute lessons grew significantly more than matched-control peers in judging the credibility of digital content. The abstract reports no effect size. [→ Wineburg et al. 2022](#wineburg-et-al-2022)

`q3 i?` In a small pilot in which four university course sections were randomly assigned, two 75-minute lessons on fact-checker heuristics made treatment students significantly more likely than controls to gain from pretest to a posttest given five weeks later. [→ McGrew et al. 2019](#mcgrew-et-al-2019)

`q2 i?` Eleventh graders given eight lessons on fact-checking strategies improved significantly on three of four constructed-response evaluation tasks, but the design had no control group. [→ McGrew 2020](#mcgrew-2020)

## Evidence

### Wineburg et al. 2022

Wineburg, S., Breakstone, J., McGrew, S., Smith, M. D., & Ortega, T. (2022). Lateral reading on the open Internet: A district-wide field study in high school government classes. *Journal of Educational Psychology, 114*(5), 893–909. [doi:10.1037/edu0000740](https://doi.org/10.1037/edu0000740)

`q2 · quasi-experiment, matched control design` · `i? · no effect size in abstract` · `n=499 students (271 treatment, 228 control)` · `causal · r?`

The researchers gave teachers professional development, and the teachers then taught six 50-minute lessons on [lateral reading](../strategies/lateral-reading.md) inside a required high school government course in an urban district. Lateral reading means leaving an unfamiliar website to search the open web before trusting the site. Students in treatment classrooms (n = 271) were compared with matched peers in regular classrooms (n = 228), using a multilevel linear mixed model. Treatment students grew significantly more in their ability to judge the credibility of digital content. The ERIC abstract calls the design a matched control design, while the authors' project page calls it cluster-randomized; it is coded here by the abstract, the more conservative reading.

### McGrew et al. 2019

McGrew, S., Smith, M., Breakstone, J., Ortega, T., & Wineburg, S. (2019). Improving university students' web savvy: An intervention study. *British Journal of Educational Psychology, 89*(3), 485–500. [doi:10.1111/bjep.12279](https://doi.org/10.1111/bjep.12279)

`q3 · randomised pilot experiment, four course sections assigned` · `i? · no effect size in abstract` · `n=67 students (29 treatment, 38 control)` · `causal · r2`

Four sections of a university critical-thinking-and-writing course were randomly assigned to treatment or control. Treatment students received two 75-minute lessons on evaluating the credibility of online content. The online-reasoning assessment was given six weeks before the lessons and again five weeks after. Treatment students were significantly more likely than controls to show gains from pretest to posttest. With only four sections randomised, this is a pilot, and the class-level evidence is thin.

### McGrew 2020

McGrew, S. (2020). Learning to evaluate: An intervention in civic online reasoning. *Computers & Education, 145*, 103711. [doi:10.1016/j.compedu.2019.103711](https://doi.org/10.1016/j.compedu.2019.103711)

`q2 · single-group pre/post design, no control` · `i? · no effect size in abstract` · `n=68 students` · `causal · r?`

Sixty-eight 11th-grade students took eight lessons on strategies for evaluating digital content, based on how professional fact checkers work. They completed pre- and posttests of four brief constructed-response items. Scores improved significantly on three of the four tasks: investigating a website's source, critiquing evidence, and finding reliable sources in an open internet search. With no comparison group, the gains cannot be separated from practice or maturation. The one task that did not improve is a limit on how general the effect is.

## Discussion

**Scope.** This claim concerns instruction in the strategies of professional fact-checkers — most prominently lateral reading (leaving a page to investigate the source elsewhere) rather than staying on the page and scrutinizing its features. Evaluation skill is treated as a teachable competence, not a fixed disposition. The contrast with checklist-based approaches is central: teaching students to inspect on-page features (URL endings, design polish, "About" pages) does not reliably improve evaluation of web content, whereas modeling how fact-checkers actually work does — see [Checklist evaluation is ineffective online.](checklist-evaluation-ineffective-online.md) [-M]

**Mechanism.** Lateral reading works because it offloads evaluation onto the web itself: rather than attempting to judge an unfamiliar source from its own self-presentation, learners use search to see what independent parties say about the source. This is a form of strategy instruction paired with modeling — akin to [cognitive apprenticeship](../patterns/cognitive-apprenticeship.md) [+M], where the expert's moves (open a new tab, search the source's name plus "funding" or "bias") are made visible and then practiced. Because the strategy is general-purpose rather than domain-specific, it can be taught with a small number of worked demonstrations and transferred to novel sites.

**Moderators and boundary conditions.** Effects likely depend on instructional dosage and authenticity: brief one-off lessons may produce knowledge of strategies without durable transfer to live browsing [~W], while embedded practice with real search tasks and authentic misinformation is more likely to change behavior. This is consistent with broader findings that [authentic audiences and purposes](../principles/authentic-audiences-purposes.md) raise the quality of student work [+M] — evaluation tasks feel consequential when learners judge real pages on the open web rather than sanitized examples. Learners' prior web fluency may also moderate gains: students who already habitually check sources have less room to improve, and strategy instruction may show expertise-reversal-like diminishing returns for the most skilled evaluators (cf. [Expertise reversal effect](../theories/expertise-reversal-effect.md)) [~M]. Evaluation of unfamiliar sources is also constrained by background knowledge; strategy instruction cannot fully substitute for domain knowledge when judging substantive claims, echoing the general dependence of comprehension on [activating prior knowledge](../principles/activation.md) [+S].

**Open questions.** Durability of gains over months, transfer across platforms and languages, and whether improved evaluation translates into changed civic behavior (sharing, voting, deliberation) remain under-studied relative to the measured evaluation outcomes themselves.

*Merged from “Lateral Reading Improves Source Evaluation” (lateral-reading-improves-source-evaluation):* **Mechanism.** Lateral reading treats the source itself as a claim to be verified rather than an authority to be consulted. Instead of scrutinizing a page's design, "About Us" text, or listed credentials — moves that professional-looking sites can easily fake — the reader opens new tabs and searches for independent coverage, the organization's reputation elsewhere, and whether its funding or affiliations are disclosed by third parties. This inverts the default behavior of most web users, who tend to read vertically, staying within the page and weighing on-page signals of trustworthiness.

**Relation to checklist approaches.** Traditional media-literacy instruction often teaches criterion-based checklists (look for an author, a date, a domain suffix). Checklist evaluation of unfamiliar web sources appears to be comparatively ineffective — see [Checklist evaluation is ineffective online.](checklist-evaluation-ineffective-online.md) — partly because the criteria can be satisfied by deceptive sites and partly because applying them keeps the reader on the page. Lateral reading replaces static criteria with an active search for corroboration, and is a core move in civic online reasoning curricula — see [Civic online reasoning instruction improves evaluation.](civic-online-reasoning-instruction-improves-evaluation.md). Related classroom strategies include the [A Finder's Guide to Facts](../strategies/a_finders_guide_to_facts.md) approach and the [3-source rule](../strategies/3-source_rule.md), both of which push learners off the page to triangulate claims across independent sources.

**Boundary conditions and open questions.** Lateral reading presupposes web access, search fluency, and at least some knowledge of which out-of-page sources are themselves reliable; a reader who laterally consults equally unreliable sites gains little. The strategy is also domain-dependent: it is well suited to evaluating organizations, news outlets, and advocacy sites, but less obviously applicable to evaluating a single primary source (e.g., a historical document) where no third-party coverage exists. How quickly the habit transfers from taught contexts to independent browsing, and how durable it is over time, remain open questions.

**Constraints on effectiveness.** The advantage of lateral reading depends on conditions that are not always present in classrooms or independent browsing:

- **Reliable reference sources required.** Lateral reading only works if the reader knows where to check — established encyclopedias, fact-checking services, mainstream news archives. Novices who laterally consult low-quality or partisan sites can end up less accurate than before, since the strategy lends false confidence to whatever they find. [-M]
- **Search fluency and working memory demands.** Juggling multiple tabs, formulating queries, and synthesizing cross-site information imposes significant [cognitive load](../theories/cognitive-load-theory.md); learners with weak search skills or limited working memory may default back to vertical reading under time pressure. [~M]
- **Poor fit for primary sources.** For a single historical document, dataset, or firsthand account with no third-party coverage, lateral moves yield little and may distract from close reading of the source itself. [~M]
- **Time and access constraints.** The strategy assumes open web access and time for multiple searches; in locked-down or offline assessment environments it cannot be practiced at all. [-W]

## Related Claims

- [Checklist evaluation is ineffective online.](checklist-evaluation-ineffective-online.md) — the common checklist approach (evaluating features on the page) fails for web content, motivating lateral-reading instruction instead.
- [Cognitive apprenticeship](../patterns/cognitive-apprenticeship.md) — modeling expert strategies then fading support is the instructional pattern underlying lateral-reading instruction.
- [Authentic audiences improve student work.](../claims/authentic-audiences-improve-student-work.md) — authentic evaluation tasks on the live web increase engagement and quality.
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — strategy instruction may yield diminishing returns for already-skilled evaluators.
- [Conversational synthesis can hide source plurality behind one voice, weakening verification relative to search](opaque-synthesis-hides-plurality.md) — related

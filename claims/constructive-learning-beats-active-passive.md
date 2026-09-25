---
type: claim
title: Constructive learning beats active and passive learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: constructive-learning-beats-active-passive
evidence_strength: low
sources:
  - id: chi-and-wylie-2014
    resource: "https://doi.org/10.1080/00461520.2014.965823"
    title: "Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist, 49*(4), 219–243. [doi:10.1080/00461520.2014.965823](https://doi.org/10.1080/00461520.2014.965823)"
    author: "Chi, M. T. H., & Wylie, R."
    q: 2
    i: "?"
    n: "multiple studies reviewed, incl. one original 4-condition lab study (materials science, Menekse et al. 2013) and one 3-condition study (plate tectonics, Gobert & Clement, 1999)"
  - id: wekerle-et-al-2024
    resource: "https://doi.org/10.1038/s41598-024-66069-y"
    title: "Wekerle, C., Daumiller, M., Janke, S., Dickhäuser, O., Dresel, M., & Kollar, I. (2024). Putting ICAP to the test: How technology-enhanced learning activities are related to cognitive and affective-motivational learning outcomes in higher education. *Scientific Reports, 14*, Article 16295. [doi:10.1038/s41598-024-66069-y](https://doi.org/10.1038/s41598-024-66069-y)"
    author: "Wekerle, C., Daumiller, M., Janke, S., Dickhäuser, O., Dresel, M., & Kollar, I."
    q: 2
    i: "?"
    n: 3,820 student assessments across 170 course sessions in 42 courses at one university
---

# Constructive learning beats active and passive learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment

Learning outcomes improve as learners move from passive to active to constructive engagement — generating ideas and outputs beyond what was presented — with constructive modes generally outperforming merely active ones.

## Subclaims

`q2 i?` The ICAP framework's own four-condition lab manipulation and its reinterpretation of paired-mode classroom and lab studies find learning outcomes rising from passive to active to constructive to interactive engagement, with constructive activities outperforming merely active ones. [→ Chi and Wylie 2014](#chi-and-wylie-2014)

`q2 i?` In authentic, technology-enhanced university classrooms, a large multilevel field study found empirical support only for the passive-vs-interactive endpoints of the ICAP hierarchy; the specific prediction that constructive activities outperform active and passive ones was not confirmed for either cognitive or affective-motivational outcomes. [→ Wekerle et al. 2024](#wekerle-et-al-2024)

## Evidence

### Chi and Wylie 2014

Chi, M. T. H., & Wylie, R. (2014). The ICAP framework: Linking cognitive engagement to active learning outcomes. *Educational Psychologist, 49*(4), 219–243. [doi:10.1080/00461520.2014.965823](https://doi.org/10.1080/00461520.2014.965823)

`q2 · narrative review with an embedded four-condition lab experiment and reinterpreted pairwise/three-mode studies` · `i? · no standardized effect size reported (only percentage-gain and rank-order comparisons)` · `n=multiple studies reviewed, incl. one original 4-condition lab study (materials science, Menekse et al. 2013) and one 3-condition study (plate tectonics, Gobert & Clement, 1999)`

Chi and Wylie's target article defines four modes of cognitive engagement — passive, active, constructive, and interactive (ICAP) — and predicts learning increases monotonically across them. In their own lab study manipulating all four modes in a materials-science lesson (reading only = passive; reading + highlighting = active; interpreting a graph = constructive; interpreting it jointly = interactive), learning gains rose in the predicted order across every mode step. In a separately reinterpreted plate-tectonics study, students who drew diagrams from text (constructive) outperformed those who wrote summaries (active), who in turn outperformed those who only read the text (passive), on both spatial and causal knowledge measures — directly supporting the constructive-beats-active-beats-passive ordering this claim states. The paper is a narrative/theoretical review rather than a meta-analysis, so effect sizes for the overall hypothesis are not pooled; the one quantified result reported for the four-mode study is a percentage learning gain per mode step, not a Cohen's d.

### Wekerle et al. 2024

Wekerle, C., Daumiller, M., Janke, S., Dickhäuser, O., Dresel, M., & Kollar, I. (2024). Putting ICAP to the test: How technology-enhanced learning activities are related to cognitive and affective-motivational learning outcomes in higher education. *Scientific Reports, 14*, Article 16295. [doi:10.1038/s41598-024-66069-y](https://doi.org/10.1038/s41598-024-66069-y)

`q2 · field study with multilevel structural equation modelling and statistical controls (not a manipulated experiment)` · `i? · no standardized effect size reported; findings are reported as significant/non-significant regression-weight comparisons` · `n=3,820 student assessments across 170 course sessions in 42 courses at one university`

87 university teachers reported which of the four ICAP-mode learning activities (passive, active, constructive, interactive) their students engaged in during a session, and students in those same sessions rated their perceived learning, situational interest, and joy; the two were linked through multilevel modelling. Only the interactive mode was associated with significantly better perceived learning than the other modes, and only the passive mode was associated with significantly lower joy — the constructive mode was not shown to outperform the active or passive modes on any outcome. The authors conclude that their data support the "end points" of the ICAP continuum (passive lowest, interactive highest) but do not confirm the specific constructive-over-active-over-passive ordering in authentic, technology-enhanced classroom settings, which qualifies the generality of this claim.

## Discussion

The core intuition behind this claim is that quality of engagement matters more than quantity of behavioral activity. A learner who is physically active — highlighting, copying, manipulating materials — may still be processing shallowly, while a learner who must generate an explanation, prediction, or self-constructed product is forced to make their understanding explicit and confront gaps in it. Generation imposes self-explanation and inference, which are the mechanisms most plausibly responsible for the constructive advantage.

Important boundary conditions follow from this framing. Constructive activity is only beneficial when the generated content is relevant and correct enough to build on; if learners lack the prior knowledge to generate anything substantive, construction can degenerate into unproductive search and cognitive overload [-S] — see [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) and [Cognitive Load Theory](../theories/cognitive-load-theory.md). This parallels the expertise-reversal pattern: what helps novices construct can burden them, and highly guided or even passive presentation can be optimal when material is high in element interactivity [~S] — see [Expertise reversal effect](../theories/expertise-reversal-effect.md). Conversely, for learners with adequate background, passive presentation risks the illusion of fluency — material seems clear while being studied but is not retrievable or usable later [-M].

A second moderator is the alignment between the constructive activity and the target outcome. Generation that emphasizes the wrong features (e.g., producing attractive artifacts rather than engaging with the to-be-learned relations) can consume working memory without improving learning [~M]. Designers should therefore treat "constructive" as a claim about cognitive processing, not about visible behavior: the goal is that learners generate ideas that go beyond the presented material in the direction of the learning goal. Activities such as [self-explanation](../elements/self-explanation.md), [drawing or sketching to explain](../strategies/drawing-to-learn.md), and [predict-then-observe tasks](../strategies/predict-observe-explain.md) are constructive precisely because their outputs force inference beyond the presented material; copying, verbatim note-taking, and rereading are active at best.

A third moderator is scaffolding and sequencing. Constructive activity tends to pay off when it follows some initial exposure to the material — e.g., studying a model or worked example before generating — rather than replacing it [~S]. This is the same logic that makes example–problem sequences effective for novices: [Example–problem sequences reduce cognitive load and improve learning outcomes.](example-problem-sequences-reduce-cognitive-load.md) Unguided construction placed too early in a learning sequence asks learners to generate before they have anything to generate from. [Activation](activation-improves-learning.md) of relevant prior knowledge before a constructive task serves the same function.

A fourth moderator is collaboration. Constructive engagement can be distributed: when learners co-construct explanations, arguments, or artifacts, each participant generates beyond what the material presented while being exposed to partners' constructions. This is the mechanism by which [collaborative learning improves outcomes](collaborative-learning-improves-outcomes.md) [~M] — but only when the collaboration is structured so that both generation and listening occur; unstructured group work can collapse into passive riding along, which is active or passive at best.

Open questions include how much scaffolding converts a failing constructive attempt into a productive one, and whether the passive–active–constructive ordering holds uniformly across domains or mainly in conceptually demanding ones. Empirical entries supporting the specific effect sizes still need to be added to this page.

## Related Claims

- [Active learning improves exam performance.](active-learning-improves-exam-performance.md) — the broader active-vs-passive contrast this claim refines
- [Collaborative learning improves outcomes.](collaborative-learning-improves-outcomes.md) — collaborative modes are a constructive mode in engagement hierarchies
- [Activation improves learning.](activation-improves-learning.md) — prior-knowledge activation supports productive construction
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — the load constraint on unguided construction
- [Example–problem sequences reduce cognitive load and improve learning outcomes.](example-problem-sequences-reduce-cognitive-load.md) — sequencing construction after example study for novices
- [Constructivism](../theories/constructivism.md) — the theoretical tradition underlying the constructive-learning claim
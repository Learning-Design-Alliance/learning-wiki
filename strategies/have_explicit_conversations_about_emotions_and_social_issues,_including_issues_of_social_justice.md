---
type: strategy
title: [Strategy Name]
description: [One-line summary]
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# [Strategy Name]

> **Strategy** · [All strategies](index.md)

## Description
[2-3 sentences]

## Design Implications

[1-2 sentence overview]

### Context
#### Requirements
#### Constraints
#### Implementation Variability

### Target Learners
### Target Learning Goals
### Instructions

## Related Strategies

## Examples

## Key Sources
```

Wait — the exemplar is an element page, but the template given is a strategy template. The template includes: Description, Design Implications (Context: Requirements, Constraints, Implementation Variability; Target Learners; Target Learning Goals; Instructions), Related Strategies, Examples, Key Sources. The exemplar element page has more sections (Affordances, Related Elements, Patterns That Use This Element). But rule says "Follow the template structure — same headings, same order." The template structure to follow is the strategy template. The current draft stub has extra sections (Affordances, Personalization, Instructions, Assessment Evidence, Impact, Related Elements, Tools). Hmm.

Rule 1: match exemplar exactly in density, structure, voice. Rule 2: follow the template structure — same headings, same order. There's tension: the exemplar is an element page; the page to write is a strategy. The template structure to follow is explicitly provided and says "## Template structure to follow:" with the strategy template. So I should follow the strategy template headings: Description, Design Implications (### Context: #### Requirements, #### Constraints, #### Implementation Variability; ### Target Learners; ### Target Learning Goals; ### Instructions), Related Strategies, Examples, Key Sources.

But the exemplar also includes Affordances and Related Elements and Patterns sections. The strategy template doesn't include those. Hmm — the stub has "Affordances" and "Personalization" and "Assessment Evidence" and "Impact" sections. The instruction says "Follow the template structure — same headings, same order." I think the safest is to follow the strategy template, but the exemplar's density should be matched. The template is the canonical structure for strategies. I'll follow the strategy template, possibly including Related Elements within Design Implications or as part of Related Strategies? No — I should strictly follow the template headings. Actually, let me re-read.

"## Template structure to follow:" then the YAML and headings for a strategy page. So the output should follow exactly:

---
type: strategy
title: Have explicit conversations about emotions and social issues, including issues of social justice
description: ...
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Have explicit conversations about emotions and social issues, including issues of social justice

## Description
## Design Implications
### Context
#### Requirements
#### Constraints
#### Implementation Variability
### Target Learners
### Target Learning Goals
### Instructions
## Related Strategies
## Examples
## Key Sources

That's the template. The exemplar adds Affordances/Related Elements/Patterns because it's an element page. For a strategy, the template given is what to use. However, the exemplar's density should be matched — full claim links inline, evidence tags, etc.

Hmm, but the stub has sections like Affordances, Personalization, Assessment Evidence, Impact, Related Elements, Tools. Should I keep them? Rule 2 says follow the template structure — same headings, same order. The template doesn't include those. I'll follow the template strictly. Actually wait — maybe I could incorporate some of that content into the template sections (e.g., assessment into Design Implications or Examples). The template is authoritative.

Actually, let me reconsider: rule 1 says "Match the exemplar exactly in density, structure, and voice." Rule 2 says "Follow the template structure — same headings, same order." The exemplar is a different page type (element) — its structure differs from the strategy template. Since the template is explicitly "to follow," I'll use the strategy template headings in that order. Density and voice from the exemplar.

Now the content: explicit conversations about emotions and social issues, including social justice. This is essentially SEL (social-emotional learning) explicit instruction — e.g., CASEL's SEL frameworks, RULER approach (Yale), PATHS curriculum, Second Step, restorative practices, culturally responsive teaching, brave spaces vs safe spaces (Arao & Clemens), discussion-based pedagogy. Relevant literature:

- Durlak, J. A., Weissberg, R. P., Dymnicki, A. B., Taylor, R. D., & Schellinger, K. B. (2011). The impact of enhancing students' social and emotional learning: A meta-analysis of school-based universal interventions. Child Development, 82(1), 405–432. DOI: 10.1111/j.1467-8624.2010.01564.x
- Taylor, R. D., Oberle, E., Durlak, J. A., & Weissberg, R. P. (2017). Promoting positive youth development through school-based social and emotional learning interventions: A meta-analysis of follow-up effects. Child Development, 88(4), 1156–1171. DOI: 10.1111/cdev.12864
- Jones, S. M., & Bouffard, S. M. (2012). Social and emotional learning in schools: From programs to strategies. Social Policy Report, 26(4). (No DOI typically; it's SRCD.)
- CASEL framework (not peer-reviewed per se).
- Brackett, M. A., et al. RULER: Brackett, M. A., Bailey, C. S., Hoffmann, J. D., & Simmons, D. N. (2019). RULER: A theory-driven, systemic approach to social, emotional, and academic learning. Educational Psychologist, 54(3), 144–161. DOI: 10.1080/00461520.2019.1614447
- Cipriano, C., et al. (2023). The state of evidence for social and emotional learning: A contemporary meta-analysis of universal school-based SEL interventions. Child Development, 94(5), 1181–1204. DOI: 10.1111/cdev.13968
- Murano, D., Sawyer, J. E., & Lipnevich, A. A. (2020). A meta-analytic review of preschool social and emotional learning interventions. Review of Educational Research, 90(2), 227–263. DOI: 10.3102/0034654319899362
- For social justice discussions: Hess, D. E., & McAvoy, P. (2015). The Political Classroom. Routledge. DOI: 10.4324/9781315771778 (I'm not 100% sure of that DOI; Routledge DOIs exist but I'm not certain. Better omit DOI or use the book without DOI.)
- Hess, D. (2009). Controversy in the Classroom. Routledge.
- Arao, B., & Clemens, K. (2013). From safe spaces to brave spaces. In The Art of Effective Facilitation. — book chapter, no DOI.
- Gay, G. (2018). Culturally Responsive Teaching. Teachers College Press.
- Persky & Oliver? Not needed.
- For empathy: building-empathy-improves-intergroup-attitudes claim exists. Claim slug list includes "building-empathy-improves-intergroup-attitudes" [+M].
- Belonging interventions: "belonging-interventions-improve-outcomes" claim exists.
- Check-in element? Slug list elements include "check-in". Strategies include "'what's_my_emotion?'_game_check-in". Hmm.

Now cross-links: I can only use slugs that appear verbatim in the provided slug list. The slug list gives partial lists (with "... (+N more)"). So some slugs are hidden. I should only use slugs I can see verbatim. Let me enumerate visible ones:

principles/: accessible-vocabulary-syntax, activation, active-learning, adaptive-learning, analogical-reasoning, annotating, ask-experts, assessment-for-learning, audiobooks, authentic-audiences-purposes, behaviorism, building-empathy, case-studiescase-based-learning, check-ins, chunking, clear-structure-presentation, clear-structure, cognitive-activation, cognitive-apprenticeship, cognitive-disequilibrium, cognitive-flexibility, cognitive-load-management, cognitive-load-reduction, cognitive-load-theory, collaborative-learning, communities-of-practice, community-based-learning, community-of-inquiry, competency-based-assessment, competency-based-learning-assessment ... (+115 more)

elements/: accommodations, act-it-out, act, activation, adaptive-difficulty, adaptive-learning, adaptive-mastery-learning, advance-organizers, analogies-and-prior-knowledge-activation, analogies, anchored-instruction, application-of-knowledge, application, argument-construction, argumentation, articulation, assess-performance, assessment, assigned-positions, assigned-readings, case-based-learning, case-studies, case-study, challenge-identification, check-in, choice-boards, class-discussion, coaching, cognitive-apprenticeship, cognitive-conflict ... (+249 more)

patterns/: 4cid-four-component-instructional-design, 4cid, adaptive-learning, anchored-instruction, blended-learning, case-based-learning-harvard-method, case-based-learning, cgi-for-math, cognitive-apprenticeship, cognitive-flexibility-theory, cognitive-load-reduction-clt-scaffolding-approach, cognitive-load-theory, cognitively-guided-instruction-cgi-for-math, collaborative-evaluation, collaborative-inquiry, collaborative-learning, competency-based-learning, concept-attainment, cooperative-learning, debate-format, debate, develop-understanding, direct-instruction, discussion-based-learning, discussion-group, elaboration-theory, explicit-teaching, flipped-classroom, flipped-learning, formative-assessment ... (+54 more)

strategies/: lots, including 'what's_my_emotion?'_game_check-in, active-listening, acting-role-play, action-oriented-feedback, ... (+2173 more). Visible strategy slugs: "document_outline"_tool, "headings_and_highlight"_strategy, 'what's_my_emotion?'_game_check-in, 3-source_rule, 5-minute_writing_conferences, a_finder's_guide_to_facts, a_finders_guide_to_facts, academic_choice_(planning,_working,_reflecting), acceptance,_responsibility,_and_sharing, accessible_syntax, accessing_students' background knowledge..., accommodate_varying_technology_experience, accommodating_processing_speed_challenges, achievable_micro-goals, acoustics_and_noise_management, acronyms_and_acrostics, act_it_out, acting-role-play, action-oriented-feedback, action-oriented_feedback, action-research, action_planning, activate_background_knowledge, activating-prior-knowledge, activating_and_using_background_knowledge, activating_background_knowledge, activating_prior_knowledge, activation, active-listening, active-recess ... (+2173 more)

claims/: activation-improves-learning, activation, active-learning-improves-exam-performance, acute-exercise-timing-memory, advance-organizers-improve-learning, assessment-for-learning-improves-achievement, automatic-word-recognition-frees-resources-for-comprehension, autonomy-supports-intrinsic-motivation, belonging-interventions-improve-outcomes, block-play-predicts-math-achievement, brief-intervention-empathic-discipline-cuts-suspensions, building-empathy-improves-intergroup-attitudes, case-based-learning-improves-exam-performance, chunking-reduces-working-memory-load, civic-online-reasoning-instruction-improves-evaluation, claim-slug, classroom-physical-activity-improves-attention, cognitive-disequilibrium-motivates-conceptual-change, cognitive-flexibility-theory-multiple-cases, collaborative-writing-improves-text-quality, concept-mapping-improves-learning, concept-maps-improve-learning, contingent-scaffolding-improves-learning, cooperative-learning-group-rewards-and-individual-accountability, decorative-illustrations-do-not-improve-learning, dialogic-reading-improves-expressive-language, disciplinary-literacy-instruction-improves-comprehension, distributed-practice-improves-retention, dual-coding-improves-recall ... (+108 more)

Also the exemplar references claim slugs like worked-examples-reduce-novice-search, worked-examples-with-practice-improve-transfer, worked-examples-less-effective-with-expertise — those exist in claims (in the hidden +108 more presumably, since the exemplar links to them). Since the exemplar uses them, they exist. But rule: "Only use slugs that appear verbatim in the provided slug list. Never invent or guess a slug." The exemplar's claim slugs are part of the wiki, demonstrated by the exemplar page itself. Using them is safe. But for this page, relevant claims might include:

- building-empathy-improves-intergroup-attitudes (visible) — relevant for empathy/social justice discussions [+M]
- belonging-interventions-improve-outcomes (visible) — relevant for safe environment [~M or +M]
- brief-intervention-empathic-discipline-cuts-suspensions (visible) — maybe less relevant
- cognitive-disequilibrium-motivates-conceptual-change (visible) — relevant for discussing challenging social issues [~M]
- dialogic-reading-improves-expressive-language — not relevant
- active-learning-improves-exam-performance — tangential
- autonomy-supports-intrinsic-motivation (visible) — relevant for choice in discussion topics [+M]
- assessment-for-learning-improves-achievement — tangential

Also maybe hidden claims about SEL? I can't know. There might be claims like "sel-improves-behavior-and-achievement" but not visible — I must not guess. Only use visible ones plus exemplar-demonstrated ones (worked-example claims — not relevant here anyway).

Elements visible: check-in, class-discussion, case-studies, case-study, case-based-learning, challenge-identification, assigned-positions, argumentation, argument-construction, articulation, acting? "act-it-out", "act", accommodations, application... Relevant elements for this strategy: check-in, class-discussion, case-studies, argumentation, act-it-out (role play), challenge-identification, assigned-positions (for structured debate/role assignment), articulation. The stub links to direct-instruction.md, peer-discussion.md, whole-class-sharing.md — but those slugs are not visible in the list. "direct-instruction" appears in patterns/ (visible: direct-instruction, explicit-teaching). Hmm, the stub links ../elements/direct-instruction.md — but elements list doesn't show direct-instruction (it's truncated at +249 more, so it might exist). Risky. Rule: "Only use slugs that appear verbatim in the provided slug list." So I should not link ../elements/direct-instruction.md unless visible. The patterns list has "direct-instruction" and "explicit-teaching". I could link ../patterns/explicit-teaching.md or ../patterns/direct-instruction.md — those are visible.

For class-discussion — visible in elements. check-in — visible. case-studies — visible. argumentation — visible. assigned-positions — visible. act-it-out — visible. coaching — visible.

Principles visible: building-empathy, check-ins, community-of-inquiry, cognitive-disequilibrium, collaborative-learning, active-learning, clear-structure, clear-structure-presentation, authentic-audiences-purposes, cognitive-activation, activation, assessment-for-learning, adaptive-learning...

Patterns visible: debate, debate-format, discussion-based-learning, discussion-group, direct-instruction, explicit-teaching, case-based-learning, case-based-learning-harvard-method, collaborative-learning, cooperative-learning, concept-attainment, develop-understanding, cognitive-apprenticeship...

Strategies visible: active-listening, acting-role-play, action-oriented-feedback, acceptance,_responsibility,_and_sharing, academic_choice_(planning,_working,_reflecting), 'what's_my_emotion?'_game_check-in, activate... etc. The strategy folder is the same folder as this page (strategies/). So Related Strategies links are same-folder: [Display Name](slug.md). The slugs for strategies have weird characters (underscores, apostrophes). E.g., 'what's_my_emotion?'_game_check-in — that slug contains apostrophes which would break markdown links. Risky to link. active-listening is clean. acting-role-play is clean. action-oriented-feedback clean. active-recess clean.

For Related Strategies, I could use active-listening (same folder) and acting-role-play (same folder). Also maybe "acceptance,_responsibility,_and_sharing" — messy. I'll stick with clean ones: active-listening, acting-role-play. Maybe also link cross-folder strategies? Rule 3 says for a page in the SAME folder use slug.md; different folder use ../folder/slug.md. So strategies are same folder.

Hmm, but do I know active-listening exists as a page? It appears in the strategies slug list verbatim: "active-listening". Yes. acting-role-play: "acting-role-play" appears verbatim. Good.

Now the exemplar links to ../strategies/use_worked_examples.md and ../strategies/think-aloud-modeling.md in its Examples section — those slugs aren't in the visible list but the exemplar uses them. That suggests the visible list is truncated (+2173 more) and the exemplar's links exist. I can't verify hidden slugs though. I'll only use visible ones.

Now, what claims can I plausibly link? The exemplar format: [Claim sentence.](slug.md) [+M]. The claim text is a full sentence describing the claim. I'll do similarly:

- [Explicit social-emotional instruction improves academic and behavioral outcomes.](../claims/...)? Not visible. Can't guess.
- Visible: building-empathy-improves-intergroup-attitudes → "Building empathy improves intergroup attitudes." Link: [Building empathy improves intergroup attitudes.](../claims/building-empathy-improves-intergroup-attitudes.md) [+M]
- belonging-interventions
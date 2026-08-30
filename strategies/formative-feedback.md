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

## Description
[What this strategy is and how it is carried out — 2-3 sentences.]

## Design Implications

[1-2 sentence overview connecting to learning science.]

### Context
#### Requirements
- [what is needed]

#### Constraints
- [conditions where effectiveness drops]

#### Implementation Variability
- [variations or adaptations]

### Target Learners
- [who benefits most]

### Target Learning Goals
- [types of objectives served]

### Instructions
1. [Step with links to elements]

## Related Strategies
- [Related Strategy](slug.md)

## Examples
- [Concrete example in a real context]

## Key Sources
- [APA citation with DOI link if available]
```

Wait, the exemplar has a different structure (it's an element, with Affordances, Related Elements, Patterns That Use This Element). But rule 1 says "Match the exemplar exactly in density, structure, and voice." And rule 2 says "Follow the template structure — same headings, same order."

There's tension: the exemplar is an element page; the page to write is a strategy page. The template structure to follow is the strategy template. I think the right approach: use the strategy template headings (Description, Design Implications with Context/Requirements/Constraints/Implementation Variability, Target Learners, Target Learning Goals, Instructions, Related Strategies, Examples, Key Sources), but match the exemplar's *density, voice, evidence-tag embedding, claim links, and cross-linking style*.

Hmm, but the exemplar also has an "Affordances" section linking to principles. The strategy template doesn't have that. The template given explicitly includes "### Instructions" with links to elements. I'll follow the strategy template strictly, since rule 2 says follow the template structure — same headings, same order. But I can enrich within that structure, matching density.

Actually, let me reconsider. The instructions say "Match the exemplar exactly in density, structure, and voice" AND "Follow the template structure — same headings, same order." The template is strategy-specific. Since the page type is strategy, the template structure governs headings; the exemplar governs density/voice/tagging. I could also incorporate affordance-like content... but the template doesn't have it. I'll stick to the template headings. Maybe I can include principle links within Design Implications prose (like the exemplar does with claim links inline).

Hmm, actually, looking more carefully — the exemplar includes frontmatter with sources listed. The template strategy frontmatter doesn't include sources in frontmatter. The stub frontmatter has:
```
---
type: strategy
title: Formative Feedback
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---
```

The template shows:
```
---
type: strategy
title: [Strategy Name]
description: [One-line summary of what this strategy is]
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---
```

I should update status to review, add description, set by to "claude/unspecified". The exemplar frontmatter includes a sources list; the strategy template does not. Hmm. The exemplar is the gold standard... I could include a sources frontmatter list like the exemplar. The template doesn't show it, but the exemplar does. Let me include it to match the exemplar — actually, wait. Rule 2: "Follow the template structure — same headings, same order." The template frontmatter is: type, title, description, status, generated (by, at). The exemplar frontmatter: type, title, description, status, generated, sources. I think including sources in frontmatter matches the exemplar and doesn't conflict with the template materially. I'll include a sources list in frontmatter like the exemplar does — it's consistent with "match the exemplar exactly."

Hmm, but the template explicitly shows the frontmatter without sources. Risky either way. The exemplar is called "gold-standard" — match quality exactly. I'll include sources in frontmatter since the exemplar does, formatted the same way.

Now, content. The CSV frames formative feedback for teachers (performance management). But the strategy name is just "Formative Feedback." In learning design wikis, formative feedback is usually about feedback to learners during instruction. The CSV description is specifically about teacher performance management with a growth mindset framing. Hmm.

The page should honor the CSV source data — it's about teachers receiving formative feedback on their teaching. But it could also generalize: formative feedback as a strategy applies to learners; here the "learners" are teachers in professional development. Actually, the CSV's target is "Teachers and educators at all levels, particularly those seeking to improve their teaching practices." The objectives are about improving teaching practices via feedback to teachers.

I think the best approach: write the page about formative feedback as a strategy whose primary framing here is feedback *to teachers* as professional learners (per the CSV), while drawing on the general feedback literature (Hattie & Timperley, Black & Wiliam, Shute). The feedback literature applies to teachers-as-learners too. I can note that the same principles govern formative feedback to any learner, and this page focuses on teacher-directed formative feedback within performance management/growth systems.

Actually wait — let me reconsider. Maybe the wiki intends "Formative Feedback" as a general strategy, and the CSV description is just a particular application (teacher evaluation). The elements list includes "Provide Feedback" as an element. The strategy could cover formative feedback generally with the teacher-performance context as the specific instantiation. Hmm.

Given the CSV is the source of truth for this page's content ("Use the CSV data... as your inputs"), I should center the teacher-performance-management framing but connect to the broader evidence base. The description in the CSV: "Teacher performance management processes can be viewed as part of a growth mindset by making it formative, rather than summative, and inviting participation of the teacher in the process. The feedback can be more meaningful and applicable to the teacher's daily practice."

So the page: Formative Feedback — feedback processes designed to improve performance (here, teaching practice) rather than to rate/evaluate it; iterative, participatory, growth-oriented.

I'll write it primarily about formative feedback in teacher development/performance management, but ground it in the general formative feedback literature (Hattie & Timperley 2007; Shute 2008; Black & Wiliam 1998). I can also mention that the same design rules apply to formative feedback for students — cross-link to relevant claims.

Available claim slugs (from the list, partial): I need to only use slugs that appear verbatim in the provided slug list. The claims list shown:
- activation-improves-learning
- activation
- active-learning-improves-exam-performance
- automatic-word-recognition-frees-resources-for-comprehension
- autonomy-supports-intrinsic-motivation
- block-play-predicts-math-achievement
- brief-intervention-empathic-discipline-cuts-suspensions
- building-empathy-improves-intergroup-attitudes
- case-based-learning-improves-exam-performance
- chunking-reduces-working-memory-load
- claim-slug
- cognitive-disequilibrium-motivates-conceptual-change
- cognitive-flexibility-theory-multiple-cases
- contingent-scaffolding-improves-learning
- cooperative-learning-group-rewards-and-individual-accountability
- decorative-illustrations-do-not-improve-learning
- dialogic-reading-improves-expressive-language
- dual-coding-improves-recall
- erroneous-examples-build-conceptual-knowledge
- example-problem-sequences-reduce-cognitive-load
- experimenter-underlining-effective-as-student-underlining
- expertise-reversal-effect
- expressive-writing-improves-health-outcomes
- fading-support-promotes-transfer-of-responsibility
- feedback-most-effective-at-task-and-process-levels
- fiction-reading-improves-empathy
- graphic-organizers-support-novice-comprehension
- high-confidence-errors-improve-retention
- intuitive-learners-outperform-sensing-learners
- joint-book-reading-predicts-literacy-success
- ... (+51 more)

The exemplar used these claim slugs: worked-examples-reduce-novice-search, worked-examples-with-practice-improve-transfer, worked-examples-less-effective-with-expertise. These aren't in the visible list but were used in the exemplar — the list is truncated ("+51 more"), so there are 85+ claims total. The exemplar's claim links presumably exist. For my page, the most relevant claim is clearly "feedback-most-effective-at-task-and-process-levels" — that's Hattie & Timperley's finding. That's in the visible list. 

Other potentially relevant claims I can see: "autonomy-supports-intrinsic-motivation" (feedback inviting participation — autonomy support), "contingent-scaffolding-improves-learning", "fading-support-promotes-transfer-of-responsibility", "erroneous-examples-build-conceptual-knowledge", "high-confidence-errors-improve-retention", "growth mindset" related? Not visible. "self-regulated-learning" theory page exists in theories.

I must be careful: only use slugs that appear verbatim. The visible ones I can safely use:
- feedback-most-effective-at-task-and-process-levels ✓ (perfect fit)
- autonomy-supports-intrinsic-motivation ✓ (participation/agency in feedback process)
- fading-support-promotes-transfer-of-responsibility (maybe for coaching fade)
- contingent-scaffolding-improves-learning (maybe)

The exemplar also linked to claims with full display names like "[Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]". So format: [Claim sentence.](slug.md) [+tag].

For "feedback-most-effective-at-task-and-process-levels", a claim sentence: "[Feedback is most effective when directed at the task and process levels rather than the self level.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]". The claim page title presumably is "Feedback most effective at task and process levels". The exemplar uses the claim text as display with a period. I'll write claim-display sentences that plausibly match the claim's content.

Now the slug list also includes principles, elements, patterns, strategies. Let me look at what's visible:

Principles visible (truncated at "...(+114 more)"): accessible-vocabulary-syntax, activation, active-learning, adaptive-learning, analogical-reasoning, annotating, ask-experts, assessment-for-learning, audiobooks, authentic-audiences-purposes, behaviorism, building-empathy, case-studiescase-based-learning, check-ins, chunking, clear-structure-presentation, clear-structure, cognitive-activation, cognitive-apprenticeship, cognitive-disequilibrium, cognitive-flexibility, cognitive-load-management, cognitive-load-reduction, cognitive-load-theory, collaborative-learning, communities-of-practice, community-based-learning, community-of-inquiry, competency-based-assessment, competency-based-learning-assessment...

"assessment-for-learning" is a principle — highly relevant! Formative assessment/feedback is assessment for learning.

Elements visible (truncated, +244 more): accommodations, act-it-out, act, activation, adaptive-difficulty, adaptive-learning, adaptive-mastery-learning, advance-organizers, analogies-and-prior-knowledge-activation, analogies, anchored-instruction, application-of-knowledge, application, argument-construction, argumentation, articulation, assess-performance, assessment, assigned-positions, assigned-readings, case-based-learning, case-studies, case-study, challenge-identification, check-in, choice-boards, class-discussion, coaching, cognitive-apprenticeship, cognitive-conflict...

"coaching" element — relevant. "assessment" — relevant. "check-in" — relevant maybe. The CSV says "elements: Provide Feedback" — so there's presumably an element "provide-feedback" or similar. It's not in the visible list, but the list is truncated (+244 more). The CSV explicitly lists "Provide Feedback" as the element. Should I link to it? Rule 3: "Only use slugs that appear verbatim in the provided slug list. Never invent or guess a slug." The slug list is truncated, so I can't verify "provide-feedback" exists. Risky. But the CSV says elements: Provide Feedback. Hmm. The slug would likely be "provide-feedback". But I can't verify. Safer to write plain text "Provide Feedback" or link to "assessment"? Actually, hmm.

The instructions for the template say: "### Instructions — 1. [Step with links to elements: [Element](slug.md)]". I need element links. Verified element slugs I can use: coaching, assessment, check-in, articulation, act-it-out... "coaching" is a great fit for personalized coaching mentioned in CSV personalization. "assessment" fits. "check-in" fits for feedback conversations? Maybe.

Let me be careful with the check-in slug: "check-in" is in the elements list. There's also "check-ins" in principles. For elements, use "check-in".

Patterns visible (truncated, +52 more): 4cid-four-component-instructional-design, 4cid, adaptive-learning, anchored-instruction, blended-learning, case-based-learning-harvard-method, case-based-learning, cgi-for-math, cognitive-apprenticeship, cognitive-flexibility-theory, cognitive-load-reduction-clt-scaffolding-approach, cognitive-load-theory, cognitively-guided-instruction-cgi-for-math, collaborative-evaluation, collaborative-inquiry, collaborative-learning, competency-based-learning, cooperative-learning, debate-format, debate, develop-understanding, direct-instruction, discussion-based-learning, discussion-group, elaboration-theory, explicit-teaching, flipped-classroom, flipped-learning, formative-assessment, fostering-communities-of-learning-fcl...

"formative-assessment" pattern exists! Highly relevant cross-link. Also "collaborative-evaluation" — relevant to peer observation. "competency-based-learning" maybe.

Strategies visible (truncated, +2072 more): lots of odd slugs. Relevant ones visible: action-oriented-feedback, action-oriented_feedback (both appear!), 5-minute_writing_conferences, action-research, action_planning, activate_background_knowledge... "action-oriented-feedback" is directly relevant to feedback strategy. Also "check-ins"? Not visible. "peer observation"? Not visible in the truncated list. Hmm.

For Related Strategies, I need same-folder links: [Display](slug.md). Visible strategy slugs that are relevant: "action-oriented-feedback" (and "action-oriented_feedback" — duplicate with underscore; I'll use the hyphenated one... actually both appear in the list, weird. The list shows: "action-oriented-feedback, action-oriented_feedback". Both verbatim. I'll use "action-oriented-feedback"). Also "action-research" is relevant (teachers investigating their own practice informed by feedback). "5-minute_writing_conferences" — feedback conferences, relevant-ish.

Hmm, but Related Strategies — should I link only to strategies I'm confident exist? The visible list is truncated at +2072 more, so many exist that I can't see. I should only use visible slugs to be safe. Relevant visible strategies:
- action-oriented-feedback
- action-research
- 5-minute_writing_conferences (weird formatting but verbatim)
- Maybe "check-ins"? Not visible. Skip.

Also there might be strategies like "peer-observation" not visible. Avoid.

Now Key Sources — real peer-reviewed sources with DOIs I'm confident about:

1. Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. DOI: 10.3102/003465430298487. This is a well-known DOI; I'm confident: https://doi.org/10.3102/003465430298487.

2. Shute, V. J. (2008). Focus on formative feedback. *Review of Educational Research, 78*(1), 153–189. DOI: 10.3102/0034654307313795. Confident.

3. Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. DOI: 10.1080/0969595980050102. Confident.

4. Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. DOI: 10.1037/0033-2909.119.2.254. Confident.

5. For teacher-specific feedback/coaching: Kraft, M. A., Blazar, D., & Hogan, D. (2018). The effect of teacher coaching on instruction and achievement: A
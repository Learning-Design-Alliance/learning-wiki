# Conversion wave 4 (2026-10-05)

The next 15 canonical pages by inbound links after wave 3 (`wave-3.md`), taken after the open findings of waves 1–3
were settled (#163). Pages that the triage marked canonical but that are stubs or duplicates of converted pages
(`patterns/adaptive-learning`, `principles/case-studiescase-based-learning`, `principles/competency-based-learning-assessment`,
`patterns/reflective-practice`, `principles/debate`, `patterns/game-based-mastery-learning`, `principles/peer-feedbackpeer-review`)
or theories filed as principles (`principles/situated-learning`) were skipped: they want a fold or a move, which is
the maintainer's call. `patterns/formative-assessment` was converted by #144 and is not in the list.

One agent per page from a single-page brief (scratch, not committed). It is the wave 3 brief with these additions:
- the dose and progression across sessions that the wave 3 rework added;
- a rule that the page is written for a designer who will not see it, so it names design moves, not its own section names;
- a rule for HTML comments in the old body: they cannot nest, so the deprecated block is closed before each existing comment and reopened after it.

| Page | Inbound | Converted neighbours placed | Situation rows (citing a claim) |
|---|---|---|---|
| patterns/experiential-learning-cycle | 13 | principles/experiential-learning, reflection | 12 (8) |
| principles/evaluating-sources | 12 | epistemic-cognition | 12 (7) |
| principles/ask-experts | 12 | communities-of-practice, cognitive-apprenticeship, scaffolding-and-fading | 13 (11) |
| principles/cultural-life-experiences-connections | 11 | activation, community-based-learning, authentic-audiences-purposes | 13 (8) |
| principles/universal-design-for-learning | 10 | multimodal-instruction, accessible-vocabulary-syntax, autonomy | 13 (10) |
| principles/social-interdependence | 10 | cooperative-learning, collaborative-learning | 12 (12) |
| principles/engagement | 10 | active-learning, cognitive-activation, autonomy, goal-setting-monitoring | 13 (11) |
| principles/deliberate-practice | 10 | guided-practice, retrieval-practice, immediate-feedback | 12 (9) |
| patterns/authentic-assessment | 10 | constructive-alignment, competency-based-assessment, authentic-audiences-purposes | 13 (7) |
| principles/graphic-organizers | 9 | clear-structure, chunking, activation | 12 (10) |
| principles/dual-coding | 9 | multimedia-learning, multimodal-instruction | 12 (11) |
| patterns/develop-understanding | 9 | gagnes-9-events, direct-instruction, activation, guided-practice | 12 (7) |
| principles/digital-learning | 8 | blended-learning, adaptive-learning, immediate-feedback | 12 (8) |
| patterns/collaborative-evaluation | 8 | structured-academic-controversy, assessment-for-learning | 11 (10) |
| principles/transfer-of-learning | 7 | analogical-reasoning, cognitive-flexibility | 12 (10) |

"Citing a claim" counts rows whose Basis cell links a claim. Several of those link one only for its limit, or carry
it to learners it did not test, and the cell says so.

**Checked by script, as in waves 1–3.** No old line was lost. No frontmatter key changed except `description`,
`status` and `generated`, apart from the DOI corrections below. No cited claim was dropped, every claim link carries
a marker, and no marker is above its cap. There are no broken links and every section is present. Every quoted
decimal or percentage is found on a cited claim page or the old page, with one exception: digital learning's 80%
move-on rule, which the page labels a proposal.

**No claim tests the page's relationship as a whole on 11 of the 15.** It is partly tested on four:
- evaluating sources: civic online reasoning lessons against untaught classes;
- graphic organizers: concept-map meta-analyses and two story-map designs;
- dual coding: a meta-analysis of supplied visuals, and drawing and concept-map syntheses;
- social interdependence: group rewards tied to individual learning, and one null on interdependence type.

Every page keeps a labelled default design or sequence with doses and a plan across 4–8 sessions or weeks.

**Markers lowered to their caps**, where the old pages had them above:
- `specific-difficult-goals-lead-to-higher-performance`: one q2 review, [S] → [M], on four pages;
- `whole-task-performance-improves-transfer`: [S] → [M] or [W], on two pages.

The verbatim old bodies keep the old markers. Where a retitled claim now cuts the other way, the converted page cites
it with a different direction:
- activation and advance organizers: `+` → `~`;
- concept mapping against time-matched retrieval: `+` → `~`.

## Citations corrected in passing (Crossref: first author, year, title)

As in #163, each was a frontmatter `resource:` that disagreed with the Key Sources line, and the frontmatter was the
wrong side:
- Rapchak et al. (2015): `…594150` is a book review by Zarestky.
- Singleton & Filce (2015): `…603129` has no record.
- MacArthur & Lembo (2009): `…9133-5` has no record.
- Hansman (2001): `ace.6` is Hayes's chapter in the same issue.
- Papen & Tusting (2019): `…1600504` has no record.
- Capp (2017): the frontmatter named *Review of Educational Research* 87(4) with a DOI that has no record; it is
  *International Journal of Inclusive Education* 21(8) 791–807, `10.1080/13603116.2017.1325074`.

**Left unchanged:**
- Wiggins (1989) on authentic assessment: the DOI on the page is the 2011 reprint in *Phi Delta Kappan* 92(7), and
  Crossref has no record of the 1989 original.

## Brief test (2026-10-05)

Same design as waves 1–3 (scratch only). 30 briefs were written by GPT 5.6 Luna from each page's title and one-line
description before any draft existed, one complete and one sparse per page, each set where its facts should change
the design:
- a debrief for care coordinators after a simulated crisis call;
- community health workers judging WhatsApp health claims;
- a hybrid makerspace repair class;
- tenant-advice volunteers at a legal-aid centre.

Kimi K3 answered from one version of the page (OLD = main after #163, NEW = this change). Gemini 3.8 Flash and
DeepSeek V4 Pro graded each answer against a digest of every claim either version cites (title, evidence line,
subclaims), then judged blind pairs in both orders.

**One change to the answer prompt.** It now says to write for a designer who has not seen the page and never to refer
to "the page", its sections, steps or tables. Wave 3 found answers citing "page, step 4" marked down, which biased the
comparison towards the old pages. Scores are therefore not strictly comparable with earlier waves.

$6.85 in all: $3.68 for answers, including the regenerated ones; $2.65 for grading; $0.51 for the rework re-test; $0.01 for briefs.

**Three NEW answers, and no OLD one, were cut off mid-sentence** at the answerer's 4,000-token limit:
- experiential learning cycle, complete brief;
- deliberate practice, complete brief;
- develop understanding, sparse brief.

The new pages are longer, so the answering model's reasoning used more of the budget. A fourth NEW answer (develop
understanding, complete) was cut off as well and was regenerated before grading. Graders called the cut answers
incomplete, and both complete briefs above were lost 0–4. The three were regenerated with a 16,000-token limit and
their briefs re-graded. Both sets are reported:

| | OLD | NEW (raw) | NEW (cut answers regenerated) |
|---|---|---|---|
| affordances /12 (all / complete / sparse) | 5.6 / 6.2 / 4.9 | 8.7 / 9.4 / 8.1 | 9.1 / 9.9 / 8.3 |
| accuracy (1–5) | 3.33 | 4.02 | 4.08 |
| decision value (1–5) | 4.12 | 4.42 | 4.50 |
| brief fit (all / complete / sparse) | 4.33 / 4.53 / 4.13 | 4.42 / 4.47 / 4.37 | 4.47 / 4.53 / 4.40 |
| situation fit, anchored (all / complete / sparse) | 4.03 / 4.47 / 3.60 | 4.33 / 4.53 / 4.13 | 4.38 / 4.57 / 4.20 |
| blind pairs NEW–OLD (all / complete / sparse) | | 81–39 / 36–24 / 45–15 | **86–34 / 40–20 / 46–14** |

**What the numbers say:**
- **The new pages win, by less than in earlier waves** (101–19, 113–7, 100–20). The margin is narrower on complete
  briefs, 40–20.
- **Fit is up, mostly on sparse briefs**: situation fit 3.60 → 4.20 and brief fit 4.13 → 4.40. Waves 2 and 3 had
  gained only on complete briefs. This is the first wave where sparse answers became more fitted. Plausibly the cause
  is the "Inputs: establish the design brief" and situation sections, which make the answer ask for or assume the
  missing facts. It could also be the prompt change.
- **Accuracy rose by about as much as in wave 3** (3.33 → 4.08, against +0.45 there).
- **Decision value rose least of the four waves** (+0.38): the old pages already gave answers a concrete plan.
- **DeepSeek picked the answer shown first in 48 of 60 pairs**, so most of the pairwise signal is Gemini's. Gemini
  picked first in 26 of 60. All four judgements agree on 6 of 30 briefs.

**Where the new page lost or tied** (counts are NEW–OLD, after regeneration):
- **ask-experts, complete brief: 1–3.** Both graders preferred the old answer's handling of four learners joining by
  phone: each paired with an in-room buddy, against the new answer's recorded think-aloud and written reply afterwards.
- **authentic-assessment, complete brief: 1–3.** Both preferred the old answer's split of the tenant advice pack
  (for the client) from a decision memo (for the supervisor), which assesses the reasoning without distorting the
  product.
- **Ties at 2–2**:
  - authentic assessment, sparse brief;
  - experiential learning cycle, both briefs;
  - deliberate practice, complete brief;
  - digital learning, sparse brief;
  - evaluating sources, complete brief.
- **Neither winning move was on the old page**; the answerer brought it from general practice. They are the kind of
  setting-specific move the situation table exists for, and both tables lacked the row.

## Rework (2026-10-05)

Each losing page gained one situation row, labelled an untested proposal:
- **ask-experts**: when some learners join remotely, keep them in the live exchange. Take their questions first, pair
  each with an in-room partner who relays, and have the expert say aloud what they see and check.
- **authentic-assessment**: when the product goes to a client or audience who should not see the working, split the
  submission into the product (scored on audience criteria) and a short decision memo for the assessor (scored on
  reasoning), and revise both.

Re-tested on the two complete briefs: two fresh NEW answers each against the same OLD answer, with both graders
and both orders ($0.51):

| Brief | Wave 4 | After rework (answer 1, answer 2) |
|---|---|---|
| ask-experts, complete (hybrid makerspace) | 1–3 | **3–1**, 2–2 |
| authentic-assessment, complete (legal-aid volunteers) | 1–3 | **3–1**, **4–0** |

Graders now credited the relay partner for the phone learners and the separate decision memo. Gemini still preferred
the old ask-experts answer in three of four judgements. Its reasons were the old answer's clustering of appliances
by fault, so that every learner gets expert feedback in 30 minutes, and its norms against "stupid questions". DeepSeek
preferred the new answer in all four. **One missing situation row can lose a brief.** The table is where a page
earns its fit, and rows for the hybrid setting and for a product whose audience should not see the working were
both missing.

## Open findings from the agents

**Claim titles that overstate their evidence:**
- `peer-feedback-accuracy-depends-on-expertise`: its own Discussion says so.
- `learner-constructed-graphic-organizers-outperform-provided`: Stull & Mayer's direct evidence runs against it.
- `peer-assessment-structured-criteria-improve-learning`: its opening paragraph still asserts the old title.
- `misconceptions-interfere-with-new-learning`: it tests interventions, not interference.
- `interleaving-improves-transfer`: its evidence is classifying new category examples.
- `deliberate-practice-improves-performance`: one correlational meta-analysis.
- `teacher-student-relationships-improve-engagement-and-achievement`: correlational, and states a cause.
- `incorporating-home-culture-improves-academic-performance`: no data.
- `sms-vocabulary-learning-beats-paper-materials`: a whole-medium comparison.
- `dual-coding-improves-recall`: the outcome is comprehension.
- `engineering-rubric-low-scoring-reliability`: one class.
- `far-transfer-floor-effect-and-equal-time`: bundles two findings.
- `reward-interdependence-benefit-attitudes` and `high-affiliation-motive-favorable-group-attitudes`: say "adult
  learners" where Brewer & Klein (2003)'s entries say undergraduate business majors.

**Stale "no evidence yet" text beside entries:**
- `self-explanation-improves-conceptual-understanding`: the merged Open-questions paragraphs from #163's folds.
- `concept-mapping-improves-learning`
- `cognitive-disequilibrium-motivates-conceptual-change`
- `assessment-for-learning-improves-achievement`
- `rubrics-improve-student-work`: its opening; #163 fixed only its later sentences.
- `rubrics-improve-peer-feedback-quality`
- `peer-assessment-benefits-assessor`
- `peer-assessment-improves-performance`
- `drawing-improves-learning`
- `decorative-illustrations-do-not-improve-learning`
- `learner-constructed-graphic-organizers-outperform-provided`
- `dual-coding-improves-recall`
- `feedback-most-effective-at-task-and-process-levels`
- `belonging-interventions-improve-outcomes`
- `self-affirmation-improves-outcomes`
- `positive-greetings-at-the-door-improve-engagement`
- `teacher-student-relationships-improve-engagement`
- `goal-setting-improves-performance`: its "placeholder" opening.
- `small-group-learning-improves-stem-achievement`
- `cooperative-learning-group-rewards-and-individual-accountability`
- `retrieval-practice-improves-transfer`
- `principles/epistemic-cognition`: still calls lateral reading and civic online reasoning a merge candidate; they were
  merged in #163.

**Merge candidates:**
- `peer-feedback-improves-work-quality` and `peer-assessment-improves-performance` (one entry, one subclaim);
- `teacher-student-relationships-improve-engagement` and `…-and-achievement`;
- `dual-coding-improves-recall` and `dual-coding-improves-learning`;
- `seductive-details-effect` and `seductive-details-distract-from-learning`;
- the two `tutor-background-…` claims (Walker & Leary 2023);
- `cooperative-learning-group-rewards-and-individual-accountability` and `cooperative-learning-free-rider-without-accountability`;
- `education-dp-4-5-percent-variance` into `deliberate-practice-improves-performance`;
- `interleaving-improves-transfer` and `interleaving-improves-inductive-learning`;
- the principle `creating-visual-representations` against dual coding and graphic organizers.

**Codes to recheck:**
- `minimal-guidance-less-effective-for-novices` codes Alfieri et al. (2011), a meta-analysis, as `design · r3`.
- Nesbit & Adesope (2006) is `q4 i2` on one claim and `q3 i?` on another.
- Chi et al. (2001) is q3 on `contingent-scaffolding-improves-learning` and q2 on `tutoring-effectiveness-…`.
- `germane-load-gains-limited-…` has `i0` beside a null with no effect size, and a Google Scholar search link for a
  citation.
- `positioning-personal-experience-as-epistemic-resource…` has `i1` on an entry that says "not a quantified effect size".
- Three deliberate-practice claims come from one dissertation linked by a search URL.

**Wrong claim cited or labelled:**
- The old authentic-assessment page, `rubrics-improve-student-work` and `peer-assessment-structured-criteria-…` cite
  the CRAAP checklist claim as evidence that rubrics breed compliance, which it does not test.
- `computer-based-no-better-than-individual-paper` labels its sibling from the same study "reports the opposite".
- The learning-styles claim links "meshing hypothesis" to `theories/dual-coding-theory`.

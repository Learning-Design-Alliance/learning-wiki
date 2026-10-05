# Conversion wave 6 (2026-10-05)

The next 15 canonical pages, ranked by inbound links from content pages. Index pages, `log.md` and revision cards
no longer count, since they inflated the ranking. These are the last pages of the conversion core: after them, no
unconverted canonical principle or pattern has more than five such links, apart from the pages skipped below.

**Folded beforehand** (`merge_pages.py`, across kinds where noted):
- `principles/self-determination-theory` into `theories/self-determination-theory`: a theory in all but folder.
- `principles/reinforcement-theory` into `theories/behaviorism`, the same way. The fold stamped an `id:` and an alias
  on the theory; both were removed, since theories carry no id and an alias cannot cross kinds.
- The stub patterns `journaling`, `inquiry-based-learning` and `summative-assessment` into their principles.

**Skipped:**
- `patterns/game-based-mastery-learning`: misfiled.
- `patterns/peer-teaching`: a stub with no clear fold target.
- The four critical-communication-pedagogy principles and `patterns/shared-power-co-creation-of-educational-systems`:
  source-framed stances that link mostly to each other.

Same brief as wave 5, with three additions:
- **Wave 5's lessons.** Add a row for scarce facilitator time. Add a row saying that when a brief names its own
  routine, the page keeps it and changes only what the evidence says matters.
- **A `## Design Decisions` section stays live**, after the model sections.

| Page | Situation rows (citing a claim) |
|---|---|
| principles/journaling | 16 (13) |
| principles/gamification | 17 (8) |
| principles/debriefing | 16 (8) |
| principles/note-taking | 16 (8) |
| principles/functional-behavior-assessment | 16 (7) |
| principles/multiple-methods-of-assessment | 18 (9) |
| principles/supporting-students-with-intellectual-disabilities | 16 (11) |
| principles/summative-assessment | 15 (8) |
| principles/standardized-test-fairness-and-bias | 15 (8) |
| principles/motivation | 16 (12) |
| principles/knowledge-organization | 17 (13) |
| principles/culturally-responsive-classroom-norms | 16 (10) |
| patterns/professional-development | 14 (12) |
| patterns/learning-by-producing-pattern | 14 (9) |
| patterns/experience-with-languaging-activities | 16 (8) |

Counts are after the rework below. Rows citing a claim mostly carry a finding to a setting it did not test, and say so.

**Checked by script, as before:**
- No old line lost.
- No frontmatter key changed except `description`, `status` and `generated`, apart from the DOI corrections below.
- No cited claim dropped, and no marker above its cap. Two links were missing markers; the coordinator added them.
- No broken links.
- Every quoted number is on a cited claim or the old page. The exceptions are thresholds labelled as proposals and one
  invented illustration (gamification's "80% recall" objective).

**Which claims test each page's relationship:**
- **Partly tested on three pages:**
  - gamification: a meta-analysis of gamified against non-gamified instruction, g = .49 on cognitive outcomes, with
    motivational effects not holding in the rigorous studies;
  - knowledge organization: Eylon & Reif's (1979) hierarchical-organization experiments with physics students;
  - note-taking: guided notes only.
- **Untested on the other twelve.** Each keeps a labelled default design with doses across sessions.

**Markers lowered to cap:** `self-efficacy-predicts-academic-persistence` and
`specific-difficult-goals-lead-to-higher-performance` [S] → [M] on motivation. `whole-task-performance-improves-transfer`
[~S] → [~W] on summative assessment and [+M] → [+W] on multiple methods: it is a design argument, not a study.

## Citations corrected in passing (Crossref)

Frontmatter `resource:` lines that disagreed with Key Sources, where the frontmatter side was wrong each time:
- note-taking: Hughes & Suritsky (1994), `…700104` (Opp's paper in the same issue) → `10.1177/002221949402700105`.
- journaling:
  - Larrotta (2009), `ace.325` (another chapter) → `10.1002/ace.323`;
  - Sage & Sele (2015), `…1076264` (no record) → `10.1080/10437797.2015.1076274`.
- debriefing: Secheresse et al. (2021), `…102967` (no record) → `10.1016/j.nepr.2020.102914`.

## Brief test (2026-10-05)

Same design as wave 5.
- **Briefs:** 30, written by GPT 5.6 Luna from each page's title and description before any draft existed.
- **Answers:** Kimi K3, 16,000-token limit.
- **Grading:** Gemini 3.8 Flash and DeepSeek V4 Pro, scored answers and blind pairs in both orders.
- **Cost:** $3.51 for answers, $2.12 for grading, $1.05 for the three rework re-tests.

| | OLD | NEW |
|---|---|---|
| affordances /12 (all / complete / sparse) | 5.7 / 7.5 / 4.0 | 9.6 / 10.4 / 8.8 |
| accuracy (1–5) | 3.18 | 3.80 |
| decision value (1–5) | 3.72 | 3.97 |
| brief fit (all / complete / sparse) | 4.08 / 4.13 / 4.03 | 4.10 / 3.90 / 4.30 |
| situation fit, anchored (all / complete / sparse) | 3.80 / 3.93 / 3.67 | 4.05 / 3.87 / 4.23 |
| blind pairs NEW–OLD (all / complete / sparse) | | **86–34 / 37–23 / 49–11** |

**What the numbers show:**
- **The smallest gains of the last three waves.** Accuracy rose 0.62 and decision value 0.25. Fit rose on sparse
  briefs and fell slightly on complete ones.
- **The graders disagree on level:**
  - Gemini scores NEW higher on every measure (accuracy 3.97 → 4.90);
  - DeepSeek scores NEW lower on decision value and fit (3.40 → 3.20), and picked the answer shown first in 43 of
    60 pairs.
- **The pairwise wins are mostly on sparse briefs.** On complete briefs the old pages' concrete plans held up: six
  complete briefs were lost or tied. All four judgements agree on 10 of 30 briefs.

**Where the new page lost or tied:**
- **Lost 1–3** (complete briefs unless stated): note-taking (complete and sparse), journaling, multiple methods of
  assessment, summative assessment.
- **Tied 2–2**: languaging activities, debriefing and gamification (complete); multiple methods (sparse).

## Rework

Each loss was a design that did not fit the brief's setting:
- **Note-taking, complete** (nursing assistants preparing a handover): answers used fill-in-the-blank guided notes.
  Graders preferred the old answer's reusable shift grid, built from the brief's own four categories.
- **Note-taking, sparse** (older adults in a library workshop): answers used a closed-note memory check.
  Graders preferred judging the notes by use.
- **Journaling** (care assistants writing on phones): the scaffold did not map onto the brief's rubric. Answers had
  the trainer read entries, where the old answer let learners choose which anonymised entries anyone reads.
- **Multiple methods** (two 90-minute sessions, one assessor): answers overpacked the sessions.
- **Summative** (a high-stakes ambulance scenario): answers split the whole-task scenario into paper items.

Rows added, each an untested proposal:
- **Note-taking:**
  - adults whose notes become a job aid: a reusable grid in the brief's own categories, a 75-minute session plan with
    sentence frames for second-language learners, and a check by briefing a partner;
  - a take-home aid evaluated without a test: judge it by use, on the learner's own device.
- **Journaling:** the brief gives its own criteria and entries are private on phones. Map the scaffold to the criteria
  line for line, keep it to five lines, and let the learner choose which entries anyone reads.
- **Multiple methods:** little time and one assessor. Use two methods, run them as a rotation, and write an evidence
  matrix in advance.
- **Summative:** keep a single whole-task scenario as the judgment, put recall checks in the practice before it, and
  prompt decisions aloud.

| Brief | Wave 6 | Rework 1 | Rework 2 | Rework 3 |
|---|---|---|---|---|
| note-taking, complete | 1–3 | 1–3 | 1–3 | **4–0** |
| note-taking, sparse | 1–3 | 1–3 | 1–3 | **3–1** |
| journaling, complete | 1–3 | 0–4 | **3–1** | |
| multiple methods, complete | 1–3 | 1–3 (answer cut off) | **3–1** | |
| multiple methods, sparse | 2–2 | **3–1** | | |
| summative, complete | 1–3 | **3–1** | | |

Each re-test regenerates one NEW answer, so a single result is noisy.

**What the reworks show:**
- **The same lesson again, from a new angle: a page loses when its rows assume a setting the brief does not have.**
  Note-taking won once its row used the brief's own categories and avoided device swapping. Journaling won once it
  left learners in control of who reads their entries.
- **One answer was cut off.** It stopped mid-sentence at 533 words even with the 16,000-token limit. A cut-off answer
  loses its pairs, so check the endings before reading a loss.

## Open findings from the agents

**Duplicate claims:**
- `summarization-effective-with-training` and `summarization-improves-learning` share the same two entries.
- `pbis-reduces-clinically-significant-behavior-problems` and `pbis-reduces-externalizing-total-problems-ed-self-contained`
  rest on one study (Benner 2008).
- `overjustification-effect-reduces-intrinsic-motivation` and `rewards-undermine-intrinsic-motivation`.
- `autonomy-supports-intrinsic-motivation` and `autonomy-support-versus-controlling-teaching`.
- `johnson-meta-analysis-cooperative-achievement` and `cooperative-learning-higher-achievement-than-competitive-individualistic`.
- `generative-learning-improves-retention` and `generative-processing-improves-learning`: both rest only on a
  self-explanation meta-analysis.
- `retrieval-practice-produces-more-learning-than-concept-mapping…`: repeats an entry on `concept-mapping-improves-learning`.
- `increasing-wait-time-improves-response-quality` and `questioning-strategies-improve-learning`: both rest on Tobin (1987).
- Bangert-Drowns et al. (2004) is coded `i2` on `reflective-practice-improves-outcomes-when-structured` and `i?` on
  `writing-to-learn-improves-understanding`.

**Overstated titles:**
- `laptop-notes-verbatim-shallower`: its replication failed.
- `teacher-expectation-effects-on-achievement`: causal, from one associational study.
- `math-anxiety-degrades-performance`: causal, from correlations.
- `low-stress-tbl-higher-isat-scores`: two non-randomised cohorts.
- `growth-mindset-improves-achievement`: d = .11, coded `i0`.
- `interactive-beats-constructive-concept-mapping`: second-hand.
- `funds-of-knowledge-tasks-reveal-computational-thinking`: no comparison.
- `test-scores-gate-gifted-program-entry` and `minority-females-doubly-penalized-on-tests`.
- `direct-experience-questions-stimulate-thinking`: a q1 document.
- `learning-strategy-instruction-contextualized-more-effective`: contradicted by its only evidence.
- `peer-coaching-supports-teacher-professional-development`.
- The Mangomon "significantly improved": pre–post, no control.

**Stale "no evidence" text:**
- `rewards-undermine-intrinsic-motivation`
- `cognitive-overload-degrades-learning`
- `collaborative-learning-improves-outcomes`
- `expressive-writing-improves-health-outcomes`
- `brief-intervention-empathic-discipline-cuts-suspensions`
- `growth-mindset-improves-achievement`
- `summarization-effective-with-training`

**Codes:**
- **An `i` code with no effect size printed:**
  - the Eylon & Reif claims (`hierarchical-organization-…`, `strong-acquisition-tasks-…`, `higher-hierarchy-levels-…`,
    `ability-moderates-…`);
  - `psat-national-merit-awards-skew-male`;
  - `gifted-underrepresentation-diverse-students`;
  - `low-fidelity-pbis-smaller-student-improvements`, which codes an authors' interpretation `i3`.
- **Second-hand or web-sourced, coded q2:** `behaviorist-reinforcement-effective-positive-behavior`.
- **Inconsistent across pages:** Cameron & Pierce (1994) q4/q3; Deci et al. (1999) i1/i2.
- **Header against subclaim:** `self-efficacy-accuracy-lower-in-learning-settings`, `i1` against `i?`.

**Citations:**
- Sturgill & Motley (2014): a Google Scholar link on three claims.
- The 1974 criterion-referenced claims: no author, a bare ERIC link.
- `grading-harms-maker-education-outcomes`: its heading says Lundberg, its citation Lundberg & Rasmussen.
- Freedle (2002) on test fairness: probably 2003.
- Van de Sande (2013) on the BKT claims (from #167).

**Links and labels:**
- `strategies/functional-behavior-assessment` cites "function-based treatments outperform…" but links the feedback-levels
  claim. It also carries bare markers.
- `exam-questions-concentrate-lower-bloom-levels` labels a different population "reports the opposite".
- `activation-improves-learning` links to itself.

**Fold candidates:**
- `principles/multimedia-literacy-through-production` and `principles/multimedia-projects`, into the
  learning-by-producing pattern.
- `elements/debriefing` and `strategies/debriefing`, beside `elements/debrief`.

**Sources with no claim page:**
- Kraft et al. (2018), the coaching meta-analysis.
- Darling-Hammond et al. (2017), the professional-development review.
- Hughes & Suritsky (1994).
- Secheresse et al. (2021).

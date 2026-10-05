# Conversion wave 7 (2026-10-05)

This is the first wave below the conversion core: 15 canonical principles with 3–5 inbound links each from content
pages. As in earlier waves, the source-framed stances (the four critical-communication-pedagogy principles, the
rightful-presence pages), misfiled pages (`patterns/game-based-mastery-learning`) and stubs with no fold target
(`patterns/peer-teaching`) were skipped.

The brief was the same as wave 6's, with one addition: **wave 6's lesson**. Rows must take the brief's own categories,
criteria, privacy terms, time budget and whole-task performances as given. Every page has those rows.

| Page | Situation rows (citing a claim) |
|---|---|
| principles/sequencing | 22 (12) |
| principles/social-presence | 20 (10) |
| principles/procedural-learning | 19 (12) |
| principles/positive-self-talk | 21 (9) |
| principles/observationshadowing | 18 (11) |
| principles/memory-consolidation | 18 (8) |
| principles/explicit-instruction-vocabulary | 15 (8) |
| principles/effective-classroom-management-plan | 21 (9) |
| principles/developing-your-cultural-awareness | 17 (9) |
| principles/criterion-and-norm-referenced-testing | 21 (7) |
| principles/flipped-learning | 20 (5) |
| principles/flexible-grouping | 16 (7) |
| principles/wise-feedback-across-difference | 18 (7) |
| principles/supporting-gifted-and-talented-students | 18 (8) |
| principles/text-to-speech | 22 (5) |

Counts are after the rework. The tables are longer than the brief's "about 10" because the setting rows from waves 4–6
are now required, and most of those rows are untested proposals.

## Checks

Each page was checked by script against its old version, as in earlier waves:
- no old line was lost (social presence's split around an inline comment was checked by hand);
- no frontmatter key changed except `description`, `status`, `generated`, and the `sources` DOI fixes below;
- no cited claim was dropped, and no marker sits above its cap;
- there are no broken links;
- every quoted number is on a cited claim or the old page, or is a labelled proposal.

**Which claims test each page's relationship:**
- **Partly tested on two pages:**
  - explicit vocabulary instruction: two school-age syntheses (d = 0.50 on researcher measures, 0.10 on standardised ones);
  - classroom management: Oliver, Wehby & Reschly (2011), universal management against usual practice.
- **Untested on the other thirteen**, each of which keeps a labelled default design with doses across sessions.

## Citations corrected in passing (Crossref)

Frontmatter `resource:` lines that disagreed with Key Sources were wrong on the frontmatter side every time:

| Page | Source | Wrong DOI | Corrected DOI |
|---|---|---|---|
| positive self-talk | Gainsburg & Kross (2020) | `…2019.103971` (no record) | `10.1016/j.jesp.2020.103969` |
| text-to-speech | Hillaire et al. (2019) | `jime.510` (Baas et al., another paper) | `10.5334/jime.519` |
| explicit vocabulary | Madrigal-Hopes et al. (2014) | `…527923` (no record) | `10.1177/1045159514522432` |
| flexible grouping | Burris et al. (2006) | `…043001137` (Sadoski, another paper) | `10.3102/00028312043001105` |
| cultural awareness | Reinholz et al. (2019) | `…1692210` (no record) | `10.1080/1360144X.2019.1692211` |
| observation and shadowing | Tenenberg (2016) | `…950955` (no record) | `10.1080/03075079.2014.950954` |
| memory consolidation | Dudai (2004) | `10.1016/j.neuron.2004.09.007` (Dan & Poo) | `10.1146/annurev.psych.55.090902.142050` |

Dudai (2004)'s Key Sources line also gave the wrong journal. It is now *Annual Review of Psychology* 55, 51–86, and the
old line is kept in a comment.

## Brief test (2026-10-05)

The design was the same as wave 6's: 30 briefs, Kimi K3 answering (16,000-token limit, no answer cut off), and Gemini 3.8
Flash and DeepSeek V4 Pro grading. The container restarted during grading, which was re-run on the same answers. The
test cost about $5.3, and the rework re-tests about $0.6.

| | OLD | NEW |
|---|---|---|
| affordances /12 (all / complete / sparse) | 5.8 / 6.8 / 4.7 | 9.7 / 10.3 / 9.1 |
| accuracy (1–5) | 3.08 | 3.78 |
| decision value (1–5) | 3.57 | 3.95 |
| brief fit (all / complete / sparse) | 3.83 / 3.97 / 3.70 | 3.98 / 4.17 / 3.80 |
| situation fit, anchored (all / complete / sparse) | 3.57 / 3.77 / 3.37 | 3.90 / 4.17 / 3.63 |
| blind pairs NEW–OLD (all / complete / sparse) | | **76–44 / 33–27 / 43–17** |

**What the numbers show:**
- **This was the weakest wave in the pairs.** Fit rose a little on complete briefs, unlike wave 6.
- **DeepSeek's pairwise picks carry little signal here.** It picked the answer shown first in 48 of 60 pairs (Gemini in
  30), and it scored NEW below OLD on decision value. Unanimous briefs: 7 of 30.
- **Lost 1–3**: criterion- and norm-referenced testing (sparse), flipped learning (both briefs), positive self-talk,
  sequencing, text-to-speech, wise feedback (complete).
- **Tied 2–2**: classroom management (sparse), explicit vocabulary, flexible grouping, memory consolidation, procedural
  learning (complete), and observation and shadowing (both briefs).

## Rework

| Brief | Why it lost | Row added (untested proposal) | Wave 7 | Rework 1 | Rework 2 |
|---|---|---|---|---|---|
| positive self-talk, complete | the NEW answer came out garbled (a generation fault) | none | 1–3 | **4–0** | |
| wise feedback, complete | the brief asked for training the tutor who gives feedback | the learner is the feedback-giver: model, rewrite against the brief's rubric, role-play, review | 1–3 | **4–0** | |
| criterion/norm testing, sparse | answers had secondary learners write test items on phones | self-paced mobile for school-age learners: tap-to-sort and auto-scored items | 1–3 | **3–1** | |
| flipped learning, complete | answers said flipped and unflipped teaching had never been compared, and moved the brief's pre-class check | keep the brief's own session structure | 1–3 | **3–1** | |
| flipped learning, sparse | the same overclaim | little home internet or short lessons: printable material or an in-class flip, keeping discussion | 1–3 | 2–2 | |
| sequencing, complete | answers ignored the four stages the brief named | use the brief's stages as the skeleton | 1–3 | 2–2 | |
| text-to-speech, complete | answers set 600–900-word texts, then ignored the brief's own assessment criteria | short texts read sentence by sentence; playback control taught as a skill; TTS on feedback; assess what the brief names | 1–3 | 1–3 | **3–1** |

Each re-test regenerates one NEW answer, so single results are noisy.

**The new lesson: "no claim here" must not become "no research exists".** The flipped-learning page said, correctly,
that no claim in this wiki compares flipped and unflipped teaching. Answers repeated that as a fact about the
literature, and both graders marked it inaccurate. The page now says the wider literature has such comparisons and
that none is recorded here. **Any page that states an absence of claims should say it is an absence in the wiki, not
in the field.**

## Open findings from the agents

**Duplicate claims:**
- `feedback-addressing-task-improves-learning` and `feedback-most-effective-at-task-and-process-levels` (same two
  meta-analyses, `r2` against `r?`).
- `redundancy-principle` and `redundancy-effect-impairs-learning` (same Trypke entry).
- `universal-classroom-management-reduces-problem-behavior` and `treatment-classrooms-less-disruptive-than-control`
  (both report the Oliver 2011 overall result).
- `deep-prompting-insufficient-long-term-retention` and `deep-prompt-advantage-fades-at-follow-up` (Opre 2023).
- `ptfc-beats-cfc-conceptual-understanding` and `prior-achievement-affects-conceptual-understanding` (Ramadoni 2022).
- `pairing-contextual-encounters…` and `combined-intentional-incidental-greater-gains`.
- `incidental-vocabulary-exposure-limited` and `vocabulary-knowledge-grows-incrementally…`.
- `skill-specificity-l2-grammar-practice` and `automatization-requires-practice-consistent-environment`.
- Single studies split several ways: the four Sadaf (2022) claims, the PATHS claims, and the ERIC digests behind
  funds-of-knowledge and home visits.

**Overstated or contradicted titles:**
- `self-talk-improves-learning-and-performance`: sport and motor evidence only, and its Discussion contradicts Tod et
  al. (2011).
- `repeated-listening-improves-oral-reading-fluency`.
- `cooperative-learning-gifted-students`.
- `heterogeneous-teams-more-benefits-than-homogeneous`.
- `human-embodiment-video-presence-effects`.
- `method-achievement-interaction-self-efficacy`.
- `clinical-supervision-effectiveness-inconclusive`.
- `brief-intervention-empathic-discipline-cuts-suspensions` (not a sentence; Okonofua 2016 `r?` against the header's
  `r3`).
- `di-medium-positive-effect-academic-achievement` (CI −3.66 to 5.12; garbled figures).
- `worked-examples-example-problem-sequences`: its lead sentence contradicts its corrected entry.

**Stale text:**
- `acute-exercise-timing-memory`
- `incidental-vocabulary-exposure-limited`
- `morphological-instruction-improves-vocabulary`
- `teacher-expectation-effects-on-achievement`: Discussion statements with no entry behind them.

**Codes:**
- **An `i` code with no effect size printed:**
  - `effective-classroom-management-engages-students-over-90-percent-of-time`
  - `pbis-suspensions-decreased-41-percent`
  - `tkss-fidelity-ancova-interaction-problem-behavior`
- **Header disagrees with the entries:**
  - `interleaving-improves-discrimination`: header `i2`–`i3`, entries `i?`.
  - `automatic-word-recognition-…`
- **Kind miscoded:**
  - `math-vocabulary-levels-improve-post-test`: `causal` on a pre–post design.
  - `expert-teachers-interpret-classroom-phenomena-better`: `theoretical` on an observational study.
  - `mba-students-experience-courses-as-coi`: `qualitative` on a survey.
- **Other:** the Zimmerman (2000) chapter is coded q3; the testimony claims are `theoretical` on some pages and `review`
  on others.

**Citations:**
- Homepage links in place of articles:
  - Oliver et al. (2011): `www.sree.org`, on four claims; its Campbell DOI `10.4073/csr.2011.4` needs checking.
  - Chorianopoulos (2018), Guo et al. (2014) and VanPatten (2010).
  - Two irrodl/voicethread claims.
- `bimodal-captioned-input-improves-segmentation` links a blog.
- `strategies/wise-feedback` cites "Yeager & Cohen (2012). Turning play into work…", which looks garbled.
- `principles/summative-assessment` still calls Pikulski a 1974 article.

**Links:**
- `elements/audiobooks` links the automatic-word-recognition claim for "listening and reading comprehension are strongly
  correlated".
- `pretraining-improves-transfer` links a theory page for expertise reversal.
- `cooperative-learning-higher-achievement-…` links to itself in its Discussion.
- `principles/continuum-of-gifted-services` has a bare unlinked marker.

**Fold candidates:**
- `principles/flexible-grouping-in-science` into flexible grouping.
- The three criterion-referenced theory pages, under one hub.

**Ingest candidates:**
- Richardson et al. (2017), social presence meta-analysis
- Kraft et al. (2018)
- Yeager et al. (2014), and Cohen, Steele & Ross (1999), wise feedback
- Kross et al. (2014), and Gainsburg & Kross (2020), distanced self-talk
- Wood et al. (2018), text-to-speech meta-analysis
- Burris et al. (2006)
- an ability-grouping synthesis
- McNeil & Fyfe (2012)

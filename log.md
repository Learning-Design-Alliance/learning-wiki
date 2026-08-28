# Wiki Log

Append-only chronological record of ingests, edits, and reviews.

Format: `## [YYYY-MM-DD] <operation> | <page or batch> | <notes>`

Operations: `ingest` · `edit` · `review` · `merge` · `deprecate` · `lint`

---

## 2026-08-28

* **Deprecate**: [strategies/"headings_and_highlight"_strategy](strategies/"headings_and_highlight"_strategy.md) — Deprecated as a duplicate of headings_and_highlight_strategy.md; content merged into the canonical page, this page kept as a redirect stub per CLAUDE.md's no-delete convention
* **Content**: [strategies/headings_and_highlight_strategy](strategies/headings_and_highlight_strategy.md) — Merged in the genuinely different observations from the duplicate "headings_and_highlight"_strategy.md page: sharper Impact framing (the real affordance is clean multi-edit headings), social-studies example folded into Target Learners, and a new Implementation Variability note on broad reading-comprehension use vs. content-specific use

## 2026-08-27

* **Ingest**: `theories/cognitive-information-processing-theory` (page removed before commit — see below) — Ingested from eric-ed616622 (A Bibliography of Cognitive Information Processing Theory, Research, and Practice) via eval_harness.py + ingest_extractions.py
* **Deprecate**: `theories/cognitive-information-processing-theory` — Removed before commit: matched the "information processing theory" search topic on keyword overlap only, but the source is a career/vocational-counseling bibliography, not a learning-science theory; out of scope for this wiki
* **Ingest**: [claims/intuitive-learners-outperform-sensing-learners](claims/intuitive-learners-outperform-sensing-learners.md) — Ingested from eric-ed476964 (Dual Coding Theory and Computer Education: Some Media Experiments To Examine the Effects of Different Media on Learning.) via eval_harness.py + ingest_extractions.py
* **Ingest**: [claims/media-combinations-affect-recall-and-retention](claims/media-combinations-affect-recall-and-retention.md) — Ingested from eric-ed476964 (Dual Coding Theory and Computer Education: Some Media Experiments To Examine the Effects of Different Media on Learning.) via eval_harness.py + ingest_extractions.py
* **Ingest**: [elements/text-underlining-and-annotating](elements/text-underlining-and-annotating.md) — Ingested from eric-ed265520 (The Effects of High and Low Relevant Text Underlining on Test Performance.) via eval_harness.py + ingest_extractions.py
* **Ingest**: [theories/von-restorff-effect-text-marking](theories/von-restorff-effect-text-marking.md) — Ingested from eric-ed265520 (The Effects of High and Low Relevant Text Underlining on Test Performance.) via eval_harness.py + ingest_extractions.py
* **Ingest**: [claims/prior-knowledge-not-related-to-performance](claims/prior-knowledge-not-related-to-performance.md) — Ingested from eric-ed265520 (The Effects of High and Low Relevant Text Underlining on Test Performance.) via eval_harness.py + ingest_extractions.py
* **Ingest**: [claims/experimenter-underlining-effective-as-student-underlining](claims/experimenter-underlining-effective-as-student-underlining.md) — Ingested from eric-ed265520 (The Effects of High and Low Relevant Text Underlining on Test Performance.) via eval_harness.py + ingest_extractions.py
* **Ingest**: [claims/relevancy-of-emphasis-directs-attention](claims/relevancy-of-emphasis-directs-attention.md) — Ingested from eric-ed265520 (The Effects of High and Low Relevant Text Underlining on Test Performance.) via eval_harness.py + ingest_extractions.py

## [2026-04-06] ingest | batch from research_briefs CSVs | 74 principles; 100 elements; 32 patterns; 1637 strategies pages created

## [2026-04-06] enrich | Whole-task performance | enriched from elements CSV via Claude

## [2026-04-06] enrich | Supportive information | enriched from elements CSV via Claude

## [2026-04-06] enrich | Whole-task performance | enriched from elements CSV via Claude

## [2026-04-06] enrich | Supportive information | enriched from elements CSV via Claude

## [2026-04-06] enrich | Whole-task performance | enriched from elements CSV via Claude

## [2026-04-06] enrich | Supportive information | enriched from elements CSV via Claude
## [2026-04-06] enrich | whole-task-performance | enriched via wiki-enrich skill
## [2026-04-06] enrich | chunking | enriched via wiki-enrich skill
## [2026-04-06] enrich | scaffolding-and-fading | enriched via wiki-enrich skill
## [2026-04-06] enrich | explaining-their-thinking | enriched via wiki-enrich skill
## [2026-04-06] enrich | error-analysis | enriched via wiki-enrich skill
## [2026-04-06] enrich | goal-setting-monitoring | enriched via wiki-enrich skill
## [2026-04-07] edit | ask-experts | completed principle page structure, linked claims/examples, and normalized sources
## [2026-04-07] edit | principles batch A | enriched accessible-vocabulary-syntax, annotating, audiobooks, authentic-audiences-purposes, case-studiescase-based-learning, and communities-of-practice
## [2026-04-07] edit | principles batch B | enriched clear-structure-presentation and competency-based-learning-assessment
## [2026-04-07] edit | principles batch C | enriched debate, debriefing, and evaluating-sources after git init
## [2026-04-07] edit | principles batch D | enriched expanding-social-networks, experiential-learning, and explicit-instruction-internet-search after initial commit
## [2026-04-07] edit | principles batch E | enriched explicit-instruction-computer-basics, explicit-instruction-math-strategies, and explicit-instruction-online-reading-strategies with linked claims
## [2026-04-07] edit | principles batch F | enriched explicit-instruction-phonics, explicit-instruction-vocabulary, and flexible-grouping with linked claims

## [2026-04-07] edit | principles batch G | enriched formative-assessment, foster-growth-mindset, and game-based-learning with linked claims

## [2026-04-07] edit | claims batch A | created missing claims expertise-reversal-effect, self-monitoring-improves-self-regulation, we-1, we-2, we-3, we-4, we-5, and worked-examples-expertise-reversal

## [2026-04-07] edit | elements batch A | created missing elements act, adaptive-difficulty, and adaptive-learning

## [2026-04-07] edit | elements batch B | created missing elements analogies, anchored-instruction, and assessment

## [2026-04-07] edit | principles batch H | enriched building-empathy, check-ins, and creating-visual-representations with linked claims

## [2026-04-07] edit | principles batch I | enriched cultural-life-experiences-connections, developing-your-cultural-awareness, and discussing-race with linked claims

## [2026-04-07] edit | principles batch J | enriched empathy-interviews, graphic-organizers, and guided-practice with linked claims

## [2026-04-07] edit | principles batch K | enriched handoutsonline-guidesvisual-reading-aids, immediate-feedback, and inquiry-based-learning with linked claims

## [2026-04-07] edit | principles batch L | enriched instructor-accessibility, journaling, and learner-choice with linked claims

## [2026-04-07] edit | principles batch M | enriched mentoringcoaching, metaphors-analogies, and mindfulness-activities with linked claims

## [2026-04-07] edit | principles batch N | enriched mnemonic-device, multimedia-projects, and multimodal-instruction with linked claims

## [2026-04-07] edit | principles batch O | enriched multiple-methods-of-assessment, note-taking, and observationshadowing with linked claims

## [2026-04-07] edit | principles batch P | enriched pairing-non-examples-with-examples, peer-discussion, and peer-feedbackpeer-review with linked claims

## [2026-04-07] edit | principles batch Q | enriched perspective-seekingmultiple-perspectives, physical-activity, and positive-self-talk with linked claims

## [2026-04-07] edit | principles batch R | enriched pre-reading-questioning, problem-based-learning, and process-based-writing with linked claims

## [2026-04-07] edit | principles batch S | enriched purposeful-reflection, quiet-learning-spaces, and real-world-math with linked claims

## [2026-04-07] edit | principles batch T | enriched self-monitoring, simulations-immersive-virtual-environments, and skills-sprint with linked claims

## [2026-04-07] edit | principles batch U | enriched speech-to-text, strengths-based-approach, and text-chats with linked claims

## [2026-04-07] edit | principles batch V | enriched text-to-speech and video-replay-analysis with linked claims

## [2026-04-07] edit | patterns batch A | enriched 4cid-four-component-instructional-design, anchored-instruction, and case-based-learning-harvard-method with linked dependencies

## [2026-04-07] edit | patterns batch B | enriched cognitive-flexibility-theory, cognitive-load-reduction-clt-scaffolding-approach, and cognitively-guided-instruction-cgi-for-math with linked dependencies

## [2026-04-07] edit | patterns batch C | enriched collaborative-evaluation, collaborative-inquiry, and debate-format with linked dependencies

## [2026-04-07] edit | patterns batch D | enriched develop-understanding, discussion-group, and flipped-classroom with linked dependencies

## [2026-04-07] edit | patterns batch E | enriched fostering-communities-of-learning-fcl, gagnés-9-events-of-instruction, and game-based-mastery-learning-eg-duolingo-pattern with linked dependencies

## [2026-04-07] edit | patterns batch F | enriched goal-based-scenarios-gbs, guided-discovery-learning, and jigsaw-method with linked dependencies

## [2026-04-07] edit | patterns batch G | enriched lda-reflection, learning-for-use-lfu-model, and merrills-first-principles-of-instruction with linked dependencies

## [2026-04-07] edit | patterns batch H | enriched model-evidence-link-mel-reasoning-pattern, peer-instruction, and problem-based-learning-pbl with linked dependencies

## [2026-04-07] edit | patterns batch I | enriched process-oriented-guided-inquiry-learning-pogil, reigeluths-elaboration-theory, and socratic-seminar with linked dependencies

## [2026-04-07] edit | patterns batch J | enriched structured-academic-controversy-sac, structured-peer-review, and think-pair-share with linked dependencies

## [2026-04-07] edit | patterns batch K | enriched traditional-lecture-reading-midterm-final-assessment with linked dependencies

## [2026-04-07] edit | cleanup batch A | created self-regulated-learning, self-determination-theory, information-processing-theory, and smarter-goals to resolve repeated broken links

## [2026-04-07] edit | cleanup batch B | created constructivism, removed placeholder claim links from elements, and repaired worked-examples strategy links

## [2026-04-07] edit | cleanup batch C | created shared mastery and assessment principle, element, and pattern pages to resolve repeated broken links across elements

## [2026-04-07] edit | cleanup batch D | created think-aloud, hints, and erroneous-examples elements and removed literal placeholder wikilinks from index and spaced-learning

## [2026-04-07] edit | cleanup batch E | removed placeholder claim links from strategies, added social-learning and discussion-related pages, and repaired the malformed standards-based grading strategy link

## [2026-04-07] edit | cleanup batch F | added active-learning, structured-discussion, scenario-based-learning, just-in-time-learning, and short-form structured academic controversy targets to reduce the remaining real broken-link backlog

## [2026-04-07] edit | pattern cleanup batch G | added short-form pattern targets for goal-based-scenarios and Merrill demonstration references

## [2026-04-07] edit | pattern cleanup batch H | added short-form flipped-learning target to close the remaining pattern-specific broken link

## [2026-04-07] edit | element cleanup batch I | added metacognition, scaffolding, CLT, dual-coding, guided-discovery, concept-mapping, immediate-feedback, problem-based-learning, and short-form POGIL/elaboration/CLT pattern targets for the element backlog

## [2026-04-07] edit | element cleanup batch J | added reflection and self-regulation support pages plus situated-learning, dual-coding-theory, and constructivist-learning aliases for remaining element dependencies

## [2026-04-07] edit | element cleanup batch K | added iterative-learning, community-based-learning, information-literacy, research-based-learning, and competency-based-assessment targets for the next element dependency cluster

## [2026-04-08] edit | element cleanup batch L | added summative-assessment and performance-based-assessment targets plus non-examples for the next assessment and demonstration dependency cluster

## [2026-04-08] edit | element cleanup batch M | added comparing-cases, fading, explicit-instruction, cognitive-load-management, and think-aloud-modeling for the next demonstration dependency cluster

## [2026-04-08] edit | element cleanup batch N | added social-constructivism, collaborative-discussion, structured-debate, holistic-learning, and conceptual-overviews for the next consensus and elaboration dependency cluster

## [2026-04-08] edit | element cleanup batch O | added community-of-inquiry, group-work, hands-on-learning, and short-form Merrill's First Principles targets for the next collaboration and application dependency cluster

## [2026-04-08] edit | element cleanup batch P | added epistemic-cognition, MEL reasoning, self-regulation, reflection-activities, and analogical-reasoning targets for the next argumentation and integration dependency cluster

## [2026-04-08] edit | element cleanup batch Q | added cognitive-load-reduction, metaphors, prior-knowledge-activation, retrieval-practice, and pre-reading-activities for the next analogy and activation dependency cluster

## [2026-04-08] edit | element cleanup batch R | added contextualization, metacognitive-reflection, cognitive-flexibility, cognitive-disequilibrium, and discrepant-events for the next activation and cognitive-conflict dependency cluster

## [2026-04-08] edit | element cleanup batch S | added learning-outcomes, goal-setting, scientific-reasoning, justification, and peer-learning for the next objectives and explanation dependency cluster

## [2026-04-08] edit | element cleanup batch T | added CGI for Math alias plus pre-class-preparation, case-studies, seminar-format, and collaborative-decision-making for the next discussion and preparation dependency cluster

## [2026-04-08] edit | element cleanup batch U | added role-playing, self-explanation, memory-consolidation, spaced-repetition, and spiral-curriculum for the next review and explanation dependency cluster

## [2026-04-08] edit | element cleanup batch V | added behaviorism, deliberate-practice, reinforcement-theory, game-based-mastery-learning, and digital-learning for the next mastery and hypertext dependency cluster

## [2026-04-08] edit | element cleanup batch W | added multimedia-learning, self-paced-learning, and multimedia-learning pattern targets for the next digital media dependency cluster

## [2026-04-08] edit | element cleanup batch X | added expert-modeling, guided-inquiry, game-based-mastery-learning-duolingo-pattern, and social-interdependence for the next modeling and inquiry dependency cluster

## [2026-04-08] edit | element cleanup batch Y | added literature-review, data-analysis, problem-scenarios, negotiation, and Merrill activation targets for the next research and scenario dependency cluster

## [2026-04-08] edit | element cleanup batch Z | added knowledge-organization, sequencing, conceptual-scaffolding, gradual-release, and motivation for the next summarization and sequencing dependency cluster

## [2026-04-08] edit | element cleanup batch AA | added engagement, cognitive-activation, video-prompts, real-world-problems, and drill-practice for the next attention and practice dependency cluster

## [2026-04-08] edit | element cleanup batch AB | added 4C/ID alias, problem-solving, Merrill application, peer-assessment, and rubric-design for the next practice and criteria dependency cluster

## [2026-04-08] edit | element cleanup batch AC | added self-directed-learning, procedural-learning, scaffolding-fading, and fading-scaffolding for the next procedural support dependency cluster

## [2026-04-08] edit | element cleanup batch AD | added knowledge-building, clear-structure, explicit-teaching, and multimedia-instruction for the next direct instruction dependency cluster

## [2026-04-08] edit | element cleanup batch AE | added jigsaw-learning, rhetorical-skill-development, transfer-of-learning, and Merrill integration targets for the next argument and transfer dependency cluster

## [2026-04-08] edit | element cleanup batch AF | added rhetorical-strategies, public-speaking, self-testing, traditional-lecture-based-instruction, and blended-learning for the next persuasion and delivery dependency cluster

## [2026-04-08] edit | element cleanup batch AG | added distributed-cognition, collaboration, observation, and task-management aliases for the next cross-element and strategy dependency cluster

## [2026-04-08] edit | element cleanup batch AH | added progress-tracking, communication-channels, resource-hubs, digital-tools, and small-group-instruction for the next strategy dependency cluster

## [2026-04-13] ingest | claims/autonomy-supports-intrinsic-motivation | new claim (motiv-1); evidence: Ryan & Deci 2000, Deci et al. 1999 meta-analysis (128 studies), Stefanou et al. 2004
## [2026-04-13] ingest | claims/self-efficacy-predicts-academic-persistence | new claim (motiv-2); evidence: Bandura 1997, Pajares 1996 systematic review
## [2026-04-13] ingest | claims/task-value-increases-motivation-and-engagement | new claim (motiv-3); evidence: Eccles & Wigfield 2002, Wigfield & Cambria 2010
## [2026-04-13] edit | principles/motivation | added motiv-1, motiv-2, motiv-3 to Claims section; updated Implications prose to reference autonomy, efficacy, and task-value facets

## [2026-08-28] fix | strategies/* (49 pages) | renamed files containing a literal `:` in the filename (e.g. `blocks_and_legos:_maker_spaces_and_fab_labs.md` → `blocks_and_legos-maker_spaces_and_fab_labs.md`) — the colon was parsed as a URI scheme separator by Jekyll/GitHub Pages, breaking the Pages build with "Invalid scheme format"; updated all cross-links in strategies/index.md and principles/explicit-instruction-math-strategies.md, principles/explicit-instruction-online-reading-strategies.md; regenerated indexes and verified with `scripts/lint.py`

# Wiki Log

Append-only chronological record of ingests, edits, and reviews.

Format: `## [YYYY-MM-DD] <operation> | <page or batch> | <notes>`

Operations: `ingest` · `edit` · `review` · `merge` · `deprecate` · `lint`

---

## 2026-08-29

* **Content**: [theories/social-learning-theory](theories/social-learning-theory.md) — Cross-linked new Sociocultural Theory page (LIDT Foundations ingest)
* **Content**: [theories/situated-learning](theories/situated-learning.md) — Cross-linked new Sociocultural Theory and Connectivism pages (LIDT Foundations ingest)
* **Content**: [theories/cognitive-apprenticeship](theories/cognitive-apprenticeship.md) — Cross-linked new Sociocultural Theory page (LIDT Foundations ingest)
* **Source**: [theories/constructivism](theories/constructivism.md) — Added Ertmer & Newby (2013) key source and cross-links to new Cognitivism and Sociocultural Theory pages (LIDT Foundations ingest)
* **Source**: [theories/behaviorism](theories/behaviorism.md) — Added Ertmer & Newby (2013) key source and cross-links to new Cognitivism and Connectivism theory pages (LIDT Foundations ingest)
* **Ingest**: [theories/first-principles-of-instruction](theories/first-principles-of-instruction.md) — Ingested from Merrill "Using the First Principles of Instruction..." (ch. 21 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [theories/connectivism](theories/connectivism.md) — Ingested from Siemens "Connectivism" (ch. 19 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [theories/sociocultural-theory](theories/sociocultural-theory.md) — Ingested from Polly, Casto, Norwood & Allman "Sociocultural Perspectives of Learning" (ch. 12 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [theories/cognitivism](theories/cognitivism.md) — Ingested from Ertmer & Newby (2013) "Behaviorism, Cognitivism, Constructivism" (ch. 11 of LIDT Foundations, edtechbooks.org/lidtfoundations)

## 2026-08-28

* **Deprecate**: [strategies/"headings_and_highlight"_strategy](strategies/"headings_and_highlight"_strategy.md) — Deprecated as a duplicate of headings_and_highlight_strategy.md; content merged into the canonical page, this page kept as a redirect stub per CLAUDE.md's no-delete convention
* **Content**: [strategies/headings_and_highlight_strategy](strategies/headings_and_highlight_strategy.md) — Merged in the genuinely different observations from the duplicate "headings_and_highlight"_strategy.md page: sharper Impact framing (the real affordance is clean multi-edit headings), social-studies example folded into Target Learners, and a new Implementation Variability note on broad reading-comprehension use vs. content-specific use
* **Fix**: `strategies/* (49 pages)` — renamed files containing a literal `:` in the filename (e.g. `blocks_and_legos:_maker_spaces_and_fab_labs.md` → `blocks_and_legos-maker_spaces_and_fab_labs.md`) — the colon was parsed as a URI scheme separator by Jekyll/GitHub Pages, breaking the Pages build with "Invalid scheme format"; updated all cross-links in strategies/index.md and principles/explicit-instruction-math-strategies.md, principles/explicit-instruction-online-reading-strategies.md; regenerated indexes and verified with `scripts/lint.py`

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

## 2026-04-06

* **Ingest**: `batch from research_briefs CSVs` — 74 principles; 100 elements; 32 patterns; 1637 strategies pages created
* **Enrich**: [elements/whole-task-performance](elements/whole-task-performance.md) — enriched from elements CSV via Claude
* **Enrich**: [elements/supportive-information](elements/supportive-information.md) — enriched from elements CSV via Claude
* **Enrich**: [elements/whole-task-performance](elements/whole-task-performance.md) — enriched from elements CSV via Claude
* **Enrich**: [elements/supportive-information](elements/supportive-information.md) — enriched from elements CSV via Claude
* **Enrich**: [elements/whole-task-performance](elements/whole-task-performance.md) — enriched from elements CSV via Claude
* **Enrich**: [elements/supportive-information](elements/supportive-information.md) — enriched from elements CSV via Claude
* **Enrich**: [elements/whole-task-performance](elements/whole-task-performance.md) — enriched via wiki-enrich skill
* **Enrich**: [principles/chunking](principles/chunking.md) — enriched via wiki-enrich skill
* **Enrich**: [principles/scaffolding-and-fading](principles/scaffolding-and-fading.md) — enriched via wiki-enrich skill
* **Enrich**: [principles/explaining-their-thinking](principles/explaining-their-thinking.md) — enriched via wiki-enrich skill
* **Enrich**: [principles/error-analysis](principles/error-analysis.md) — enriched via wiki-enrich skill
* **Enrich**: [principles/goal-setting-monitoring](principles/goal-setting-monitoring.md) — enriched via wiki-enrich skill

## 2026-04-07

* **Edit**: [principles/ask-experts](principles/ask-experts.md) — completed principle page structure, linked claims/examples, and normalized sources
* **Edit**: `principles batch A` — enriched accessible-vocabulary-syntax, annotating, audiobooks, authentic-audiences-purposes, case-studiescase-based-learning, and communities-of-practice
* **Edit**: `principles batch B` — enriched clear-structure-presentation and competency-based-learning-assessment
* **Edit**: `principles batch C` — enriched debate, debriefing, and evaluating-sources after git init
* **Edit**: `principles batch D` — enriched expanding-social-networks, experiential-learning, and explicit-instruction-internet-search after initial commit
* **Edit**: `principles batch E` — enriched explicit-instruction-computer-basics, explicit-instruction-math-strategies, and explicit-instruction-online-reading-strategies with linked claims
* **Edit**: `principles batch F` — enriched explicit-instruction-phonics, explicit-instruction-vocabulary, and flexible-grouping with linked claims
* **Edit**: `principles batch G` — enriched formative-assessment, foster-growth-mindset, and game-based-learning with linked claims
* **Edit**: `claims batch A` — created missing claims expertise-reversal-effect, self-monitoring-improves-self-regulation, we-1, we-2, we-3, we-4, we-5, and worked-examples-expertise-reversal
* **Edit**: `elements batch A` — created missing elements act, adaptive-difficulty, and adaptive-learning
* **Edit**: `elements batch B` — created missing elements analogies, anchored-instruction, and assessment
* **Edit**: `principles batch H` — enriched building-empathy, check-ins, and creating-visual-representations with linked claims
* **Edit**: `principles batch I` — enriched cultural-life-experiences-connections, developing-your-cultural-awareness, and discussing-race with linked claims
* **Edit**: `principles batch J` — enriched empathy-interviews, graphic-organizers, and guided-practice with linked claims
* **Edit**: `principles batch K` — enriched handoutsonline-guidesvisual-reading-aids, immediate-feedback, and inquiry-based-learning with linked claims
* **Edit**: `principles batch L` — enriched instructor-accessibility, journaling, and learner-choice with linked claims
* **Edit**: `principles batch M` — enriched mentoringcoaching, metaphors-analogies, and mindfulness-activities with linked claims
* **Edit**: `principles batch N` — enriched mnemonic-device, multimedia-projects, and multimodal-instruction with linked claims
* **Edit**: `principles batch O` — enriched multiple-methods-of-assessment, note-taking, and observationshadowing with linked claims
* **Edit**: `principles batch P` — enriched pairing-non-examples-with-examples, peer-discussion, and peer-feedbackpeer-review with linked claims
* **Edit**: `principles batch Q` — enriched perspective-seekingmultiple-perspectives, physical-activity, and positive-self-talk with linked claims
* **Edit**: `principles batch R` — enriched pre-reading-questioning, problem-based-learning, and process-based-writing with linked claims
* **Edit**: `principles batch S` — enriched purposeful-reflection, quiet-learning-spaces, and real-world-math with linked claims
* **Edit**: `principles batch T` — enriched self-monitoring, simulations-immersive-virtual-environments, and skills-sprint with linked claims
* **Edit**: `principles batch U` — enriched speech-to-text, strengths-based-approach, and text-chats with linked claims
* **Edit**: `principles batch V` — enriched text-to-speech and video-replay-analysis with linked claims
* **Edit**: `patterns batch A` — enriched 4cid-four-component-instructional-design, anchored-instruction, and case-based-learning-harvard-method with linked dependencies
* **Edit**: `patterns batch B` — enriched cognitive-flexibility-theory, cognitive-load-reduction-clt-scaffolding-approach, and cognitively-guided-instruction-cgi-for-math with linked dependencies
* **Edit**: `patterns batch C` — enriched collaborative-evaluation, collaborative-inquiry, and debate-format with linked dependencies
* **Edit**: `patterns batch D` — enriched develop-understanding, discussion-group, and flipped-classroom with linked dependencies
* **Edit**: `patterns batch E` — enriched fostering-communities-of-learning-fcl, gagnés-9-events-of-instruction, and game-based-mastery-learning-eg-duolingo-pattern with linked dependencies
* **Edit**: `patterns batch F` — enriched goal-based-scenarios-gbs, guided-discovery-learning, and jigsaw-method with linked dependencies
* **Edit**: `patterns batch G` — enriched lda-reflection, learning-for-use-lfu-model, and merrills-first-principles-of-instruction with linked dependencies
* **Edit**: `patterns batch H` — enriched model-evidence-link-mel-reasoning-pattern, peer-instruction, and problem-based-learning-pbl with linked dependencies
* **Edit**: `patterns batch I` — enriched process-oriented-guided-inquiry-learning-pogil, reigeluths-elaboration-theory, and socratic-seminar with linked dependencies
* **Edit**: `patterns batch J` — enriched structured-academic-controversy-sac, structured-peer-review, and think-pair-share with linked dependencies
* **Edit**: `patterns batch K` — enriched traditional-lecture-reading-midterm-final-assessment with linked dependencies
* **Edit**: `cleanup batch A` — created self-regulated-learning, self-determination-theory, information-processing-theory, and smarter-goals to resolve repeated broken links
* **Edit**: `cleanup batch B` — created constructivism, removed placeholder claim links from elements, and repaired worked-examples strategy links
* **Edit**: `cleanup batch C` — created shared mastery and assessment principle, element, and pattern pages to resolve repeated broken links across elements
* **Edit**: `cleanup batch D` — created think-aloud, hints, and erroneous-examples elements and removed literal placeholder wikilinks from index and spaced-learning
* **Edit**: `cleanup batch E` — removed placeholder claim links from strategies, added social-learning and discussion-related pages, and repaired the malformed standards-based grading strategy link
* **Edit**: `cleanup batch F` — added active-learning, structured-discussion, scenario-based-learning, just-in-time-learning, and short-form structured academic controversy targets to reduce the remaining real broken-link backlog
* **Edit**: `pattern cleanup batch G` — added short-form pattern targets for goal-based-scenarios and Merrill demonstration references
* **Edit**: `pattern cleanup batch H` — added short-form flipped-learning target to close the remaining pattern-specific broken link
* **Edit**: `element cleanup batch I` — added metacognition, scaffolding, CLT, dual-coding, guided-discovery, concept-mapping, immediate-feedback, problem-based-learning, and short-form POGIL/elaboration/CLT pattern targets for the element backlog
* **Edit**: `element cleanup batch J` — added reflection and self-regulation support pages plus situated-learning, dual-coding-theory, and constructivist-learning aliases for remaining element dependencies
* **Edit**: `element cleanup batch K` — added iterative-learning, community-based-learning, information-literacy, research-based-learning, and competency-based-assessment targets for the next element dependency cluster

## 2026-04-08

* **Edit**: `element cleanup batch L` — added summative-assessment and performance-based-assessment targets plus non-examples for the next assessment and demonstration dependency cluster
* **Edit**: `element cleanup batch M` — added comparing-cases, fading, explicit-instruction, cognitive-load-management, and think-aloud-modeling for the next demonstration dependency cluster
* **Edit**: `element cleanup batch N` — added social-constructivism, collaborative-discussion, structured-debate, holistic-learning, and conceptual-overviews for the next consensus and elaboration dependency cluster
* **Edit**: `element cleanup batch O` — added community-of-inquiry, group-work, hands-on-learning, and short-form Merrill's First Principles targets for the next collaboration and application dependency cluster
* **Edit**: `element cleanup batch P` — added epistemic-cognition, MEL reasoning, self-regulation, reflection-activities, and analogical-reasoning targets for the next argumentation and integration dependency cluster
* **Edit**: `element cleanup batch Q` — added cognitive-load-reduction, metaphors, prior-knowledge-activation, retrieval-practice, and pre-reading-activities for the next analogy and activation dependency cluster
* **Edit**: `element cleanup batch R` — added contextualization, metacognitive-reflection, cognitive-flexibility, cognitive-disequilibrium, and discrepant-events for the next activation and cognitive-conflict dependency cluster
* **Edit**: `element cleanup batch S` — added learning-outcomes, goal-setting, scientific-reasoning, justification, and peer-learning for the next objectives and explanation dependency cluster
* **Edit**: `element cleanup batch T` — added CGI for Math alias plus pre-class-preparation, case-studies, seminar-format, and collaborative-decision-making for the next discussion and preparation dependency cluster
* **Edit**: `element cleanup batch U` — added role-playing, self-explanation, memory-consolidation, spaced-repetition, and spiral-curriculum for the next review and explanation dependency cluster
* **Edit**: `element cleanup batch V` — added behaviorism, deliberate-practice, reinforcement-theory, game-based-mastery-learning, and digital-learning for the next mastery and hypertext dependency cluster
* **Edit**: `element cleanup batch W` — added multimedia-learning, self-paced-learning, and multimedia-learning pattern targets for the next digital media dependency cluster
* **Edit**: `element cleanup batch X` — added expert-modeling, guided-inquiry, game-based-mastery-learning-duolingo-pattern, and social-interdependence for the next modeling and inquiry dependency cluster
* **Edit**: `element cleanup batch Y` — added literature-review, data-analysis, problem-scenarios, negotiation, and Merrill activation targets for the next research and scenario dependency cluster
* **Edit**: `element cleanup batch Z` — added knowledge-organization, sequencing, conceptual-scaffolding, gradual-release, and motivation for the next summarization and sequencing dependency cluster
* **Edit**: `element cleanup batch AA` — added engagement, cognitive-activation, video-prompts, real-world-problems, and drill-practice for the next attention and practice dependency cluster
* **Edit**: `element cleanup batch AB` — added 4C/ID alias, problem-solving, Merrill application, peer-assessment, and rubric-design for the next practice and criteria dependency cluster
* **Edit**: `element cleanup batch AC` — added self-directed-learning, procedural-learning, scaffolding-fading, and fading-scaffolding for the next procedural support dependency cluster
* **Edit**: `element cleanup batch AD` — added knowledge-building, clear-structure, explicit-teaching, and multimedia-instruction for the next direct instruction dependency cluster
* **Edit**: `element cleanup batch AE` — added jigsaw-learning, rhetorical-skill-development, transfer-of-learning, and Merrill integration targets for the next argument and transfer dependency cluster
* **Edit**: `element cleanup batch AF` — added rhetorical-strategies, public-speaking, self-testing, traditional-lecture-based-instruction, and blended-learning for the next persuasion and delivery dependency cluster
* **Edit**: `element cleanup batch AG` — added distributed-cognition, collaboration, observation, and task-management aliases for the next cross-element and strategy dependency cluster
* **Edit**: `element cleanup batch AH` — added progress-tracking, communication-channels, resource-hubs, digital-tools, and small-group-instruction for the next strategy dependency cluster

## 2026-04-13

* **Ingest**: [claims/autonomy-supports-intrinsic-motivation](claims/autonomy-supports-intrinsic-motivation.md) — new claim (motiv-1); evidence: Ryan & Deci 2000, Deci et al. 1999 meta-analysis (128 studies), Stefanou et al. 2004
* **Ingest**: [claims/self-efficacy-predicts-academic-persistence](claims/self-efficacy-predicts-academic-persistence.md) — new claim (motiv-2); evidence: Bandura 1997, Pajares 1996 systematic review
* **Ingest**: [claims/task-value-increases-motivation-and-engagement](claims/task-value-increases-motivation-and-engagement.md) — new claim (motiv-3); evidence: Eccles & Wigfield 2002, Wigfield & Cambria 2010
* **Edit**: [principles/motivation](principles/motivation.md) — added motiv-1, motiv-2, motiv-3 to Claims section; updated Implications prose to reference autonomy, efficacy, and task-value facets

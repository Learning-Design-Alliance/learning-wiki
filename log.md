# Wiki Log

Append-only chronological record of ingests, edits, and reviews.

Format: `## [YYYY-MM-DD] <operation> | <page or batch> | <notes>`

Operations: `ingest` · `edit` · `review` · `merge` · `deprecate` · `lint`

---

## 2026-08-30

* **Edit**: `goal-map batch: resolved alignment rendering` — goals/exploresel-taxonomy.md gained a Framework Coverage table (per domain/subdomain: mapped-term counts + top contributing frameworks) and each goals/exploresel-fw-*.md gained resolved Taxonomy Alignment and Similar Competencies sections (grouped/capped, sourced from the crosswalk/similarity ndjson), replacing the earlier grep-yourself placeholder text
* **Ingest**: [goals/exploresel-entrepreneurship-search-fragment.md](goals/exploresel-entrepreneurship-search-fragment.md) — separate, smaller ExploreSEL-adjacent scrape (13 unresolved entrepreneurship-competency anchors + 152 matched U.S. state CTE competencies, no edge data); kept explicitly unresolved rather than forced into the goal-map nodes/relationships shape; data in goals/data/exploresel-entrepreneurship-search-fragment.ndjson
* **Ingest**: `goal-map batch from ExploreSEL/EASEL graph export` — [goals/exploresel-taxonomy.md](goals/exploresel-taxonomy.md) (206-node full-depth taxonomy) + 43 framework goal-map pages (goals/exploresel-fw-*.md); cross-framework alignment data kept separate as goals/data/exploresel-framework-taxonomy-crosswalk.ndjson (6506 edges) and goals/data/exploresel-cross-framework-similarity.ndjson (8136 edges) — see sources/manifest.ndjson id=exploresel-graph-export-2026-08-30

## 2026-08-29

* **Ingest**: [claims/relationship-focused-pd-shifts-teacher-conceptions-of-rigor-and-safety](claims/relationship-focused-pd-shifts-teacher-conceptions-of-rigor-and-safety.md) — New claim: relationship-focused PD shifts teacher conceptions of rigor and safety (Chowning 2023)
* **Ingest**: [principles/relationships-as-foundation-for-argumentation](principles/relationships-as-foundation-for-argumentation.md) — New principle: relationships as foundation for argumentation, from Chowning 2023
* **Ingest**: [strategies/collaborative-autoethnography-for-teacher-pd](strategies/collaborative-autoethnography-for-teacher-pd.md) — New strategy: collaborative autoethnography for teacher PD, from Chowning 2023
* **Ingest**: [claims/external-evidence-can-refute-computational-models-of-particle-interactions](claims/external-evidence-can-refute-computational-models-of-particle-interactions.md) — New claim: external evidence can refute computational models of particle interactions (Wagh et al. 2025)
* **Ingest**: [patterns/three-practices-for-ontological-alignment-in-computational-modeling](patterns/three-practices-for-ontological-alignment-in-computational-modeling.md) — New pattern: three practices for ontological alignment in computational modeling (Wagh et al. 2025)
* **Ingest**: [theories/ontological-alignment](theories/ontological-alignment.md) — New theory page on ontological alignment, from Wagh et al. 2025
* **Ingest**: [claims/teacher-appropriation-of-edp-reframes-restrictive-stem-narratives](claims/teacher-appropriation-of-edp-reframes-restrictive-stem-narratives.md) — New claim: teacher appropriation of EDP reframes restrictive STEM narratives (Watkins 2023)
* **Ingest**: [principles/appropriating-disciplinary-tools-to-challenge-restrictive-narratives](principles/appropriating-disciplinary-tools-to-challenge-restrictive-narratives.md) — New principle: appropriating disciplinary tools to challenge restrictive narratives, from Watkins 2023
* **Ingest**: [claims/dialogic-teacher-support-cultivates-statistical-modeling-practice](claims/dialogic-teacher-support-cultivates-statistical-modeling-practice.md) — New claim: dialogic teacher support cultivates statistical modeling practice (Wisittanawat & Lehrer 2024)
* **Ingest**: [strategies/dialogic-facilitation-of-statistical-modeling-practice](strategies/dialogic-facilitation-of-statistical-modeling-practice.md) — New strategy: dialogic facilitation of statistical modeling practice, from Wisittanawat & Lehrer 2024
* **Ingest**: [claims/heterogeneity-seeking-curricula-surface-diverse-epistemic-commitments](claims/heterogeneity-seeking-curricula-surface-diverse-epistemic-commitments.md) — New claim: heterogeneity-seeking curricula surface diverse epistemic commitments (Pierson et al. 2023)
* **Ingest**: [patterns/heterogeneity-seeking-modeling-curriculum](patterns/heterogeneity-seeking-modeling-curriculum.md) — New pattern: heterogeneity-seeking modeling curriculum (Pierson et al. 2023)
* **Ingest**: [theories/epistemic-commitments](theories/epistemic-commitments.md) — New theory page on epistemic commitments, from Pierson et al. 2023
* **Ingest**: [claims/historians-epistemic-processes-extend-beyond-source-analysis](claims/historians-epistemic-processes-extend-beyond-source-analysis.md) — New claim: academic historians' epistemic processes extend well beyond source analysis and writing (Kainulainen et al. 2025)
* **Content**: [theories/historical-reasoning-framework](theories/historical-reasoning-framework.md) — Extended with Kainulainen et al. 2025's 14-category empirical expansion of historians' epistemic processes; added claim link and source
* **Ingest**: [claims/fiber-crafting-develops-proportional-reasoning-through-unitizing](claims/fiber-crafting-develops-proportional-reasoning-through-unitizing.md) — New claim: fiber crafting develops proportional reasoning through unitizing (Peppler et al. 2025)
* **Ingest**: [patterns/fiber-crafting-for-proportional-reasoning](patterns/fiber-crafting-for-proportional-reasoning.md) — New pattern: fiber crafting for proportional reasoning (Peppler et al. 2025)
* **Ingest**: [theories/materialized-action](theories/materialized-action.md) — New theory page on materialized action, from Peppler et al. 2025
* **Ingest**: [claims/mixed-disciplinary-teacher-making-supports-transdisciplinary-epistemic-liberation](claims/mixed-disciplinary-teacher-making-supports-transdisciplinary-epistemic-liberation.md) — New claim: mixed-disciplinary teacher making supports transdisciplinary epistemic liberation (Finch et al. 2021)
* **Ingest**: [patterns/luminous-science-transdisciplinary-curriculum](patterns/luminous-science-transdisciplinary-curriculum.md) — New pattern: Luminous Science transdisciplinary curriculum, from Finch et al. 2021
* **Ingest**: [claims/co-design-tools-support-balancing-standards-and-student-interests](claims/co-design-tools-support-balancing-standards-and-student-interests.md) — New claim: co-design tools support balancing standards and student interests (Penuel et al. 2022)
* **Ingest**: [strategies/co-design-tools-for-standards-and-interest-balancing](strategies/co-design-tools-for-standards-and-interest-balancing.md) — New strategy: co-design tools for standards and interest balancing (Penuel et al. 2022)
* **Ingest**: [patterns/storyline-science-curriculum-design](patterns/storyline-science-curriculum-design.md) — New pattern: storyline science curriculum design, from Penuel et al. 2022
* **Ingest**: [claims/choice-rich-infrastructure-supports-productive-deviation-and-learning](claims/choice-rich-infrastructure-supports-productive-deviation-and-learning.md) — New claim: choice-rich infrastructure supports productive deviation and learning (Hilppö & Stevens 2024)
* **Ingest**: [patterns/alternative-in-school-steam-learning-infrastructure](patterns/alternative-in-school-steam-learning-infrastructure.md) — New pattern: alternative in-school STEAM learning infrastructure, from Hilppö & Stevens 2024
* **Ingest**: [claims/ambiguous-tasks-with-revision-help-students-recognize-role-of-assumptions](claims/ambiguous-tasks-with-revision-help-students-recognize-role-of-assumptions.md) — New claim: ambiguous tasks with revision help students recognize role of assumptions (Komatsu et al. 2024)
* **Ingest**: [patterns/productive-ambiguity-task-design-for-assumptions](patterns/productive-ambiguity-task-design-for-assumptions.md) — New pattern: productive ambiguity task design for assumptions, from Komatsu et al. 2024
* **Ingest**: [claims/unfolding-knowledge-elements-produces-deeper-conceptual-learning-opportunities](claims/unfolding-knowledge-elements-produces-deeper-conceptual-learning-opportunities.md) — New claim: unfolding knowledge elements produces deeper conceptual learning opportunities (Ademmer & Prediger 2025)
* **Ingest**: [patterns/grounding-and-unfolding-facilitation-moves](patterns/grounding-and-unfolding-facilitation-moves.md) — New pattern: grounding and unfolding facilitation moves, from Ademmer & Prediger 2025
* **Ingest**: [claims/mentored-inquiry-supports-transition-from-intuitive-to-formal-equation-reasoning](claims/mentored-inquiry-supports-transition-from-intuitive-to-formal-equation-reasoning.md) — New claim: mentored inquiry supports transition from intuitive to formal equation reasoning (Kapon & Schvartzer 2024)
* **Ingest**: [patterns/guided-equation-appropriation](patterns/guided-equation-appropriation.md) — New pattern: guided equation appropriation (Kapon & Schvartzer 2024)
* **Ingest**: [theories/equations-as-language](theories/equations-as-language.md) — New theory page on equations as language, from Kapon & Schvartzer 2024
* **Content**: [principles/epistemic-cognition](principles/epistemic-cognition.md) — Cross-linked Dishon et al. 2024 claim and Collaborative Critique strategy; added Epistemic Commitments as a related theory
* **Ingest**: [claims/collaborative-evidence-critique-shifts-students-toward-procedural-objectivity](claims/collaborative-evidence-critique-shifts-students-toward-procedural-objectivity.md) — New claim: collaborative evidence critique shifts students toward procedural objectivity (Dishon et al. 2024)
* **Ingest**: [strategies/collaborative-critique-and-redesign-of-flawed-studies](strategies/collaborative-critique-and-redesign-of-flawed-studies.md) — New strategy: collaborative critique and redesign of flawed studies, from Dishon et al. 2024
* **Ingest**: [claims/spontaneous-sentence-production-in-synthetic-planning-increases-understanding](claims/spontaneous-sentence-production-in-synthetic-planning-increases-understanding.md) — New claim: spontaneous sentence production in synthetic planning increases understanding (Baaijen & Galbraith 2018)
* **Ingest**: [patterns/synthetic-planning-for-discovery-oriented-writing](patterns/synthetic-planning-for-discovery-oriented-writing.md) — New pattern: synthetic planning for discovery-oriented writing (Baaijen & Galbraith 2018)
* **Ingest**: [theories/dual-process-account-of-discovery-in-writing](theories/dual-process-account-of-discovery-in-writing.md) — New theory page on the dual-process account of discovery in writing, from Baaijen & Galbraith 2018
* **Ingest**: [claims/curricular-knowledge-enables-responsive-instructional-moves](claims/curricular-knowledge-enables-responsive-instructional-moves.md) — New claim: curricular knowledge enables responsive instructional moves (Robertson et al. 2021)
* **Ingest**: [principles/curricular-knowledge-as-a-resource-for-responsiveness](principles/curricular-knowledge-as-a-resource-for-responsiveness.md) — New principle on curricular knowledge as a resource for responsiveness, from Robertson et al. 2021
* **Ingest**: [claims/spontaneous-additive-strategy-relates-to-multiplicative-reasoning](claims/spontaneous-additive-strategy-relates-to-multiplicative-reasoning.md) — New claim: spontaneous additive strategy relates to multiplicative reasoning (Tzur et al. 2021)
* **Ingest**: [theories/steffes-number-sequences-and-multiplicative-double-counting](theories/steffes-number-sequences-and-multiplicative-double-counting.md) — New theory page on Steffe's number sequences and multiplicative double counting, from Tzur et al. 2021
* **Content**: [principles/scaffolding-and-fading](principles/scaffolding-and-fading.md) — Added Kupers et al. 2017 claim link and key source
* **Ingest**: [claims/scaffolding-autonomy-dynamics-form-self-reinforcing-attractor-states](claims/scaffolding-autonomy-dynamics-form-self-reinforcing-attractor-states.md) — New claim: scaffolding/autonomy attractor-state dynamics, Kupers et al. 2017
* **Ingest**: [principles/persistent-autonomy-support-during-resistance](principles/persistent-autonomy-support-during-resistance.md) — New principle: persistent autonomy support during resistance, Kupers et al. 2017
* **Ingest**: [claims/student-uptake-of-support-predicts-small-group-answer-accuracy](claims/student-uptake-of-support-predicts-small-group-answer-accuracy.md) — New claim: student uptake of support predicts small-group answer accuracy, van de Pol et al. 2019
* **Content**: [strategies/small-group-scaffolding-tool](strategies/small-group-scaffolding-tool.md) — Cross-linked Step 5 to van de Pol et al. 2019's timely-fading finding
* **Content**: [principles/scaffolding-and-fading](principles/scaffolding-and-fading.md) — Added timely-fading and abrupt-shift constraints from van de Pol et al. 2019 and Kupers et al. 2017
* **Content**: [elements/scaffolding](elements/scaffolding.md) — Added timely-fading constraint from van de Pol et al. 2019
* **Ingest**: [claims/scripted-personal-inquiry-associated-with-inquiry-knowledge-gains](claims/scripted-personal-inquiry-associated-with-inquiry-knowledge-gains.md) — New claim (weak-moderate evidence): scripted personal inquiry and inquiry-knowledge gains, Sharples et al. 2015
* **Ingest**: [patterns/scripted-personally-meaningful-inquiry](patterns/scripted-personally-meaningful-inquiry.md) — New pattern: scripted personally meaningful inquiry, Sharples et al. 2015
* **Ingest**: [theories/personal-inquiry](theories/personal-inquiry.md) — New theory: personal inquiry and scripted orchestration, Sharples et al. 2015
* **Ingest**: [claims/boundary-crossing-mechanisms-unfold-sequentially-and-brokers-face-an-involvement-paradox](claims/boundary-crossing-mechanisms-unfold-sequentially-and-brokers-face-an-involvement-paradox.md) — New claim: sequential boundary-crossing mechanisms and broker involvement paradox, Akkerman & Bruining 2016
* **Ingest**: [strategies/broker-position-circulation](strategies/broker-position-circulation.md) — New strategy: broker position circulation, Akkerman & Bruining 2016
* **Ingest**: [patterns/multilevel-professional-development-school-partnership](patterns/multilevel-professional-development-school-partnership.md) — New pattern: multilevel PDS partnership structure, Akkerman & Bruining 2016
* **Content**: [theories/boundary-crossing-learning](theories/boundary-crossing-learning.md) — Extended with temporal sequencing, broker paradox, and three-way tension findings from Akkerman & Bruining 2016
* **Ingest**: [claims/students-progress-through-zones-of-mathematical-play](claims/students-progress-through-zones-of-mathematical-play.md) — New claim (weak evidence): students progress through zones of mathematical play, Williams-Pierce & Thevenow-Harrison 2021
* **Ingest**: [elements/provocative-objects](elements/provocative-objects.md) — New element: provocative objects, Williams-Pierce & Thevenow-Harrison 2021
* **Ingest**: [theories/zones-of-mathematical-play](theories/zones-of-mathematical-play.md) — New theory: zones of mathematical play, from Williams-Pierce & Thevenow-Harrison 2021
* **Ingest**: [claims/reflexive-noticing-shifts-stabilization-to-possibility-discourse](claims/reflexive-noticing-shifts-stabilization-to-possibility-discourse.md) — New claim: reflexive noticing shifts stabilization to possibility discourse, Rainio & Hofmann 2021
* **Ingest**: [strategies/reflexive-noticing-facilitation](strategies/reflexive-noticing-facilitation.md) — New strategy: reflexive noticing facilitation, Rainio & Hofmann 2021
* **Ingest**: [theories/reflexive-noticing](theories/reflexive-noticing.md) — New theory: reflexive noticing, from Rainio & Hofmann 2021
* **Ingest**: [claims/justice-oriented-youth-maker-programs-support-critical-identity-and-resistance](claims/justice-oriented-youth-maker-programs-support-critical-identity-and-resistance.md) — New claim: justice-oriented maker programs support critical identity and resistance, Greenberg et al. 2020
* **Ingest**: [patterns/critical-maker-entrepreneurialism-program](patterns/critical-maker-entrepreneurialism-program.md) — New pattern: critical maker-entrepreneurialism program, Greenberg et al. 2020
* **Ingest**: [theories/critical-maker-entrepreneurialism](theories/critical-maker-entrepreneurialism.md) — New theory: critical maker-entrepreneurialism, from Greenberg et al. 2020
* **Ingest**: [claims/resolving-participation-double-bind-requires-redesigned-activity-structures](claims/resolving-participation-double-bind-requires-redesigned-activity-structures.md) — New claim: resolving participation double-bind requires redesigned activity structures, Meléndez 2021
* **Ingest**: [patterns/differentiated-activity-structures-for-inclusive-participation](patterns/differentiated-activity-structures-for-inclusive-participation.md) — New pattern: differentiated activity structures for inclusive participation, Meléndez 2021
* **Content**: [theories/cultural-historical-activity-theory](theories/cultural-historical-activity-theory.md) — Extended with collective-vs-system-level expansive learning distinction and double-bind, from Meléndez 2021
* **Content**: [theories/self-regulated-learning](theories/self-regulated-learning.md) — Linked new claim from Omarchevska et al. 2022 on scientific reasoning and self-regulation
* **Ingest**: [claims/argumentation-quality-associated-with-reasoning-self-regulation-co-occurrence](claims/argumentation-quality-associated-with-reasoning-self-regulation-co-occurrence.md) — New claim: argumentation quality associated with reasoning/self-regulation co-occurrence, Omarchevska et al. 2022
* **Ingest**: [principles/integrate-self-regulation-with-scientific-reasoning-instruction](principles/integrate-self-regulation-with-scientific-reasoning-instruction.md) — New principle: integrate self-regulation with scientific reasoning instruction, Omarchevska et al. 2022
* **Ingest**: [claims/numerical-routines-individualize-through-bonding](claims/numerical-routines-individualize-through-bonding.md) — New claim: three-stage bonding sequence for numerical routines, Lavie & Sfard 2019
* **Ingest**: [principles/vertical-and-horizontal-bonding-in-numerical-routines](principles/vertical-and-horizontal-bonding-in-numerical-routines.md) — New principle: vertical/horizontal bonding in numerical routines, Lavie & Sfard 2019
* **Ingest**: [theories/commognition](theories/commognition.md) — New theory: commognition, from Lavie & Sfard 2019
* **Ingest**: [claims/explicit-contextualization-instruction-improves-writing-procedure-not-scores](claims/explicit-contextualization-instruction-improves-writing-procedure-not-scores.md) — New claim: contextualization instruction improves procedure not scores, Sendur et al. 2021
* **Ingest**: [patterns/explicit-instruction-in-historical-contextualization](patterns/explicit-instruction-in-historical-contextualization.md) — New pattern: explicit instruction in historical contextualization, Sendur et al. 2021
* **Ingest**: [theories/historical-reasoning-framework](theories/historical-reasoning-framework.md) — New theory: historical reasoning framework, from Sendur et al. 2021
* **Ingest**: [claims/emotion-dynamics-during-problem-solving-predict-learning-outcomes-context-dependently](claims/emotion-dynamics-during-problem-solving-predict-learning-outcomes-context-dependently.md) — New claim: emotion dynamics during PS-I predict outcomes context-dependently, Sinha 2022
* **Ingest**: [strategies/failure-driven-scaffolding](strategies/failure-driven-scaffolding.md) — New strategy: failure-driven scaffolding, from Sinha 2022
* **Ingest**: [theories/problem-solving-followed-by-instruction](theories/problem-solving-followed-by-instruction.md) — New theory: Problem-Solving Followed by Instruction (PS-I), from Sinha 2022
* **Ingest**: [claims/critical-constructive-feedback-is-neglected-at-multiple-stages](claims/critical-constructive-feedback-is-neglected-at-multiple-stages.md) — New claim: multi-stage feedback neglect and agent-signaling effect, Tärning et al. 2020
* **Ingest**: [elements/pedagogical-agent-signaling](elements/pedagogical-agent-signaling.md) — New element: pedagogical agent signaling for feedback salience, from Tärning et al. 2020
* **Ingest**: [theories/critical-constructive-feedback-processing](theories/critical-constructive-feedback-processing.md) — New theory: five-stage feedback-processing model from Tärning et al. 2020
* **Ingest**: [claims/critical-speculative-design-supports-critical-consciousness-in-science](claims/critical-speculative-design-supports-critical-consciousness-in-science.md) — New claim from Arad, Sanchez, & Bell 2023 (speculative design pedagogy for racial justice)
* **Ingest**: [patterns/threading-weaving-patternmaking](patterns/threading-weaving-patternmaking.md) — New pattern from Arad, Sanchez, & Bell 2023 (speculative design pedagogy for racial justice)
* **Ingest**: [theories/critical-speculative-design-pedagogy](theories/critical-speculative-design-pedagogy.md) — New theory from Arad, Sanchez, & Bell 2023 (speculative design pedagogy for racial justice)
* **Content**: [elements/scaffolding](elements/scaffolding.md) — Cross-linked Small-Group Scaffolding Tool from Calor et al. 2022
* **Ingest**: [claims/group-level-scaffolding-training-increases-teacher-process-support-and-student-participation](claims/group-level-scaffolding-training-increases-teacher-process-support-and-student-participation.md) — New claim from Calor, Dekker, van Drie, & Volman 2022 (group-level scaffolding)
* **Ingest**: [strategies/small-group-scaffolding-tool](strategies/small-group-scaffolding-tool.md) — New strategy from Calor, Dekker, van Drie, & Volman 2022 (group-level scaffolding)
* **Content**: [theories/epistemic-injustice](theories/epistemic-injustice.md) — Cross-linked Womanist Restorying from Shaw et al. 2023
* **Ingest**: [claims/restorying-supports-computing-identity-reconstruction](claims/restorying-supports-computing-identity-reconstruction.md) — New claim from Shaw, Coleman, Thomas, & Kafai 2023 (restorying computing education)
* **Ingest**: [strategies/restorying-through-electronic-quilting](strategies/restorying-through-electronic-quilting.md) — New strategy from Shaw, Coleman, Thomas, & Kafai 2023 (restorying computing education)
* **Ingest**: [theories/womanist-restorying](theories/womanist-restorying.md) — New theory from Shaw, Coleman, Thomas, & Kafai 2023 (restorying computing education)
* **Ingest**: [claims/positioning-students-as-sources-increases-productive-participation-in-science-discourse](claims/positioning-students-as-sources-increases-productive-participation-in-science-discourse.md) — New claim from Furberg & Silseth 2022 (invoking student resources)
* **Ingest**: [strategies/dialogic-facilitation-of-student-resources](strategies/dialogic-facilitation-of-student-resources.md) — New strategy from Furberg & Silseth 2022 (invoking student resources)
* **Ingest**: [claims/ai-mediated-feedback-in-hands-on-exhibits-improves-learning-and-engagement](claims/ai-mediated-feedback-in-hands-on-exhibits-improves-learning-and-engagement.md) — New claim from Yannier et al. 2022 (intelligent science exhibits)
* **Ingest**: [patterns/intelligent-mixed-reality-exhibit](patterns/intelligent-mixed-reality-exhibit.md) — New pattern from Yannier et al. 2022 (intelligent science exhibits)
* **Content**: [principles/collaborative-learning](principles/collaborative-learning.md) — Cross-linked group creativity claim and new principle from Pierroux et al. 2022
* **Ingest**: [claims/well-defined-tasks-and-accessible-materials-support-shared-creative-influence](claims/well-defined-tasks-and-accessible-materials-support-shared-creative-influence.md) — New claim from Pierroux, Steier, & Ludvigsen 2022 (group creativity in adolescence)
* **Ingest**: [principles/conditions-for-productive-group-creativity](principles/conditions-for-productive-group-creativity.md) — New principle from Pierroux, Steier, & Ludvigsen 2022 (group creativity in adolescence)
* **Content**: [elements/perspective-taking](elements/perspective-taking.md) — Cross-linked Participant Examples from Cohen, Hod, & Ben-Zvi 2023
* **Ingest**: [claims/participant-examples-support-identity-reconstruction-through-academic-content](claims/participant-examples-support-identity-reconstruction-through-academic-content.md) — New claim from Cohen, Hod, & Ben-Zvi 2023 (national identity reconstruction)
* **Ingest**: [elements/participant-examples](elements/participant-examples.md) — New element from Cohen, Hod, & Ben-Zvi 2023 (national identity reconstruction)
* **Ingest**: [strategies/humanistic-knowledge-building-community](strategies/humanistic-knowledge-building-community.md) — New strategy from Cohen, Hod, & Ben-Zvi 2023 (national identity reconstruction)
* **Content**: [principles/cultural-life-experiences-connections](principles/cultural-life-experiences-connections.md) — Cross-linked embodied dance improvisation claim from Solomon et al. 2022
* **Ingest**: [claims/embodied-dance-improvisation-supports-physics-engagement-and-sensemaking](claims/embodied-dance-improvisation-supports-physics-engagement-and-sensemaking.md) — New claim from Solomon et al. 2022 (embodied physics dance)
* **Ingest**: [patterns/embodied-physics-inquiry-through-dance](patterns/embodied-physics-inquiry-through-dance.md) — New pattern from Solomon et al. 2022 (embodied physics dance)
* **Content**: [theories/funds-of-knowledge](theories/funds-of-knowledge.md) — Extended to include embodied and cultural-practice resources per Solomon et al. 2022
* **Correction**: [strategies/broker-facilitated-cross-domain-integration](strategies/broker-facilitated-cross-domain-integration.md) — Removed leftover template placeholder comments that lint flagged as broken links
* **Content**: [principles/epistemic-cognition](principles/epistemic-cognition.md) — Added Epistemic Games related theory link from Arthars et al. (2024)
* **Ingest**: [claims/epistemic-games-reveal-unacknowledged-disciplinary-differences-in-teams](claims/epistemic-games-reveal-unacknowledged-disciplinary-differences-in-teams.md) — Initial ingest from Arthars, Markauskaite & Goodyear (2024), JLS 33(2)
* **Ingest**: [elements/epistemic-games-shared-understanding-moves](elements/epistemic-games-shared-understanding-moves.md) — Initial ingest from Arthars, Markauskaite & Goodyear (2024), JLS 33(2)
* **Ingest**: [theories/epistemic-games](theories/epistemic-games.md) — Initial ingest from Arthars, Markauskaite & Goodyear (2024), JLS 33(2)
* **Content**: [principles/authentic-audiences-purposes](principles/authentic-audiences-purposes.md) — Added Organization Simulation and Interdisciplinary CBRE examples from the JLS interdisciplinary-learning special issue
* **Content**: [elements/group-work](elements/group-work.md) — Added Organization Simulation for Interdisciplinary Learning as a pattern using this element
* **Ingest**: [claims/organization-simulation-knowledge-practices-support-interdisciplinary-learning](claims/organization-simulation-knowledge-practices-support-interdisciplinary-learning.md) — Initial ingest from Muukkonen & Kajamaa (2024), JLS 33(2)
* **Ingest**: [patterns/organization-simulation-for-interdisciplinary-learning](patterns/organization-simulation-for-interdisciplinary-learning.md) — Initial ingest from Muukkonen & Kajamaa (2024), JLS 33(2)
* **Ingest**: [theories/knowledge-objects-and-knowledge-practices](theories/knowledge-objects-and-knowledge-practices.md) — Initial ingest from Muukkonen & Kajamaa (2024), JLS 33(2)
* **Ingest**: [claims/subtle-teacher-guidance-not-imposition-enables-interdisciplinary-integration](claims/subtle-teacher-guidance-not-imposition-enables-interdisciplinary-integration.md) — Initial ingest from Schwarz, Heyd-Metzuyanim, Koichu, Tabach & Yarden (2024), JLS 33(2)
* **Ingest**: [patterns/interdisciplinary-societal-dilemma-units](patterns/interdisciplinary-societal-dilemma-units.md) — Initial ingest from Schwarz, Heyd-Metzuyanim, Koichu, Tabach & Yarden (2024), JLS 33(2)
* **Ingest**: [claims/interdisciplinary-humanities-units-improve-interdisciplinary-competences](claims/interdisciplinary-humanities-units-improve-interdisciplinary-competences.md) — Initial ingest from Novis-Deutsch et al. (2024), JLS 33(2)
* **Content**: [principles/inquiry-based-learning](principles/inquiry-based-learning.md) — Added Interdisciplinary CBRE and ISD Units examples from the JLS interdisciplinary-learning special issue
* **Ingest**: [claims/course-based-research-experience-boundary-objects-support-disciplinary-integration-and-authentic-research-networks](claims/course-based-research-experience-boundary-objects-support-disciplinary-integration-and-authentic-research-networks.md) — Initial ingest from Papendieck & Clarke (2024), JLS 33(2)
* **Ingest**: [patterns/interdisciplinary-course-based-research-experience](patterns/interdisciplinary-course-based-research-experience.md) — Initial ingest from Papendieck & Clarke (2024), JLS 33(2)
* **Ingest**: [theories/ecological-paradigm-of-interdisciplinary-learning](theories/ecological-paradigm-of-interdisciplinary-learning.md) — Initial ingest from Kali (2024), JLS 33(2), synthesizing design implications from the JLS interdisciplinary-learning special issue
* **Content**: [principles/community-based-learning](principles/community-based-learning.md) — Added Humanizing Co-Design with Educators example from Potvin et al. (2024)
* **Content**: [principles/reflection](principles/reflection.md) — Added Humanizing Co-Design with Educators example from Potvin et al. (2024)
* **Ingest**: [claims/attending-to-affect-in-co-design-supports-community-and-cross-scale-transfer](claims/attending-to-affect-in-co-design-supports-community-and-cross-scale-transfer.md) — Initial ingest from Potvin, Teeters, Penuel & Dimidjian (2024), JLS 33(1)
* **Ingest**: [patterns/humanizing-co-design-with-educators](patterns/humanizing-co-design-with-educators.md) — Initial ingest from Potvin, Teeters, Penuel & Dimidjian (2024), JLS 33(1)
* **Content**: [theories/cultural-historical-activity-theory](theories/cultural-historical-activity-theory.md) — Added Boundary Crossing Learning related theory link
* **Content**: [theories/situated-learning](theories/situated-learning.md) — Added Boundary Crossing Learning related theory link
* **Content**: [elements/hands-on-learning](elements/hands-on-learning.md) — Added Broker-Facilitated Cross-Domain Integration affordance from Liukkonen et al. (2023)
* **Ingest**: [claims/multivoiced-boundary-crossing-supports-holistic-nature-connection-and-ethical-reflection](claims/multivoiced-boundary-crossing-supports-holistic-nature-connection-and-ethical-reflection.md) — Initial ingest from Liukkonen, Vartiainen, Pöllänen & Kokko (2023), JLS 32(4-5)
* **Ingest**: [strategies/broker-facilitated-cross-domain-integration](strategies/broker-facilitated-cross-domain-integration.md) — Initial ingest from Liukkonen, Vartiainen, Pöllänen & Kokko (2023), JLS 32(4-5)
* **Ingest**: [patterns/bioart-boundary-crossing-making](patterns/bioart-boundary-crossing-making.md) — Initial ingest from Liukkonen, Vartiainen, Pöllänen & Kokko (2023), JLS 32(4-5)
* **Ingest**: [theories/boundary-crossing-learning](theories/boundary-crossing-learning.md) — Initial ingest from Liukkonen, Vartiainen, Pöllänen & Kokko (2023), JLS 32(4-5); also draws on Papendieck & Clarke (2024)
* **Ingest**: [claims/rpp-adaptive-practices-sustain-partnerships-during-disruption](claims/rpp-adaptive-practices-sustain-partnerships-during-disruption.md) — Initial ingest from Popa, Anderson, Denner, McKenney & Peurach (2023), JLS 32(4-5)
* **Ingest**: [strategies/responsive-rpp-adaptation-during-disruption](strategies/responsive-rpp-adaptation-during-disruption.md) — Initial ingest from Popa, Anderson, Denner, McKenney & Peurach (2023), JLS 32(4-5)
* **Content**: [claims/positioning-personal-experience-as-epistemic-resource-supports-critical-orientation-expansion](claims/positioning-personal-experience-as-epistemic-resource-supports-critical-orientation-expansion.md) — Linked related claim from Sedawi & Calabrese Barton (2024)
* **Content**: [claims/personal-connection-to-data-supports-critical-data-literacy-stance-taking](claims/personal-connection-to-data-supports-critical-data-literacy-stance-taking.md) — Linked related claim from Sedawi & Calabrese Barton (2024)
* **Content**: [patterns/data-storytelling-forage-remix-diy](patterns/data-storytelling-forage-remix-diy.md) — Added Agentic Data-Engagement Positions affordance link
* **Content**: [theories/onto-epistemic-heterogeneity](theories/onto-epistemic-heterogeneity.md) — Added Epistemic Injustice related theory link
* **Content**: [principles/cultural-life-experiences-connections](principles/cultural-life-experiences-connections.md) — Added Epistemic Injustice theory and linked claim from Sedawi & Calabrese Barton (2024)
* **Ingest**: [claims/lively-data-and-agentic-positions-support-epistemically-just-crisis-sensemaking](claims/lively-data-and-agentic-positions-support-epistemically-just-crisis-sensemaking.md) — Initial ingest from Sedawi & Calabrese Barton (2024), JLS 33(4-5)
* **Ingest**: [elements/agentic-data-engagement-positions](elements/agentic-data-engagement-positions.md) — Initial ingest from Sedawi & Calabrese Barton (2024), JLS 33(4-5)
* **Ingest**: [theories/epistemic-injustice](theories/epistemic-injustice.md) — Initial ingest from Sedawi & Calabrese Barton (2024), JLS 33(4-5)
* **Content**: [theories/constructivism](theories/constructivism.md) — Added Sociomaterial Agency of Tools related theory link
* **Content**: [elements/hands-on-learning](elements/hands-on-learning.md) — Added Sociomaterial Agency of Tools affordance and material-choice constraint claim from Peppler & Thompson (2024)
* **Ingest**: [claims/material-choice-shapes-conceptual-learning-and-participation](claims/material-choice-shapes-conceptual-learning-and-participation.md) — Initial ingest from Peppler & Thompson (2024), JLS 33(4-5)
* **Ingest**: [theories/sociomaterial-agency-of-tools](theories/sociomaterial-agency-of-tools.md) — Initial ingest from Peppler & Thompson (2024), JLS 33(4-5)
* **Content**: [theories/cultural-historical-activity-theory](theories/cultural-historical-activity-theory.md) — Added Adaptive Cycles Framework related theory link
* **Ingest**: [claims/pd-support-salience-depends-on-adaptive-cycle-phase](claims/pd-support-salience-depends-on-adaptive-cycle-phase.md) — Initial ingest from Ehrenfeld & Stengel (2025), JLS 34(3)
* **Ingest**: [strategies/video-based-feedback-cycle-for-teacher-teams](strategies/video-based-feedback-cycle-for-teacher-teams.md) — Initial ingest from Ehrenfeld & Stengel (2025), JLS 34(3)
* **Ingest**: [theories/adaptive-cycles-framework](theories/adaptive-cycles-framework.md) — Initial ingest from Ehrenfeld & Stengel (2025), JLS 34(3)
* **Content**: [theories/situated-learning](theories/situated-learning.md) — Added new Claims section linking Marshall & Horn (2025) on teachers as agentic synthesizers of PD practices
* **Ingest**: [claims/teachers-synthesize-pd-practices-with-context-not-just-transfer-them](claims/teachers-synthesize-pd-practices-with-context-not-just-transfer-them.md) — Initial ingest from Marshall & Horn (2025), JLS
* **Content**: [patterns/reflective-practice](patterns/reflective-practice.md) — Linked claim from Clark, Scott, DiPasquale & Becker (2024) on designerly stances in pre-service teacher PD
* **Ingest**: [claims/course-emphasis-on-reframing-shifts-teachers-toward-designerly-stances](claims/course-emphasis-on-reframing-shifts-teachers-toward-designerly-stances.md) — Initial ingest from Clark, Scott, DiPasquale & Becker (2024), JLS
* **Ingest**: [theories/designerly-stances](theories/designerly-stances.md) — Initial ingest from Clark, Scott, DiPasquale & Becker (2024), JLS
* **Content**: [principles/epistemic-cognition](principles/epistemic-cognition.md) — Added Mechanistic Reasoning theory and linked claim from Shtechman, Ergazaki & Haskel-Ittah (2025)
* **Ingest**: [claims/elementary-students-prefer-mechanistic-explanations](claims/elementary-students-prefer-mechanistic-explanations.md) — Initial ingest from Shtechman, Ergazaki & Haskel-Ittah (2025), JLS
* **Ingest**: [elements/evaluating-and-justifying-mechanistic-explanations](elements/evaluating-and-justifying-mechanistic-explanations.md) — Initial ingest from Shtechman, Ergazaki & Haskel-Ittah (2025), JLS
* **Ingest**: [theories/mechanistic-reasoning](theories/mechanistic-reasoning.md) — Initial ingest from Shtechman, Ergazaki & Haskel-Ittah (2025), JLS
* **Content**: [theories/onto-epistemic-heterogeneity](theories/onto-epistemic-heterogeneity.md) — Added Funds of Knowledge related theory link
* **Content**: [principles/cultural-life-experiences-connections](principles/cultural-life-experiences-connections.md) — Added Funds of Knowledge theory and linked claim from Randall, Earnest, Thota & Mensing (2025)
* **Ingest**: [claims/funds-of-knowledge-tasks-reveal-computational-thinking](claims/funds-of-knowledge-tasks-reveal-computational-thinking.md) — Initial ingest from Randall, Earnest, Thota & Mensing (2025), JLS
* **Ingest**: [strategies/family-interview-based-assessment-task-design](strategies/family-interview-based-assessment-task-design.md) — Initial ingest from Randall, Earnest, Thota & Mensing (2025), JLS
* **Ingest**: [theories/funds-of-knowledge](theories/funds-of-knowledge.md) — Initial ingest from Randall, Earnest, Thota & Mensing (2025), JLS
* **Content**: [elements/video-based-reflection](elements/video-based-reflection.md) — Extended element to cover children's self-interpretation of play video (Vescio 2025) alongside teacher PD use (Ehrenfeld & Stengel 2025)
* **Content**: [principles/learner-choice](principles/learner-choice.md) — Linked claim from Vescio (2025) on children's video interpretation of unscripted play
* **Ingest**: [claims/childrens-video-interpretation-of-play-reveals-mathematical-and-social-sensemaking](claims/childrens-video-interpretation-of-play-reveals-mathematical-and-social-sensemaking.md) — Initial ingest from Vescio (2025), JLS 34(3)
* **Content**: [principles/authentic-audiences-purposes](principles/authentic-audiences-purposes.md) — Added Identity-Centered e-Textile Making example from Tofel-Grehl et al. (2024)
* **Content**: [theories/self-determination-theory](theories/self-determination-theory.md) — Added Rightful Presence related theory and Identity-Centered e-Textile Making example from Tofel-Grehl et al. (2024)
* **Ingest**: [claims/identity-centered-making-supports-stem-engagement-and-identity-affirmation](claims/identity-centered-making-supports-stem-engagement-and-identity-affirmation.md) — Initial ingest from Tofel-Grehl et al. (2024), JLS
* **Ingest**: [patterns/identity-centered-e-textile-making](patterns/identity-centered-e-textile-making.md) — Initial ingest from Tofel-Grehl et al. (2024), JLS
* **Ingest**: [theories/rightful-presence](theories/rightful-presence.md) — Initial ingest from Tofel-Grehl et al. (2024), JLS
* **Content**: [theories/cognitive-apprenticeship](theories/cognitive-apprenticeship.md) — Added Examples link to Computational Essay Writing pattern from Odden & Zwicki (2025)
* **Ingest**: [claims/creating-computational-literature-develops-computational-literacy](claims/creating-computational-literature-develops-computational-literacy.md) — Initial ingest from Odden & Zwicki (2025), JLS
* **Ingest**: [patterns/computational-essay-writing](patterns/computational-essay-writing.md) — Initial ingest from Odden & Zwicki (2025), JLS
* **Content**: [principles/discussing-race](principles/discussing-race.md) — Added Person-Centered Psychology as supporting theory from Hod & Tueg (2026)
* **Content**: [principles/building-empathy](principles/building-empathy.md) — Added Person-Centered Psychology as supporting theory from Hod & Tueg (2026)
* **Ingest**: [theories/person-centered-psychology](theories/person-centered-psychology.md) — Initial ingest from Hod & Tueg (2026), JLS
* **Claim**: [patterns/reflective-practice](patterns/reflective-practice.md) — Linked claim from Sarfati-Shaulov & Vedder-Weiss (2025)
* **Ingest**: [claims/elaborated-discussion-of-narrated-emotions-supports-teacher-learning](claims/elaborated-discussion-of-narrated-emotions-supports-teacher-learning.md) — Initial ingest from Sarfati-Shaulov & Vedder-Weiss (2025), JLS 35(1)
* **Ingest**: [strategies/narrated-emotional-storytelling-in-teacher-pd](strategies/narrated-emotional-storytelling-in-teacher-pd.md) — Initial ingest from Sarfati-Shaulov & Vedder-Weiss (2025), JLS 35(1)
* **Claim**: [patterns/problem-based-learning-pbl](patterns/problem-based-learning-pbl.md) — Linked claim from Miller & Li (2026) on spontaneous vs. contrived authenticity
* **Ingest**: [claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry](claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry.md) — Initial ingest from Miller & Li (2026), JLS 35(2)
* **Ingest**: [claims/awareness-of-heterogeneity-does-not-predict-regulation-success](claims/awareness-of-heterogeneity-does-not-predict-regulation-success.md) — Initial ingest from Spang, Greisel & Kollar (2026), JLS 35(2)
* **Ingest**: [claims/homogeneous-problem-perceptions-predict-regulation-success](claims/homogeneous-problem-perceptions-predict-regulation-success.md) — Initial ingest from Spang, Greisel & Kollar (2026), JLS 35(2)
* **Claim**: [principles/cultural-life-experiences-connections](principles/cultural-life-experiences-connections.md) — Linked claim from Champion, Solomon & Lammey (2025)
* **Claim**: [patterns/formative-assessment](patterns/formative-assessment.md) — Linked claim from Champion, Solomon & Lammey (2025)
* **Ingest**: [claims/multimodal-culturally-grounded-assessment-supports-engagement-and-agency](claims/multimodal-culturally-grounded-assessment-supports-engagement-and-agency.md) — Initial ingest from Champion, Solomon & Lammey (2025), JLS 34(4)
* **Ingest**: [elements/embodied-choreographic-assessment](elements/embodied-choreographic-assessment.md) — Initial ingest from Champion, Solomon & Lammey (2025), JLS 34(4)
* **Ingest**: [elements/listening-palette](elements/listening-palette.md) — Initial ingest from Champion, Solomon & Lammey (2025), JLS 34(4)
* **Claim**: [principles/collaborative-learning](principles/collaborative-learning.md) — Linked claims from Palatnik & Abrahamson (2026) and Spang, Greisel & Kollar (2026)
* **Ingest**: [claims/embodied-collaborative-construction-can-build-shared-geometric-reasoning](claims/embodied-collaborative-construction-can-build-shared-geometric-reasoning.md) — Initial ingest from Palatnik & Abrahamson (2026), JLS
* **Ingest**: [patterns/body-scale-collaborative-construction](patterns/body-scale-collaborative-construction.md) — Initial ingest from Palatnik & Abrahamson (2026), JLS
* **Ingest**: [claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction](claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) — Initial ingest from Su, Chi & Nagashima (2026), JLS 35(1)
* **Ingest**: [patterns/pair-c-framework](patterns/pair-c-framework.md) — Initial ingest from Su, Chi & Nagashima (2026), JLS 35(1)
* **Claim**: [principles/authentic-audiences-purposes](principles/authentic-audiences-purposes.md) — Linked claims from Kahn & Hall (2026) and Miller & Li (2026)
* **Ingest**: [claims/personal-connection-to-data-supports-critical-data-literacy-stance-taking](claims/personal-connection-to-data-supports-critical-data-literacy-stance-taking.md) — Initial ingest from Kahn & Hall (2026), JLS
* **Ingest**: [patterns/data-storytelling-forage-remix-diy](patterns/data-storytelling-forage-remix-diy.md) — Initial ingest from Kahn & Hall (2026), JLS
* **Claim**: [principles/cultural-life-experiences-connections](principles/cultural-life-experiences-connections.md) — Added Onto-Epistemic Heterogeneity as a supporting theory and linked a new claim from Higgs, Kaimana & Isero (2026)
* **Ingest**: [claims/positioning-personal-experience-as-epistemic-resource-supports-critical-orientation-expansion](claims/positioning-personal-experience-as-epistemic-resource-supports-critical-orientation-expansion.md) — Initial ingest from Higgs, Kaimana & Isero (2026), JLS ahead-of-print
* **Ingest**: [theories/onto-epistemic-heterogeneity](theories/onto-epistemic-heterogeneity.md) — Initial ingest from Higgs, Kaimana & Isero (2026), JLS ahead-of-print
* **Claim**: [principles/community-based-learning](principles/community-based-learning.md) — Added CHAT as a qualifying theory and linked a new constraint claim from Engeström & Käyhkö (2021)
* **Ingest**: [claims/community-projects-need-conceptual-framing-to-avoid-narrowing-the-learning-object](claims/community-projects-need-conceptual-framing-to-avoid-narrowing-the-learning-object.md) — Initial ingest from Engeström & Käyhkö (2021), JLS 30(3)
* **Ingest**: [theories/cultural-historical-activity-theory](theories/cultural-historical-activity-theory.md) — Initial ingest from Engeström & Käyhkö (2021), JLS 30(3) — CHAT with boundary object and dialogicality
* **Content**: [principles/validity-reliability-and-bias-in-classroom-assessment](principles/validity-reliability-and-bias-in-classroom-assessment.md) — Enriched with constructs, three types of reliability, and the reliability-does-not-imply-validity distinction (Unit 2)
* **Ingest**: [strategies/teacher_action_research](strategies/teacher_action_research.md) — New strategy: teacher action research cycle (Unit 2)
* **Ingest**: [theories/developmental-research-designs](theories/developmental-research-designs.md) — New theory: cross-sectional/longitudinal/sequential developmental research designs (Unit 2)
* **Ingest**: [elements/research-data-collection-methods](elements/research-data-collection-methods.md) — New element: observation/survey/archival research data-collection methods (Unit 2)
* **Ingest**: [principles/designing-a-valid-experiment](principles/designing-a-valid-experiment.md) — New principle: experimental design mechanics, IV/DV, blinding, random sampling vs assignment (Unit 2)
* **Ingest**: [claims/illusory-correlations-persist-through-confirmation-bias](claims/illusory-correlations-persist-through-confirmation-bias.md) — New claim (ld-13): illusory correlations and the full-moon lunar-lunacy meta-analysis (Unit 2)
* **Ingest**: [theories/research-design-taxonomy](theories/research-design-taxonomy.md) — New theory: quant/qual, descriptive/correlational/experimental research design taxonomy (Unit 2)
* **Ingest**: [principles/evidence-based-teaching-and-scientific-reasoning](principles/evidence-based-teaching-and-scientific-reasoning.md) — New principle: evidence-based teaching, confirmation bias, falsifiability, scientific method (Unit 2)
* **Content**: [strategies/consider_socio-cultural_factors](strategies/consider_socio-cultural_factors.md) — Enriched with NCES digital-divide statistics (Unit 1)
* **Content**: [principles/intelligence-testing-uses-and-limits](principles/intelligence-testing-uses-and-limits.md) — Enriched with Binet's founding history and purpose for intelligence testing (Unit 1)
* **Ingest**: [theories/critical-pedagogy](theories/critical-pedagogy.md) — New theory: Critical Pedagogy (Unit 1)
* **Ingest**: [theories/essentialism-and-perennialism-educational-philosophy](theories/essentialism-and-perennialism-educational-philosophy.md) — New theory: Essentialism and Perennialism as educational philosophies (Unit 1)
* **Ingest**: [theories/existentialism-educational-philosophy](theories/existentialism-educational-philosophy.md) — New theory: Existentialism as an educational philosophy (Unit 1)
* **Ingest**: [theories/pragmatism-and-progressivism-educational-philosophy](theories/pragmatism-and-progressivism-educational-philosophy.md) — New theory: Pragmatism and Progressivism as educational philosophies (Unit 1)
* **Ingest**: [theories/realism-educational-philosophy](theories/realism-educational-philosophy.md) — New theory: Realism as an educational philosophy (Unit 1)
* **Ingest**: [theories/idealism-educational-philosophy](theories/idealism-educational-philosophy.md) — New theory: Idealism as an educational philosophy (Unit 1)
* **Ingest**: [principles/twelve-characteristics-of-effective-teachers](principles/twelve-characteristics-of-effective-teachers.md) — New principle: Walker (2008) twelve characteristics of effective teachers (Unit 1)
* **Ingest**: [principles/nbpts-five-core-propositions](principles/nbpts-five-core-propositions.md) — New principle: NBPTS Five Core Propositions for accomplished teaching (Unit 1)
* **Ingest**: [theories/fullers-concerns-theory](theories/fullers-concerns-theory.md) — New theory: Fuller's Concerns Theory of teacher development, self/task/impact stages (Unit 1)
* **Ingest**: [principles/educational-psychology-as-art-and-science](principles/educational-psychology-as-art-and-science.md) — New principle: educational psychology as both art and science (Unit 1)
* **Ingest**: [patterns/herbarts-formal-steps](patterns/herbarts-formal-steps.md) — New pattern: Herbart's five formal steps for lesson sequencing (Unit 1)
* **Content**: [elements/observation](elements/observation.md) — Enriched with classroom-assessment-specific observation content (Unit 10)
* **Content**: [principles/intelligence-testing-uses-and-limits](principles/intelligence-testing-uses-and-limits.md) — Cross-linked terminology-shift and standardized-test-bias pages (Unit 10)
* **Content**: [principles/assessment-for-learning](principles/assessment-for-learning.md) — Enriched with Dweck incremental/fixed view of ability shaping assessment purpose (Unit 10)
* **Content**: [strategies/addressing_stereotype_threat](strategies/addressing_stereotype_threat.md) — Enriched with Aronson & Steele 2005 mechanism and citation (Unit 10)
* **Content**: [strategies/effort-based_praise](strategies/effort-based_praise.md) — Enriched with precise Dweck 2000 mechanism and citation (Unit 10)
* **Content**: [strategies/frequent,_low-stakes_quizzes](strategies/frequent,_low-stakes_quizzes.md) — Enriched with Dempster & Perkins and Bangert-Downs citations (Unit 10)
* **Content**: [strategies/portfolio_development](strategies/portfolio_development.md) — Enriched with four-dimension purpose taxonomy, implementation steps, Vermont reliability case study (Unit 10)
* **Content**: [elements/performance-based-assessment](elements/performance-based-assessment.md) — Enriched with authentic/alternative assessment distinction and advantages/disadvantages (Unit 10)
* **Content**: [strategies/checklists](strategies/checklists.md) — Enriched with checklist-vs-rating-scale distinction (Unit 10)
* **Content**: [strategies/rubrics](strategies/rubrics.md) — Enriched with holistic/analytic/rating-scale distinctions and citations (Unit 10)
* **Ingest**: [strategies/traffic-lights-self-assessment](strategies/traffic-lights-self-assessment.md) — New strategy page: Black & Wiliam's traffic-lights confidence self-assessment technique (Unit 10)
* **Ingest**: [claims/teacher-effectiveness-compounds-over-consecutive-years](claims/teacher-effectiveness-compounds-over-consecutive-years.md) — New claim page: Dallas study on teacher effectiveness and assignment patterns (Unit 10)
* **Ingest**: [principles/grading-policy-decisions](principles/grading-policy-decisions.md) — New principle page: weighting, hodgepodge grading, absolute vs relative grading, grade descriptions (Unit 10)
* **Ingest**: [principles/wise-feedback-across-difference](principles/wise-feedback-across-difference.md) — New principle page: Cohen/Steele/Ross wise feedback across racial/ethnic difference (Unit 10)
* **Ingest**: [principles/standardized-test-fairness-and-bias](principles/standardized-test-fairness-and-bias.md) — New principle page: item content/format bias, differential prediction, stereotype threat mechanism (Unit 10)
* **Ingest**: [principles/high-stakes-testing-accountability-effects](principles/high-stakes-testing-accountability-effects.md) — New principle page: NCLB content-standard/alignment problems, AYP growth-vs-proficiency, teaching to the test (Unit 10)
* **Ingest**: [principles/criterion-and-norm-referenced-testing](principles/criterion-and-norm-referenced-testing.md) — New principle page: criterion vs norm-referenced testing, norm groups, achievement/aptitude/diagnostic test types (Unit 10)
* **Ingest**: [principles/validity-reliability-and-bias-in-classroom-assessment](principles/validity-reliability-and-bias-in-classroom-assessment.md) — New principle page: validity types, Table of Specifications, reliability, offensiveness/unfair penalization bias (Unit 10)
* **Ingest**: [elements/constructed-response-assessment-items](elements/constructed-response-assessment-items.md) — New element page: completion/short-answer and extended-response items, scoring reliability challenges (Unit 10)
* **Ingest**: [elements/selected-response-assessment-items](elements/selected-response-assessment-items.md) — New element page: multiple-choice, true-false, and matching items consolidated with common-error tables (Unit 10)
* **Correction**: [strategies/establish_consistent_routines](strategies/establish_consistent_routines.md) — Fixed in-text citation abbreviation (EIS -> IES) and added its full reference to Key Sources
* **Content**: [strategies/warning_and_consequence](strategies/warning_and_consequence.md) — Cross-linked low-profile control and natural/logical consequences pages (Unit 9)
* **Content**: [strategies/repairing_harm](strategies/repairing_harm.md) — Cross-linked conflict-resolution and natural/logical consequences pages (Unit 9)
* **Content**: [theories/turiels-social-domain-theory](theories/turiels-social-domain-theory.md) — Cross-linked classroom rules-vs-procedures application (Unit 9)
* **Content**: [principles/culturally-responsive-classroom-norms](principles/culturally-responsive-classroom-norms.md) — Enriched with Tharp/Dillon/Bowers & Flinders on culturally responsive behavior management (Unit 9)
* **Content**: [principles/reinforcement-theory](principles/reinforcement-theory.md) — Enriched with Thorndike's puzzle box and the negative reinforcement trap (Unit 9)
* **Content**: [strategies/conditioning-natural-reinforcers](strategies/conditioning-natural-reinforcers.md) — Enriched with classroom-specific natural reinforcer examples (Unit 9)
* **Content**: [strategies/establish_consistent_routines](strategies/establish_consistent_routines.md) — Enriched with engaged learning time and the five elements of teaching routines (Unit 9)
* **Content**: [strategies/classroom_seating_arrangements](strategies/classroom_seating_arrangements.md) — Enriched with seating configuration options, citations, and ABC-model antecedent cross-link (Unit 9)
* **Ingest**: [strategies/teacher-effectiveness-training-conflict-resolution](strategies/teacher-effectiveness-training-conflict-resolution.md) — New strategy page: Gordon's problem-ownership/active-listening/I-message/negotiation model (Unit 9)
* **Ingest**: [strategies/ignoring-and-nonverbal-redirection](strategies/ignoring-and-nonverbal-redirection.md) — New strategy page: ignoring minor misbehavior and nonverbal cues (Unit 9)
* **Ingest**: [strategies/low-profile-classroom-control](strategies/low-profile-classroom-control.md) — New strategy page: Rinne's anticipation/deflection/reaction (Unit 9)
* **Ingest**: [elements/antecedent-behavior-consequence-model](elements/antecedent-behavior-consequence-model.md) — New element page: ABC model, Dead Person's Rule, negative reinforcement trap (Unit 9)
* **Ingest**: [principles/natural-and-logical-consequences](principles/natural-and-logical-consequences.md) — New principle page: natural/logical consequences vs punishment (Unit 9)
* **Ingest**: [principles/classroom-space-and-procedural-design](principles/classroom-space-and-procedural-design.md) — New principle page: arranging space, procedures vs rules, task difficulty sequencing, transitions (Unit 9)
* **Ingest**: [principles/effective-classroom-management-plan](principles/effective-classroom-management-plan.md) — New principle page: six criteria for an effective classroom management plan (Unit 9)
* **Ingest**: [theories/kounins-classroom-management-research](theories/kounins-classroom-management-research.md) — New theory page: Kounin's withitness, overlapping, ripple effect, and the Emmer et al. 1980 study (Unit 9)
* **Ingest**: [theories/glassers-choice-theory-and-cooperative-learning](theories/glassers-choice-theory-and-cooperative-learning.md) — New theory page: Glasser's choice theory, boss/leader management, cooperative learning (Unit 9)
* **Ingest**: [theories/ginotts-congruent-communication](theories/ginotts-congruent-communication.md) — New theory page: Ginott's congruent communication approach (Unit 9)
* **Ingest**: [theories/teaching-styles-warmth-and-control](theories/teaching-styles-warmth-and-control.md) — New theory page: Soar & Soar's warmth x control teaching-style framework (Unit 9)
* **Content**: [patterns/blended-learning](patterns/blended-learning.md) — Substantially enrich stub with definitions, Means 2010, Palloff & Pratt 2013 (Unit 8 enrichment)
* **Content**: [strategies/differentiated_teaching](strategies/differentiated_teaching.md) — Substantially enrich stub with Tomlinson's content/process/product framework (Unit 8 enrichment)
* **Content**: [patterns/flipped-learning](patterns/flipped-learning.md) — Add Lage Platt Treglia 2000 historical precursor citation (Unit 8 enrichment)
* **Content**: [patterns/peer-instruction](patterns/peer-instruction.md) — Add Hake 1998, Crouch & Mazur 2001, Deslauriers 2011 effect sizes (Unit 8 enrichment)
* **Content**: [patterns/traditional-lecture-based-instruction](patterns/traditional-lecture-based-instruction.md) — Add Bligh 2000 objective-dependent effectiveness breakdown (Unit 8 enrichment)
* **Content**: [principles/active-learning](principles/active-learning.md) — Add Freeman 2014 precise effect sizes and equity/discussion claim cross-links (Unit 8 enrichment)
* **Content**: [elements/advance-organizers](elements/advance-organizers.md) — Add attention-focusing appeals and anticipatory-set content (Unit 8 enrichment)
* **Content**: [elements/state-objectives](elements/state-objectives.md) — Add cognitive-vs-behavioral objectives distinction (Gronlund/Mager) (Unit 8 enrichment)
* **Ingest**: [strategies/pause-procedure](strategies/pause-procedure.md) — New strategy: pause procedure (Unit 8 ingest)
* **Ingest**: [claims/active-learning-narrows-achievement-gaps](claims/active-learning-narrows-achievement-gaps.md) — New claim ld-11: active learning narrows achievement gaps (Unit 8 ingest)
* **Ingest**: [claims/discussion-promotes-more-active-thought-than-lecture](claims/discussion-promotes-more-active-thought-than-lecture.md) — New claim ld-10: discussion vs lecture active thought (Unit 8 ingest)
* **Ingest**: [patterns/emergent-curriculum](patterns/emergent-curriculum.md) — New pattern: emergent curriculum (Unit 8 ingest)
* **Ingest**: [elements/addressing-student-misconceptions](elements/addressing-student-misconceptions.md) — New element: addressing student misconceptions (Unit 8 ingest)
* **Ingest**: [patterns/team-based-learning](patterns/team-based-learning.md) — New pattern: Team-Based Learning (TBL), RAP/4S framework (Unit 8 ingest)
* **Ingest**: [patterns/just-in-time-teaching](patterns/just-in-time-teaching.md) — New pattern: Just-In-Time Teaching (JiTT) (Unit 8 ingest)
* **Ingest**: [patterns/understanding-by-design](patterns/understanding-by-design.md) — New pattern: Understanding by Design backward design framework (Unit 8 ingest)
* **Content**: [principles/social-interdependence](principles/social-interdependence.md) — Cross-link culturally responsive classroom norms (Unit 7 enrichment)
* **Content**: [theories/metacognition](theories/metacognition.md) — Cross-link bilingual metalinguistic awareness claim (Unit 7 enrichment)
* **Content**: [strategies/multi-tiered_system_of_supports_(mtss)](strategies/multi-tiered_system_of_supports_(mtss).md) — Substantially rewrite stub with RTI/MTSS tier structure and history (Unit 7 enrichment)
* **Content**: [principles/universal-design-for-learning](principles/universal-design-for-learning.md) — Add concrete classroom tactics and alternative-assessment content (Unit 7 enrichment)
* **Content**: [theories/triarchic-theory-of-intelligence](theories/triarchic-theory-of-intelligence.md) — Add creativity-components table and practical-intelligence validity caveat (Unit 7 enrichment)
* **Ingest**: [principles/culturally-responsive-classroom-norms](principles/culturally-responsive-classroom-norms.md) — New page: culturally responsive classroom norms (Unit 7 ingest)
* **Ingest**: [claims/bilingual-fluency-enhances-metalinguistic-awareness](claims/bilingual-fluency-enhances-metalinguistic-awareness.md) — New claim ld-9: bilingual fluency enhances metalinguistic awareness (Unit 7 ingest)
* **Ingest**: [claims/heritage-language-preservation-supports-english-acquisition](claims/heritage-language-preservation-supports-english-acquisition.md) — New claim ld-8: heritage language preservation supports English acquisition (Unit 7 ingest)
* **Ingest**: [principles/gender-equitable-classroom-interaction](principles/gender-equitable-classroom-interaction.md) — New page: gender-equitable classroom interaction patterns (Unit 7 ingest)
* **Ingest**: [principles/least-restrictive-environment](principles/least-restrictive-environment.md) — New page: least restrictive environment (Unit 7 ingest)
* **Ingest**: [strategies/explicit-interpersonal-skills-instruction](strategies/explicit-interpersonal-skills-instruction.md) — New strategy: explicit interpersonal skills instruction (Unit 7 ingest)
* **Ingest**: [principles/functional-behavior-assessment](principles/functional-behavior-assessment.md) — New page: functional behavior assessment and trigger identification (Unit 7 ingest)
* **Ingest**: [principles/supporting-students-with-autism-spectrum-disorder](principles/supporting-students-with-autism-spectrum-disorder.md) — New page: supporting students with autism spectrum disorder (Unit 7 ingest)
* **Ingest**: [principles/supporting-students-with-adhd](principles/supporting-students-with-adhd.md) — New page: supporting students with ADHD (Unit 7 ingest)
* **Ingest**: [elements/specific-learning-disabilities](elements/specific-learning-disabilities.md) — New page: specific learning disabilities, dyslexia/dysgraphia/dyscalculia (Unit 7 ingest)
* **Ingest**: [principles/cognitive-styles](principles/cognitive-styles.md) — New page: cognitive styles, field dependence/independence and impulsivity/reflectivity (Unit 7 ingest)
* **Ingest**: [principles/supporting-students-with-intellectual-disabilities](principles/supporting-students-with-intellectual-disabilities.md) — New page: supporting students with intellectual disabilities (Unit 7 ingest)
* **Ingest**: [principles/supporting-gifted-and-talented-students](principles/supporting-gifted-and-talented-students.md) — New page: supporting gifted and talented students, Terman study (Unit 7 ingest)
* **Ingest**: [principles/intelligence-testing-uses-and-limits](principles/intelligence-testing-uses-and-limits.md) — New page: IQ testing, standardization, and bias (Unit 7 ingest)
* **Ingest**: [claims/flynn-effect-rising-iq-scores-over-generations](claims/flynn-effect-rising-iq-scores-over-generations.md) — New claim ld-7: the Flynn effect (Unit 7 ingest)
* **Content**: [theories/cognitive-load-theory](theories/cognitive-load-theory.md) — Cross-link seductive details effect as an extraneous-load source (Unit 6 enrichment)
* **Content**: [principles/reinforcement-theory](principles/reinforcement-theory.md) — Add overjustification effect as a documented constraint (Unit 6 enrichment)
* **Content**: [theories/behaviorism](theories/behaviorism.md) — Add overjustification effect cross-link (Unit 6 enrichment)
* **Content**: [theories/arcs-model](theories/arcs-model.md) — Add sub-tactics table and interest-model/Skinner cross-links (Unit 6 enrichment)
* **Content**: [theories/expectancy-value-theory](theories/expectancy-value-theory.md) — Add multiplicative expectancy x value formula and expectancy/instrumentality/valence teaching tactics (Unit 6 enrichment)
* **Content**: [theories/self-determination-theory](theories/self-determination-theory.md) — Add intrinsic-extrinsic continuum and autonomy/competence/relatedness teaching tactics (Unit 6 enrichment)
* **Content**: [theories/self-efficacy-theory](theories/self-efficacy-theory.md) — Expand four sources of self-efficacy and learned helplessness with moderators/citations (Unit 6 enrichment)
* **Content**: [theories/attribution-theory](theories/attribution-theory.md) — Add stable-attribution downside, effort-based-attribution conditions, mindset citations (Unit 6 enrichment)
* **Ingest**: [theories/student-orientation-toward-achievement](theories/student-orientation-toward-achievement.md) — New page: Student Orientation Toward Achievement, Covington's self-worth typology (Unit 6 ingest)
* **Ingest**: [theories/goal-orientation-theory](theories/goal-orientation-theory.md) — New page: Goal Orientation Theory, 2x2 mastery/performance x approach/avoidance model (Unit 6 ingest)
* **Ingest**: [claims/seductive-details-distract-from-learning](claims/seductive-details-distract-from-learning.md) — New claim ld-6: seductive details effect (Unit 6 ingest)
* **Ingest**: [theories/four-phase-interest-development](theories/four-phase-interest-development.md) — New page: Four-Phase Model of Interest Development (Unit 6 ingest)
* **Ingest**: [claims/overjustification-effect-reduces-intrinsic-motivation](claims/overjustification-effect-reduces-intrinsic-motivation.md) — New claim ld-5: overjustification effect (Unit 6 ingest)
* **Ingest**: [theories/instinct-drive-and-arousal-theories](theories/instinct-drive-and-arousal-theories.md) — New page: Instinct, Drive, and Arousal Theories (Unit 6 ingest)
* **Content**: [strategies/project-based_learning_(pbl)](strategies/project-based_learning_(pbl).md) — Enriched from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Content**: [patterns/socratic-seminar](patterns/socratic-seminar.md) — Enriched from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Content**: [principles/annotating](principles/annotating.md) — Enriched from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Content**: [theories/metacognition](theories/metacognition.md) — Enriched from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Content**: [principles/social-interdependence](principles/social-interdependence.md) — Enriched from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Content**: [patterns/jigsaw-method](patterns/jigsaw-method.md) — Enriched from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Ingest**: [patterns/hunters-effective-teaching-model](patterns/hunters-effective-teaching-model.md) — Ingested from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Ingest**: [strategies/student-teams-achievement-divisions](strategies/student-teams-achievement-divisions.md) — Ingested from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Ingest**: [principles/fostering-creative-thinking](principles/fostering-creative-thinking.md) — Ingested from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Ingest**: [strategies/ideal-problem-solving-model](strategies/ideal-problem-solving-model.md) — Ingested from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Ingest**: [principles/well-structured-vs-ill-structured-problems](principles/well-structured-vs-ill-structured-problems.md) — Ingested from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Ingest**: [claims/functional-fixedness-limits-problem-solving](claims/functional-fixedness-limits-problem-solving.md) — Ingested from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Ingest**: [theories/critical-thinking](theories/critical-thinking.md) — Ingested from Educational Psychology Unit 5 (Facilitating Complex Thinking), Arduini-Van Hoose
* **Content**: [theories/self-efficacy-theory](theories/self-efficacy-theory.md) — Enriched from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Content**: [theories/self-regulated-learning](theories/self-regulated-learning.md) — Enriched from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Content**: [theories/social-learning-theory](theories/social-learning-theory.md) — Enriched from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Content**: [principles/reinforcement-theory](principles/reinforcement-theory.md) — Enriched from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Content**: [theories/behaviorism](theories/behaviorism.md) — Enriched from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Content**: [principles/transfer-of-learning](principles/transfer-of-learning.md) — Enriched from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [elements/self-regulation-questionnaire](elements/self-regulation-questionnaire.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/prosocial-modeling](strategies/prosocial-modeling.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/learning-hierarchy-task-analysis](strategies/learning-hierarchy-task-analysis.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/conditioning-natural-reinforcers](strategies/conditioning-natural-reinforcers.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/behavioral-feedback-for-responses](strategies/behavioral-feedback-for-responses.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/effective-presentation-for-errorless-learning](strategies/effective-presentation-for-errorless-learning.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/prompting-hierarchy](strategies/prompting-hierarchy.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/time-out-negative-punishment](strategies/time-out-negative-punishment.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/token-economies](strategies/token-economies.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [strategies/hugging-and-bridging-for-transfer](strategies/hugging-and-bridging-for-transfer.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [principles/educational-readiness](principles/educational-readiness.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [claims/early-delay-of-gratification-predicts-later-outcomes](claims/early-delay-of-gratification-predicts-later-outcomes.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [patterns/five-e-model](patterns/five-e-model.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [theories/blooms-taxonomy](theories/blooms-taxonomy.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Ingest**: [theories/locus-of-control](theories/locus-of-control.md) — Ingested from Educational Psychology Unit 4 (The Learning Process), Arduini-Van Hoose
* **Content**: [theories/kohlberg-moral-development](theories/kohlberg-moral-development.md) — Enriched with content from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Content**: [theories/psychosocial-theory-of-identity-development](theories/psychosocial-theory-of-identity-development.md) — Enriched with content from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Content**: [theories/information-processing-theory](theories/information-processing-theory.md) — Enriched with content from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Content**: [theories/sociocultural-theory](theories/sociocultural-theory.md) — Enriched with content from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Content**: [theories/stages-of-cognitive-development](theories/stages-of-cognitive-development.md) — Enriched with content from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/metacognition](theories/metacognition.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/executive-function-development](theories/executive-function-development.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [principles/bullying-prevention-and-intervention](principles/bullying-prevention-and-intervention.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/adolescent-peer-group-structure](theories/adolescent-peer-group-structure.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [claims/motor-milestones-vary-by-cultural-childcare-practices](claims/motor-milestones-vary-by-cultural-childcare-practices.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [claims/conversational-turns-predict-language-development](claims/conversational-turns-predict-language-development.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [principles/heritage-language-maintenance](principles/heritage-language-maintenance.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [principles/supporting-early-language-development](principles/supporting-early-language-development.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [elements/child-directed-speech](elements/child-directed-speech.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/language-acquisition-theory](theories/language-acquisition-theory.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [principles/character-education](principles/character-education.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/turiels-social-domain-theory](theories/turiels-social-domain-theory.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/gilligans-ethic-of-care](theories/gilligans-ethic-of-care.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/piaget-moral-development](theories/piaget-moral-development.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/play-and-cognitive-development](theories/play-and-cognitive-development.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Ingest**: [theories/adolescent-brain-development](theories/adolescent-brain-development.md) — New page from Educational Psychology (Arduini-Van Hoose), Unit 3: The Developing Learner
* **Content**: [theories/constructionism](theories/constructionism.md) — Cross-link to new theories/stages-of-cognitive-development.md
* **Content**: [theories/constructivism](theories/constructivism.md) — Cross-link to new theories/stages-of-cognitive-development.md
* **Source**: [theories/cognitive-load-theory](theories/cognitive-load-theory.md) — Add Chandler & Sweller (1991) key source found via Educational Learning Theories ch12
* **Content**: [theories/information-processing-theory](theories/information-processing-theory.md) — Add forgetting theories, metacognition/metamemory, rehearsal vs elaboration, criticisms from Educational Learning Theories ch12
* **Ingest**: [theories/maslow-hierarchy-of-needs](theories/maslow-hierarchy-of-needs.md) — New page: Maslow's hierarchy of needs, from Educational Learning Theories ch11
* **Content**: [strategies/develop_observable_criteria](strategies/develop_observable_criteria.md) — Cross-link to new theories/blooms-taxonomy.md
* **Ingest**: [theories/blooms-taxonomy](theories/blooms-taxonomy.md) — New page: Bloom's Taxonomy across cognitive/psychomotor/affective domains, from Educational Learning Theories ch10
* **Content**: [theories/multiple-intelligences-theory](theories/multiple-intelligences-theory.md) — Add existential intelligence, identification criteria, g-factor/no-validation critique thread from Educational Learning Theories ch9
* **Ingest**: [theories/psychosocial-theory-of-identity-development](theories/psychosocial-theory-of-identity-development.md) — New page: Erikson's psychosocial theory of identity development, from Educational Learning Theories ch8
* **Ingest**: [theories/bioecological-model-of-human-development](theories/bioecological-model-of-human-development.md) — New page: Bronfenbrenner's bioecological model, from Educational Learning Theories ch7
* **Content**: [principles/experiential-learning](principles/experiential-learning.md) — Cross-link to new theories/experiential-learning-theory.md
* **Ingest**: [theories/experiential-learning-theory](theories/experiential-learning-theory.md) — New page: Kolb's Experiential Learning Theory, split from principles/experiential-learning.md, from Educational Learning Theories ch6
* **Ingest**: [theories/kohlberg-moral-development](theories/kohlberg-moral-development.md) — New page: Kohlberg's stages of moral development, from Educational Learning Theories ch5
* **Content**: [theories/sociocultural-theory](theories/sociocultural-theory.md) — Add private speech, cultural-tool transmission modes, internalization, expanded criticisms from Educational Learning Theories ch4
* **Content**: [theories/social-learning-theory](theories/social-learning-theory.md) — Add Social Cognitive Theory expansion: triadic reciprocal causation, agency, capability, self-regulation, criticisms, from Educational Learning Theories ch3
* **Ingest**: [theories/stages-of-cognitive-development](theories/stages-of-cognitive-development.md) — New page: Piaget's stages of cognitive development, from Educational Learning Theories ch2
* **Content**: [theories/behaviorism](theories/behaviorism.md) — Add Pavlov/classical conditioning, Skinner box, named techniques, criticisms from Educational Learning Theories ch1
* **Content**: [elements/makerspace](elements/makerspace.md) — Cross-linked new Constructionism theory page (LIDT Foundations ingest)
* **Content**: [theories/constructivism](theories/constructivism.md) — Cross-linked new Constructionism theory page (LIDT Foundations ingest)
* **Content**: [principles/learner-centered-paradigm](principles/learner-centered-paradigm.md) — Enriched with Reigeluth's new-roles taxonomy for teachers/students/technology, from "An Instructional Theory for the Post-Industrial Age" (ch. 20 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Content**: [principles/problem-based-learning](principles/problem-based-learning.md) — Added Savery (2019) key source and PBI-critique caveat from Reigeluth (ch. 20), LIDT Foundations ingest
* **Content**: [principles/performance-technology](principles/performance-technology.md) — Enriched with Rossett & Schafer's Performance Support Tools taxonomy, from Boileau, "Informal Learning" (ch. 17 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Content**: [theories/information-processing-theory](theories/information-processing-theory.md) — Enriched with encoding types, working-memory model, and memory taxonomy from Spielman et al., "Memory" (ch. 9 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [patterns/project-and-instructional-space](patterns/project-and-instructional-space.md) — Ingested from Reigeluth, "An Instructional Theory for the Post-Industrial Age" (ch. 20 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [patterns/massive-open-online-course](patterns/massive-open-online-course.md) — Ingested from Weller, "Twenty Years of EdTech" (ch. 8) and Wiley, "Open Educational Resources" (ch. 37) of LIDT Foundations, edtechbooks.org/lidtfoundations
* **Ingest**: [elements/open-educational-resources](elements/open-educational-resources.md) — Ingested from Wiley, "Open Educational Resources" (ch. 37) and Weller, "Twenty Years of EdTech" (ch. 8) of LIDT Foundations, edtechbooks.org/lidtfoundations
* **Ingest**: [claims/media-comparison-studies-produce-uninterpretable-results](claims/media-comparison-studies-produce-uninterpretable-results.md) — Ingested from Lockee, Moore & Burton, "Old Concerns with New Distance Education Research" (ch. 36 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/free-choice-learning-environment-design](principles/free-choice-learning-environment-design.md) — Ingested from Ashton, Nelson & Millward, "Careers in Museum Learning" (ch. 52 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/access-use-effectiveness-framework](principles/access-use-effectiveness-framework.md) — Ingested from Davies & West, "Technology Integration in Schools" (ch. 31 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/universal-design-for-learning](principles/universal-design-for-learning.md) — Ingested from U.S. Office of Educational Technology, "National Educational Technology Plan" (ch. 30 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/informal-learning](principles/informal-learning.md) — Ingested from Boileau, "Informal Learning" (ch. 17 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/communities-of-innovation](principles/communities-of-innovation.md) — Ingested from West, "Communities of Innovation" (ch. 14 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/four-boundaries-of-learning-community](principles/four-boundaries-of-learning-community.md) — Ingested from Williams & West, "Learning Communities" (ch. 13 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [theories/triarchic-theory-of-intelligence](theories/triarchic-theory-of-intelligence.md) — Ingested from Spielman et al., "Intelligence" (ch. 10 of LIDT Foundations, edtechbooks.org/lidtfoundations) -- Sternberg's Triarchic Theory
* **Ingest**: [theories/multiple-intelligences-theory](theories/multiple-intelligences-theory.md) — Ingested from Spielman et al., "Intelligence" (ch. 10 of LIDT Foundations, edtechbooks.org/lidtfoundations) -- Gardner's Multiple Intelligences
* **Ingest**: [theories/constructionism](theories/constructionism.md) — Ingested from Lee, "A Short History of the Learning Sciences" (ch. 4 of LIDT Foundations, edtechbooks.org/lidtfoundations) -- Papert's constructionism
* **Ingest**: [theories/design-layers-theory](theories/design-layers-theory.md) — Ingested from Gibbons, "What and How Do Designers Design?" (ch. 24 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Content**: [theories/first-principles-of-instruction](theories/first-principles-of-instruction.md) — Cross-linked new ARCS Model theory page
* **Content**: [theories/self-determination-theory](theories/self-determination-theory.md) — Cross-linked new ARCS Model theory page
* **Content**: [theories/self-efficacy-theory](theories/self-efficacy-theory.md) — Cross-linked new ARCS Model theory page
* **Content**: [theories/expectancy-value-theory](theories/expectancy-value-theory.md) — Cross-linked new ARCS Model theory page
* **Ingest**: [theories/arcs-model](theories/arcs-model.md) — Ingested from Park, "Motivation Theories and Instructional Design" (ch. 15 of LIDT Foundations, edtechbooks.org/lidtfoundations) -- Keller's ARCS model
* **Content**: [theories/self-determination-theory](theories/self-determination-theory.md) — Cross-linked new Self-Efficacy, Attribution, and Expectancy-Value theory pages (LIDT Foundations ingest)
* **Content**: [theories/social-learning-theory](theories/social-learning-theory.md) — Cross-linked new Self-Efficacy Theory page (LIDT Foundations ingest)
* **Ingest**: [theories/expectancy-value-theory](theories/expectancy-value-theory.md) — Ingested from Park, "Motivation Theories and Instructional Design" (ch. 15 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [theories/attribution-theory](theories/attribution-theory.md) — Ingested from Park (ch. 15) and Seifert & Sutton (ch. 16), "Motivation Theories" chapters of LIDT Foundations, edtechbooks.org/lidtfoundations
* **Ingest**: [theories/self-efficacy-theory](theories/self-efficacy-theory.md) — Ingested from Park (ch. 15) and Seifert & Sutton (ch. 16), "Motivation Theories" chapters of LIDT Foundations, edtechbooks.org/lidtfoundations
* **Content**: [theories/constructivism](theories/constructivism.md) — Cross-linked new Makerspace element (LIDT Foundations ingest)
* **Content**: [principles/user-centered-design-for-learning](principles/user-centered-design-for-learning.md) — Cross-linked new Cone of Experience principle (LIDT Foundations ingest)
* **Content**: [theories/self-determination-theory](theories/self-determination-theory.md) — Cross-linked new Digital Open Badges element (LIDT Foundations ingest)
* **Ingest**: [principles/cone-of-experience](principles/cone-of-experience.md) — Ingested from Lee & Reeves, "Edgar Dale and the Cone of Experience" (ch. 7 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [elements/digital-open-badges](elements/digital-open-badges.md) — Ingested from Farmer & West, "Opportunities and Challenges with Digital Open Badges" (ch. 41 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [elements/learning-analytics-feedback](elements/learning-analytics-feedback.md) — Ingested from Baker & Inventado, "Educational Data Mining and Learning Analytics" (ch. 40 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [elements/makerspace](elements/makerspace.md) — Ingested from Dousay, "Defining and Differentiating the Makerspace" (ch. 28 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Content**: [principles/community-of-inquiry](principles/community-of-inquiry.md) — Cross-linked new Online Course Design pattern (LIDT Foundations ingest)
* **Content**: [patterns/game-based-mastery-learning](patterns/game-based-mastery-learning.md) — Cross-linked new Programmed Instruction and Epistemic Games patterns (LIDT Foundations ingest)
* **Content**: [theories/situated-learning](theories/situated-learning.md) — Cross-linked new Epistemic Games pattern (LIDT Foundations ingest)
* **Content**: [theories/self-determination-theory](theories/self-determination-theory.md) — Cross-linked new Epistemic Games pattern (LIDT Foundations ingest)
* **Ingest**: [patterns/epistemic-games](patterns/epistemic-games.md) — Ingested from Shaffer, Squire, Halverson & Gee, "Video Games and the Future of Learning" (ch. 39) and Rieber, Smith & Noah, "The Value of Serious Play" (ch. 38) of LIDT Foundations, edtechbooks.org/lidtfoundations
* **Ingest**: [patterns/online-course-design](patterns/online-course-design.md) — Ingested from Martin & Oyarzun, "Distance Learning" (ch. 35 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [patterns/programmed-instruction](patterns/programmed-instruction.md) — Ingested from Molenda, "Programmed Instruction" (ch. 6 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Content**: [theories/cognitive-load-theory](theories/cognitive-load-theory.md) — Cross-linked new User-Centered Design for Learning principle (LIDT Foundations ingest)
* **Ingest**: [principles/learner-centered-paradigm](principles/learner-centered-paradigm.md) — Ingested from Watson & Reigeluth, "The Learner-Centered Paradigm of Education" (ch. 34 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/user-centered-design-for-learning](principles/user-centered-design-for-learning.md) — Ingested from Earnshaw, Tawfik & Schmidt, "User Experience Design" (ch. 29 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/technology-integration-levels](principles/technology-integration-levels.md) — Ingested from Kimmons, "K-12 Technology Frameworks" (ch. 32 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/tpack](principles/tpack.md) — Ingested from Koehler & Mishra, "What Is Technological Pedagogical Content Knowledge?" (ch. 33 of LIDT Foundations, edtechbooks.org/lidtfoundations)
* **Ingest**: [principles/performance-technology](principles/performance-technology.md) — Ingested from Stefaniak, "Performance Technology" (ch. 27 of LIDT Foundations, edtechbooks.org/lidtfoundations)
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

* **Content**: [theories/sociocultural-theory](theories/sociocultural-theory.md) — Cross-linked to new Stages of Cognitive Development theory page
* **Content**: [theories/constructionism](theories/constructionism.md) — Cross-linked to new Stages of Cognitive Development theory page
* **Content**: [theories/constructivism](theories/constructivism.md) — Cross-linked to new Stages of Cognitive Development theory page
* **Content**: [theories/social-learning-theory](theories/social-learning-theory.md) — Enriched with content from Educational Learning Theories (2nd ed., Zhou & Brown)
* **Content**: [theories/behaviorism](theories/behaviorism.md) — Enriched with content from Educational Learning Theories (2nd ed., Zhou & Brown)
* **Ingest**: [theories/maslow-hierarchy-of-needs](theories/maslow-hierarchy-of-needs.md) — New theory page from Educational Learning Theories (2nd ed., Zhou & Brown)
* **Ingest**: [theories/psychosocial-theory-of-identity-development](theories/psychosocial-theory-of-identity-development.md) — New theory page from Educational Learning Theories (2nd ed., Zhou & Brown)
* **Ingest**: [theories/bioecological-model-of-human-development](theories/bioecological-model-of-human-development.md) — New theory page from Educational Learning Theories (2nd ed., Zhou & Brown)
* **Ingest**: [theories/kohlberg-moral-development](theories/kohlberg-moral-development.md) — New theory page from Educational Learning Theories (2nd ed., Zhou & Brown)
* **Ingest**: [theories/stages-of-cognitive-development](theories/stages-of-cognitive-development.md) — New theory page from Educational Learning Theories (2nd ed., Zhou & Brown)
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

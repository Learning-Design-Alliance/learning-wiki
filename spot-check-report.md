# Duplicate-judge spot check: GLM vs Sonnet

10 group(s) compared.
Agreement on is_duplicate: 6/10 (60%)

## creating-visual-representations (principles, elements) — DISAGREE
- GLM:    is_duplicate=True  canonical=principles
  - reasoning: The element page is a thin stub whose description restates the principle's core idea and whose 'Affordances' section simply links back to the principle itself, adding no distinct lens or content. It substantially duplicates the principle under a different type label.
- Sonnet: is_duplicate=False  canonical=None
  - reasoning: The principle page argues why/when to have learners create visual representations (rationale, evidence, contexts, constraints), while the element page names the concrete instructional component (the activity/artifact type) that enacts that principle, fitting the schema's principle-vs-element distinction. The element is thin but structurally distinct, linking to the principle as its affordance rather than restating it.

## anchored-instruction (elements, patterns) — AGREE
- GLM:    is_duplicate=False  canonical=None
  - reasoning: The element page describes anchored instruction as a reusable instructional component (a rich anchor scenario) with design requirements and related elements, while the pattern page describes a lesson-level design sequence built on that component, including sequencing, theory, claims, and grain size. This matches the wiki's schema where an element and a pattern can legitimately share a name while covering different facets. Both pages cross-reference each other appropriately and cite different primary sources.
- Sonnet: is_duplicate=False  canonical=None
  - reasoning: The element page describes anchored instruction as a reusable instructional component (the anchor scenario itself), detailing its requirements, affordances, and design implications as a building block. The pattern page describes a full lesson-level design that uses this element along with others (Problem Scenario, Peer Interaction), providing a sequence, theoretical grounding, claims, and impact—consistent with the schema's element/pattern distinction.

## just-in-time-learning (elements, patterns) — AGREE
- GLM:    is_duplicate=True  canonical=elements
  - reasoning: The pattern page is a thin stub that restates the element's description nearly verbatim and adds no distinct lesson-level design content — it merely links back to the element and one related pattern. This is the same facet of the concept under two type labels, not a genuinely different lens like a theory or principle would be.
- Sonnet: is_duplicate=True  canonical=elements/just-in-time-learning
  - reasoning: The pattern page adds no lesson-level structure, sequence, or procedure beyond restating the element's definition, and even lists the element itself as one of its 'Elements Used,' which is circular. It functions as a thin stub duplicating the element rather than a genuinely distinct lesson-level design.

## inquiry-based-learning (principles, elements, patterns) — DISAGREE
- GLM:    is_duplicate=False  canonical=None
  - reasoning: The three pages occupy genuinely different facets per the schema: the principle page is a rich, claim-linked treatment of when and why inquiry works; the element page describes the instructional component and its affordances; the pattern page is a lesson-level design composition referencing the element. They cross-link appropriately rather than repeating content, so all three are worth keeping.
- Sonnet: is_duplicate=True  canonical=principles/inquiry-based-learning
  - reasoning: The element and pattern pages don't actually add a distinct component-level or lesson-design lens; they just restate the principle's definition, requirements, and constraints in thinner form, with the pattern offering no real lesson structure beyond an 'elements used' list. This is a case of the same content sliced across type labels rather than genuinely different facets.

## guided-discovery (elements, patterns) — AGREE
- GLM:    is_duplicate=True  canonical=elements
  - reasoning: The pattern page is a stub that adds no distinct lesson-level design content: its description merely restates the element's definition, and its 'Design' section just links back to the element itself. It covers the same facet of guided discovery under a different type label rather than a genuinely different lens.
- Sonnet: is_duplicate=True  canonical=elements
  - reasoning: The pattern page is a bare stub that merely restates the element's description and lists the element itself as its main 'design' component, adding no lesson-level structure, sequence, or context distinct from the element. There's already a separate, more developed 'Guided Discovery Learning' pattern that fills the pattern role, making this thin pattern page redundant with the element.

## digital-learning (principles, elements) — AGREE
- GLM:    is_duplicate=False  canonical=None
  - reasoning: The two pages cover genuinely different facets: the principle page argues when and why digital environments improve instruction (with claims, theory links, and design conditions), while the element page describes digital mediation as a structural component of instruction with affordances and patterns that use it. Their content overlaps only in topic, not substance, and both fit the schema's allowance for shared names across types.
- Sonnet: is_duplicate=False  canonical=None
  - reasoning: The principle page argues *why/when* to use digital environments (rationale, tradeoffs, supporting claims, target learners), while the element page treats digital learning as a concrete instructional component (a medium/tool that patterns like Flipped Learning or Game-Based Mastery Learning plug into, with its own affordances and related elements). This mirrors the schema's intended principle-vs-element split rather than duplication.

## constructivism (principles, theories) — AGREE
- GLM:    is_duplicate=False  canonical=None
  - reasoning: The two pages cover genuinely different facets: the theory page explains the underlying perspective/mechanism (Piaget, Vygotsky, family of approaches), while the principle page prescribes instructional design moves (active meaning-making tasks, constraints like under-guidance risk) and links back to the theory as its base. This matches the schema's allowance for same-name pages under different types. Both are worth keeping.
- Sonnet: is_duplicate=False  canonical=None
  - reasoning: The theory page describes constructivism as a broad explanatory view of how learners build knowledge, with implications for a wide family of approaches (inquiry, problem-based learning, discussion, reflection). The principle page narrows this into an actionable instructional recommendation with specific requirements, constraints, and target learners/objectives for designing active meaning-making tasks. They occupy distinct schema roles (mechanism vs. actionable recommendation) despite shared sources and claims.

## observationshadowing (principles, elements) — AGREE
- GLM:    is_duplicate=False  canonical=None
  - reasoning: The principle page is a full treatment of observation/shadowing as a learning design, with evidence claims, theory grounding, target learners/objectives, and examples. The element page is a brief instructional-component stub that explicitly links back to the principle as an affordance, consistent with the schema's intended cross-type relationship. They share a name and lens but differ in depth and role, and both are worth keeping.
- Sonnet: is_duplicate=False  canonical=None
  - reasoning: The principle page argues for the pedagogical value of observation/shadowing (rationale, claims, theory, contexts for use), while the element page describes it as a discrete instructional component with minimal design requirements and affordances linking back to the principle. This is the schema's intended principle-element pairing rather than duplication, since the element explicitly treats the principle as its rationale.

## peer-teaching (elements, patterns) — DISAGREE
- GLM:    is_duplicate=False  canonical=None
  - reasoning: The two pages occupy different grains and lenses: the element describes the instructional component (learners explaining to peers) with design implications, affordances, and related elements, while the pattern is a lesson-level design that explicitly composes the element alongside Peer Discussion. The pattern page even links to the element page, showing intentional schema layering rather than duplication. Both are thin but legitimately distinct and worth keeping.
- Sonnet: is_duplicate=True  canonical=elements
  - reasoning: The pattern page is not a distinct lesson-level design built from the element—it merely restates the element's definition and even lists 'Peer Teaching' itself as an element it uses, which is circular. There's no unique instructional sequence, structure, or context described that differentiates it from the element page.

## scaffolding (principles, elements, strategies) — DISAGREE
- GLM:    is_duplicate=True  canonical=principles
  - reasoning: The principles and elements pages cover the same facet — temporary support for tasks beyond independent performance, with fading to build independence — differing only in type label and depth, so they are duplicates. The strategies page is legitimately distinct, applying scaffolding specifically to emotional self-regulation in an emotionally safe context, and should be kept.
- Sonnet: is_duplicate=False  canonical=None
  - reasoning: The principle and element pages are the expected type-pair (rationale vs. instructional component) and are clearly complementary, not duplicative. The strategy page, while it repeats the fade-support-over-time idea, actually narrows the concept to a specific applied context (emotional self-regulation) with its own target learners, instructions, and example, which is a legitimate strategy-level instantiation rather than a restatement of the general principle.

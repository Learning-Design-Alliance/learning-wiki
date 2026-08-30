---

Frontmatter:
```
---
type: strategy
title: Multiple Representations
description: Presenting the same concept in several forms — verbal, visual, symbolic, tabular, concrete — so learners build integrated, flexible understanding and can translate between notations.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
sources:
  - id: ainsworth-2006
    resource: "https://doi.org/10.1016/j.learninstruc.2006.03.001"
    title: "Ainsworth, S. (2006). DeFT: A conceptual framework for considering learning with multiple representations. *Learning and Instruction, 16*(3), 183–198"
    author: "Ainsworth, S"
  - id: mayer-2009
    resource: "https://doi.org/10.1017/CBO9780511811678"
    title: "Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press"
    author: "Mayer, R. E"
  - id: rau-2017
    resource: "https://doi.org/10.1007/s10648-016-9365-3"
    title: "Rau, M. A. (2017). Conditions for the effectiveness of multiple visual representations in enhancing STEM learning. *Educational Psychology Review, 29*(4), 717–761"
    author: "Rau, M. A"
  - id: goldstone-2005
    resource: "https://doi.org/10.1207/s15327809jls1401_4"
    title: "Goldstone, R. L., & Son, J. Y. (2005). The transfer of scientific principles using concrete and idealized simulations. *Journal of the Learning Sciences, 14*(1), 69–110"
    author: "Goldstone, R. L., & Son, J. Y"
---
```

Description: 2-3 sentences. Define, name DeFT functions, note translation is the hard part.

Design Implications overview: Multiple representations work through three functions (Ainsworth): complementing, constraining, constructing. Multimedia evidence [+S]. But connections don't form spontaneously — need prompts [self-explanation claim +S].

Requirements:
- Representations that are genuinely complementary, not redundant duplicates
- Explicit support for mapping/translation between forms (prompts, [Articulation](../elements/articulation.md))
- Learners must be able to interpret each individual form first — an unread representation contributes nothing but load
- Contiguous/integrated presentation ([Cognitive Load Management](../elements/cognitive-load-management.md))

Constraints:
- Poorly coordinated representations cause split-attention and redundancy effects, harming learning [-S] (Mayer redundancy; split-attention). Link chunking claim? Chunking-reduces-working-memory-load is about chunking; maybe link [Chunking](../principles/chunking.md) principle instead. Or cognitive-load-theory theory page.
- Expertise reversal: extra representations/guidance hurt experts [~M] — link expertise-reversal-effect claim and theory.
- Learners rarely connect representations spontaneously; without translation support they process each in isolation and gains vanish [~S] (Rau 2017).
- Unfamiliar notation adds extraneous load for novices (symbolic forms before interpretation skill) [-M].
- Dynamic/animated not automatically better — can overload [~M]. Maybe skip or include.

Implementation Variability:
- Simultaneous (side-by-side, linked) vs sequential presentation
- Concrete→abstract sequencing (CRA; Goldstone & Son — concrete first then idealized supports transfer [~M])
- Learner-generated vs instructor-provided representations
- Static vs dynamic/interactive (Desmos, PhET)

Target Learners:
- Novices in a domain with multiple conventional notations (math, science) [+M]
- Low prior knowledge learners benefit from complementary + constraining functions
- Less benefit / harm for high-knowledge learners [expertise-reversal claim ~M]
- Students with learning disabilities: CRA sequence [+M] — hmm, need a source. Could cite Bouck et al.? I'm not confident of a specific DOI. I can mention CRA without a claim link, or cite in Key Sources. Bouck, Satsangi & Park (2018) "The Concrete–Representational–Abstract approach for students with learning disabilities" *Remedial and Special Education* — I believe this exists but DOI uncertain. I could omit DOI. Rule: omit DOI if uncertain. I'll include it as a 5th source without DOI? I already have 5. Keep 5 max. Maybe swap Paivio for Bouck? Paivio is seminal for dual coding and links to the theory page. Keep Paivio, mention CRA in prose without citation, or cite Bouck without DOI. I'll keep 5: Ainsworth 2006, Mayer 2009, Rau 2017, Goldstone & Son 2005, Paivio 1986. CRA mentioned in prose.

Target Learning Goals:
- Conceptual understanding and abstraction (multiple-contrasting-cases claim +S)
- Representational fluency / translation as a goal in itself
- Transfer (Goldstone & Son)
- Flexible problem solving

Instructions:
1. Select 2–3 representations that each carry unique information; drop any that merely duplicate ([Cognitive Load Management](../elements/cognitive-load-management.md))
2. Sequence from concrete/verbal toward symbolic as interpretation skill develops ([Analogies](../elements/analogies.md), advance-organizers)
3. Present contiguously with explicit mapping cues (color-coding, labels linking elements)
4. Prompt translation: ask learners to explain how elements of one form map to another ([Articulation](../elements/articulation.md)) [self-explanation claim +S]
5. Assess translation directly ([Assessment](../elements/assessment.md), [Application](../elements/application.md))

Related Strategies: same-folder only. Available: act_it_out (enacting/embodied representation), activating-prior-knowledge? Hmm. "act_it_out" — acting out a concept is a bodily representation; plausible. Also "analogies_and_prior_knowledge_activation"? Not in list. Elements analogies exists. For Related Strategies I'll use:
- [Act It Out](act_it_out.md) — embodied/kinesthetic representation as a fourth form
- [Activating Prior Knowledge](activating-prior-knowledge.md) — representations anchor to existing schemas
Hmm, is that too weak? Maybe also "3-source_rule"? No. "acronyms_and_acrostics"? verbal mnemonic representations — weak. Keep two, with one-line explanations (rule 8 applies to Related items).

Actually the exemplar's Related Elements has one-line explanations. I'll do the same.

Examples:
- Desmos — equation, graph, table linked dynamically.
- PhET Interactive Simulations — multiple synchronized views.
- CPM Educational Program — "y = mx + b" connections? CPM uses situations, tables, graphs, equations, rules.
- NCTM Illuminations? Maybe skip; 3 examples enough. Exemplar has 4. Add Concrete–Representational–Abstract (CRA) intervention as a published instructional routine.

Key Sources list as planned.

Now write prose with inline tags. Watch direction rule in Constraints.

Links check — every link slug must be in my verified list:
- ../claims/multiple-contrasting-cases-support-abstraction.md ✓
- ../claims/media-combinations-affect-recall-and-retention.md ✓
- ../claims/self-explanation-improves-conceptual-understanding.md ✓
- ../claims/expertise-reversal-effect.md ✓
- ../claims/chunking-reduces-working-memory-load.md ✓
- ../theories/dual-coding-theory.md ✓
- ../theories/cognitive-load-theory.md ✓
- ../theories/expertise-reversal-effect.md ✓
- ../elements/cognitive-load-management.md ✓
- ../elements/analogies.md ✓
- ../elements/articulation.md ✓
- ../elements/assessment.md ✓
- ../elements/application.md ✓
- ../elements/advance-organizers.md ✓
- ../elements/act.md ✓ (element "act" — Act It Out? risky display; I'll link strategy act_it_out instead)
- ../principles/cognitive-load-management.md ✓, ../principles/chunking.md ✓, ../principles/cognitive-load-theory.md ✓, ../principles/analogical-reasoning.md ✓, ../principles/cognitive-activation.md ✓, ../principles/active-learning.md ✓
- ../patterns/cognitive-flexibility-theory.md ✓, ../patterns/4cid-four-component-instructional-design.md ✓, ../patterns/cgi-for-math.md ✓, ../patterns/elaboration-theory.md ✓, ../patterns/gagnés-9-events-of-instruction.md ✓
- strategies same
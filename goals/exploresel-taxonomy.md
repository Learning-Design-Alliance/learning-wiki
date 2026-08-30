---
type: goal-map
title: "ExploreSEL — EASEL Lab Taxonomy Project (Six Domains, 23 Sub-Domains)"
description: The full six-domain, 23-sub-domain SEL skill taxonomy that Harvard's EASEL Lab built to compare ~40 SEL frameworks, normalized into this wiki's goal-map schema.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-30
source:
  framework: "EASEL Lab Taxonomy Project (ExploreSEL)"
  kind: standard
  version: "2017 taxonomy (Jones, Bailey, Brush, Kahn et al.)"
  source_url: https://easel.gse.harvard.edu/taxonomy-project
  license: "Confirm EASEL Lab / Wallace Foundation terms before real ingest"
nodes:
  - id: sel-cognitive-regulation
    display_id: "1"
    label: Cognitive Regulation
    description: Basic cognitive skills required to direct behavior toward goal attainment — concentration, focus, memory, task prioritization, impulse control, goal-setting, and decision-making.
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-cog-attention-control
    display_id: "1.1"
    label: Attention Control
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-cog-inhibitory-control
    display_id: "1.2"
    label: Inhibitory Control
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-cog-working-memory-planning
    display_id: "1.3"
    label: Working Memory & Planning
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-cog-cognitive-flexibility
    display_id: "1.4"
    label: Cognitive Flexibility
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-cog-critical-thinking
    display_id: "1.5"
    label: Critical Thinking
    competency_framework: "ExploreSEL/EASEL Taxonomy"

  - id: sel-emotion
    display_id: "2"
    label: Emotion
    description: Skills that help you recognize, express, and control your own emotions, and understand and empathize with the emotions of others.
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-emo-knowledge-expression
    display_id: "2.1"
    label: Emotion Knowledge & Expression
    student_facing_label: Notice and name how I'm feeling
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-emo-regulation
    display_id: "2.2"
    label: Emotion & Behavior Regulation
    competency_framework: "ExploreSEL/EASEL Taxonomy"
    assessment_suggestion: Behavioral observation checklist during a structured peer-conflict scenario.
  - id: sel-emo-empathy-perspective-taking
    display_id: "2.3"
    label: Empathy / Perspective-Taking
    competency_framework: "ExploreSEL/EASEL Taxonomy"

  - id: sel-social
    display_id: "3"
    label: Social (Interpersonal Skills)
    description: Skills for navigating social situations and relationships with peers and adults.
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-soc-understanding-social-cues
    display_id: "3.1"
    label: Understanding Social Cues
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-soc-conflict-resolution
    display_id: "3.2"
    label: Conflict / Social Problem-Solving
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-soc-prosocial-behavior
    display_id: "3.3"
    label: Prosocial / Cooperative Behavior
    competency_framework: "ExploreSEL/EASEL Taxonomy"

  - id: sel-values
    display_id: "4"
    label: Values
    description: Beliefs about what is important and how one should behave, spanning ethical, performance, intellectual, and civic domains.
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-val-ethical
    display_id: "4.1"
    label: Ethical Values
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-val-performance
    display_id: "4.2"
    label: Performance Values
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-val-intellectual
    display_id: "4.3"
    label: Intellectual Values
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-val-civic
    display_id: "4.4"
    label: Civic Values
    competency_framework: "ExploreSEL/EASEL Taxonomy"

  - id: sel-perspectives
    display_id: "5"
    label: Perspectives
    description: General outlooks or dispositions toward life and experience.
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-per-optimism
    display_id: "5.1"
    label: Optimism
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-per-gratitude
    display_id: "5.2"
    label: Gratitude
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-per-openness
    display_id: "5.3"
    label: Openness
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-per-zest
    display_id: "5.4"
    label: Enthusiasm / Zest
    competency_framework: "ExploreSEL/EASEL Taxonomy"

  - id: sel-identity
    display_id: "6"
    label: Identity / Self-Image
    description: How you understand and perceive yourself and your abilities — your knowledge and beliefs about yourself and your capacity to learn and grow.
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-id-self-knowledge
    display_id: "6.1"
    label: Self-Knowledge
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-id-purpose
    display_id: "6.2"
    label: Purpose
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-id-self-efficacy-growth-mindset
    display_id: "6.3"
    label: Self-Efficacy & Growth Mindset
    competency_framework: "ExploreSEL/EASEL Taxonomy"
  - id: sel-id-self-esteem
    display_id: "6.4"
    label: Self-Esteem
    competency_framework: "ExploreSEL/EASEL Taxonomy"

relationships:
  - { source: sel-cognitive-regulation, target: sel-cog-attention-control, type: default }
  - { source: sel-cognitive-regulation, target: sel-cog-inhibitory-control, type: default }
  - { source: sel-cognitive-regulation, target: sel-cog-working-memory-planning, type: default }
  - { source: sel-cognitive-regulation, target: sel-cog-cognitive-flexibility, type: default }
  - { source: sel-cognitive-regulation, target: sel-cog-critical-thinking, type: default }
  - { source: sel-emotion, target: sel-emo-knowledge-expression, type: default }
  - { source: sel-emotion, target: sel-emo-regulation, type: default }
  - { source: sel-emotion, target: sel-emo-empathy-perspective-taking, type: default }
  - { source: sel-social, target: sel-soc-understanding-social-cues, type: default }
  - { source: sel-social, target: sel-soc-conflict-resolution, type: default }
  - { source: sel-social, target: sel-soc-prosocial-behavior, type: default }
  - { source: sel-values, target: sel-val-ethical, type: default }
  - { source: sel-values, target: sel-val-performance, type: default }
  - { source: sel-values, target: sel-val-intellectual, type: default }
  - { source: sel-values, target: sel-val-civic, type: default }
  - { source: sel-perspectives, target: sel-per-optimism, type: default }
  - { source: sel-perspectives, target: sel-per-gratitude, type: default }
  - { source: sel-perspectives, target: sel-per-openness, type: default }
  - { source: sel-perspectives, target: sel-per-zest, type: default }
  - { source: sel-identity, target: sel-id-self-knowledge, type: default }
  - { source: sel-identity, target: sel-id-purpose, type: default }
  - { source: sel-identity, target: sel-id-self-efficacy-growth-mindset, type: default }
  - { source: sel-identity, target: sel-id-self-esteem, type: default }
  - { source: sel-emo-knowledge-expression, target: sel-emo-regulation, type: prerequisite }
---

# ExploreSEL — EASEL Lab Taxonomy Project (Six Domains, 23 Sub-Domains)

> **Provenance note.** This wiki's outbound network access currently blocks `exploresel.gse.harvard.edu`, `easel.gse.harvard.edu`, and the Wallace Foundation PDF mirrors directly, so this page was built from cross-validated web-search snippets rather than the primary source document (Jones, Bailey, Brush, Kahn et al., *Navigating Social and Emotional Learning from the Inside Out*, Harvard EASEL Lab / Wallace Foundation, 2017) — not fabricated, but also not yet checked against the original PDF line-by-line. The six domain names, all 23 sub-domain names, and the "23 subcategories" total are corroborated across two independent searches. Treat `status: draft` here as "verify domain/sub-domain wording and any missing benchmark-level detail against the primary PDF" rather than "invented."
>
> This replaces an earlier, differently-named draft (`exploresel-core-competencies.md`) that had mistakenly modeled this page on CASEL's 5-domain framework instead of ExploreSEL's own 6-domain Taxonomy Project structure — those are related but distinct: CASEL is one of the ~40 frameworks ExploreSEL's taxonomy is used to *compare against*, not the taxonomy itself.

## Description
The EASEL Lab's Taxonomy Project is the framework behind the ExploreSEL site: six top-level domains (Cognitive Regulation, Emotion, Social, Values, Perspectives, Identity/Self-Image), each broken into sub-domains — 23 in total — that the lab then uses as a common coding scheme to compare roughly 40 published SEL frameworks and programs (CASEL's own framework among them) side by side. Nearly all edges here are `default` (hierarchical domain → sub-domain); the one `prerequisite` edge (Emotion Knowledge & Expression → Emotion & Behavior Regulation) reflects that naming an emotion is a developmental precursor to regulating it, not just a sibling sub-skill.

## What's not in this page yet
ExploreSEL's own site content — the ~40 individual frameworks it maps onto this taxonomy (CASEL, PATHS, RULER, Second Step, etc.) — is a separate, larger ingest: each of those would need its own goal-map page (or a `related_frameworks` cross-reference into this one), and pulling their actual node-level content requires either direct access to `exploresel.gse.harvard.edu`'s comparison tool (currently blocked here) or source PDFs/CSVs supplied directly.

## Related Wiki Pages
- [Cognitive Flexibility](../principles/cognitive-flexibility.md) — direct match to sub-domain 1.4.
- [Goal Setting](../elements/goal-setting.md) and [Gain Attention](../elements/gain-attention.md) relate to Working Memory & Planning (1.3) and Attention Control (1.1).
- [Self-Regulation](../principles/self-regulation.md) / [Self-Regulated Learning](../theories/self-regulated-learning.md) relate to Emotion & Behavior Regulation (2.2) and Inhibitory Control (1.2).
- [Building Empathy](../principles/building-empathy.md) relates to Empathy/Perspective-Taking (2.3).
- [Foster Growth Mindset](../principles/foster-growth-mindset.md) is a direct match to Self-Efficacy & Growth Mindset (6.3).
- [Character Education](../principles/character-education.md) spans several Values (4.x) sub-domains.

## Key Sources
- Jones, S. M., Bailey, R., Brush, K., Kahn, J., et al. (2017). *Navigating Social and Emotional Learning from the Inside Out.* Harvard Graduate School of Education / Wallace Foundation.
- EASEL Lab. *Taxonomy Project.* https://easel.gse.harvard.edu/taxonomy-project
- Explore SEL. https://exploresel.gse.harvard.edu/

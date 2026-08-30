---
type: goal-map
title: "ExploreSEL — Core Social-Emotional Competencies (CASEL-Aligned)"
description: Flattened goal map of ExploreSEL's core SEL competency domains and sub-skills.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-30
source:
  framework: "ExploreSEL (CASEL-aligned)"
  kind: standard
  version: illustrative
  source_url: https://exploresel.gse.harvard.edu/
  license: "Confirm ExploreSEL's terms before real ingest"
nodes:
  - id: sel-self-awareness
    display_id: "1"
    label: Self-Awareness
    description: Recognize one's own emotions, thoughts, and values and how they influence behavior.
    competency_framework: "ExploreSEL/CASEL"
  - id: sel-identify-emotions
    display_id: "1.1"
    label: Identify and name one's own emotions accurately
    student_facing_label: Notice and name how I'm feeling
    competency_framework: "ExploreSEL/CASEL"
  - id: sel-self-management
    display_id: "2"
    label: Self-Management
    description: Regulate emotions, thoughts, and behaviors across situations and to achieve goals.
    competency_framework: "ExploreSEL/CASEL"
  - id: sel-regulate-emotions
    display_id: "2.1"
    label: Regulate emotions and impulses in response to stress or conflict
    competency_framework: "ExploreSEL/CASEL"
    assessment_suggestion: Behavioral observation checklist during a structured peer-conflict scenario.
  - id: sel-set-goals
    display_id: "2.2"
    label: Set and work toward personal and academic goals
    competency_framework: "ExploreSEL/CASEL"
  - id: sel-social-awareness
    display_id: "3"
    label: Social Awareness
    description: Take the perspective of and empathize with others, including those from diverse backgrounds.
    competency_framework: "ExploreSEL/CASEL"
  - id: sel-perspective-taking
    display_id: "3.1"
    label: Take the perspective of others from diverse backgrounds
    competency_framework: "ExploreSEL/CASEL"
  - id: sel-relationship-skills
    display_id: "4"
    label: Relationship Skills
    description: Establish and maintain healthy, supportive relationships; communicate and cooperate effectively.
    competency_framework: "ExploreSEL/CASEL"
  - id: sel-responsible-decision-making
    display_id: "5"
    label: Responsible Decision-Making
    description: Make caring, constructive choices about personal behavior in varied situations.
    competency_framework: "ExploreSEL/CASEL"
relationships:
  - source: sel-self-awareness
    target: sel-identify-emotions
    type: default
  - source: sel-self-management
    target: sel-regulate-emotions
    type: default
  - source: sel-self-management
    target: sel-set-goals
    type: default
  - source: sel-social-awareness
    target: sel-perspective-taking
    type: default
  - source: sel-identify-emotions
    target: sel-regulate-emotions
    type: prerequisite
---

# ExploreSEL — Core Social-Emotional Competencies (CASEL-Aligned)

> **Illustrative placeholder.** The five top-level domains follow CASEL's well-established framework, but the specific sub-skill wording, `display_id` numbering, and omission of the full Relationship Skills / Responsible Decision-Making sub-trees are illustrative — a real ingest should pull ExploreSEL's actual published sub-competency list rather than this abbreviated set.

## Description
ExploreSEL's five core competency domains, each with one or two illustrative sub-skills, normalized into this wiki's flat goal-map schema. Unlike the ESCO example, most edges here are `default` (hierarchical domain → sub-skill) rather than `prerequisite`, since CASEL's framework describes co-occurring competency domains rather than a strict skill-acquisition order — though a genuine dependency does exist between naming an emotion and regulating it, captured as the one `prerequisite` edge.

## Related Wiki Pages
- [Self-Regulation](../principles/self-regulation.md) and [Self-Regulated Learning](../theories/self-regulated-learning.md) directly inform the Self-Management domain's sub-skills.
- [Building Empathy](../principles/building-empathy.md) directly informs the Social Awareness domain.
- [Character Education](../principles/character-education.md) overlaps with Responsible Decision-Making and is worth cross-linking once that sub-tree is fleshed out.

## Key Sources
- CASEL. *CASEL's SEL Framework*. https://casel.org/fundamentals-of-sel/
- ExploreSEL. https://exploresel.gse.harvard.edu/

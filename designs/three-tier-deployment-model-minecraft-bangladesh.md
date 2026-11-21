---
type: design
id: three-tier-deployment-model-minecraft-bangladesh
title: Three-tier deployment model matching school infrastructure variability (cloud, LAN, fully offline)
description: "The framework's Infrastructure Layer adopts a three-tier deployment model aligned with actual variability across Bangladeshi schools."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: mohd-ruhul-ameen-2025
    resource: "https://arxiv.org/abs/2510.18385"
    title: "Mohd Ruhul Ameen, Akif Islam, Momen Khandokar Ope. (2025). Khelte Khelte Shikhi: A Proposed HCI Framework for Gamified Interactive Learning with Minecraft in Bangladeshi Education Systems. https://arxiv.org/abs/2510.18385"
    author: Mohd Ruhul Ameen, Akif Islam, Momen Khandokar Ope
---

# Three-tier deployment model matching school infrastructure variability (cloud, LAN, fully offline)

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The framework's Infrastructure Layer adopts a three-tier deployment model aligned with actual variability across Bangladeshi schools. "Tier 1 supports the 15% of urban schools with stable electricity and broadband, enabling cloud-hosted multiplayer"; Tier 2 targets semi-urban schools (~30%) with "local WiFi multiplayer, intermittent cloud syncing, and optional solar backup"; Tier 3 serves rural schools (~55%) "through fully offline operation on low-spec or refurbished devices, turn-based shared gameplay, and USB/SD-based content distribution."

## Design Implications

### Context
#### Requirements
- Content and assessments preloaded on local storage for Tier 3; reduced visual settings so Minecraft runs on low-spec or refurbished devices
#### Constraints
- Tier percentages are stated estimates of school infrastructure distribution; turn-based shared gameplay substitutes for simultaneous multiplayer in offline settings

### Target Learners
- Students across urban, semi-urban, and rural Bangladeshi schools, including those without internet or reliable electricity

### Learning Goals
- Equitable access to game-based learning regardless of connectivity or hardware constraints

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Mohd Ruhul Ameen, Akif Islam, Momen Khandokar Ope. (2025). Khelte Khelte Shikhi: A Proposed HCI Framework for Gamified Interactive Learning with Minecraft in Bangladeshi Education Systems. https://arxiv.org/abs/2510.18385

---
type: design
id: elevate-avatar-asset-production-pipeline
title: Five-stage game-ready asset production pipeline for a pedagogically controlled 3D Virtual Teacher avatar
description: "The prototype's Virtual Teacher avatar was manually authored rather than sourced from a pre-packaged library, to give pedagogical control over appearance and expressive affordances."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: lorenzo-stacchio-2026
    resource: "https://arxiv.org/abs/2606.30662"
    title: "Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662"
    author: Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni
---

# Five-stage game-ready asset production pipeline for a pedagogically controlled 3D Virtual Teacher avatar

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The prototype's Virtual Teacher avatar was manually authored rather than sourced from a pre-packaged library, to give pedagogical control over appearance and expressive affordances. The pipeline runs through Character Creator, ZBrush sculpt refinement, Substance Painter material authoring, Mixamo auto-rigging and animation, and OBJ export. The authors treat the avatar as part of the interaction channel, in which "facial expressions, turn-taking cues, and lip synchronization are treated as communicative signals that shape how students interpret the tutor's epistemic stance and instructional intent".

## Design Implications

### Context
#### Requirements
- Face mesh must support clear lip articulation to avoid degrading comprehension during voice-based tutoring
- Polygon count, texture sizes, and shader complexity must keep the asset computationally tractable on consumer hardware for stable frame rates under concurrency
#### Constraints
- Texture resolution was balanced to preserve facial readability while limiting VRAM and bandwidth overhead for mobile and consumer devices

### Target Learners
- school students interacting with the avatar on smartphones and PCs

### Learning Goals
- legible embodied communication of tutor state and instructional intent

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662

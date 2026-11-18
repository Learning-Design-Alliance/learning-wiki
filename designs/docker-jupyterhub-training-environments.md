---
type: design
id: docker-jupyterhub-training-environments
title: Docker containers and JupyterHub to eliminate the software installation step in training
description: "To address the \"tremendous loss of time in software installation\" when students have not prepared their machines, the paper proposes containers: \"Here containers may bring real progress, provided that everyone has at..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
sources:
  - id: dario-berzano-2018
    resource: "https://arxiv.org/abs/1807.02875"
    title: "Dario Berzano, Riccardo Maria Bianchi, Peter Elmer, Sergei V. Gleyzer, John Harvey, Roger Jones, Michel Jouvin, Daniel S. Katz, Sudhir Malik, Dario Menasce, Mark Neubauer, Fernanda Psihas, Albert Puig Navarro, Graeme A. Stewart, Christopher Tunnell, Justin A. Vasel, and Sean-Jiun Wang. (2018). HEP Software Foundation Community White Paper Working Group – Training, Staffing and Careers. https://arxiv.org/abs/1807.02875"
    author: Dario Berzano, Riccardo Maria Bianchi, Peter Elmer, Sergei V. Gleyzer, John Harvey, Roger Jones, Michel Jouvin, Daniel S. Katz, Sudhir Malik, Dario Menasce, Mark Neubauer, Fernanda Psihas, Albert Puig Navarro, Graeme A. Stewart, Christopher Tunnell, Justin A. Vasel, and Sean-Jiun Wang
---

# Docker containers and JupyterHub to eliminate the software installation step in training

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
To address the "tremendous loss of time in software installation" when students have not prepared their machines, the paper proposes containers: "Here containers may bring real progress, provided that everyone has at least Docker[ 6] installed on their machine." JupyterHub is cited as a technology supporting training sessions without specialist installations. The IN2P3 Gitlab tutorials use Docker images to avoid the installation step that often absorbs half of a training session.

## Design Implications

### Context
#### Requirements
- Participants must have Docker installed, or use a hosted service such as JupyterHub
#### Constraints
- The benefit is conditional on everyone having Docker installed on their machine

### Target Learners
- Training session participants in HEP computing workshops

### Learning Goals
- Hands-on exercises with pre-configured software environments

### Claims
- 

## Related Designs

- [Docker container technology and a shared course image for an identical, no-install course computing environment with UNIX CLI training](docker-course-image-identical-environment.md)

## Examples
-

## Key Sources
- Dario Berzano, Riccardo Maria Bianchi, Peter Elmer, Sergei V. Gleyzer, John Harvey, Roger Jones, Michel Jouvin, Daniel S. Katz, Sudhir Malik, Dario Menasce, Mark Neubauer, Fernanda Psihas, Albert Puig Navarro, Graeme A. Stewart, Christopher Tunnell, Justin A. Vasel, and Sean-Jiun Wang. (2018). HEP Software Foundation Community White Paper Working Group – Training, Staffing and Careers. https://arxiv.org/abs/1807.02875

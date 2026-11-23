---
type: strategy
id: three-free-deployment-routes-notebooks
title: Offer three free deployment routes (mybinder.org, dokku, institutional JupyterHub) matched to user needs
description: Because most users will not install Python and dependencies locally, OSSCAR identifies and suggests three free deployment solutions depending on teacher and student needs.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: dou-du-2022
    resource: "https://arxiv.org/abs/2203.12019"
    title: "Dou Du, Taylor J. Baird, Sara Bonella, Giovanni Pizzi. (2022). OSSCAR, an open platform for collaborative development of computational tools for education in science. arXiv. https://arxiv.org/abs/2203.12019"
    author: Dou Du, Taylor J. Baird, Sara Bonella, Giovanni Pizzi
---

# Offer three free deployment routes (mybinder.org, dokku, institutional JupyterHub) matched to user needs

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because most users will not install Python and dependencies locally, OSSCAR identifies and suggests three free deployment solutions depending on teacher and student needs. mybinder.org requires almost zero maintenance but has slow startup (from a few tens of seconds to some minutes); dokku deployment reduces startup "typically to 5 seconds or less" but requires server expertise; institutional JupyterHub servers give students persistent home folders where they can modify code. The article concludes no single solution covers all requirements.

## Design Implications

### Context
#### Requirements
- Easy access to the applications with just a web link is essential; dokku deployment requires expertise in managing and deploying web servers and an online server
#### Constraints
- mybinder.org offers very limited computing power, an issue for sophisticated notebooks; dokku requires special care to avoid unexpected interactions between users sharing one container

### Target Learners
- teachers distributing notebooks to students
- students accessing applications via browser

### Target Learning Goals
- frictionless access to interactive course content without local software installation

## Related Strategies

- [Provide open access to notebook source code to enable feedback, adaptation and peer instruction](open-source-code-access-peer-instruction.md)
- [Local deployment via PyPI installation or flash-drive distribution for regions with limited internet](local-deployment-flash-drive-pypi-distribution.md)
- [Combine custom JupyterLab extensions on an institutional JupyterHub to give students a bespoke, ready-to-use computing environment](institutional-jupyterhub-custom-extensions-strategy.md)

## Examples
-

## Key Sources
- Dou Du, Taylor J. Baird, Sara Bonella, Giovanni Pizzi. (2022). OSSCAR, an open platform for collaborative development of computational tools for education in science. arXiv. https://arxiv.org/abs/2203.12019

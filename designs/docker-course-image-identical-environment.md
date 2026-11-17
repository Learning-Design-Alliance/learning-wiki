---
type: design
id: docker-course-image-identical-environment
title: Docker container technology and a shared course image for an identical, no-install course computing environment with UNIX CLI training
description: "The course used Docker container technology so that students on their own machines could work in a uniform environment: the authors \"chose to use the Docker container technology, because our course would start with an..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: robert-j-brunner-and-edward-j-kim-2016
    resource: "https://arxiv.org/abs/1604.07397"
    title: "Robert J. Brunner and Edward J. Kim. (2016). Teaching Data Science. arXiv preprint. https://arxiv.org/abs/1604.07397"
    author: Robert J. Brunner and Edward J. Kim
---

# Docker container technology and a shared course image for an identical, no-install course computing environment with UNIX CLI training

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The course used Docker container technology so that students on their own machines could work in a uniform environment: the authors "chose to use the Docker container technology, because our course would start with an introduction to UNIX and the Command Line Interface (CLI)," built and provided "a Docker course image that contained all software and libraries needed for the course," and required reading on virtualization and basic Docker usage. Later, containers of the course image were run on Google Compute Engine to provide web-accessible Jupyter notebook servers in the cloud.

## Design Implications

### Context
#### Requirements
- Students install Docker following provided documentation before the semester starts
- The instructional team builds and maintains a course Docker image containing all software and libraries
#### Constraints
- Running Docker on Mac OSX or Windows requires another layer of virtualization; Windows tools (Boot2docker, Docker Machine) "are not yet mature, and Windows users faced various problems during installation and at runtime"

### Target Learners
- Online students using their own machines, with no programming experience assumed

### Learning Goals
- UNIX command-line skills; software acquisition and environment setup; cloud and container computing

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Robert J. Brunner and Edward J. Kim. (2016). Teaching Data Science. arXiv preprint. https://arxiv.org/abs/1604.07397

---
type: design
id: fabric-prototype-four-educational-smart-contracts
title: Hyperledger Fabric prototype with four educational smart contracts
description: A working prototype built on Hyperledger Fabric with 4 peer nodes belonging to four different institutions.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: fuan-xiao-2026
    resource: "https://doi.org/10.1186/s41239-026-00618-5"
    title: "Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5"
    author: Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li
---

# Hyperledger Fabric prototype with four educational smart contracts

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A working prototype built on Hyperledger Fabric with 4 peer nodes belonging to four different institutions. It implements four core smart contracts—EnrollmentContract, AssessmentContract, CertificationContract, and IdentityContract—covering "course registration, automatic grading, certificate issuance, and decentralized identity management". The on-chain data model includes StudentProfile, EnrollmentRecord, GradeRecord (preserving all regrade history), and Certificate records; large content such as feedback text is stored off-chain with hashes on-chain.

## Design Implications

### Context
#### Requirements
- Instructor identity must hold restricted grading permissions for grade records to be accepted by the contract
#### Constraints
- The prototype does not include a fully functional user interface; interactions are scripted to represent multiple users and actions
- Grading used simple keyword matching against an expected answer rather than a full AI grader

### Target Learners
- online higher-education students

### Learning Goals
- enrollment, assessment, and credential workflows with verifiable records

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5

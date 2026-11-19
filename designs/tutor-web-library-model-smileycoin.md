---
type: design
id: tutor-web-library-model-smileycoin
title: Tutor-web library model with SmileyCoin tablet-purchase rewards
description: "An implementation of the tutor-web drilling system in Kenyan community libraries: tablets are donated to libraries rather than to individual students, pre-registered accounts are assigned by librarians, and students e..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: g-stefansson-2022
    resource: "https://libraries.tutor-web.net/"
    title: "G. Stefansson, J. Lentin, A. H. Jonsdottir, E. Eiríksson, A. Kristjánsson. (2022). Mathematics and Incentives in the Slums. https://libraries.tutor-web.net/"
    author: G. Stefansson, J. Lentin, A. H. Jonsdottir, E. Eiríksson, A. Kristjánsson
---

# Tutor-web library model with SmileyCoin tablet-purchase rewards

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
An implementation of the tutor-web drilling system in Kenyan community libraries: tablets are donated to libraries rather than to individual students, pre-registered accounts are assigned by librarians, and students earn SmileyCoin (SMLY) by acing KCSE drillsets. "Acing the KCSE drill set gives a predefined reward of 1 M SMLY," and each tablet carries a QR-code payment address allowing purchase with 1M SMLY, after which the Smiley Charity replenishes the stock. Rewards depend on persistent studying rather than prior knowledge.

## Design Implications

### Context
#### Requirements
- Libraries with local WiFi and Internet access so the blockchain and SmileyCoin rewards are usable
- Pre-registered student accounts assigned by the librarian
- Reward tuning within the finite SMLY and fiat budgets of the SmileyCoin Fund and Smiley Charity
#### Constraints
- The SmileyCoin Fund grant is limited to some 1.5 bn SMLY per year and tablet shipments to 10-15 per week
- Each library initially receives only 5-15 tablets
- Abuse by non-student users must be monitored

### Target Learners
- secondary school students in slums and low-income regions of Kenya

### Learning Goals
- secondary school mathematics and passing the KCSE national exam, toward university entry

### Claims
- [Kenya Library Model Participation 1301 Students](../claims/kenya-library-model-participation-1301-students.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- G. Stefansson, J. Lentin, A. H. Jonsdottir, E. Eiríksson, A. Kristjánsson. (2022). Mathematics and Incentives in the Slums. https://libraries.tutor-web.net/

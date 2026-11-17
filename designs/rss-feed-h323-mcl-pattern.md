---
type: design
id: rss-feed-h323-mcl-pattern
title: Mobile collaborative learning supported through RSS-feed content sharing plus real-time H.323 communication
description: "The article's MCL architecture combines asynchronous and synchronous collaboration."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: khaled-elleithy-2012
    resource: "https://scholar.google.com/scholar?q=Fostering+of+innovative+usability+testing+to+develop+mobile+application+for+mobile+collaborative+learning"
    title: "Khaled Elleithy, Abdul Razaque. (2012). Fostering of innovative usability testing to develop mobile application for mobile collaborative learning (MCL). ICGST-AIML Journal, Volume 12, Issue 1, July 2012. https://scholar.google.com/scholar?q=Fostering+of+innovative+usability+testing+to+develop+mobile+application+for+mobile+collaborative+learning"
    author: Khaled Elleithy, Abdul Razaque
---

# Mobile collaborative learning supported through RSS-feed content sharing plus real-time H.323 communication

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article's MCL architecture combines asynchronous and synchronous collaboration. Participants store files, audio and video in a store component, upload them to RSS feeds, and notify their collaborative group by multicasting message; members then download the required information from the requesting user's RSS feed and begin collaboration. Synchronous discussion is supported "by using H.323 at the server side to facilitate the real-time audio and video communication", whose point-to-multipoint provision lets all members participate simultaneously while maintaining quality of service.

## Design Implications

### Context
#### Requirements
- A server with H.323 support
- RSS feeds for each user to put and get contents
- Multicasting messaging to notify group members
#### Constraints
- The article notes handheld device limitations such as small screen size, low resolution, limited memory and bandwidth can hinder effective MCL

### Target Learners
- students in collaborative groups
- teachers
- administrators

### Learning Goals
- sharing and updating course contents
- group discussion of multimedia materials
- collaborative learning anytime and anywhere

### Claims
- Group Application Android Mcl [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Khaled Elleithy, Abdul Razaque. (2012). Fostering of innovative usability testing to develop mobile application for mobile collaborative learning (MCL). ICGST-AIML Journal, Volume 12, Issue 1, July 2012. https://scholar.google.com/scholar?q=Fostering+of+innovative+usability+testing+to+develop+mobile+application+for+mobile+collaborative+learning

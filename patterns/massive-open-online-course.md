---
type: pattern
title: Massive Open Online Course (MOOC)
description: A course-grain pattern combining open enrollment, video-based instruction, and light-touch automated or peer assessment at scale — whose original connectivist, networked-learning design was largely abandoned once commercial "xMOOC" platforms adopted a broadcast, video-lecture-plus-quiz model instead.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
---

# Massive Open Online Course (MOOC)

## Description
The MOOC combines several earlier innovations — open enrollment, video-based instruction, discussion-forum interaction, and open-content licensing — into a single, free, large-scale online course (Weller, 2018). The earliest MOOCs (Downes and Siemens's open courses in 2008–2009) were built around [Connectivism](../theories/connectivism.md): learning was meant to happen through learners forming and navigating their own network of connections across distributed content and peers, not through a fixed instructor-delivered sequence.

That original design was largely abandoned once the pattern scaled commercially. After Stanford's 2011 course (Sebastian Thrun) drew over 100,000 learners and attracted venture-capital investment, "xMOOC" platforms (Coursera, Udacity, edX) adopted a broadcast, video-lecture-plus-quiz model — closer to a traditional course delivered at scale than to the connectivist, learner-networked design the format is named for. Weller (2018) notes this is a recurring edtech pattern: the pedagogical model a technology is originally named for and the model it is actually implemented with can diverge sharply once it scales for a commercial audience. Wiley (2014) makes a sharper version of the same critique from a licensing angle: because xMOOC content is typically not openly licensed (no free copying, translation, or redistribution), imposes registration deadlines and start/end dates, and charges for credentials, it fails the [Open Educational Resources (5Rs)](../elements/open-educational-resources.md) test for genuine openness — in his words, once you strip away the "open entry" framing, a typical xMOOC is "nothing more than" a traditional online class.

## Implications

### Context
#### Requirements
- Infrastructure capable of serving very large, unbounded enrollment with minimal marginal cost per additional learner — which pushes toward pre-recorded video and automated or peer assessment rather than instructor-graded feedback
- A content licensing decision (open vs. closed) that determines whether the course is "open" only in the open-entry sense or also in the 5R licensing sense
#### Constraints
- At scale, individualized instructor feedback becomes impractical, so assessment shifts to automated quizzes or peer grading — a real reduction in feedback quality and immediacy relative to smaller-enrollment courses
- The connectivist pedagogy the pattern was originally built around does not survive contact with a broadcast, video-lecture delivery model — a "MOOC" today is more reliably described by its scale and open enrollment than by any specific pedagogy
- Completion rates for MOOCs are notoriously low relative to traditional courses, a direct consequence of minimal enrollment commitment and light-touch support structures
#### Grain Size
- Course

### Target Goals
- Reaching very large, geographically dispersed audiences with a single course offering
- Reducing per-learner marginal cost for widely-demanded introductory content

### Target Learners
- Self-directed learners able to persist through a course with minimal individualized instructor support or accountability structure
- Learners for whom free, open enrollment (regardless of prior credentials) is the primary access barrier being removed

### Theory
#### Supporting
- [Connectivism](../theories/connectivism.md) [~M] — the pattern's original design rationale, though largely abandoned in mainstream commercial implementations
#### Contradicting / Qualifying
- [Open Educational Resources (5Rs)](../elements/open-educational-resources.md) — most commercial xMOOC content fails the 5R openness test (no free copying, translation, or redistribution), which Wiley (2014) argues undermines the "open" framing of the pattern's own name

## Design

### Sequence
1. Produce pre-recorded video lectures and other content, since live, individualized delivery does not scale to the intended enrollment.
2. Open enrollment broadly, with minimal or no prerequisite screening.
3. Deliver content asynchronously, typically week-by-week, with embedded low-stakes quizzes.
4. Support peer interaction through discussion forums (with variable, self-organized engagement).
5. Assess primarily through automated quizzes or peer/rubric-based grading rather than instructor feedback.
6. Optionally charge a fee for a verified certificate or credential, separate from free access to the content itself.

### Elements Used
- [Open Educational Resources (5Rs)](../elements/open-educational-resources.md) (when the content is genuinely openly licensed)

### Affordances
- [Online Course Design (Community of Inquiry)](online-course-design.md) — the same interaction-design concerns (learner-learner, learner-instructor, learner-content) apply at MOOC scale, though instructor interaction is necessarily far thinner

### Personalization
- Some platforms allow self-paced progression through pre-recorded content rather than a fixed weekly schedule
- Discussion forums allow learners to self-select which topics or peer discussions to engage with

## Related Patterns
- [Online Course Design (Community of Inquiry)](online-course-design.md) — shares concern for interaction design, but MOOC scale makes deep learner-instructor interaction impractical in a way a smaller online course does not face

## Examples
- Coursera, edX, and Udacity's commercial xMOOC platforms, built around video lectures and automated quizzes
- The original Downes/Siemens connectivist MOOCs (2008–2009), built around distributed, learner-networked content rather than centralized video lectures

## Key Sources
- Weller, M. (2018). Twenty years of EdTech. *EDUCAUSE Review, 53*(4). Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/twenty_years_of_edtech](https://edtechbooks.org/lidtfoundations/twenty_years_of_edtech)
- Wiley, D. (2014). The MOOC misstep and the open education infrastructure. Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/open_educational_resources](https://edtechbooks.org/lidtfoundations/open_educational_resources)

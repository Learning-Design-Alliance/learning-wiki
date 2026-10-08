---
type: principle
id: text-to-speech
title: Text-to-Speech
description: "For a learner whose barrier to a text is decoding, vision or fatigue rather than its language, and when the goal is its meaning rather than reading the words, hearing the text read aloud while following the print with control of pace is expected to raise comprehension over print alone; no claim in the wiki tests text-to-speech itself."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-05
sources:
  - id: hillaire-2019
    resource: "https://doi.org/10.5334/jime.519"
    title: "Hillaire, G., Iniesto, F., & Rienties, B. (2019). Humanising text-to-speech through emotional expression in online courses. *Journal of Interactive Media in Education, 2019*(1), 12"
    author: "Hillaire, G., Iniesto, F., & Rienties, B"
  - id: podsiadlo-2016
    resource: "https://doi.org/10.21437/Interspeech.2016-1289"
    title: "Podsiadlo, M., & Chahar, S. (2016). Text-to-speech for individuals with vision loss: A user study. In *Interspeech 2016* (pp. 347-351)"
    author: "Podsiadlo, M., & Chahar, S"
  - id: stodden-2012
    resource: "https://doi.org/10.1016/j.procs.2012.10.041"
    title: "Stodden, R. A., Roberts, K. D., Takahashi, K., Park, H. J., & Stodden, N. J. (2012). Use of text-to-speech software to improve reading skills of high school struggling readers. *Procedia Computer Science, 14*, 359-362"
    author: "Stodden, R. A., Roberts, K. D., Takahashi, K., Park, H. J., & Stodden, N. J"
  - id: wood-2018
    resource: "https://doi.org/10.1177/0022219416688170"
    title: "Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73-84"
    author: "Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K"
---

# Text-to-Speech

> **Principle** · [All principles](index.md)
> **Evidence** · 11 claims (1 for, 10 mixed) · 17 studies (7 review, 4 quant-synthesis, 3 causal, 3 theoretical), `q1`–`q4` · 4 of 17 report an effect size · 5 claims rest on one study

## Conditional relationship

This page owns **synthetic speech as a route into written text**: software that reads aloud the text a learner is meant to work with (a reading, instructions, a question, written feedback), with the print usually still in view. For a learner whose barrier to that text is getting the words off the page (decoding well below the level of the ideas, low vision, reading fatigue, a second language read more slowly than it is understood by ear), and when the goal is the meaning of the text rather than reading the words unaided, hearing the text while following the print, with control over pace, pausing and replay, is expected to let the learner understand more of it (`conceptual-understanding`, `immediate-performance`) than print alone, and to keep them working on it longer (`persistence`). The expected gain is bounded by how well the learner understands the same language when it is spoken: speech removes a decoding demand, not a language or knowledge demand.

**No claim in the wiki tests text-to-speech as such**, or compares reading with synthetic speech against reading print alone. The page's earlier Key Sources include a meta-analysis of text-to-speech and read-aloud tools for students with reading disabilities (Wood et al., 2018) and a high-school study of struggling readers (Stodden et al., 2012); neither has a claim page here, so their findings are not used in the model. What the wiki holds are claims about neighbouring parts: spoken against written words beside a picture, written text duplicating narration with and without a picture, learning vocabulary by listening against reading, narration with a tracking highlight in children's e-books, one second-grade comparison of listening, reading and reading while listening, and the treatments that do improve word reading for children with reading disabilities. The design below is therefore a labelled default.

The relationship is conditional on four things a page cannot settle in advance. **Whether decoding is part of the goal**: if the goal is reading the words, speech removes the very thing being learned, and it is not an access support for that task. **The learner's listening comprehension of this text**: if the learner does not follow it when it is read aloud, speech will not help, and the barrier is vocabulary, knowledge or language. **What else is on the screen**: words read aloud while the learner must also study a diagram behave differently from words read aloud over plain text. **Whether the learner uses the tool actively** (pausing, replaying, checking understanding) or lets the audio run.

How the converted siblings sit beside this page: [Universal Design for Learning](universal-design-for-learning.md) holds the planning audit that decides whether decoding print is a demand outside the goal, and the rule that the goal and its criterion stay the same whatever the route; this page is one of the routes that audit can call for. [Multimodal Instruction](multimodal-instruction.md) holds the general choice between spoken and written words and the provision of an alternative mode where one is inaccessible; [Multimedia Learning](multimedia-learning.md) holds narration beside pictures and duplicated words. [Dual Coding](dual-coding.md) holds pairing words with a visual of the same idea, which is a different pairing (words with a picture) from this page's (printed words with the same words spoken). [Accessible Vocabulary and Syntax](accessible-vocabulary-syntax.md) holds removing language the goal does not need, which speech does not do. The [Audiobooks](../elements/audiobooks.md) element describes human-narrated whole books; most of the default below applies to them too. This page does not repeat those models.

## Default design, while the relationship is untested

The earlier page's guidance, kept as a concrete default a designer can act on and revise. Each step is a design proposal; its evidence status is stated beside it.

1. **Decide whether reading the words is part of the goal.** List what the task asks of the learner. If the goal is the content of the text (a science chapter, a policy, a case, a word problem's situation), speech is an access route and may be offered to anyone who needs it. If the goal is decoding, word reading, spelling or reading fluency, keep speech off for that practice and its assessment, and use it only for the content tasks around it. Untested here; the audit is modelled in [Universal Design for Learning](universal-design-for-learning.md).
2. **Check that the learner follows the text by ear.** Before relying on speech, read (or play) a short passage of the target text aloud and ask three or four questions about it; compare with the same learner's answers on a matched passage read silently. If the learner understands it heard but not read, speech is likely to help; if neither, work on vocabulary, background knowledge or simpler language first. Untested proposal; it rests on an argument that reading skill cannot exceed listening skill, reported second-hand ([Sticht's Law holds that reading skill cannot exceed listening skill](../claims/sticht-law-reading-cannot-exceed-listening.md) [~W]).
3. **Set the tool up for following, not only for listening.** Keep the print on screen with the word or sentence being read highlighted as it is spoken; start at the voice's default rate and let the learner change it; make pause, back-one-sentence and replay a single tap or key; and check the voice on the text's technical terms, names and abbreviations before the session, fixing any it mispronounces (most tools take a custom pronunciation or an alias). Evidence: in children's e-books, narration with a finger-tracking animation drew preschoolers' eyes to the text being read, including in their weaker language ([Audio narration with finger-tracking animation directs bilingual preschoolers' attention to the target-language print in dual-language e-books, including the nondominant language](../claims/enhancing-features-direct-attention-dual-language-e-books.md) [+M]); whether that attention became comprehension is weaker (below). The rate, control and pronunciation steps are untested proposals from the earlier page.
4. **Make the learner stop and do something with each section.** Break the text at paragraph or section boundaries (about 150–300 words, or one screen, as a proposal) and ask for one move at each break: answer a question, write a one-line summary, highlight the sentence that matters, or note a word to look up. Audio that runs on without breaks is the passive-listening risk the earlier page named. Untested as a TTS routine; the reason for asking learners to check their own understanding is a general self-regulation claim (listed under Further evidence).
5. **Where the text sits beside a diagram, decide what is spoken and what is shown.** If the learner must study a diagram, animation or chart while taking in the words, let the speech carry the explanation and keep on-screen words to labels and key terms, rather than showing the full paragraph highlighted and spoken at once; if pacing is in the learner's hands, the cost of showing both is smaller. Over plain text with no picture, showing the words while speaking them is the case the evidence reports as helping. Evidence: [Presenting words as spoken narration rather than on-screen text alongside graphics improves learning](../claims/modality-effect-narration-over-text.md) [~S] (strongest when system-paced) and [Redundant on-screen text impairs learning when it competes with a visualization, though written text duplicating narration alone can help](../claims/redundancy-principle.md) [~M] (a review of 63 studies, no pooled effect). Both come from short multimedia lessons with human or recorded narration, not text-to-speech tools.
6. **Keep reading instruction going for learners who struggle to decode.** For a learner with a reading disability, speech is for content classes and independent study; time for explicit, systematic decoding instruction stays in the timetable alongside it. Evidence: among treatments for children and adolescents with reading disabilities, phonics instruction was the only one with a statistically confirmed effect on reading and spelling, and that effect was small ([Phonics instruction has a small but statistically confirmed effect for children with reading disabilities, while Orton-Gillingham structured-literacy programs show positive but non-significant effects](../claims/structured-literacy-interventions-help-struggling-readers.md) [~M]); speech was not among the treatments tested.
7. **Use speech for instructions and feedback, not only for readings.** Make task instructions, quiz items and written comments readable aloud by the same tool, so a learner who needs speech for the reading is not left with print for what to do next. Untested; from the earlier page's examples.
8. **Plan the hand-over across sessions.** A default arc, all untested proposals:
   - *Sessions 1–2*: show the controls on a short text (10–15 minutes), then run one section-by-section reading with the questions supplied at each break.
   - *Sessions 3–6*: the learner sets the rate and the break points and writes their own question or summary at each break; the teacher or software checks two or three answers per text.
   - *Later sessions*: the learner chooses when to switch speech on. Every two to four weeks, give two matched short passages, one with speech and one without (order alternated), and five comprehension questions on each. Keep speech for that kind of text while the with-speech score is clearly higher; if the two scores are close for two checks in a row, offer the learner the choice to read unaided for that kind of text, and keep speech for denser material.
   - A learner moves from supplied questions to their own once they use pause and replay without prompting and answer most supplied questions correctly on two consecutive texts.

When a condition is not met: if the learner does not follow the text by ear either, simplify the language or teach the key vocabulary before offering speech; if the voice garbles the text (formulas, code, tables, many proper names), give a human recording or a version written for listening; if no device or headphones are available, pair the learner with a reader for the key passages.

## Fitting the design to a situation

The three facts that most change the decision:

- **Whether reading the words is part of what is being learned or assessed.** If it is, speech is withheld for that practice and its check; if it is not, speech is an access route like any other. If unstated, ask: is this task about understanding the content, or about reading it unaided?
- **The learner's barrier.** Decoding, low vision, fatigue, a second language, attention or limited vocabulary each call for a different set-up, and only some are helped by speech. If unstated, ask: when this learner reads this text, where does it break down, and do they understand it when it is read to them?
- **What else is on the screen and who controls pace.** Plain text, text with a diagram, and system-paced video each change what should be spoken and what shown. If unstated, ask: will the learner be looking at anything besides the words, and can they pause and replay?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are fluent readers of this text (`advanced` for its print), or the goal includes reading the words unaided | Do not build the lesson around speech; offer it as an optional control for fatigue or proofreading only, and keep it off during reading practice and any check of reading | untested; from the earlier page ("some learners comprehend better through print") |
| Learners are `child` early readers building fluency | Use speech or read-along for access to stories and content above their reading level, not as the main fluency practice; keep the child reading the words aloud themselves in separate practice, and check comprehension after read-along rather than assuming it | [Repeated listening improves oral reading fluency in second-grade students, with Listening Only outgaining Reading While Listening and Reading Only](../claims/repeated-listening-improves-oral-reading-fluency.md) [~M] (one seven-week study of 75 second graders, reported second-hand in a review; reading while listening had the smallest fluency gain and an average comprehension loss; no statistical test printed) |
| Young children with an e-book or app, possibly in two languages | Choose narration with a highlight that tracks the words, in the language whose print the child should look at; ask two or three story questions after, since attention to print did not reliably become comprehension | [Audio narration with finger-tracking animation directs bilingual preschoolers' attention to the target-language print in dual-language e-books, including the nondominant language](../claims/enhancing-features-direct-attention-dual-language-e-books.md) [+M]; [Multimedia features improved story comprehension in dual-language e-books (marginal trend) but not in single-language e-books](../claims/comprehension-benefit-dual-language-only.md) [~M] (one eye-tracking study, bilingual preschoolers) |
| Learners have a reading disability or dyslexia | Give speech for content reading and tests of content in every subject; keep explicit decoding instruction in its own time; record that the content scores were earned with speech | [Phonics instruction has a small but statistically confirmed effect for children with reading disabilities, while Orton-Gillingham structured-literacy programs show positive but non-significant effects](../claims/structured-literacy-interventions-help-struggling-readers.md) [~M] (speech itself untested here) |
| Learners have low vision or are blind and use a screen reader | The learner will not follow print, so make the text navigable by ear: real headings, alternative text on images, tables that read in order, equations in a speakable form; let the learner use their own screen reader and settings rather than an in-app voice | untested; from the earlier page (vision loss); [Universal Design for Learning](universal-design-for-learning.md) holds the alternative-route rule |
| Second-language learners | Use speech to hear the pronunciation of new words while reading them and to read along with texts at their listening level; expect vocabulary from listening or read-along to be learned at proportions similar to reading, with reading ahead on immediate tests only | [Reading and listening yield similar proportions of incidental vocabulary learning, with reading ahead only on some immediate posttests](../claims/reading-versus-listening-incidental-vocabulary-gains.md) [~S] (second-language vocabulary only; says nothing about synthetic voices) |
| Adults in work settings (manuals, procedures, compliance documents, forms) | Let workers listen to the document on their own device, in sections, and act on each section (find the step, fill the field) rather than only listen; fix the voice's pronunciation of product names and codes first | untested proposal |
| The text explains a diagram, animation or chart | Speak the explanation and show only labels and key terms on the visual; if the learner controls pace, full text can stay available on demand | [Presenting words as spoken narration rather than on-screen text alongside graphics improves learning](../claims/modality-effect-narration-over-text.md) [~S]; [Redundant on-screen text impairs learning when it competes with a visualization, though written text duplicating narration alone can help](../claims/redundancy-principle.md) [~M] (multimedia lessons with recorded narration, carried to synthetic speech) |
| Text is dense with notation (equations, code, tables, citations) | Do not rely on default speech; provide a version written for listening or a human recording, or limit speech to the prose around the notation | untested; from the earlier page (synthetic voices distort domain vocabulary) |
| Setting is `online-self-paced`, no teacher present | Build the speech control into every page and question, put a question or summary prompt at each section break with automatic checking where possible, and add the periodic with/without check from the default arc | untested proposal |
| Mixed modes: some learners remote, some in the room, or phone-only | Give everyone the same digital text so each can use their own device's speech with headphones; for phone-only learners, keep sections short enough for one screen and avoid layouts that read out of order | untested proposal |
| One teacher for a large class | Make speech available to all rather than assigned to a few; at each section break use a whole-class check (a quick poll or one written line) so the teacher sees who is lost, and go to those learners | untested proposal |
| Scarce facilitator time (volunteers, a busy shift, a brief check-in) | Spend the facilitator's time once, on showing the controls and the section-break routine; after that, the learner works alone with the supplied questions, and the facilitator looks only at the answers to one or two questions per text | untested proposal |
| A single session only | Ten minutes on the controls with a short text, then one section-by-section reading of the real text with supplied questions; record the answers and do not claim lasting benefit | untested proposal |
| Learners with low confidence or low literacy, adult or child | Offer speech privately (headphones, own device), as a normal option for everyone rather than a label; let the learner choose rate and voice; start on short texts that matter to them | untested proposal |
| Stakes are high, or the test is meant to measure reading | If the test measures content, allow speech as an accommodation and say so in the record; if it measures reading, do not, and give the learner a fair version of the test that does not depend on speech for its instructions | untested; follows from step 1 |
| The brief names its own routine (its reading log, question set, rubric, annotation code or listening guide) | Keep that routine and its categories as given; add only speech for the text and a break at each section where the routine's own question or code is applied | untested proposal (a lesson from page testing, not from a claim) |
| The material is private or sensitive (a learner's own writing, a health or HR document, a personal letter) | The learner decides who hears it: headphones, their own device, and an on-device voice rather than a cloud service where the text would leave the device; nobody else listens unless the learner asks | untested proposal |
| A fixed short time budget (for example, 20 minutes) | Fit the text to it: one text of about 600–900 words in three or four sections, 3–4 minutes of listening per section plus one minute at each break, the last five minutes for the brief's own task | untested proposal (speech runs at roughly the voice's set rate, so time the actual audio first) |
| The brief wants a whole task kept whole (read a real policy and decide; follow a real procedure) | Keep the real document and the real decision; use speech and section breaks inside it, and do not split it into separate comprehension items | untested proposal |
| Learners use speech on their own writing, or produce audio for a real audience (an announcement, a podcast, a museum guide) | For proofreading, have the learner listen to their draft at a slow rate and mark every place it sounds wrong. For audio a real audience will hear, check every name and term by ear and have a person approve it before release | untested proposal |
| Adult second-language learners in short evening classes, reading workplace instructions | Use short texts (about 100–250 words, one procedure) read sentence by sentence; teach playback control as a skill (slow the voice, replay a sentence, replay a single word for pronunciation) and let learners practise privately with headphones; give teacher feedback in a form TTS can read aloud; each lesson end with one unaided reread of a step. If the brief names its own assessment (accuracy, control of playback, a reflection comparing listening and unaided reading), assess exactly those, and keep checks to one or two items so the class is not mostly testing | untested proposal |

Five of the 21 rows cite a claim, and none of those tests text-to-speech: one carries two multimedia-narration findings to synthetic speech, one a second-language vocabulary synthesis, one a children's e-book eye-tracking study, one a second-hand report of a single fluency study, and one a reading-disabilities meta-analysis that bears only on keeping decoding instruction. The other sixteen are untested proposals; two of them point to a converted sibling for the rule they apply.

## Observation, state and explanation

What can be observed is a session with the tool under stated conditions: the text, whether speech was on, the rate, how often the learner paused and replayed, what they did at each section break, how long they stayed with the text, and their answers to questions about it. "Has an access barrier", "is listening passively" and "understands the content" are inferred states. A good answer with speech on shows what the learner understood with speech; it does not show what they can read unaided.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Answers well with speech on, poorly on a matched passage read silently | Decoding or reading fatigue is the barrier, as assumed; the with-speech passage was easier; the learner was more attentive in the speech session | Swap which passage gets speech in the next check; ask the learner to read a few sentences aloud from the silent passage and note where it breaks down. |
| Answers poorly with speech on and off | The barrier is vocabulary, knowledge or the language, not decoding; the questions test something the text does not make clear; the learner did not attend to either | Read one section aloud and ask the learner to retell it in their own words; ask which words they did not know; try a simpler text on the same content. |
| Lets the audio run through, never pausing, then cannot answer | Passive listening; the rate is too fast; the learner does not know the controls or feels watched using them | Watch one session; show the controls again and set breaks at each section; ask whether the rate felt comfortable and let them lower it. |
| Turns speech off soon after starting | The voice is unpleasant or mispronounces terms; the learner reads faster than the voice; using it marks them out in front of peers | Ask which; try another voice or a faster rate; offer it with headphones and without others seeing. |
| Good on read-aloud content, no progress in reading the words over a term | Speech is doing its job for content and decoding has not been taught; decoding instruction was crowded out; progress is too slow to show over a term | Check whether decoding instruction happened and how much; give a short word-reading measure at the start and end of the term. |

These rows are proposals, untested with learners as diagnostics. A check is itself practice and changes what it measures, so record each one, and keep the explanations that remain open rather than choosing the one whose name fits.

## Evidence and qualifications

No claim in the wiki compares text-to-speech with print alone, varies the voice or the rate, or tests the section-break routine. The claims below test neighbouring parts of the relationship.

- [Presenting words as spoken narration rather than on-screen text alongside graphics improves learning](../claims/modality-effect-narration-over-text.md) [~S]: a meta-analysis of 43 independent effects comparing graphics with narration against graphics with on-screen text supported the advantage for narration, moderated by material complexity, pacing (strongest when system-paced) and field; and an experiment with 146 college students learning lightning formation from an animation. No pooled effect size is recorded. It bears on what to speak when text explains a picture; it does not compare speech with print over plain text.
- [Redundant on-screen text impairs learning when it competes with a visualization, though written text duplicating narration alone can help](../claims/redundancy-principle.md) [~M]: a literature review of 63 studies found that adding written text duplicating the narration of a narrated visualization most often impaired learning, with reversals for older learners, learner-paced delivery and abridged text; adding written text to narration with no visualization was reported as positive. This is the closest the wiki comes to the read-along case (print shown while the same words are spoken, no picture), and it points in the helpful direction, but the review reports no pooled effect and its studies are multimedia lessons, not reading assignments.
- [Reading and listening yield similar proportions of incidental vocabulary learning, with reading ahead only on some immediate posttests](../claims/reading-versus-listening-incidental-vocabulary-gains.md) [~S]: a meta-analysis of 24 second-language studies (2,771 participants) found large effects of meaning-focused input on incidental vocabulary against controls; reading had the largest effect on first posttests (g = 1.45, listening 0.97, reading while listening 0.78), but proportions of words learned were similar for reading and listening, and mode no longer mattered on follow-up posttests. It supports offering listening or read-along to second-language learners without expecting a large vocabulary cost; it says nothing about synthetic voices.
- [Repeated listening improves oral reading fluency in second-grade students, with Listening Only outgaining Reading While Listening and Reading Only](../claims/repeated-listening-improves-oral-reading-fluency.md) [~M]: one seven-week study of 75 second graders, reported second-hand in a review: listening only gained 24 words per minute in oral reading fluency, reading only 19 and reading while listening 18; on comprehension, reading only gained 6.5%, listening only 4%, and reading while listening showed an average loss of 1%. No statistical test is printed, and the claim's title says "improves" though no group without listening was measured. It is the one entry in the wiki on reading while listening with young readers, and it qualifies the model: read-along was not the best condition on either outcome.
- [Audio narration with finger-tracking animation directs bilingual preschoolers' attention to the target-language print in dual-language e-books, including the nondominant language](../claims/enhancing-features-direct-attention-dual-language-e-books.md) [+M] and [Multimedia features improved story comprehension in dual-language e-books (marginal trend) but not in single-language e-books](../claims/comprehension-benefit-dual-language-only.md) [~M]: one eye-tracking study of bilingual preschoolers. Narration with a tracking animation drew the eyes to the text being read; story comprehension was only marginally higher in dual-language books and not different in single-language books. Highlighting can direct attention to print; that is not the same as comprehension.
- [Phonics instruction has a small but statistically confirmed effect for children with reading disabilities, while Orton-Gillingham structured-literacy programs show positive but non-significant effects](../claims/structured-literacy-interventions-help-struggling-readers.md) [~M]: a meta-analysis of 22 randomized trials of treatments for children and adolescents reading below the 25th percentile found phonics instruction the only treatment with a statistically confirmed effect on reading and spelling (small after adjustment for publication bias), and a second meta-analysis found Orton-Gillingham effects positive but not significant. It limits the model: whatever speech does for access to content, the evidence for improving word reading lies elsewhere.
- [Automatic word recognition frees resources for comprehension](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [~W]: a theoretical model and a review; the mechanism by which removing a decoding demand could free attention for meaning. The claim page itself says neither source shows that changing decoding changes comprehension, so it is a reason to expect the effect, not evidence of it.
- [Sticht's Law holds that reading skill cannot exceed listening skill](../claims/sticht-law-reading-cannot-exceed-listening.md) [~W]: an argument reported second-hand in a conference paper, coded `q1`. It is the basis for checking listening comprehension before relying on speech (step 2), and nothing stronger.

Learners, materials and outcomes differ across these claims (college students with animations, second-language learners' vocabulary, second graders' fluency, preschoolers' eye movements), so do not rank them by effect label. None used a text-to-speech tool on an assigned reading, and none measured delayed retention or use outside the session.

## Further evidence, not yet read against this model

Claims this page cited before it was rewritten as a conditional model. Neither tests text-to-speech; each is kept with what it is and how far it bears.

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — two reviews and an experiment on how grouping items into chunks reduces what working memory must hold. The earlier page used it as an analogy (speech shifts part of the processing burden); it does not test listening or reading, and bears on this page only through the general working-memory account. Not checked against its sources (abstracts and entries only).
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] — a synthesis and a theoretical review arguing that checking performance against a goal leads learners to adjust strategy. It is the general reason for the section-break check in the default design; it does not test that check with speech. Not checked against its sources (abstracts only).

## Objective and learner-valued goal

The designer's objective is usually understanding of a particular text or body of content, shown on a stated task at a stated time, and sometimes independence in reading. Elicit separately what the learner wants from the tool: to keep up with classmates, to get through the reading faster, not to be seen struggling, to read the real documents of their job, or to become able to read without it. These can pull apart. A learner who values not standing out may refuse speech they need; one who values speed may play everything at a fast rate and keep less; a learner who wants to read unaided may want speech withdrawn sooner than the comprehension checks suggest.

For example, an adult in a workplace programme may want to read the safety procedures for a new machine without asking a colleague, while the designer's objective for the week is understanding the procedure well enough to follow it. Speech serves the designer's objective at once. The learner's goal is served only if the arc gives them unaided reading of those procedures over time, with decoding help if that is the barrier. Record both, so that understanding with speech is not read as the reading independence the learner came for.

## What would revise this model?

The expectation should weaken if comparisons of reading with text-to-speech against print alone, on assigned texts with comparable learners and content outcomes, show no advantage for learners with decoding or vision barriers, or show that the gain on the day does not carry to later tests on the same content. If read-along (print shown and spoken together) does worse than listening alone or reading alone for older learners too, as one second-grade study reported, the default of keeping print in view should change to a choice. If learners with access barriers do no better with the section-break routine than with uninterrupted speech, step 4 should go. If speech used across content classes is found to slow progress in word reading even when decoding instruction continues, step 6 should say so. Do not protect the model by calling every failure "passive use" or "the wrong voice" after the fact.

Understanding with speech on, understanding without it, reading the words unaided, delayed retention and use of the content in the setting the learner values are separate claims. The present evidence establishes no rate, no section length, no voice and no criterion for withdrawing speech.

## Related Principles
- [Accessible Vocabulary & Syntax](accessible-vocabulary-syntax.md) — simpler language and audio support often work together.
- [Instructor Accessibility](instructor-accessibility.md) — TTS is one route for improving access to written materials.
- [Annotating](annotating.md) — learners can combine audio playback with highlighting, notes, and questions.
- [Speech-to-text](../elements/speech-to-text.md) — reading and writing access tools often complement one another.
- [Universal Design for Learning](universal-design-for-learning.md) — the planning audit that decides whether decoding print is a demand outside the goal; speech is one of the routes it can call for.
- [Multimodal Instruction](multimodal-instruction.md) — the general choice between spoken and written words, and alternative modes where one is inaccessible.
- [Multimedia Learning](multimedia-learning.md) — narration beside pictures and duplicated on-screen words.
- [Dual Coding](dual-coding.md) — pairing words with a visual of the same idea, a different pairing from printed and spoken words.
- [Audiobooks](../elements/audiobooks.md) — human-narrated whole texts; most of the default design above applies to them.

## Examples

- **Read-aloud support for assigned text**: Learners listen while following along in the print version.
- **Audio review of instructor feedback**: Written comments are revisited through TTS so learners can process them more carefully.
- **Chunked listening routine**: Learners pause after each paragraph or section to summarize and annotate.
- **Pronunciation-supported vocabulary review**: Learners use TTS to hear unfamiliar academic language while reading it.
- **Strategy pages describing the tool in use**: [Text-to-Speech (TTS)](../strategies/text-to-speech-tts.md), [Text To Speech Technology](../strategies/text-to-speech-technology.md), [Text To Speech Tools](../strategies/text-to-speech-tools.md), [Text-to-Speech Software](../strategies/text-to-speech_software.md).
- [Apply Section 508 accessibility tips and tools when preparing presentations, Excel files, websites, and multimedia products](../strategies/508-compliance-accessibility-tips-for-education-materials.md)

## Key Sources
- Hillaire, G., Iniesto, F., & Rienties, B. (2019). Humanising text-to-speech through emotional expression in online courses. *Journal of Interactive Media in Education, 2019*(1), 12. [https://doi.org/10.5334/jime.519](https://doi.org/10.5334/jime.519)
- Podsiadlo, M., & Chahar, S. (2016). Text-to-speech for individuals with vision loss: A user study. In *Interspeech 2016* (pp. 347-351).
- Stodden, R. A., Roberts, K. D., Takahashi, K., Park, H. J., & Stodden, N. J. (2012). Use of text-to-speech software to improve reading skills of high school struggling readers. *Procedia Computer Science, 14*, 359-362. [https://doi.org/10.1016/j.procs.2012.10.041](https://doi.org/10.1016/j.procs.2012.10.041)
- Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73-84. [https://doi.org/10.1177/0022219416688170](https://doi.org/10.1177/0022219416688170)

<!-- deprecated 2026-10-05: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Text-to-speech (TTS) converts written text into spoken audio, giving learners an additional way to access reading materials, instructions, and feedback. It is useful when decoding, visual fatigue, pace, or attention barriers make print alone harder to process. TTS can widen access to content, support rereading, and help learners coordinate listening with visual text.

TTS is most effective when it is treated as an access and support tool, not as a substitute for all reading instruction. Learners still need support in comprehension, vocabulary, annotation, and independent meaning-making. The tool helps when it removes unnecessary access barriers so that the learner's effort can shift toward understanding and using the content.

## Implications
Text-to-speech is most useful when reading access, not conceptual ability, is the main barrier to engagement. By shifting part of the processing burden from print decoding to coordinated listening and reading, TTS can make dense text more manageable [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S]. But its value depends on active use: learners still need to pause, replay, annotate, and monitor comprehension rather than letting audio wash over them [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M]. TTS works best as an access support inside a broader reading routine, not as a substitute for strategy instruction.

### Context
#### Requirements
- **A genuine access need or comprehension benefit**: TTS is most useful when audio support reduces barriers to engaging with text.
- **Learner control over pacing**: Playback speed, pausing, replay, and chunking are important for usefulness.
- **Appropriate text selection**: Dense, technical, or lengthy text often benefits most from supported listening.
- **Integration with comprehension routines**: TTS should be paired with note-taking, annotation, questioning, or discussion.
#### Constraints
- **Passive listening risk**: Audio alone does not guarantee active comprehension.
- **Voice quality and pronunciation issues**: Synthetic voices may distort meaning, especially with domain-specific vocabulary.
- **Not equally helpful for every learner or task**: Some learners comprehend better through print, and some tasks require close visual attention.
- **Access without strategy**: TTS can remove one barrier while leaving comprehension problems untouched if instruction does not adapt.

### Target Learners
- **Learners with reading-access barriers**: Strong fit for learners with decoding difficulty, visual impairment, or reading fatigue.
- **Learners processing dense academic text**: Audio support can help learners sustain engagement with long or complex materials.
- **Multilingual learners**: TTS can support pronunciation, listening, and vocabulary access when paired with text.
- **Adult learners balancing speed and stamina**: Listening while following print can help learners manage effort and persistence.

### Target Learning Objectives
- **Access to print-based content**: Making written materials more usable.
- **Reading comprehension support**: Helping learners stay with text long enough to make meaning.
- **Independent study habits**: Enabling learners to use audio support strategically outside class.
- **Engagement with feedback and instructions**: Making written guidance easier to revisit and process.

### Theory
#### Supporting
- Dual-channel and multimedia perspectives — coordinated visual and auditory presentation can support processing when designed carefully.
- Cognitive load perspectives — audio support can reduce some access burdens and free attention for comprehension.
- Accessibility and universal design perspectives — multiple representations increase the likelihood that learners can engage with the material.
#### Contradicting / Qualifying
- TTS is not automatically beneficial; poor pacing, low-quality synthesis, or passive use can limit comprehension.
- The tool supports access, but it does not replace explicit reading strategy instruction.

### Claims
- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — audio support can reduce some of the access burden that print alone places on working memory
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] — TTS is strongest when learners actively check and regulate comprehension while listening

## Related Principles
- [Accessible Vocabulary & Syntax](accessible-vocabulary-syntax.md) — simpler language and audio support often work together.
- [Instructor Accessibility](instructor-accessibility.md) — TTS is one route for improving access to written materials.
- [Annotating](annotating.md) — learners can combine audio playback with highlighting, notes, and questions.
- [Speech-to-text](../elements/speech-to-text.md) — reading and writing access tools often complement one another.

## Examples
- **Read-aloud support for assigned text**: Learners listen while following along in the print version.
- **Audio review of instructor feedback**: Written comments are revisited through TTS so learners can process them more carefully.
- **Chunked listening routine**: Learners pause after each paragraph or section to summarize and annotate.
- **Pronunciation-supported vocabulary review**: Learners use TTS to hear unfamiliar academic language while reading it.

## Key Sources
- Hillaire, G., Iniesto, F., & Rienties, B. (2019). Humanising text-to-speech through emotional expression in online courses. *Journal of Interactive Media in Education, 2019*(1), 12. [https://doi.org/10.5334/jime.519](https://doi.org/10.5334/jime.519)
- Podsiadlo, M., & Chahar, S. (2016). Text-to-speech for individuals with vision loss: A user study. In *Interspeech 2016* (pp. 347-351).
- Stodden, R. A., Roberts, K. D., Takahashi, K., Park, H. J., & Stodden, N. J. (2012). Use of text-to-speech software to improve reading skills of high school struggling readers. *Procedia Computer Science, 14*, 359-362. [https://doi.org/10.1016/j.procs.2012.10.041](https://doi.org/10.1016/j.procs.2012.10.041)
- Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73-84. [https://doi.org/10.1177/0022219416688170](https://doi.org/10.1177/0022219416688170)
-->

# Usability Test Protocol and SUS Instrument: Weber State Class Registration

**Researcher:** Kaden Donaldson
**Course:** Human Computer Interaction
**Target system:** Weber State University eWeber portal, *Register for Classes* flow (desktop web)
**Live SUS survey:** https://kaden-13.github.io/HCI-Lab05-Usability-SUS/

---

## Repository contents

| Path | Purpose |
|---|---|
| `README.md` | This document: the full consolidated usability test protocol |
| `docs/index.html` | Accessible 10 item SUS questionnaire (deployed with GitHub Pages) |
| `empirical_usability/usability_logging_sheet.xlsx` | Observation logger: task log with sub task milestone timestamps, an error log that categorizes and counts errors automatically, integrity checks, SUS scoring with percentile, grade, adjective, and acceptability, and a summary tab |
| `empirical_usability/usability_logging_sheet.csv` | Same task log as a plain CSV for tools that cannot open .xlsx |
| `empirical_usability/error_log.csv` | Blank per error log in CSV form |

### Table of contents
1. [Study scope and participant screener](#step-1-study-scope-and-participant-screener)
2. [Moderator script and informed consent](#step-2-moderator-script-and-informed-consent-protocol)
3. [Performance metrics and data logger](#step-3-performance-metrics-and-data-logger-sheet)
4. [SUS instrument and scoring algorithm](#step-4-system-usability-scale-sus-instrument)
5. [Accessibility audit of the instrument and environment](#step-5-accessibility-first-survey-and-environment-audit)
6. [Post mortem reflection](#post-mortem-reflection)
7. [Appendix: session run sheet](#appendix-a-session-run-sheet)

---

## Step 1: Study Scope and Participant Screener

### 1.1 Study goals

Earlier phases of this project (Phase 1 Usability Audit, Lab 03 Cognitive Audit, Phase 2 IA Blueprint) found problems in the Register for Classes flow through expert review: search results that keyboard users cannot reach, vague error messages when a section is full, and dense results tables. (See my [Contextual-Research](https://github.com/Kaden-13/Contextual-Research) repo for the Phase 1 and Phase 2 work.) This study collects **empirical benchmark data from real users** so the team can measure how much those problems actually cost in time, errors, and perceived usability before any redesign.

**Research questions**
1. Can students independently find and enroll in a specific open section, and how long does it take?
2. Can students independently remove a class from their schedule without help?
3. Where do errors and hesitation cluster in the flow?
4. What is the baseline SUS score for the current system, so a redesign can be compared against it?

### 1.2 Target system and test environment

| Item | Setting |
|---|---|
| System | eWeber > Register for Classes (production site, or a sandbox term if the registrar provides one) |
| Device | Participant's usual device type when possible; lab default is a 15 inch laptop, Chrome, 100% zoom |
| Assistive technology | Participant's own setup (screen reader, zoom, keyboard only, voice control). The moderator never changes their settings. |
| Recording | OBS screen and audio capture; webcam only with separate consent |
| Session length | About 30 minutes |
| Participants | 5 (minimum 3) |

> **Safety note for a live system:** Participants use a moderator provided test account, or their own account with the rule that nothing is finalized. If only a live account is available, Task 1 ends when the participant reaches the final confirmation step and the moderator says "Stop there." Task 2 uses a placeholder class added during setup.

### 1.3 Task scenarios

Two high priority tasks were chosen because they are the most frequent and most failure prone registration actions found in Phase 1.

| ID | Internal task name (moderator only) | Success criteria (end state) | Time cap |
|---|---|---|---|
| **T1** | Find an open section of a required course matching a schedule constraint and enroll in it | CS 4110 section that meets Tuesday and Thursday and has open seats appears in the participant's pending or registered schedule | 300 s |
| **T2** | Remove a class from the current term schedule | The placeholder class no longer appears as registered for the term | 300 s |

The participant facing wording of each task is in [Section 2.4](#24-task-scenario-handouts). It avoids the interface's own labels.

**Task order is counterbalanced** to reduce learning effects: P01, P03, P05 do T1 then T2; P02 and P04 do T2 then T1.

### 1.4 Participant screener

**Recruitment target:** 3 to 5 current or incoming college students, 18 or older, who represent a spread of age, technology comfort, and assistive technology use. The screener is sent as a short online form. Questions use neutral wording and balanced answer options so no answer looks like the "right" one.

**Q1. Which of these best describes you right now?**
- Currently enrolled at Weber State University
- Currently enrolled at another college or university
- Planning to enroll in college within the next year
- None of these

*Purpose: eligibility. "None of these" is screened out.*

**Q2. What is your age range?**
- 18 to 24
- 25 to 34
- 35 to 44
- 45 or older
- Prefer not to say

*Purpose: age diversity. Aim for at least one participant aged 25 or older. Under 18 is not offered and is screened out.*

**Q3. In a typical semester, how often do you use an online portal to look up, change, or sign up for classes?**
- I have not used one yet
- Once or twice a semester
- Three to five times a semester
- More than five times a semester

*Purpose: filters for registration experience without implying more is better. Aim for a mix of first time or low frequency users and frequent users.*

**Q4. How would you rate your comfort using websites to complete forms and online tasks?**
- 1 Not at all comfortable
- 2
- 3
- 4
- 5 Very comfortable

*Purpose: technological literacy. Aim to include at least one participant at 3 or below and at least one at 4 or above. Participants at 1 are still eligible; the study needs them.*

**Q5. Do you use any of the following when you use a computer or phone? (Select all that apply)**
- Screen reader (for example NVDA, JAWS, VoiceOver)
- Screen magnifier or browser zoom above 150%
- Keyboard only, no mouse
- Voice control or dictation
- High contrast or dark mode for readability
- Captions or transcripts
- Something else (optional to describe)
- None of these
- Prefer not to say

*Purpose: ability and assistive technology representation. Aim for at least one participant who uses an assistive technology. No question asks about a diagnosis or disability; only tools are asked about.*

**Selection matrix (fill after screening)**

| Slot | Age range | Registration frequency (Q3) | Comfort (Q4) | AT use (Q5) | Task order |
|---|---|---|---|---|---|
| P01 | | | | | T1 then T2 |
| P02 | | | | | T2 then T1 |
| P03 | | | | | T1 then T2 |
| P04 | | | | | T2 then T1 |
| P05 | | | | | T1 then T2 |

**Exclusions:** anyone who has worked on the eWeber registration interface, current HCI classmates (they know the heuristics being tested), and anyone under 18.

---

## Step 2: Moderator Script and Informed Consent Protocol

The moderator reads every scripted block **word for word** for every participant. Lines in *italics* are moderator actions and are not read aloud.

### 2.1 Pre test ethical briefing and consent

*Seat the participant. Moderator sits slightly behind and to the side, out of the participant's direct line of sight to the screen. Recording is off.*

> "Hi, thank you for coming in today. My name is ______, and I'll be guiding this session. It should take about 30 minutes.
>
> Before we start, I want to go over a few things.
>
> **We are testing the software, not you.** We want to find where the class registration website is confusing or hard to use so it can be improved. There are no right or wrong answers, and nothing you do today is a mistake on your part. If something is hard, that tells us the website needs work, and that is exactly what we are here to learn. Nothing from today will be connected to your grades, your student record, or your account standing.
>
> **Participation is completely voluntary.** You can skip any task or question, ask for a break, or stop the session at any time for any reason, and you don't have to explain why. There is no penalty of any kind for stopping. If you withdraw, I will delete your recording and notes unless you tell me I can keep them.
>
> **How your data is handled.** With your permission I will record the screen and audio while you work, and I'll take notes. Here is how that information is protected:
> - You'll be identified only by a participant code, like P01. Your name will not appear in the notes, the spreadsheet, or the survey.
> - The recording is saved to an encrypted, password protected drive that only the research team can access. It is never posted online or uploaded to the course repository.
> - If your name, student ID, or other personal details appear on screen, those parts will be blurred or cut before anyone else on the team reviews the video.
> - Only summary numbers and anonymized quotes will be reported. Recordings are deleted at the end of the semester.
>
> Do you have any questions about any of that?"

*Answer questions. Then hand over the consent form.*

> "This form says the same things I just told you. Please read it, and if you agree, check each box and sign. You can say no to the recording and still take part; I'll just take notes instead."

**Consent form checklist** (participant initials each line)

| | Statement | Initials |
|---|---|---|
| ☐ | I understand participation is voluntary and I can pause, skip, or withdraw at any time without penalty. | |
| ☐ | I understand the session evaluates the website, not my ability. | |
| ☐ | I agree to screen and audio recording. *(Optional: I can still participate if I decline.)* | |
| ☐ | I agree to webcam recording of my face for expression notes. *(Optional.)* | |
| ☐ | I understand my data will be stored securely under a participant code and deleted at the end of the semester. | |
| ☐ | I am 18 years of age or older. | |

*Start the recording only after consent is signed. Say aloud: "Recording started, participant P0__, [date]."*

### 2.2 Concurrent Think Aloud (CTA) instructions

> "While you work, I'd like you to **think out loud**. That means saying whatever is going through your mind as it happens: what you're looking for, what you expect to happen when you click something, what surprises you, and anything that's confusing or annoying. Imagine you're talking to yourself, just loudly enough for the recording.
>
> I'm going to stay quiet during the tasks. That isn't me being rude; it's so I don't accidentally influence what you do. **I won't be able to answer questions about how to do the task**, because we need to see how the website works on its own. If you ask me something, I may say 'What would you do if I weren't here?'
>
> When you feel you've finished a task, or if you'd stop trying if you were on your own, just say **'Done.'** Either answer is completely fine.
>
> Let's practice with something unrelated first."

**Practice task (not logged):**

> "Please open the Weber State homepage and, while thinking out loud, find out what time the campus library closes today."

*Allow up to 2 minutes. If the participant goes silent, use the neutral reminder N1 so they learn what it sounds like. Do not comment on how they did. Then say:* "Great, that's exactly the kind of talking out loud that helps. Let's start the real tasks."

### 2.3 Standardized moderator prompt bank

The moderator may only say the following during a timed task. Every prompt used is logged by code in `Moderator_Prompts_Used`.

**Neutral prompts (do not change Task_Success)**

| Code | When | Exact wording |
|---|---|---|
| N1 | Participant silent for 15 seconds or more | "What are you thinking right now?" |
| N2 | Participant asks how to do something | "What would you do if I weren't here?" |
| N3 | Participant asks if they are right or done | "Whatever you decide is fine. Tell me when you think you're done." |
| N4 | Participant apologizes or blames themselves | "You're doing fine. Anything that's hard here is useful for us to see." |
| N5 | Participant makes a vague comment ("hmm", "weird") | "Can you say more about that?" |

**Assist ladder (changes Task_Success to 0.5)**
Given only if (a) the participant has made no forward progress for 120 seconds, **or** (b) the participant says they would give up but agrees to keep going. The timer is not paused.

| Code | Exact wording |
|---|---|
| A1 | "Take a look at the whole page again. Is there anything else that might help?" |
| A2 | "Try reading the task card once more." *(Moderator re-reads the card exactly as written.)* |

No other hints are allowed: no pointing, no naming menus or buttons, no "almost", no "you're close".

**Recovery scripts (R1 to R3)** for stressed participants are in [Section 2.6](#26-recovery-scripts-for-stressed-or-distressed-participants). They lower stress without giving task hints and are logged by code the same way.

**Terminal failure (Task_Success = 0)** when the participant says "Done" at a wrong end state, gives up, or reaches the 300 second cap. At the cap, say: "Thank you, that's all the time for this one. Let's move on." Then ask the SEQ as normal.

**Permitted neutral acknowledgements:** "Thank you." "Okay." Said in the same flat tone every time, and only *after* the participant says "Done", never during the task.

### 2.4 Task scenario handouts

Each task is printed on its own card in 16 pt sans serif text (also provided as a large print and screen reader friendly digital copy). The moderator reads the card aloud, hands it over, and says **"Begin."** The timer starts on "Begin."

The cards deliberately avoid the interface's exact labels. The Register for Classes screens use words such as **"Register for Classes," "Find Classes," "Search," "Add," "Submit," "Drop,"** **"Schedule and Options,"** and **"Web Drop."** None of these appear on the cards.

---

> **Task card T1**
>
> You're planning your next semester. Your advisor told you that you need to take **Software Engineering (CS 4110)** next term. You work on Mondays, Wednesdays, and Fridays, so you can only take it on **Tuesdays and Thursdays**.
>
> Using the Weber State student portal, get yourself a seat in a section of that course that fits your schedule and still has space available.
>
> Tell me "Done" when you believe you have a seat in the course.

---

> **Task card T2**
>
> You've changed your mind about one of the courses you're signed up for this term, **[placeholder course, for example PE 1094]**. You've decided you no longer want to take it.
>
> Using the Weber State student portal, make it so that course is no longer part of your schedule for this term.
>
> Tell me "Done" when you believe the course is no longer on your schedule.

---

**Cue bias check**

| Interface label | Card wording used instead |
|---|---|
| Register for Classes / Add / Submit | "get yourself a seat" |
| Find Classes / Search | (no search verb; goal stated as an outcome) |
| Open seats / Status: Open | "still has space available" |
| Meeting days TR | "on Tuesdays and Thursdays" |
| Drop / Web Drop | "make it so that course is no longer part of your schedule" |
| Schedule and Options | "your schedule" (lower case, generic) |

### 2.5 Post task and post test scripts

**Immediately after each task** (moderator stops the timer at "Done", the give up, or the cap):

> "On a scale from 1 to 7, where 1 is very difficult and 7 is very easy: **Overall, how easy or difficult was this task to complete?**"

*Show the printed SEQ card (Section 3.3). Record the number. Do not react to it.*

**After both tasks:**

> "Thank you. Last step: please fill out this short questionnaire about the website as a whole. Your participant code is P0__."

*Open the SUS survey on the same device. Step away from the screen while they complete it.*

### 2.6 Recovery scripts for stressed or distressed participants

Registration has real stakes for students, so people can feel tested even after being told they aren't. If a participant starts apologizing, blaming themselves, sighing a lot, or going quiet and tense, the moderator uses one of these. None of them give hints about the task.

| Code | Situation | What to say | How to log it |
|---|---|---|---|
| R1 | Frustration or self blame | "You're not doing anything wrong. If something is confusing, that's on the website, and that's what we're trying to find." | Log R1; timer keeps running; success not affected |
| R2 | Wants to give up, or is clearly upset | "It's totally fine to stop this one. Do you want to keep trying or move on?" If they seem really upset, pause the session and offer to end it with no penalty. | If they stop: log End time, success 0, note "chose to stop" |
| R3 | Portal error, timeout, or crash | "That's a problem with the website, not you. Give me a second to reset it." | Log SYS in Error_Log; if the reset takes over 60 s, leave the attempt out of timing |

If a participant ever worries they changed their real schedule, stop the task and check the account together right away. Their wellbeing comes before the data.

### 2.7 Debrief

The debrief happens after the SUS, even if the session ended early.

1. **Open floor:** "That's it for the tasks. Anything about the website you want to tell me that we didn't get to?"
2. **Explain the study:** "Now I can tell you more. Earlier reviews of this site found problems like a vague message when a class is full. Today was about measuring how much those problems actually slow people down. I stayed quiet so I wouldn't influence you."
3. **Reassure and check in:** "Anywhere you got stuck is useful info about the website, not you. How are you feeling after that?"
4. **Data rights:** "You're only identified as P0__. The recording stays on an encrypted drive and gets deleted at the end of the semester. If you change your mind about us keeping your data, email me with your code and I'll delete it, no reason needed." *(Hand them a card with their code and my school email.)*
5. **Check their real schedule** (live portal only): "Let's double check your real schedule so we know nothing changed."
6. **Thank them:** "Thanks so much for your time. This will help make registration easier for other students."

*Afterward: stop the recording, write down anything unusual in Notes, download the SUS CSV, and move the recording to the encrypted drive.*

---

## Step 3: Performance Metrics and Data Logger Sheet

The logger is `empirical_usability/usability_logging_sheet.xlsx` (plain `.csv` copies included). Yellow cells are moderator inputs, blue cells are formulas, and grey rows are a filled example that every summary ignores.

| Tab | What it does |
|---|---|
| **Instructions** | Legend, workflow, and operational definitions |
| **Task_Log** | One row per participant per task, pre filled for P01 to P05 with counterbalanced order. Captures start, three sub task milestones, and end times; calculates elapsed seconds; pulls error counts from Error_Log; runs integrity checks |
| **Error_Log** | One row per error, logged live. The moderator picks a code; category, user error status, and seconds since task start fill in automatically |
| **SUS_Responses** | Raw Q1 to Q10 ratings; per item contributions, SUS score, percentile, curved grade, adjective, acceptability, and response pattern flags by formula |
| **Summary** | Per task completion rate, average times (overall, successful only, and per milestone), errors by category, average SEQ, rows that need fixing, and the average SUS with its percentile, grade, and adjective |
| **Milestones** | Definition of M1, M2, M3 for each task |
| **Error_Codes** | Error taxonomy used for automatic categorization |
| **SUS_Benchmarks** | Grade, adjective, and acceptability lookup tables with sources |

### 3.1 Quantitative fields (Task_Log)

| Field | Type | Definition and capture rule |
|---|---|---|
| `Participant_ID` | Text | P01 to P05. Never a name. |
| `Task_ID` / `Task_Order` | Text / Int | T1 or T2; 1 or 2 within the session. |
| `Start_Timestamp` | hh:mm:ss | Moment the moderator says **"Begin."** |
| `M1_Time`, `M2_Time`, `M3_Time` | hh:mm:ss | **Sub task milestones** (defined below). Left blank if never reached. |
| `End_Timestamp` | hh:mm:ss | **Terminal user action:** participant says "Done", says they give up, or the 300 s cap is reached. |
| `M1_sec` to `M3_sec` | Int (formula) | Seconds from Start to each milestone. Shows *where* in the flow time is lost. |
| `Task_Time_sec` | Int (formula) | End minus Start in seconds. The timer is never paused for think aloud or prompts. |
| `Task_Success` | 1 / 0.5 / 0 | **1** independent completion at the correct end state. **0.5** correct end state reached after an assist prompt (A1 or A2). **0** terminal failure: wrong end state, gave up, timed out, or stopped for wellbeing (R2). |
| `Assist_Count` | Int | Number of A level prompts given. |
| `Nav_Missteps`, `Dead_Clicks`, `Input_Errors` | Int (formula) | Counted automatically from Error_Log by code. |
| `Error_Count` | Int (formula) | Nav_Missteps + Dead_Clicks + Input_Errors. System faults are excluded. |
| `System_Faults` | Int (formula) | SYS rows from Error_Log, kept separate so portal problems are not blamed on the user. |
| `SEQ_Rating` | 1 to 7 | Single Ease Question answer, captured right after the task. |
| `Integrity_Flag` | Text (formula) | Turns red when the row breaks a protocol rule (see 3.4). |

**Failure criteria (any one means Task_Success = 0)**
- Participant says "Done" but the success end state in Section 1.3 is not on screen (for example, a Monday/Wednesday section, or a full section).
- Participant says they would give up and declines to continue.
- Timer reaches 300 seconds.
- Task stopped for participant wellbeing or to protect their real account.

### 3.2 Sub task milestones

| Task | M1 | M2 | M3 |
|---|---|---|---|
| T1 | Search results listing CS 4110 sections are on screen | A Tuesday/Thursday section with open seats is chosen | Final confirmation or registered status is on screen |
| T2 | Current term schedule is on screen | The removal action for the placeholder course is chosen | Confirmation that the course is no longer registered |

The gaps between milestones split each task into phases. For example, if M2 minus M1 is large for most participants, the results table is the bottleneck, which matches the Phase 1 heuristic finding about dense results.

### 3.3 Automated error categorization (Error_Log)

The moderator logs each error as it happens with three quick entries: participant, task, time, and a code from a dropdown. The workbook does the rest.

| Code | Category | Counts as user error | Definition |
|---|---|---|---|
| NAV | Navigational misstep | Yes | Opens a page, tab, panel, or menu off the success path and must back out |
| DEAD | Dead click | Yes | Clicks or taps something non interactive, or a control with no visible response |
| INPUT | Input error | Yes | Wrong typed or selected value, or triggers a validation error |
| SYS | System fault | No | Portal error, timeout, or crash not caused by the participant |

Each Error_Log row automatically gets its category name, whether it counts as a user error, and **seconds since task start** (looked up from the matching Task_Log row through a `Participant|Task` key). Task_Log counts each category with `COUNTIFS`, so the moderator never tallies by hand. Each error also gets a Nielsen severity rating (1 cosmetic to 4 catastrophic) and the screen or element where it happened, which feeds the redesign priority list.

**Counting rules:** count each misstep once (clicking the same dead spot three times in a row is one error). If the participant says they're just exploring, or uses a different path that still works, it isn't an error.

### 3.4 Built in integrity checks

| Check | Rule it enforces |
|---|---|
| "assist given, success cannot be 1" | Any A prompt caps success at 0.5 |
| "hit 300 s cap, success must be 0" | Timeouts are failures |
| "milestones out of order" | Catches typing mistakes in timestamps |
| "SEQ missing" | Every scored task needs its SEQ |
| SUS "same answer on all 10" | Flags straightlining |
| SUS "agreed with opposite items" | Flags agreeing (4 or 5) with both items 1 and 3 and items 2 and 4, a contradictory pattern |

Dropdowns restrict Task_Success to 1, 0.5, 0; SEQ to 1 to 7; SUS ratings to whole numbers 1 to 5; and error codes to the four defined codes.

### 3.5 Qualitative observation fields

| Field | What to record | Example |
|---|---|---|
| `Facial_Expressions` | Visible expression with timestamp. Describe, don't interpret. | "Frown and brow raise at 14:06:02 when results loaded" |
| `Verbalized_Friction` | Direct quotes in double quotes, with timestamp | "\"Wait, where's the seat count?\" (14:06:20)" |
| `Physical_Hesitation` | Cursor hovering or circling, long pauses with no input, hand off mouse | "Cursor hovered over results table about 8 s" |
| `Ergonomic_Posture` | Leaning in, squinting, sitting back, rubbing eyes, zoom changes | "Leaned toward screen; pressed Ctrl + to zoom" |
| `Moderator_Prompts_Used` | Codes from the prompt bank and recovery scripts | "N1, N1, A1, R1" |
| `Notes` | Anything else, including protocol deviations | "Portal timed out at 2:40; reloaded, timer kept running" |

Timestamps in the qualitative fields line up with Error_Log times and milestones, so a quote like "Where's the seat count?" can be placed in the M1 to M2 phase next to the dead clicks that happened at the same moment.

### 3.6 Single Ease Question (SEQ) card

**Overall, how easy or difficult was this task to complete?**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| Very Difficult | | | | | | Very Easy |

### 3.7 Planned analysis (for the statistics sprint)

The Summary tab gives a first look at completion rate, average time, errors, SEQ, and SUS for each task. The detailed stats (confidence intervals, geometric mean of task times) will be done in the upcoming statistics sprint.

---

## Step 4: System Usability Scale (SUS) Instrument

### 4.1 Deployment

The questionnaire is `docs/index.html`, a single self contained HTML page with no external dependencies. It is hosted by GitHub Pages:

1. Push this repository to GitHub as a **public** repository.
2. Go to **Settings > Pages**. Under *Build and deployment*, set Source to **Deploy from a branch**, Branch to **main**, and Folder to **/docs**. Save.
3. After about a minute the live URL appears at the top of the Pages settings: `https://<username>.github.io/<repo-name>/`. Put that URL at the top of this README.

Responses are kept in the browser on the moderator's test laptop (no server, so no participant data leaves the device). After each participant the moderator opens *Moderator view* and downloads the CSV (raw ratings plus score, percentile, grade, and adjective), then copies the ratings into the `SUS_Responses` tab of the logging workbook.

### 4.2 The 10 items (John Brooke, 1996, unaltered)

Every item uses the same 5 point scale: **1 = Strongly Disagree** to **5 = Strongly Agree**. Wording and order are canonical; the positive and negative polarity alternates.

| # | Item | Polarity |
|---|---|---|
| 1 | I think that I would like to use this system frequently. | Positive |
| 2 | I found the system unnecessarily complex. | Negative |
| 3 | I thought the system was easy to use. | Positive |
| 4 | I think that I would need the support of a technical person to be able to use this system. | Negative |
| 5 | I found the various functions in this system were well integrated. | Positive |
| 6 | I thought there was too much inconsistency in this system. | Negative |
| 7 | I would imagine that most people would learn to use this system very quickly. | Positive |
| 8 | I found the system very cumbersome to use. | Negative |
| 9 | I felt very confident using the system. | Positive |
| 10 | I needed to learn a lot of things before I could get going with this system. | Negative |

**Administration rules**
- Give the SUS once, after **all** tasks are finished, never between tasks.
- All 10 items must be answered. The form will not submit with blanks. (If a paper backup is used and an item is skipped, Brooke's guidance is to record the scale midpoint, 3.)
- The moderator steps away while it is completed and does not look at answers in front of the participant.
- "System" is not reworded; the participant is told before starting that it means the class registration website.

### 4.3 Scoring algorithm blueprint

Raw responses (1 to 5) are normalized into a 0 to 100 benchmark score in three steps.

**Step A: per item score contribution (each ranges 0 to 4)**

```
For odd numbered items (1, 3, 5, 7, 9):    Contribution = User Rating - 1
For even numbered items (2, 4, 6, 8, 10):  Contribution = 5 - User Rating
```

The odd items are positively worded, so agreeing is good and a 5 becomes 4. The even items are negatively worded, so agreeing is bad and the score is reversed: a 1 (strongly disagree that it was complex) becomes 4.

**Step B: sum the contributions** (range 0 to 40)

**Step C: scale to 0 to 100**

```
SUS = (Sum of all 10 Score Contributions) x 2.5
```

**Pseudocode**

```text
function sus_score(r[1..10]):
    require every r[i] is an integer in 1..5
    total = 0
    for i in 1..10:
        if i is odd:  total += r[i] - 1
        else:         total += 5 - r[i]
    return total * 2.5
```

**Spreadsheet formula** (ratings in B2:K2, as used in the `SUS_Responses` tab)

```text
Odd item contribution:  =IF(B2="","",B2-1)
Even item contribution: =IF(C2="","",5-C2)
SUS:                    =SUM(L2:U2)*2.5
```

**Worked example** (the example row in the workbook)

| Item | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Raw rating | 4 | 2 | 4 | 1 | 4 | 2 | 5 | 2 | 4 | 2 |
| Rule | r minus 1 | 5 minus r | r minus 1 | 5 minus r | r minus 1 | 5 minus r | r minus 1 | 5 minus r | r minus 1 | 5 minus r |
| Contribution | 3 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 3 |

Sum = 32. SUS = 32 x 2.5 = **80.0**

### 4.4 From raw score to benchmark: percentile curve, grade, adjective, acceptability

A raw SUS score is **not a percentage**. A 68 sounds like a D but is actually the average across hundreds of studies. To make scores meaningful, both the survey and the workbook convert the score four ways automatically:

| Conversion | Method | Where it is computed |
|---|---|---|
| **Percentile rank** | Normal approximation of the Sauro and Lewis benchmark database: `Percentile = NORMDIST(SUS, 68, 12.5, TRUE) x 100` | Survey result screen, `SUS_Responses` tab, Summary tab |
| **Curved grade** | Sauro and Lewis curved grading scale (table below) | Survey and workbook |
| **Adjective rating** | Bangor, Kortum, and Miller adjective bands | Survey and workbook |
| **Acceptability** | Bangor, Kortum, and Miller: below 50 not acceptable, 50 to 69.9 marginal, 70 and above acceptable | Survey, workbook |

**Lookup table used everywhere** (also in the `SUS_Benchmarks` tab)

| SUS score | Curved grade | Percentile range | Adjective |
|---|---|---|---|
| 84.1 to 100 | A+ | 96 to 100 | Excellent |
| 80.8 to 84.0 | A | 90 to 95 | Good |
| 78.9 to 80.7 | A- | 85 to 89 | Good |
| 77.2 to 78.8 | B+ | 80 to 84 | Good |
| 74.1 to 77.1 | B | 70 to 79 | Good |
| 72.6 to 74.0 | B- | 65 to 69 | Good |
| 71.1 to 72.5 | C+ | 60 to 64 | OK |
| 65.0 to 71.0 | C | 41 to 59 | OK |
| 62.7 to 64.9 | C- | 35 to 40 | OK |
| 51.7 to 62.6 | D | 15 to 34 | OK |
| 25.0 to 51.6 | F | 1 to 14 | Poor |
| 0 to 24.9 | F | 0 | Worst imaginable |

**Worked example continued:** SUS 80.0 gives percentile = NORMDIST(80, 68, 12.5) = 0.831, so **83rd percentile**, grade **A-**, adjective **Good**, **Acceptable**. The system in this example would be more usable than about 83% of systems in the benchmark.

**Reporting rules**
- Individual item scores are not interpreted on their own; the SUS is validated as an overall measure.
- With 5 participants, always report the mean with its 95% confidence interval and say plainly that it is wide.
- The percentile is an approximation of a skewed real distribution; it is most accurate between about 40 and 90.

I checked that the survey and the workbook both give 80.0 (83rd percentile, A-) for the worked example, so the scoring matches in both places.

---

## Step 5: Accessibility First Survey and Environment Audit

### 5.1 WCAG 2.1 AA instrument compliance

Each required criterion was built into `docs/index.html` and then checked. The method for each check is listed so it can be repeated.

| Requirement | WCAG SC | How the instrument meets it | Verified by | Result |
|---|---|---|---|---|
| Explicit programmatic labels | 1.3.1, 3.3.2, 4.1.2 | Every radio has a `<label for="qN-V">` that matches its `id`. Each item is a `<fieldset>` whose `<legend>` holds the full statement, so a screen reader announces "I found the system unnecessarily complex, group, 2 out of 5, radio button." The Participant ID field uses `<label for="participant-id">`. | Automated browser test: 0 of 51 inputs lack a matching `label[for]`. Screen reader pass (NVDA or VoiceOver) to be done in the pilot session | Pass |
| Keyboard arrow navigation in the radio matrix | 2.1.1 | Native `<input type="radio">` controls that share one `name` per item, so Tab moves between statements (one tab stop per item) and arrow keys change the rating within a statement. No custom JavaScript key handling to break. Radios are visually hidden but not `display:none`, so they stay focusable. | Automated keyboard test: Space selects 1, two Right Arrow presses move the selection to 3, Tab moves to item 2 | Pass |
| Visible focus ring | 2.4.7 | `:focus-visible` draws a 4 px solid #492365 outline offset 3 px around the focused rating card, plus a white halo so it shows on any background. Same style on text input, buttons, links, and the error summary. | Computed style on focus is a 4 px solid outline; no horizontal scroll at a 320 px wide viewport (equivalent to 400% zoom) | Pass |
| Text contrast of at least 4.5:1 | 1.4.3 | Body text #1B1B1B on #FFFFFF is 17.2:1. Hint text #474747 on white is 9.3:1. Selected rating white on #492365 is 12.3:1. Error text #A4161A on white is 7.7:1. Control borders #6B6B6B on white are 5.3:1, which also meets non text contrast (1.4.11, 3:1). | Ratios calculated with the WCAG relative luminance formula (re-check with WebAIM Contrast Checker) | Pass |
| Dynamic error prompts announced | 3.3.1, 4.1.3 | On submit with blanks, an error summary with `role="alert"` appears, receives focus, and lists each unanswered item as a link that jumps to it. Each item also has its own message in a `<p aria-live="polite">` tied to its radios with `aria-describedby`, so the error is read when the user reaches that item. Errors clear as soon as the item is answered. | Automated test: submitting a blank form shows the `role="alert"` summary, moves focus to it, and fills each item's error text. Confirm announcement with a screen reader in the pilot | Pass |

**Additional checks beyond the required four**

| Check | SC | Implementation |
|---|---|---|
| Page language | 3.1.1 | `<html lang="en">` |
| Descriptive page title | 2.4.2 | "System Usability Scale (SUS) Questionnaire, Weber State Class Registration Study" |
| Bypass blocks | 2.4.1 | Skip link to the questionnaire as the first focusable element |
| Reflow and resize | 1.4.4, 1.4.10 | Relative units and a responsive grid; no horizontal scroll at 320 CSS px or at 400% zoom |
| Target size | 2.5.5 (AAA, exceeded) | Each rating option is a full card at least 44 by 68 px, not a tiny radio dot |
| Not color alone | 1.4.1 | Selected option also shows the word "Selected"; invalid items get a thicker border and a text message, not just red |
| Status messages | 4.1.3 | Score result region uses `role="status"`; results heading receives focus after submit |
| Reduced motion | 2.3.3 | `prefers-reduced-motion` respected (no animation is used) |

### 5.2 Automated audit

I ran Lighthouse (Chrome DevTools) and the axe accessibility checker on the survey. Lighthouse gave an accessibility score of 100, and axe found 0 violations, including after submitting a blank form so the error messages were showing. The first axe run caught a skip link that pointed to the form after it was hidden, so I pointed it at the main content instead. Automated tools don't catch everything, so I'll also do a quick screen reader and keyboard only check during the pilot session.

### 5.3 Rating matrix design

Instead of putting the 10 items in a table, each statement is its own `<fieldset>` with a `<legend>` and one group of native radio buttons, laid out in a row so it still looks like a matrix. That way Tab goes to each statement once, the arrow keys change the rating, and a screen reader reads the full statement instead of a table cell position. The focus ring is a thick purple outline so keyboard users can always see where they are, and on small screens or high zoom the options stack vertically so nothing gets cut off.

### 5.4 Test environment audit (physical and procedural)

| Area | Check before each session |
|---|---|
| Assistive technology | Participant uses their own AT and settings. If they bring a device, the session runs on it. Moderator asks "Is there anything about the setup you'd like changed?" before the practice task. |
| Task cards | Printed at 16 pt, high contrast black on white; digital copy available for screen reader users and read aloud for everyone. |
| SEQ card | Printed large print; may also be answered verbally. |
| Seating and ergonomics | Adjustable chair, monitor at eye level, external mouse and keyboard available, lighting without glare on the screen. |
| Room | Quiet, door closed, phone notifications off on the test laptop, no other people watching from the participant's line of sight. |
| Timing | Breaks allowed any time; timer keeps running during a task but a participant initiated break ends the task early and is noted. |
| Privacy | Test laptop browser is in a fresh profile; previous participant's survey downloaded and cleared; recording saved to the encrypted drive before the next session starts. |

---

## Post Mortem Reflection

### Q1. Why does the SUS deliberately alternate between positive and negative phrasing across its 10 items, and what cognitive response bias does this structure safeguard against?

**The short answer.** Brooke alternated the wording so participants cannot get through the questionnaire on autopilot, and so a common response bias cancels itself out in the final score. The main bias it protects against is **acquiescence bias** (also called yea saying or agreement bias): the tendency to agree with statements whatever they say.

**Why acquiescence is a real threat in usability testing.** Acquiescence gets stronger when people are tired, when they don't care much about the questions, and when they feel social pressure to be agreeable. All three are present at the end of a usability session. The participant has just spent half an hour with a friendly moderator, may assume the moderator built the system, and is filling out the last form before leaving. If all ten statements were positive ("easy to use," "well integrated," "confident"), agreeing with everything would push the score toward 100 and make the system look better than it is, and there would be no way to tell polite agreement from real satisfaction.

**How the alternation works, in measurement terms.** The SUS is a summated rating scale: the ten items are added together because they are all supposed to measure the same underlying thing, perceived usability. Every answer is a mix of that real attitude and some noise, including a person's habit of agreeing. In an all positive scale, that agreeing habit pushes every item in the same direction, so it adds up instead of averaging out. It even makes the scale look more reliable than it is, because the items agree with each other partly for the wrong reason. With balanced keying, half the items are reverse scored. A participant's extra tendency to agree adds points on the five positive items and takes the same number away on the five negative items, so in the total it mostly cancels out. What is left is closer to the real attitude.

The same structure also protects against two related patterns:
- **Straightlining** (answering the same column all the way down). With reverse scoring, all 5s produce a SUS of 50, not 100, and all 1s also produce 50. A straightliner lands at "Poor" instead of artificially high or low, and the pattern is easy to spot.
- **Extreme response style** (only using 1s and 5s). Because extremes on positive and negative items cancel, this style can't inflate the score on its own.

**It also works as an attention check.** Someone who strongly agrees that the system was "easy to use" (item 3) and also strongly agrees it was "unnecessarily complex" (item 2) is giving contradictory answers. That flags the response for review.

**The tradeoff and how this protocol handles it.** Mixed wording has a cost. Sauro and Lewis (2011) compared the standard SUS with an all positive version and found the scores were about the same, but the mixed version led to two kinds of mistakes. Some participants **miss the switch** and answer a negative item as if it were positive. Some researchers **forget to reverse score** the even items, which produces badly wrong results. This protocol keeps the canonical alternating version because the published benchmarks (68 average, the percentile curve, grades) were built on it, and changing the wording would break that comparison. It handles the costs this way:

1. **Participant miscoding:** the survey instructions ask people to read every statement, and each item is shown on its own with its full text as the group label, so it is hard to skim.
2. **Researcher miscoding:** no one scores by hand. Reverse scoring is coded in two places (the survey and the workbook), and both produce 80.0 for the worked example, so a mismatch would expose a bug.
3. **Detection:** the workbook flags straightlining and contradictory agreement automatically, and the raw ratings (not just the final score) are exported so any flagged response can be checked.

**Front end data integrity.** Psychometric validity depends on the data reaching the spreadsheet unchanged, so the form was designed to protect it:
- Native radio buttons can only hold the values 1 to 5. Out of range values, typos, and half answers are impossible.
- The form will not submit with a blank item, so no missing data has to be filled in later with guessed midpoints.
- The participant ID field asks for a code, not a name, so no identifying information ends up in the response file.
- Every record gets an ISO timestamp, which can be matched to the session log.
- The CSV export contains the raw ratings, so any score can be recalculated and checked.
- Responses are saved in the browser and can be re-downloaded. If local storage is blocked, the page tells the moderator to download right away so nothing is lost.

**Self critique.** The alternating structure reduces acquiescence but can't remove social desirability bias completely, especially since participants may know a student is behind the study. Stepping away while the SUS is filled in helps. A stronger fix would be to have participants complete the SUS on a separate device with the moderator out of the room. With only 5 participants, one person who misreads a negative item can move the mean a lot, so flagged responses need to be reviewed, not just counted.

### Q2. How can a moderator's subtle verbal cues or body language during a Think Aloud session corrupt time on task and error count data, and how does this protocol prevent that bias?

**Why it happens.** A participant in a think aloud session is in an uncertain situation, being watched while working on an unfamiliar system, so they constantly look for clues about how they are doing. Psychology has names for this. **Demand characteristics** (Orne, 1962) are the cues that tell a participant what behavior is expected. The **experimenter expectancy effect** (Rosenthal) describes how a researcher who expects a result can produce it without meaning to. The classic example is **Clever Hans**, the horse that seemed to do arithmetic but was actually reading tiny, unconscious changes in his trainer's posture when he reached the right answer. A moderator who knows where the "right" button is plays the trainer's role.

**What the cues look like.**
- **Verbal:** an "mm hmm" or "okay" when the participant moves toward the right link; a pause or "hmm" when they head the wrong way; follow up questions only after mistakes ("Why did you click that?"); a slightly different tone when reading the task card to different people.
- **Nonverbal:** leaning forward as the participant gets close; glancing at a part of the screen; shifting in the chair or sighing during a wrong path; writing notes only after errors; where the moderator's eyes rest.
- **Timing:** rescuing too soon, filling a silence, or giving help at different points for different people.

**How each metric gets corrupted.**
- **Time on task** gets shorter than it should when participants skip exploration they would have done alone because a cue pointed the way. It gets longer when they stop to check the moderator's face or ask for approval. Either way, the variation comes from the moderator, not the interface.
- **Error count** goes down because participants back out of wrong paths *before* committing, when they notice disapproval. The missteps real users would make never get logged, so the real problems become invisible.
- **Task success** gets inflated, since a task finished thanks to an accidental hint is logged as independent (1) instead of assisted (0.5).
- **SEQ and SUS** get inflated too, because a participant who felt guided rates the task as easier, and one who wants to please the moderator rates the system more kindly.

The result is a system that looks more usable than it is. That is the worst outcome for a benchmark that a redesign will be compared against: an inflated baseline makes the redesign look less effective than it really is.

**How this protocol prevents it.**
1. **Everything said is scripted.** The moderator may only use the neutral prompts (N1 to N5), assist prompts (A1, A2), and recovery scripts (R1 to R3), word for word. None of them name a menu, button, or direction, and every participant hears the same thing.
2. **Rules decide when to speak, not judgment.** N1 only after 15 seconds of silence; assists only after 120 seconds with no progress or when the participant would give up. The moderator never decides in the moment that someone "needs a little help."
3. **Help is measured, not hidden.** Any assist automatically caps Task_Success at 0.5, every prompt is logged by code, and the workbook flags any row where an assist was given but success was marked 1. The timer is never paused.
4. **Acknowledgements only after "Done."** "Thank you" and "Okay" are said in the same flat tone, and only after the participant ends the task.
5. **Seating, hands, and notes.** The moderator sits behind and to the side, out of the participant's view, keeps hands away from the screen, and logs constantly (milestones, error codes, timestamps). Because writing never stops, a burst of note taking doesn't signal "you just made a mistake."
6. **Expectations set up front.** The CTA briefing tells participants the moderator will stay quiet and can't answer questions, so silence isn't read as disapproval and participants spend less effort reading the moderator.
7. **Task cards don't give away labels.** The cards avoid the interface's own words ("Add," "Drop," "Search"), so the wording itself isn't a cue.
8. **Objective start and stop points.** The timer starts on "Begin" and stops at a defined terminal action or the 300 second cap, so the moderator can't stretch or shrink a task. Milestones are defined by what is on screen, not the moderator's impression.
9. **Practice task.** The unlogged library hours task lets participants learn to think aloud before the timed tasks, so the first real task isn't slower just from learning the method.
10. **Checks on the moderator.** One pilot session is run with a non participant, and a second team member reviews a sample of recordings for any unscripted cues before the data goes to the stats sprint.

**Self critique and remaining risks.**
- **I am a biased moderator.** I ran the Phase 1 audit and the Lab 03 cognitive audit on this exact system, so I know where the problems are and I *expect* participants to struggle on the results table. That is exactly the setup for expectancy effects. The best fix is to have a teammate who hasn't studied the portal moderate while I only take notes. If that isn't possible, the recording review in step 10 matters even more.
- **The N1 prompt is itself an intervention.** Asking "What are you thinking right now?" breaks concentration and adds a few seconds. It is the same for everyone and it is logged, but participants who go quiet more often get prompted more, and that adds time. The stats sprint can check whether N1 counts relate to task time.
- **Think aloud changes behavior.** Talking while working slows people down and can make them more careful, which may lower error counts compared with silent use. Times from this study are comparable across participants and with a future redesign tested the same way, but not with times from silent tests.
- **The live portal adds noise the moderator can't control:** seat counts change between sessions, and the portal can time out. Logging SYS faults separately keeps those from being counted against participants, but a sandbox term would be better.

---

## Appendix A: Session Run Sheet

| Time | Step | Moderator action |
|---|---|---|
| T minus 15 min | Setup | Fresh browser profile, test account signed in (or placeholder class added for T2), recording software ready but off, logging sheet open on a second device, task cards in order for this participant |
| 0:00 | Welcome and briefing | Read Section 2.1 word for word |
| 0:04 | Consent | Consent form signed; start recording and state code and date |
| 0:06 | Think aloud instructions | Read Section 2.2 |
| 0:08 | Practice task | Library hours task, not logged |
| 0:10 | Task A (T1 or T2 per order) | Read card, say "Begin", log start time; log milestones and each error in Error_Log as they happen; prompts only from bank; log end time; ask SEQ |
| 0:17 | Task B | Same as Task A |
| 0:24 | SUS | Open live survey, enter participant code, step away |
| 0:27 | Debrief | Follow the Section 2.7 debrief steps; stop recording |
| 0:30 | After participant leaves | Download SUS CSV; finish qualitative notes while fresh; move recording to encrypted drive; clear browser |

## Appendix B: References

- Brooke, J. (1996). SUS: A "quick and dirty" usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, and I. L. McClelland (Eds.), *Usability Evaluation in Industry* (pp. 189 to 194). Taylor and Francis.
- Bangor, A., Kortum, P., and Miller, J. (2009). Determining what individual SUS scores mean: Adding an adjective rating scale. *Journal of Usability Studies, 4*(3), 114 to 123.
- Sauro, J., and Lewis, J. R. (2011). When designing usability questionnaires, does it hurt to be positive? *Proceedings of CHI 2011*, 2215 to 2224.
- Sauro, J., and Dumas, J. S. (2009). Comparison of three one question, post task usability questionnaires. *Proceedings of CHI 2009*, 1599 to 1608.
- W3C. (2018). *Web Content Accessibility Guidelines (WCAG) 2.1*. https://www.w3.org/TR/WCAG21/
- Bangor, A., Kortum, P. T., and Miller, J. T. (2008). An empirical evaluation of the System Usability Scale. *International Journal of Human Computer Interaction, 24*(6), 574 to 594.
- Ericsson, K. A., and Simon, H. A. (1993). *Protocol Analysis: Verbal Reports as Data* (rev. ed.). MIT Press.
- Orne, M. T. (1962). On the social psychology of the psychological experiment. *American Psychologist, 17*(11), 776 to 783.
- Rosenthal, R. (1966). *Experimenter Effects in Behavioral Research*. Appleton Century Crofts.
- Sauro, J., and Lewis, J. R. (2016). *Quantifying the User Experience* (2nd ed.). Morgan Kaufmann.

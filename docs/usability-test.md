# Usability Test Kit

This is how we checked whether the redesign actually fixes the usability issues it targets. Each participant tries the same tasks on the **current Student Center** and on **our prototype**. We record time, errors, and a System Usability Scale (SUS) score for each version.

Plan for 5 participants. Nielsen's guideline is that 5 users surface most usability problems, and that's enough for a class project.

## Who to recruit

- CSULB students who have used the Student Center to enroll at least once
- Not on our team, and not CECS 448 students if possible, since they know the design principles
- A mix of majors and class years if you can

## Setup

- One facilitator reads the script and the tasks. One note-taker runs a stopwatch and logs errors.
- Prototype: open `index.html`, or the GitHub Pages link. Set **Design notes → Demo clock** to *Tue Nov 3, 9:15 AM* so every participant sees the same state (next class: CECS 475 in ECS 404 at 9:30). Turn Design notes off before the participant starts. Reload the page between participants to reset the cart.
- Current system: use the real Student Center, logged in as a team member. Don't enroll in or drop anything. Before each session, check the real Spring 2027 schedule and set up the cart so T3 and T4 work the same way: pick a real Spring class to search for in T3, and pre-load a real section that meets at the same time, so adding it creates a conflict. If CECS 450 isn't offered in Spring, swap in any class that is and use it on both versions.
- Alternate the order. Participants 1, 3, and 5 start on the current system; participants 2 and 4 start on the prototype. That keeps learning effects from favoring either version.

## Script (read aloud)

> We're testing two versions of the Student Center, not testing you. There are no wrong answers. Please think out loud as you go. I can't help during a task, but you can give up at any time. Each task has a 2-minute limit.

## Tasks

| # | Task (read exactly) | Success means | Issue it tests |
|---|---|---|---|
| T1 | "Find the date you can start enrolling for Spring 2027." | Says "November 5" | Buried enrollment appointment (#4) |
| T2 | "Where and when is your next class?" | Names the correct class, room, and time | No "today" view (#7), time as text (#11) |
| T3 | "Search for CECS 450, Data Visualization, and add it to your shopping cart." | Class is in the cart | Two search entry points (#1) |
| T4 | "Is there anything in your cart that would stop you from enrolling? If so, fix it." | Removes one of the two overlapping classes (prototype: CECS 428 or CECS 450) | Late conflict detection (#8) |
| T5 | "When is the last day to withdraw from CECS 448?" | Says "November 20" | Deadlines behind identical icons (#6) |
| T6 | "Do you have any unread messages?" | Correct yes/no and count | No unread indicator (#9) |

On the current system, T3 and T4 stop at the shopping cart. Don't validate or enroll.

## What to record per task

- **Time on task** in seconds, from finishing reading the task to the participant's answer
- **Success**: 1 = completed, 0.5 = completed with a hint or a wrong first answer, 0 = gave up or timed out
- **Errors**: wrong clicks that lead to the wrong page, plus wrong answers
- **Quotes**: anything said out loud that shows confusion or delight

## SUS questionnaire

Ask after each version. Score each item 1 (strongly disagree) to 5 (strongly agree).

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

**Scoring:** For odd items, take score − 1. For even items, take 5 − score. Add the ten results and multiply by 2.5 to get 0–100. 68 is the commonly cited average.

## Results template

Copy this into a spreadsheet or fill it in here. The averages go on the **Evaluation** slide.

| Participant | Order | Version | T1 s | T2 s | T3 s | T4 s | T5 s | T6 s | Successes (of 6) | Errors | SUS |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Current first | Current | | | | | | | | | |
| P1 | | Prototype | | | | | | | | | |
| P2 | Prototype first | Current | | | | | | | | | |
| P2 | | Prototype | | | | | | | | | |
| P3 | Current first | Current | | | | | | | | | |
| P3 | | Prototype | | | | | | | | | |
| P4 | Prototype first | Current | | | | | | | | | |
| P4 | | Prototype | | | | | | | | | |
| P5 | Current first | Current | | | | | | | | | |
| P5 | | Prototype | | | | | | | | | |
| **Average** | | **Current** | | | | | | | | | |
| **Average** | | **Prototype** | | | | | | | | | |

## After testing

- Note any task where the prototype did **not** clearly beat the current system. That goes in the self-reflection, and it shows growth.
- If a participant struggled with something in the prototype, fix it, then say on the slides what changed and why. One change made in response to testing is the clearest evidence of user-centered design you can show.

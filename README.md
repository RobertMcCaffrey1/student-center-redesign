# CSULB Student Center Redesign

CECS 448 User Interface Design · Fall 2026 · Project 2: User-Centered Design

A clickable front-end prototype that redesigns the CSULB Student Center home page. It targets specific usability problems in the current page and ties each fix to a design principle from the course.

## How we guided our design decisions

The assignment asks how to guide design when the possibilities are essentially endless. We ran every idea through five filters, in order:

1. **Users and tasks.** Who uses the page, and which four tasks they come to do. Ideas that didn't help a task were cut.
2. **Evidence of problems.** A heuristic evaluation against Nielsen's 10 heuristics, with each issue rated for severity.
3. **Principles as tie-breakers.** For each issue we listed the possible fixes and chose the one that best satisfied the violated principle without breaking another.
4. **Keep what works.** CSULB's colors and the Student Center's own terms stayed, so returning students don't relearn the page.
5. **Test, then change.** The same tasks run on both versions with real students ([test kit](docs/usability-test.md)).

The full reasoning, including the options we rejected for each of the 11 issues, is in **[DESIGN.md](DESIGN.md)** and in the prototype under **Design notes** (bottom-left, or press **N**).

## Assignment checklist

| Requirement | Where it is covered |
|---|---|
| 1. GitHub link to runnable code | This repository. Open `index.html`, no build step |
| 2. Demo of the prototype | Live, using the [demo guide](#demo-guide) below. Record a backup video too |
| 3. Usability issues addressed | [The problem](#the-problem) table below; severity ratings in [DESIGN.md](DESIGN.md#severity-summary) |
| 3. How user-centered design was executed | [DESIGN.md](DESIGN.md#how-we-narrowed-the-options) and [usability test kit](docs/usability-test.md). **Run the test and add results** |
| 3. Design principles and guidelines applied | Every decision record in [DESIGN.md](DESIGN.md#decision-records) names its principles |
| 4. Class topics that guided decisions | Nielsen's heuristics, Norman's design principles (signifiers, mapping, feedback, constraints), Gestalt proximity, progressive disclosure, usability testing with SUS |
| 5. Self-reflection and project management | Presentation slides. Fill in the [Team](#team) table below |
| Rationale behind each interaction feature | "Options weighed" and "Why" in each decision record |
| Demo runs without error | Single file, no dependencies besides Google Fonts, tested in Chromium |

## Run it

No install or build step is needed.

1. Download or clone this repository.
2. Open `index.html` in any modern browser (Chrome, Firefox, Safari, Edge).

The only external resource is Google Fonts. Without an internet connection the page falls back to system fonts and still works.

To get a live link, turn on GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / root**. The prototype will then be at `https://<username>.github.io/<repo-name>/`.

## The problem

![Original Student Center](docs/before.png)

| # | Usability issue in the original | Fix in the prototype | Principle |
|---|---|---|---|
| 1 | Two search entry points (gold "Search for Classes" button and a "Search" menu link) with no hint of how they differ | One search field in the header finds both classes and pages. Press `/` to focus it | Consistency and standards; flexibility and efficiency of use |
| 2 | Hamburger icons hide menus that repeat links already on the page | Five labeled tabs that are always visible, with the current page marked | Recognition rather than recall; signifiers |
| 3 | Full panels used to say "No Holds." and "No To Do's." | One row of status chips. A chip only turns gold when it needs action | Aesthetic and minimalist design; visibility of system status |
| 4 | The Nov 5 enrollment appointment is a paragraph at the bottom of the sidebar | Countdown plus a three-step timeline, with the next action as the primary button | Visibility of system status; match with the real world |
| 5 | Course codes only, "SEM" abbreviation, unexplained "URL" label | Course titles under each code, "Seminar" spelled out, jargon removed | Match between system and the real world |
| 6 | An identical calendar icon on every class row. You had to click each one to learn anything | The next deadline is written on each row. Expand a row for the full list | Recognition rather than recall; progressive disclosure |
| 7 | Static table sorted by course code | "In class now / Up next" card with the room and time remaining | Task priority; visibility of system status |
| 8 | Time conflicts only appear when you validate or enroll | The cart flags overlaps the moment a class is added and shows them on a mini calendar. Enroll states when it unlocks | Error prevention; help users recover from errors |
| 9 | "View My Messages" looks the same whether or not anything is new | Unread badge on the inbox icon and the Messages tab | Visibility of system status |
| 10 | One flat menu mixes planning, enrollment, and textbooks | Shortcuts grouped under Plan, Change my classes, and Money | Gestalt proximity; information architecture |
| 11 | Meeting times shown only as text | Weekly calendar with today highlighted and a current-time line | Match between system and the real world |

## Demo guide

Click **Design notes** in the bottom-left corner (or press **N**) to show numbered pins on each fix. The side panel has two tabs. **How we decided** walks through the five filters and has a button to view the original page. **Decisions** shows, for each pin, the user need, the problem, its severity, the options we weighed, and why we chose the one we built. Click a pin to open its decision, or click **Show on page** in a decision to jump to the fix.

The **Demo clock** at the top of the notes panel sets the time, so a live demo can show "In class now" or the enrollment day regardless of when you present.

Suggested flow for the error-prevention fix:

1. Type `450` in the search box and click **Add** on CECS 450.
2. The cart flags a time conflict with CECS 428 and highlights both on the mini calendar.
3. Click **Check my cart**. It reports that the cart isn't ready until the conflict is fixed.
4. Click **Preview Nov 5** to unlock Enroll, then click **Enroll**. Enrollment is blocked and nothing changes.
5. Remove one of the conflicting classes and enroll again. It succeeds, CECS 491B stays in the cart, and **Undo** is available.

## Data

Fall 2026 course titles, meeting times, and rooms come from the [CSULB Fall 2026 CECS Schedule of Classes](https://web.csulb.edu/depts/enrollment/registration/class_schedule/Fall_2026/By_Subject/CECS.html). Deadlines, messages, and Spring 2027 sections are sample data for demonstration. There is no backend. All state resets on reload.

## Tech

A single HTML file with inline CSS and vanilla JavaScript. No frameworks or dependencies. It supports light and dark mode, works at phone width, and is fully keyboard operable.

## Team

| Member | Role / contributions |
|---|---|
| | |
| | |
| | |
| | |
| | |

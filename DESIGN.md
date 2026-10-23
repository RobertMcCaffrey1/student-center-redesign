# Design Rationale

> *"In a situation where the implementation possibilities are essentially endless, how do we guide our design process and decision-making?"*

Our answer: we didn't start from features. We started from the people using the page and the tasks they come to do. We found the problems with a structured evaluation, then used design principles to choose between possible fixes. We kept what already worked, and we test with students to check the result.

This document is generated from the same data the prototype shows in **Design notes**, so the two always match.

## How we narrowed the options

### 1. Start from users and their tasks

Who: an upper-division CSULB student planning next semester. Tasks: find when they can enroll, find their next class, build a Spring cart with no conflicts, and confirm nothing blocks them.

Ideas that help none of these tasks were cut, such as a chatbot, custom themes, and a GPA calculator.

### 2. Find problems with evidence, not taste

We ran a heuristic evaluation of the current page against Nielsen’s 10 usability heuristics and found 11 issues. Each got a severity rating from 0 (not a problem) to 4 (usability catastrophe).

Severity set the build order and how far each fix could go. High-severity issues got new features; low-severity ones got the lightest fix that works.

### 3. Use principles to choose between fixes

Most issues had several workable fixes. We wrote the options down and picked the one that best satisfied the violated principle without breaking another one.

Each decision card lists the options we weighed and why the others lost.

### 4. Keep what already works

We kept CSULB’s gold and black and the Student Center’s own terms, like Shopping cart and Enrollment appointment, so returning students don’t have to relearn the page.

Consistency applies to the system people already know, not only to the web at large.

### 5. Test with students, then change it

Both versions get the same six tasks with five students, measuring time on task, errors, and System Usability Scale (SUS) scores. The protocol is in docs/usability-test.md.

Changed after review so far: overlapping classes on the cart calendar were unreadable, so an overlap became one labeled block; the design notes button looked like part of the product, so it moved out of the header. [Add changes from user testing.]

## Severity summary

| # | Issue | Severity | Principles applied |
|---|---|---|---|
| 8 | Conflicts caught early | 4: Catastrophe | Error prevention; User control and freedom; Help users recognize and recover from errors |
| 4 | Enrollment timeline | 3: Major | Visibility of system status; Match between system and the real world |
| 6 | Deadlines in words | 3: Major | Recognition rather than recall; Progressive disclosure |
| 1 | One search box | 2: Minor | Consistency and standards; Recognition rather than recall; Flexibility and efficiency of use |
| 2 | Visible navigation | 2: Minor | Recognition rather than recall; Signifiers (Norman) |
| 5 | Plain language | 2: Minor | Match between system and the real world |
| 7 | Today first | 2: Minor | Visibility of system status; Task-centered design |
| 9 | Unread count | 2: Minor | Visibility of system status |
| 3 | Status at a glance | 1: Cosmetic | Aesthetic and minimalist design; Visibility of system status |
| 10 | Links grouped by task | 1: Cosmetic | Gestalt: proximity; Information architecture |
| 11 | Week view | 1: Cosmetic | Match between system and the real world; Mapping (Norman) |

Severity uses Nielsen's 0–4 scale and is our team's rating from the heuristic evaluation.

## Decision records

Each record shows the user need, the problem we found, the options we considered, and why the chosen option won.

### 1. One search box

- **User need:** Find a class or a page without knowing where it lives.
- **Problem:** A gold “Search for Classes” button and a “Search” link in the Academics menu, with no hint of how they differ.
- **Severity:** 2 (Minor)

**Options weighed**

- Keep both and label them, e.g. “Search classes” and “Search catalog”. Students still have to choose between two tools they can’t tell apart.
- Keep only the class search button. Pages like Textbooks stay hard to find.
- **Chosen:** One search box in the header for classes and pages, results grouped by type, with an Add button on each class.

**Why:** One way to do one thing. Grouped results keep classes and pages distinct, so nothing is lost by merging the boxes, and Add in the results saves a trip to another page.

**Principles:** Consistency and standards · Recognition rather than recall · Flexibility and efficiency of use

### 2. Visible navigation

- **User need:** Know what’s available and where you are.
- **Problem:** Two hamburger icons on section headers hid menus that repeated links already on the page.
- **Severity:** 2 (Minor)

**Options weighed**

- Keep the hamburger menus. Hidden options have to be remembered or hunted for.
- A left sidebar. Takes width the dashboard needs, and collapses back into a hamburger on phones.
- **Chosen:** Five labeled tabs under the header, current page underlined, scrolling sideways on phones.

**Why:** Five destinations fit as tabs, so nothing needs to hide. A visible label is a signifier: three lines tell you a menu exists, not what is in it.

**Principles:** Recognition rather than recall · Signifiers (Norman)

### 3. Status at a glance

- **User need:** Confirm nothing blocks enrollment.
- **Problem:** “Holds” and “To Do List” each took a full panel to say “No Holds.” and “No To Do’s.”
- **Severity:** 1 (Cosmetic)

**Options weighed**

- Hide the panels when empty. Saves space, but students lose the reassurance that nothing is blocking them.
- Keep the panels. Two large boxes for two empty states.
- **Chosen:** A row of four status chips: a green check when fine, and the gold accent only on a chip that needs action.

**Why:** Keeps the information in a quarter of the space. Color is saved for exceptions, so the one thing that needs attention stands out instead of competing with everything else.

**Principles:** Aesthetic and minimalist design · Visibility of system status

### 4. Enrollment timeline

- **User need:** Know when you can enroll and what to do before then.
- **Problem:** The Nov 5 enrollment appointment was one sentence at the bottom of the sidebar.
- **Severity:** 3 (Major)

**Options weighed**

- A banner across the top. Easy to tune out, and it doesn’t show what comes before enrollment.
- An email reminder. Lives outside the page, among many other emails.
- **Chosen:** A countdown card with the three real steps (cart opens, plan, enroll) and the next action as the main button.

**Why:** Enrollment is a process with steps, so the card shows the steps and where the student is in them. The countdown answers the most common question at a glance.

**Principles:** Visibility of system status · Match between system and the real world

### 5. Plain language

- **User need:** Recognize classes by name.
- **Problem:** Course codes only, the abbreviation “SEM”, and an unexplained “URL” label.
- **Severity:** 2 (Minor)

**Options weighed**

- Show the title in a tooltip on the code. Needs hover, so it fails on phones, and the code alone still has to be decoded.
- **Chosen:** Course title under every code, “Seminar” spelled out, and the “URL” label removed.

**Why:** Students think in course names, not catalog numbers. Text that is always visible beats text you have to go looking for.

**Principles:** Match between system and the real world

### 6. Deadlines in words

- **User need:** Know the next deadline that affects you.
- **Problem:** An identical calendar icon on every class row. You had to click each one to learn anything.
- **Severity:** 3 (Major)

**Options weighed**

- Keep the icon and add a tooltip. Same problem on phones, and deadlines stay one interaction away.
- A separate Deadlines page. Moves the information away from the class it belongs to.
- **Chosen:** Write the next deadline on each row, and expand the row for the full list.

**Why:** Identical icons carry no information, so they can’t be scanned. Showing the next deadline and keeping the rest one click away is progressive disclosure: the common answer is visible, the details are available.

**Principles:** Recognition rather than recall · Progressive disclosure

### 7. Today first

- **User need:** Find where you need to be next.
- **Problem:** A static table sorted by course code. You had to work out which class came next.
- **Severity:** 2 (Minor)

**Options weighed**

- Sort the table by time. Still a table to read, with every day mixed together.
- Highlight the current row. Only helps during class.
- **Chosen:** An “In class now / Up next” card above the class list, with the room and time left.

**Why:** “Where am I going next?” is the question asked most often, so it gets the top of the page. The full list stays below for an overview.

**Principles:** Visibility of system status · Task-centered design

### 8. Conflicts caught early

- **User need:** Build a Spring schedule that will actually enroll.
- **Problem:** Time conflicts only surfaced when you validated or tried to enroll, often on appointment day.
- **Severity:** 4 (Catastrophe)

**Options weighed**

- Warn only at enrollment, as today. The error shows up at the worst possible moment.
- Block adding a class that conflicts. Too rigid: students often add two sections to compare them.
- **Chosen:** Allow it, warn the moment it’s added, show the overlap on a mini calendar, and lock Enroll until it’s fixed.

**Why:** Prevent the error early without taking control away. Students can still compare overlapping options but can’t enroll in a broken schedule, and the message names both classes and says how to fix it.

**Principles:** Error prevention · User control and freedom · Help users recognize and recover from errors

### 9. Unread count

- **User need:** Notice messages that need action.
- **Problem:** “View My Messages” looked the same whether or not anything was new.
- **Severity:** 2 (Minor)

**Options weighed**

- A pop-up alert on login. Interrupts every visit.
- **Chosen:** A count badge on the inbox icon and the Messages tab.

**Why:** A badge reports status without interrupting. It appears only when something is new and clears once the message is read.

**Principles:** Visibility of system status

### 10. Links grouped by task

- **User need:** Find less frequent pages like Degree Planner or Financial Aid.
- **Problem:** One flat menu mixed planning, enrollment, and textbooks. Enrollment features were split across three places.
- **Severity:** 1 (Cosmetic)

**Options weighed**

- An alphabetical list. Easy to build, but people look for tasks, not words.
- **Chosen:** Shortcuts grouped under Plan, Change my classes, and Money.

**Why:** Items placed together read as related, and grouping by the task a student has in mind shortens the search. A card sort with students would confirm the groups.

**Principles:** Gestalt: proximity · Information architecture

### 11. Week view

- **User need:** See the shape of your week.
- **Problem:** Meeting times only as text, like “TuTh 3:30PM – 4:45PM”.
- **Severity:** 1 (Cosmetic)

**Options weighed**

- Keep the text list. Students have to assemble the week in their heads.
- **Chosen:** A weekly calendar grid with today highlighted and a line at the current time.

**Why:** A week is a grid on every paper planner, so the screen should match. A grid shows gaps and long days that text hides.

**Principles:** Match between system and the real world · Mapping (Norman)

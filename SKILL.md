---
name: journal-article-writing
description: Research, plan, write, fact-check, or revise a journalistic feature article, profile, explanatory story, reported essay, interview-based story, or narrative nonfiction piece. Use this skill whenever the user asks for deep research that will become an article, wants to turn a broad topic or source packet into a story, needs a story hypothesis or angle, asks how to structure leads/nut grafs/body sections/quotes/data/endings, or wants a rigorous editorial review. Do not treat academic journal papers as the default meaning of "journal article."
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Journal Article Writing

Turn a broad subject into a researched, evidence-backed, readable journalistic article.

Apply the workflow progressively. Produce only the artifacts needed for the user's current stage, but preserve enough structure that later stages can continue without restarting.

## Core operating model

Treat reporting and writing as one feedback loop:

```text
topic
→ map the change
→ form a working story hypothesis
→ research and interview against it
→ revise the hypothesis
→ organize evidence
→ draft
→ verify
→ revise from substance to sentences
```

Never use polish to hide missing reporting.

## 1. Establish the assignment

Extract or infer:

- topic and intended audience;
- article type: feature, profile, explanatory, investigation, reported essay, or narrative;
- target length, language, tone, deadline, and publication context;
- available source material and access to interviews;
- whether the user wants research, an outline, a draft, a critique, or the full workflow.

Write in the user's requested language. Preserve the original language of quotations unless translation is requested; label translations.

For a full workflow, create a working directory with:

```text
research-dossier.md
story-hypothesis.md
article-outline.md
draft.md
fact-check-ledger.csv
revision-report.md
```

Use the bundled templates rather than inventing new schemas.

## 2. Build the story hypothesis before deep research

A story hypothesis is a revisable reporting instruction, not a thesis to defend.

Identify:

1. **Central development** — who is doing what differently from before?
2. **Story maturity** — is the story mainly at development, impact, or reaction?
3. **Most important impact** — what concrete consequence matters most?
4. **Reaction** — who is adapting, resisting, exploiting, regulating, or reversing it?
5. **Human center** — who acts or bears the consequence?
6. **Conflict** — which goals, interests, institutions, constraints, or values collide?
7. **Scope boundary** — what this article will not attempt to cover.

Use one of these provisional forms:

```text
Emerging story:
[Development] is beginning to change [specific people/system] by [direct impact].

Mature story:
[Known development] is producing [underreported impact], causing [affected actors]
to [reaction], while [opposing actor/constraint] pushes the other way.

Profile:
[Person] is best understood through [2–3 traits], visible in [actions and conflicts].
```

Reject hypotheses that are merely topics, moral judgments, trend slogans, or conclusions that cannot be tested.

Read [references/story-hypothesis.md](references/story-hypothesis.md) when the angle is unclear, the topic is too broad, or multiple plausible stories compete.

## 3. Run deep research as gap-closing, not link collection

Create a research question tree using six evidence boxes:

```text
history | scope | causes | impacts | reactions | future
```

For each major claim, seek complementary evidence:

- **documents/data** for verifiable facts and scale;
- **direct participants** for action, experience, scene, and consequence;
- **independent sources** for explanation, challenge, and corroboration.

Research in passes:

1. **Landscape pass** — map terminology, timeline, actors, institutions, known disputes, and primary sources.
2. **Hypothesis pass** — test the proposed development, impact, reaction, and conflict.
3. **Contradiction pass** — actively search for counterexamples, failed cases, opposing incentives, disputed definitions, and better explanations.
4. **Gap pass** — fill only the evidence holes that would block the article.
5. **Stop decision** — stop when additional research mostly repeats existing evidence and the remaining uncertainty is clearly disclosed.

Record every usable item with:

- source title, author/organization, date, URL or file path;
- source type and role;
- exact claim supported;
- quotation or data excerpt kept within copyright limits;
- reliability notes, conflicts of interest, caveats, and access date;
- intended article section.

Do not claim to have interviewed anyone unless an actual interview transcript or notes are provided.

Read [references/research-workflow.md](references/research-workflow.md) before substantial web research or when evidence is fragmented.

## 4. Revise the hypothesis after reporting

After the first research pass, rewrite the story hypothesis from evidence.

Test it:

- Does it name a real change rather than a subject?
- Does it identify concrete people or institutions affected?
- Is there observable action or reaction?
- Can each major clause be verified?
- Does it define what is out of scope?
- Does it point toward scenes, sources, data, and a plausible ending?
- Would disconfirming evidence change it?

If not, narrow, split, or abandon it. Do not force facts into the original angle.

## 5. Choose one controlling structure

Use one dominant narrative line:

- **Logical progression** — history → scope → causes → impacts → reactions → future.
- **Chronology** — a day, journey, case, investigation, or historical sequence.
- **Thematic profile** — 2–3 traits or tensions demonstrated through actions.

Other lines may appear locally, but readers should always know why the article moves next.

For a standard feature, plan:

```text
lead
→ nut graf / theme paragraph
→ body section 1
→ body section 2
→ complication or counterevidence
→ reaction / next movement
→ ending
```

Each body section should usually perform this movement:

```text
claim or development
→ evidence/data
→ person/action/scene
→ mechanism or explanation
→ complication, limit, or counterpoint
→ concrete transition
```

Read [references/article-architecture.md](references/article-architecture.md) when selecting the overall form or arranging a long article.

## 6. Draft article components by function

### Lead

Choose the form that best serves the story:

- hard-news lead for urgent, consequential events;
- summary lead for a complex central change;
- anecdotal lead for a short, true, representative scene;
- quotation lead only for genuinely distinctive language;
- descriptive lead when the environment itself carries the theme.

An anecdotal lead must be concise, true, representative, intrinsically interesting, and tightly connected to the article's focus.

Do not stall on the lead. When needed, draft the body first and return to the opening.

### Nut graf / theme paragraph

Soon after the lead, answer:

- What is happening?
- Why does it matter now?
- Who is affected?
- What will the article reveal or test?

Convert the internal story hypothesis into a reader-facing promise without giving away every conclusion.

### Data

Keep only numbers that change the reader's understanding of scale, direction, comparison, or risk.

Prefer:

- a small number of decisive figures;
- ratios, rates, per-person values, change over time, and understandable comparisons;
- necessary definitions, time windows, and uncertainty.

Do not manufacture vivid comparisons or sacrifice accuracy for simplicity.

### Characters and quotations

Interview broadly; feature selectively.

Use direct quotations when the original wording adds:

- authority;
- emotion;
- distinctive voice;
- a decisive turn in the evidence.

Paraphrase routine facts and long explanations. Never invent, merge, clean up, or dramatize a quotation beyond what the source supports.

### Scenes and description

Include only observed or documented details that provide evidence, reveal character, establish a necessary environment, or create meaningful contrast.

Never invent sensory detail, internal thought, chronology, or dialogue.

### Transitions

Make the next section grow from a concrete change in time, place, actor, cause, consequence, or reaction. Avoid empty transitions such as "another aspect of the issue."

### Ending

Choose among:

- **echo** — return to the opening image, person, action, or phrase with deeper meaning;
- **forward movement** — show the next evidenced action, risk, or decision;
- **widening frame** — connect the specific story to a larger significance already earned by the article.

Do not hide essential facts at the end or introduce a new unsupported thesis.

Read [references/section-craft.md](references/section-craft.md) when drafting or revising individual parts.

## 7. Verify before polishing

Create or update `fact-check-ledger.csv`.

For every consequential factual statement, record:

- exact claim;
- source(s);
- source type;
- verification status;
- uncertainty or dispute;
- article location;
- required correction or follow-up.

Distinguish clearly among:

- verified fact;
- source allegation;
- expert interpretation;
- author inference;
- estimate;
- projection.

Check names, titles, dates, chronology, numbers, denominators, definitions, quotations, links, and whether a source has a relevant conflict of interest.

For current or unstable facts, search again immediately before finalizing.

Read [references/verification-and-revision.md](references/verification-and-revision.md) before calling a draft final.

## 8. Revise in three passes

### Pass 1 — substance

Check the story hypothesis, scope, missing reporting, evidence diversity, counterevidence, fairness, and factual support. Delete beautiful but irrelevant material.

### Pass 2 — structure and logic

Check the controlling line, section order, nut graf, causal leaps, repetitions, transitions, and whether the ending completes the article.

### Pass 3 — prose and rhythm

Replace abstractions with exact nouns and active verbs. Tighten quotations, vary sentence length, remove throat-clearing, and clarify attribution.

Run:

```bash
python scripts/audit_article.py draft.md
```

Treat the output as editorial prompts, not mechanical truth.

## 9. Deliver an editorially honest result

When evidence is incomplete:

- state what is missing;
- identify which claims remain provisional;
- provide the next research or interview actions;
- do not fill gaps with plausible invention.

For a final delivery, include:

1. the article or requested artifact;
2. a concise sourcing note;
3. unresolved verification items;
4. material excluded because it was unsupported, off-scope, or repetitive.

## Reference routing

- Deep research, source strategy, query design, evidence matrix, stop rules:
  [references/research-workflow.md](references/research-workflow.md)
- Theme hypothesis, scope, maturity, conflict, angle selection:
  [references/story-hypothesis.md](references/story-hypothesis.md)
- Whole-article structure and story modes:
  [references/article-architecture.md](references/article-architecture.md)
- Leads, nut grafs, data, quotes, scenes, transitions, endings:
  [references/section-craft.md](references/section-craft.md)
- Fact-checking, fairness, revision, and final review:
  [references/verification-and-revision.md](references/verification-and-revision.md)

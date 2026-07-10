---
name: journal-article-writing
description: Research, shape, outline, write, fact-check, or revise a journalistic feature, profile, explanatory story, reported essay, interview-based story, or narrative nonfiction piece. Use this skill whenever a user wants deep research to become an article, needs help turning a broad topic or source packet into a story, wants a story hypothesis or angle, needs an evidence/material system, asks how to design sections or write leads/nut grafs/body sections/quotes/data/endings, or wants rigorous editorial review. Actively use AskUserQuestion at the editorial decision gates defined below. Do not treat academic journal papers as the default meaning of "journal article."
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - WebSearch
  - WebFetch
  - AskUserQuestion
---

# Journal Article Writing

Turn a broad subject into a researched, evidence-backed, human-sounding journalistic article.

Apply the workflow progressively. Produce only the artifacts needed for the user's current stage, but preserve the evidence and design state so later stages can continue without restarting.

## Non-negotiable operating principles

1. Treat reporting and writing as one feedback loop.
2. Treat the story hypothesis as a testable working model, not a conclusion to defend.
3. Build the article from traceable source, claim, material, and section records.
4. Never invent interviews, quotations, scenes, sensory detail, chronology, motives, or internal thoughts.
5. Do not use polish to hide missing reporting.
6. Stop and involve the user at high-leverage editorial decisions.
7. Revise from evidence to structure to sentences, in that order.
8. Use the user's language and voice. Preserve quotation language unless translation is requested and label translations.

## Required human decision gates

Use `AskUserQuestion` at these gates. Present 2–4 concrete options, state your recommendation and why, and wait for confirmation before crossing the gate.

If `AskUserQuestion` is unavailable, ask the same concise question in chat and wait. Do not silently choose unless the user explicitly delegated that decision.

| Gate | Confirm with the user | Required output before asking |
|---|---|---|
| G0 Assignment | audience, article type, target length, deliverable, voice sample availability | prefilled editorial brief |
| G1 Story maturity | development, impact, reaction, or profile; human center | 2–3 candidate story models |
| G2 Story hypothesis | central change, impact, conflict, scope boundary | recommended hypothesis plus alternatives |
| G3 Article architecture | logical line, chronology, thematic profile, or hybrid; section directory | article blueprint with section jobs |
| G4 Section expansion | how each major section unfolds | expansion pattern selected for each section |
| G5 Draft voice | publication voice or user voice; humanizer strength | short voice profile and sample paragraph |
| G6 Final sign-off | unresolved facts, fairness risks, and material exclusions | verification and revision report |

Batch related decisions into one question when possible. Do not interrupt the user for low-level wording choices.

Read [references/human-checkpoints.md](references/human-checkpoints.md) before running a full end-to-end assignment.

## Project workspace

For a full assignment, create a story workspace using:

```bash
python scripts/init_story_project.py "Working title" --output .
```

The workspace follows an OKF v0.1-compatible knowledge bundle:

```text
story-slug/
├── index.md
├── editorial-brief.md
├── story-design-sop.md
├── research-dossier.md
├── article-blueprint.md
├── sources/
├── claims/
├── materials/
├── sections/
├── drafts/
└── audits/
```

Use stable IDs:

```text
SRC-001   source
CLM-001   claim
MAT-001   usable material
SEC-001   article section
DEC-001   human editorial decision
```

Read [references/okf-material-system.md](references/okf-material-system.md) before creating or reorganizing source notes.

## Workflow

### 1. Establish the assignment and prefill the form

Create `editorial-brief.md` from [templates/editorial-brief.md](templates/editorial-brief.md).

Prefill everything inferable from the user's request and supplied files. Do not make the user fill fields you already know.

Confirm G0 only for missing or consequential choices:

- audience and publication context;
- article type;
- target length and deadline;
- desired output stage;
- tone, language, and whether a writing sample should guide voice;
- interview access and research constraints.

### 2. Propose story models before deep research

Map the initial dynamic:

```text
development → impact → reaction
```

Generate 2–3 candidate story models, each with:

- central development;
- maturity stage;
- most important impact;
- human center;
- conflict;
- likely evidence;
- scope boundary;
- what would disprove it.

Ask G1 with a recommendation. After the user chooses the maturity and center, write a provisional hypothesis.

Use these provisional forms:

```text
Emerging story:
[Development] is beginning to change [specific people/system] through [direct impact].

Mature story:
[Known development] is producing [underreported impact], causing [affected actors]
to [reaction], while [opposing actor/constraint] pushes the other way.

Profile:
[Person or group] is best understood through [2–3 traits or tensions],
visible in [actions, decisions, and conflicts].
```

Read [references/story-hypothesis.md](references/story-hypothesis.md) when the angle is broad or several stories compete.

### 3. Confirm the working story hypothesis

Write:

- one recommended hypothesis;
- one narrower version;
- one broader or competing version;
- explicit in-scope and out-of-scope boundaries;
- the central claims that must be proved;
- likely scenes, characters, records, data, and counterevidence.

Ask G2. Once approved, record the decision as `DEC-###` and link it from the project index and relevant claim/section records.

### 4. Run deep research as gap-closing

Use six evidence boxes:

```text
history | scope | causes | impacts | reactions | future
```

Research in passes:

1. landscape pass;
2. hypothesis pass;
3. contradiction pass;
4. gap pass;
5. stop decision.

For every major claim, seek complementary roles:

```text
document/data
+ direct participant
+ independent corroboration
+ counterevidence
```

Create OKF records while researching:

- one `SRC-###.md` per source;
- one `CLM-###.md` per consequential claim;
- one `MAT-###.md` per reusable fact, quote, scene, number, document finding, or contradiction.

A material item belongs to one or more evidence boxes and one or more section candidates. Never store a quote without source and locator.

Read [references/research-workflow.md](references/research-workflow.md) for query design, interview planning, evidence matrices, and stop rules.

### 5. Turn materials into an article directory

Do not jump from notes to prose.

Create `article-blueprint.md` and one `SEC-###.md` card per planned section. Every section card must state:

```text
title
job
reader question answered
primary claim
evidence boxes used
material IDs
human/action element
counterpoint
expansion pattern
entry move
exit/transition
excluded material
verification gaps
approval status
```

Select one dominant line:

- logical progression;
- chronology;
- thematic profile;
- explicitly controlled hybrid.

Then ask G3 with the proposed directory. The user should be able to see what every part does and what would be lost if it were removed.

Read [references/article-architecture.md](references/article-architecture.md) when choosing the whole-article line.

### 6. Select how each section expands

Choose one primary expansion pattern for each major section:

- mechanism;
- scale;
- impact;
- character reveal;
- conflict braid;
- complication/counterevidence;
- reaction;
- historical backfill;
- future conditional.

Add the selected pattern to each section card and show the user the sequence in compact form, for example:

```text
SEC-003 Impact:
aggregate change → participant scene → cost/consequence → mechanism → response
```

Ask G4. The user may accept all recommended patterns or override specific sections.

Read [references/section-expansion-patterns.md](references/section-expansion-patterns.md) for the tool cards.

### 7. Draft by section function

Draft only after G3 and G4 are approved.

A standard feature often moves:

```text
lead
→ nut graf / theme paragraph
→ mechanism
→ concrete impact
→ complication or counterevidence
→ reaction / next movement
→ ending
```

Each paragraph or section must perform a named job. Use source, claim, material, and section IDs in drafting notes or comments when useful, then remove internal annotations from publication copy.

For individual components, use [references/section-craft.md](references/section-craft.md).

### 8. Apply language tools deliberately

Do not apply every technique everywhere. Select tools because the material needs them.

Before drafting a key passage, choose from [references/style-toolkit.md](references/style-toolkit.md), including:

- concrete noun + active verb;
- freight-train sentence;
- hook-on clause;
- parallel structure;
- controlled repetition;
- keyword placement;
- short-force sentence;
- long/short rhythm variation;
- action motion;
- macro/micro alternation;
- contrast braid;
- controlled digression and return;
- data humanization;
- quote punch;
- transition by actual movement;
- echo, forward-motion, or widening-frame ending.

Each tool card defines when to use it, its input, operation, output shape, and failure modes.

### 9. Calibrate voice and remove AI writing patterns

At G5, ask whether to use:

- the user's writing sample;
- a named publication or authorial register;
- neutral reported prose;
- a light, medium, or strong anti-AI cleanup pass.

When a user sample is available, derive a compact voice profile:

- sentence-length distribution;
- preferred vocabulary level;
- paragraph openings;
- punctuation;
- degree of explicit signposting;
- humor, skepticism, and first-person use;
- transition habits;
- tolerated roughness or asymmetry.

Then run the human-writing pass described in [references/human-writing-integration.md](references/human-writing-integration.md).

This repository references the MIT-licensed open-source `blader/humanizer` skill. If it is installed, invoke it after factual and structural revision. If it is not installed, use the compact adapted checklist in the integration reference.

Never make prose "more human" by inventing opinions, uncertainty, anecdotes, or personality not supported by the author or reporting.

### 10. Verify before polishing

Maintain `fact-check-ledger.csv`.

For every consequential statement, distinguish:

- verified fact;
- source allegation;
- expert interpretation;
- author inference;
- estimate;
- projection;
- quotation;
- scene detail;
- reconstructed chronology.

Check names, titles, dates, numbers, denominators, definitions, chronology, quotation fidelity, conflicts of interest, and current facts.

Read [references/verification-and-revision.md](references/verification-and-revision.md).

### 11. Revise in three passes

1. **Substance:** hypothesis, scope, missing reporting, evidence diversity, counterevidence, fairness.
2. **Structure:** controlling line, section order, causal leaps, repetition, transitions, ending.
3. **Prose:** exact nouns, active verbs, quotation trimming, sentence rhythm, attribution, AI-pattern cleanup.

Run:

```bash
python scripts/audit_article.py drafts/draft.md
python scripts/validate_story_project.py .
```

Treat script output as editorial prompts, not mechanical truth.

### 12. Final human sign-off

Before calling a piece final, produce:

- sourcing note;
- unresolved verification items;
- fairness/nonresponse log;
- material excluded as unsupported, off-scope, repetitive, or weak;
- remaining claims dependent on a single source;
- the final article directory and section IDs.

Ask G6. Do not conceal unresolved issues.

## Reference routing

- Human decision gates and `AskUserQuestion` patterns:
  [references/human-checkpoints.md](references/human-checkpoints.md)
- OKF project structure, IDs, metadata, and relationships:
  [references/okf-material-system.md](references/okf-material-system.md)
- Deep research and evidence acquisition:
  [references/research-workflow.md](references/research-workflow.md)
- Story maturity, hypothesis, conflict, and scope:
  [references/story-hypothesis.md](references/story-hypothesis.md)
- Whole-article architecture and section directory:
  [references/article-architecture.md](references/article-architecture.md)
- Section expansion tool cards:
  [references/section-expansion-patterns.md](references/section-expansion-patterns.md)
- Leads, nut grafs, data, quotes, scenes, transitions, endings:
  [references/section-craft.md](references/section-craft.md)
- Sentence, rhythm, motion, contrast, and ending tools:
  [references/style-toolkit.md](references/style-toolkit.md)
- Human voice and anti-AI editing:
  [references/human-writing-integration.md](references/human-writing-integration.md)
- Fact-checking, fairness, and revision:
  [references/verification-and-revision.md](references/verification-and-revision.md)

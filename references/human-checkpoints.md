# Human Editorial Checkpoints

Use this reference to keep the model helpful without letting it silently make high-leverage editorial decisions.

## Principle

The model should do the preparatory work first, then ask the user to choose among concrete, well-formed options.

Bad interaction:

```text
What angle do you want?
```

Better interaction:

```text
I found three plausible stories in the material:
A. Development-led: ...
B. Impact-led: ...
C. Reaction-led: ...

I recommend B because it has the strongest direct participants and the clearest conflict.
Which should control the article?
```

## Tool rule

At every gate, call `AskUserQuestion` when available.

- Keep the question narrow.
- Offer 2–4 options.
- Mark the recommended option.
- Explain the consequence of each choice.
- Allow "accept recommendation" as an option.
- Batch closely related choices.
- Wait for an answer before proceeding.

When the user has explicitly said "you decide," record that delegation as a decision and proceed.

## Decision record

Record every gate as `DEC-###`:

```yaml
---
okf_version: "0.1"
type: Editorial Decision
id: DEC-001
title: Choose impact-led story
status: approved
decision_gate: G1
decided_by: user
decided_at: YYYY-MM-DD
affects:
  - CLM-001
  - SEC-001
alternatives_considered:
  - development-led
  - reaction-led
---
```

Body:

```markdown
# Decision

## Question

## Options

## Recommendation

## User choice

## Consequences

## Revisit when
```

## G0 — Assignment

Ask only what remains unknown and changes the work.

Confirm:

- reader and publication;
- article type;
- target length;
- deadline;
- language and tone;
- output stage;
- research and interview access;
- whether a voice sample exists.

Recommended `AskUserQuestion` shape:

```text
I prefilled the assignment from your request. Two choices still change the workflow:

1. Intended reader
   A. General technology reader (recommended)
   B. Industry practitioner
   C. Executive decision-maker

2. Deliverable now
   A. Research dossier + blueprint (recommended)
   B. Full first draft
   C. Editorial critique only
```

## G1 — Story maturity and human center

Before asking, produce 2–3 models.

For each model show:

- stage: development / impact / reaction / profile;
- central movement;
- human center;
- conflict;
- strongest available material;
- largest reporting gap.

Ask the user to choose the stage and center.

Do not equate "new" with "good." A mature impact or reaction story often has more action and evidence than a development announcement.

## G2 — Story hypothesis and scope

Before asking, provide:

- recommended hypothesis;
- narrower alternative;
- broader or competing alternative;
- exact exclusions;
- claims that must be proved;
- disconfirming evidence that would force revision.

Ask:

```text
Which hypothesis should control the reporting?
```

Include a "recommendation accepted" option.

A user-approved hypothesis remains revisable. If later evidence materially changes it, reopen G2 rather than silently drifting.

## G3 — Controlling line and section directory

Before asking, show a readable article map.

Example:

```text
Lead — show the moment speech changes because the recorder is present
Nut graf — define the shift and stakes
SEC-001 — explain why default recording spread
SEC-002 — show how employees change behavior
SEC-003 — complicate with teams that report no chilling effect
SEC-004 — show policy and product responses
Ending — return to what people now say off-record
```

For each section include:

- unique job;
- question answered;
- main material IDs;
- expansion pattern;
- what is excluded.

Ask the user to choose the controlling line:

- logical progression;
- chronology;
- thematic profile;
- controlled hybrid.

Also ask whether the directory is missing a reader question.

## G4 — Section expansion patterns

Do not ask the user to design every paragraph.

Instead, assign a recommended expansion tool to each major section and ask for batch approval.

Example:

```text
SEC-001 Mechanism: change → process → document → example → limit
SEC-002 Impact: aggregate → person → cost → mechanism → response
SEC-003 Complication: simple claim → countercase → difference → revised claim
SEC-004 Reaction: impact → actor goal → action → obstacle → next step
```

Ask:

```text
Accept these section movements, or change any section?
```

## G5 — Voice and anti-AI pass

Before asking, analyze available samples or infer the publication register.

Offer:

- match user's sample;
- neutral feature prose;
- named publication register without imitation of protected text;
- light, medium, or strong anti-AI cleanup.

Clarify:

- Light: remove obvious filler and generic signposting.
- Medium: also vary rhythm, simplify inflated language, and tighten transitions.
- Strong: restructure passages that feel templated, while preserving facts and author intent.

Never add personal opinions unless the user owns and endorses them.

## G6 — Final sign-off

Before asking, show:

- unresolved facts;
- single-source claims;
- unanswered requests for comment;
- reconstructed scenes;
- estimates and projections;
- fairness risks;
- excluded material;
- remaining style warnings.

Ask whether to:

1. hold publication and research further;
2. publish with explicit caveats;
3. cut unsupported claims;
4. accept the current risk.

Do not label the draft final before the user answers.

## Friction control

Human involvement should be concentrated at decisions that are expensive to reverse:

```text
story identity
→ scope
→ architecture
→ section movement
→ voice
→ publication risk
```

The model may decide routine tasks such as file naming, source IDs, metadata normalization, query variants, and sentence-level cleanup.

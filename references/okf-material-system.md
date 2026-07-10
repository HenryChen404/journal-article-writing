# OKF Material System for Reported Articles

Use this reference to preserve provenance and make every piece of research reusable, traceable, and placeable in an article.

This repository uses an OKF v0.1-compatible convention: Markdown files, YAML frontmatter, stable IDs, explicit types, links, provenance, and navigable indexes.

## 1. Bundle structure

```text
story-slug/
├── index.md
├── editorial-brief.md
├── story-design-sop.md
├── research-dossier.md
├── article-blueprint.md
├── sources/
│   ├── index.md
│   └── SRC-001.md
├── claims/
│   ├── index.md
│   └── CLM-001.md
├── materials/
│   ├── index.md
│   └── MAT-001.md
├── sections/
│   ├── index.md
│   └── SEC-001.md
├── decisions/
│   ├── index.md
│   └── DEC-001.md
├── drafts/
│   └── draft.md
└── audits/
    ├── fact-check-ledger.csv
    └── revision-report.md
```

The root `index.md` begins:

```yaml
---
okf_version: "0.1"
type: Story Project
title: Working title
status: active
language: zh-CN
---
```

## 2. Stable IDs and roles

| Prefix | Type | One record represents |
|---|---|---|
| SRC | Source | a document, dataset, interview, person, page, recording, or file |
| CLM | Claim | a consequential proposition the article may assert |
| MAT | Material | one usable unit: fact, number, quote, scene, action, document finding, contradiction |
| SEC | Section | one article block with a unique reader job |
| DEC | Editorial Decision | a human-approved high-leverage choice |

Never encode section order into material IDs. IDs remain stable when the outline changes.

## 3. Source record

Use [templates/okf-source.md](../templates/okf-source.md).

Required metadata:

```yaml
---
okf_version: "0.1"
type: Source
id: SRC-001
title: ""
status: active
source_type: primary_record
source_role: document_data
author_or_organization: ""
published_at: ""
accessed_at: ""
url: ""
local_path: ""
language: ""
reliability: medium
conflicts_of_interest: []
rights_note: ""
---
```

Allowed `source_type` values:

- primary_record;
- direct_participant;
- independent_interpreter;
- interested_advocate;
- secondary_reporting;
- author_observation.

Allowed `source_role` values:

- document_data;
- action_experience;
- explanation;
- corroboration;
- opposition;
- lead_generation.

A source can play several roles, but identify the primary role.

## 4. Claim record

Use [templates/okf-claim.md](../templates/okf-claim.md).

```yaml
---
okf_version: "0.1"
type: Claim
id: CLM-001
title: ""
status: provisional
claim_kind: causal
importance: major
evidence_boxes:
  - impact
source_ids:
  - SRC-001
material_ids:
  - MAT-001
counterevidence_ids: []
section_ids:
  - SEC-002
verification_status: partial
confidence: medium
---
```

Allowed `claim_kind` values:

- factual;
- descriptive;
- quantitative;
- causal;
- comparative;
- interpretive;
- allegation;
- inference;
- estimate;
- projection.

A claim card answers:

- What exactly may the article say?
- What supports it?
- What contradicts it?
- What is the strongest permissible wording?
- What would change or kill the claim?

## 5. Material record

Use [templates/okf-material.md](../templates/okf-material.md).

One material record should be small enough to move between sections without copying a whole source note.

```yaml
---
okf_version: "0.1"
type: Material
id: MAT-001
title: ""
status: active
source_id: SRC-001
material_kind: quote
evidence_boxes:
  - impact
evidence_functions:
  - emotion
  - character
claim_ids:
  - CLM-002
section_ids:
  - SEC-002
verification_status: verified
confidence: high
observed_or_reconstructed: attributed_recollection
locator: "Interview transcript 00:14:22"
tags: []
---
```

Allowed `material_kind` values:

- fact;
- number;
- quote;
- action;
- scene;
- chronology;
- document_finding;
- mechanism;
- comparison;
- contradiction;
- color_detail;
- transition;
- ending_candidate.

Allowed `evidence_functions` values:

- establish_change;
- scale;
- mechanism;
- impact;
- reaction;
- character;
- authority;
- emotion;
- credibility;
- counterevidence;
- context;
- navigation;
- ending.

## 6. Six evidence boxes

Every useful material should be tagged with at least one box.

### History

Origins, prior conditions, enabling decisions, causal timeline.

### Scope

Scale, geography, population, time window, denominator, variation.

### Causes

Mechanisms, incentives, decision chains, competing explanations.

### Impacts

Changes in behavior, cost, time, power, risk, access, or emotion.

### Reactions

Promotion, resistance, adaptation, regulation, evasion, compensation, redesign.

### Future

Committed next actions, conditional outcomes, deadlines, invalidating evidence.

Do not force equal numbers of materials into all boxes. The approved hypothesis determines priority.

## 7. Section record

Use [templates/okf-section.md](../templates/okf-section.md).

```yaml
---
okf_version: "0.1"
type: Article Section
id: SEC-002
title: How speech changes
status: planned
order: 3
section_job: make_impact_concrete
reader_question: "What changes when every sentence is retained?"
primary_claim_ids:
  - CLM-002
material_ids:
  - MAT-004
  - MAT-011
evidence_boxes:
  - impact
expansion_pattern: impact
entry_move: participant_action
exit_move: consequence_to_reaction
human_approved: false
---
```

Every section must have:

- one unique job;
- one reader question;
- one primary claim or development;
- a material list;
- an expansion pattern;
- an entry and exit move;
- a list of deliberate exclusions;
- gaps and risk notes.

## 8. Relationship rules

Preferred relationship direction:

```text
Source → Material → Claim → Section → Draft
             ↘ counterevidence ↗
Decision ──────────────────────↗
```

A source is not automatically evidence for every statement derived from it.

A material record must link to exactly one source record unless it explicitly combines independently verified records. Combined materials should list all source IDs and explain the synthesis.

A major claim should not remain `verified` when all supporting materials come from the same interested source.

## 9. Annotation in working drafts

Internal drafts may use lightweight comments:

```markdown
<!-- SEC-002 | CLM-002 | MAT-004 MAT-011 -->
```

Or inline markers:

```text
[CLM-002][MAT-004]
```

Remove internal IDs from publication copy. Preserve them in the fact-check version.

## 10. Source capture procedure

For each new source:

1. Create `SRC-###`.
2. Record provenance and rights.
3. Extract only usable units into separate `MAT-###` cards.
4. Link each material to evidence boxes, claims, and possible sections.
5. Add contradictions immediately rather than in a later cleanup.
6. Update relevant indexes.

Do not paste entire copyrighted works into the bundle. Store short necessary excerpts and precise locators.

## 11. Material triage

Classify every material:

| Status | Meaning |
|---|---|
| active | likely usable |
| reserve | useful but not currently placed |
| blocked | cannot use until verified |
| rejected | inaccurate, redundant, off-scope, or too weak |
| published | used in final copy |

Rejected material remains traceable. Record why it was rejected.

## 12. Directory design from materials

After research, generate a proposed directory by grouping materials around reader questions, not source order.

For each candidate section:

1. identify the question;
2. identify the change in reader understanding;
3. choose a primary claim;
4. attach complementary material types;
5. select an expansion pattern;
6. define the transition out;
7. list excluded material.

If a section contains many materials but no unique job, it is a storage bucket, not an article section.

## 13. Validation checks

Run:

```bash
python scripts/validate_story_project.py .
```

The validator should flag:

- missing IDs;
- duplicate IDs;
- broken local links;
- material without a source;
- claim without evidence;
- section without a job or expansion pattern;
- unapproved decision gates;
- publication-ready claims still marked provisional;
- orphaned active materials.

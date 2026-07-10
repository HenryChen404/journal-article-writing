# journal-article-writing

A Claude Code skill for turning a broad topic into a researched, structured, fact-checked, human-sounding journalistic feature.

这是一个面向深度报道、人物特写、解释性报道、叙事非虚构和研究型长文的 Claude Code Skill。它现在包含一套完整的“人机共同编辑”工作流：

1. 用 development → impact → reaction 判断故事成熟度；
2. 用六个素材盒子组织历史、范围、原因、影响、反作用和未来；
3. 用 OKF v0.1-compatible 的 Source / Claim / Material / Section / Decision 卡保存证据；
4. 让 AI 先提出主题假设和目录，再在关键节点调用 `AskUserQuestion` 让人确认；
5. 为每个板块选择明确的展开工具；
6. 使用句段、动感、对照、平行、货运火车句、结尾等“小工具”；
7. 事实核查后，再进行 anti-AI / human-writing pass。

> This skill is for journalistic articles, not academic journal papers by default.

## Install

### User-level

```bash
git clone https://github.com/HenryChen404/journal-article-writing.git \
  ~/.claude/skills/journal-article-writing
```

### Project-level

```bash
mkdir -p .claude/skills
git clone https://github.com/HenryChen404/journal-article-writing.git \
  .claude/skills/journal-article-writing
```

Invoke directly with:

```text
/journal-article-writing
```

## Story workspace

Initialize a new reported-article project:

```bash
python scripts/init_story_project.py "Working title" --output .
```

It creates:

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
├── decisions/
├── drafts/
└── audits/
```

Stable IDs connect research to prose:

```text
SRC-001 → MAT-001 → CLM-001 → SEC-001 → draft
                         ↖ DEC-001
```

## Human decision gates

The skill uses `AskUserQuestion` for six editorial gates:

- G0 assignment;
- G1 story maturity and human center;
- G2 story hypothesis and scope;
- G3 controlling line and directory;
- G4 section expansion patterns;
- G5 voice and anti-AI cleanup;
- G6 publication/fact-check sign-off.

The model should prefill and recommend before asking, rather than asking the user to design the story from a blank page.

## Repository structure

```text
journal-article-writing/
├── SKILL.md
├── references/
│   ├── human-checkpoints.md
│   ├── okf-material-system.md
│   ├── research-workflow.md
│   ├── story-hypothesis.md
│   ├── article-architecture.md
│   ├── section-expansion-patterns.md
│   ├── section-craft.md
│   ├── style-toolkit.md
│   ├── human-writing-integration.md
│   └── verification-and-revision.md
├── templates/
├── scripts/
├── evals/
└── third_party/
    └── humanizer/
```

## Style tools

The skill treats writing choices as small tools with explicit use conditions:

- freight-train sentence;
- hook-on clause;
- parallel structure;
- keyword placement;
- controlled repetition;
- short-force sentence;
- long/short rhythm;
- action motion;
- macro/micro alternation;
- contrast braid;
- controlled digression;
- data humanization;
- quote punch;
- scene engine;
- actual-movement transitions;
- echo, forward-motion, and widening-frame endings.

## Humanizer integration

The project references the MIT-licensed open-source [`blader/humanizer`](https://github.com/blader/humanizer) skill and includes attribution and its license under `third_party/humanizer/`.

The integration is used after factual and structural editing. It must not change quotations, claim strength, chronology, or source attribution.

## Validate

Validate the skill repository:

```bash
python scripts/validate_skill.py
```

Validate a generated story workspace:

```bash
python scripts/validate_story_project.py path/to/story
```

Audit a draft:

```bash
python scripts/audit_article.py path/to/story/drafts/draft.md
python scripts/audit_article.py path/to/story/drafts/draft.md --json
```

## Methodology note

The reporting and feature-writing workflow is adapted from established narrative-nonfiction practice, especially William E. Blundell's *The Art and Craft of Feature Writing*. It is expanded for AI-assisted deep research, OKF-style provenance, explicit human editorial gates, reproducible fact-checking, and voice calibration. No source text is reproduced.

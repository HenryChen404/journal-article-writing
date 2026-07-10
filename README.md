# journal-article-writing

A Claude Code skill for turning a broad topic into a researched, structured, fact-checked journalistic feature article.

这是一个面向 **深度报道、人物特写、解释性报道、叙事非虚构和研究型长文** 的 Claude Code Skill。它覆盖：

1. Deep research：该查什么、找谁、如何保存证据；
2. Story hypothesis：如何从“大话题”收敛成可验证的故事；
3. Article architecture：导语、主题段、主体板块、数据、人物、引语、转场和结尾；
4. Verification and revision：事实核查、公平性检查、结构修改与语言修改。

> This skill is for journalistic articles, not academic journal papers by default.

## Install

### User-level

```bash
git clone https://github.com/HenryChen404/journal-article-writing.git \
  ~/.claude/skills/journal-article-writing
```

### Project-level

From the target project:

```bash
mkdir -p .claude/skills
git clone https://github.com/HenryChen404/journal-article-writing.git \
  .claude/skills/journal-article-writing
```

Claude can invoke the skill automatically when relevant, or you can invoke it directly with:

```text
/journal-article-writing
```

## Repository structure

```text
journal-article-writing/
├── SKILL.md
├── references/
│   ├── research-workflow.md
│   ├── story-hypothesis.md
│   ├── article-architecture.md
│   ├── section-craft.md
│   └── verification-and-revision.md
├── templates/
│   ├── research-dossier.md
│   ├── article-outline.md
│   └── fact-check-ledger.csv
├── scripts/
│   ├── audit_article.py
│   └── validate_skill.py
└── evals/
    └── evals.json
```

## Typical outputs

Depending on the assignment, the skill can create:

```text
research-dossier.md
story-hypothesis.md
article-outline.md
draft.md
fact-check-ledger.csv
revision-report.md
```

The workflow is progressive: it does not force every artifact when the user only asks for one stage.

## Design principles

- Research and writing are one feedback loop.
- A theme is a testable working hypothesis, not a predetermined opinion.
- Every major claim should have traceable evidence.
- Direct participants, documents/data, and independent corroboration serve different roles.
- Scenes and quotes are never invented.
- Structure follows the story's actual movement: development, impact, and reaction.
- Revision proceeds from substance to structure to sentences.

## Validate the skill

```bash
python scripts/validate_skill.py
```

## Audit a draft

```bash
python scripts/audit_article.py draft.md
python scripts/audit_article.py draft.md --json
```

The article audit is heuristic. It surfaces likely issues; it does not replace editorial judgment or fact-checking.

## Methodology note

The workflow is adapted from established feature-writing and narrative-nonfiction practice, especially William E. Blundell's *The Art and Craft of Feature Writing*, and expanded for AI-assisted deep research, evidence tracking, and reproducible fact-checking. No source text is reproduced.

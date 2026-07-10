# Human-Writing Integration

Use this reference after factual and structural revision. Human-sounding prose cannot rescue weak reporting.

## Upstream reference

This skill integrates ideas from:

- Repository: `blader/humanizer`
- Skill: `SKILL.md`
- License: MIT
- Upstream version reviewed: 2.8.2
- Purpose: detect and remove recurring signs of AI-generated writing.

See [third_party/humanizer/NOTICE.md](../third_party/humanizer/NOTICE.md) and [third_party/humanizer/LICENSE](../third_party/humanizer/LICENSE).

The upstream skill includes voice calibration and a broad audit of inflated significance, promotional language, vague attribution, formulaic structure, AI-favored vocabulary, forced parallelism, synonym cycling, excessive signposting, uniform rhythm, generic conclusions, and chatbot artifacts.

## Invocation strategy

### When the upstream skill is installed

After the article passes evidence and structure review:

1. preserve a fact-check copy;
2. invoke `/humanizer:humanizer` or the installed equivalent;
3. provide the approved voice profile and text;
4. require preservation of facts, scope, quotations, attribution, and paragraph function;
5. compare the result with the fact-check copy;
6. reject any added fact, opinion, anecdote, or emotional claim.

Do not let humanization change a quotation.

### When it is not installed

Use the compact audit below.

## Voice calibration

When the user supplies 2–5 representative paragraphs, record:

```yaml
sentence_rhythm:
vocabulary_level:
paragraph_openings:
punctuation:
transition_style:
signposting_level:
humor:
skepticism:
first_person:
preferred_roughness:
phrases_to_avoid:
```

Match tendencies, not surface tics. Do not caricature the user.

When no sample exists, use neutral, direct reported prose.

## Compact anti-AI audit

### Content inflation

Cut or prove phrases that claim significance without evidence:

```text
pivotal
transformative
profound
a testament to
marks a new era
reflects a broader shift
reshaping the landscape
```

Replace with the concrete change and consequence.

### Vague authority

Replace:

```text
experts say
observers believe
industry reports suggest
critics argue
```

with a named source, document, study, or delete the claim.

### Generic analysis tails

Watch for clauses that add fake meaning:

```text
highlighting...
underscoring...
showcasing...
reflecting...
symbolizing...
```

Either supply the factual mechanism and source or cut the tail.

### Formulaic contrast

Reduce repeated forms such as:

```text
not only X, but Y
it is not just X; it is Y
from X to Y
despite challenges...
```

State the actual relation directly.

### Forced completeness

Do not force every idea into three items. Use the number the material requires.

### Synonym cycling

Repeat the clearest term when it remains the same thing. Do not rotate among "protagonist," "central figure," "hero," and "main character" merely to avoid repetition.

### Promotional language

Remove travel-brochure and product-marketing words unless attributed or demonstrated.

### Chatbot residue

Delete:

```text
Great question
Let's dive in
Here's what you need to know
I hope this helps
Let me know if you want more
```

from article copy.

### Empty signposting

Replace headings and transitions that announce rather than move:

```text
Challenges and opportunities
Another important aspect
Looking ahead
In conclusion
```

with a concrete question, action, consequence, or deadline.

### Mechanical symmetry

Audit:

- every paragraph the same size;
- every sentence the same length;
- repeated bold-label lists;
- identical section openings;
- a compulsory counterpoint in every section;
- repeated mini-conclusions.

Break symmetry only where the material changes.

### Manufactured drama

Cut:

- unsupported aphorisms;
- strings of sentence fragments;
- fake rhetorical questions;
- generic one-line punch endings;
- overuse of dashes or colons;
- cinematic detail without sourcing.

### Excessive hedging

Distinguish uncertainty precisely:

- "may" for real possibility;
- "the study did not measure..." for method limits;
- "the company said..." for attributed claims;
- "the evidence is mixed" only when evidence is actually mixed.

Do not stack "could potentially possibly."

## Chinese-language audit

Common AI-shaped Chinese patterns include:

```text
值得注意的是
不可忽视的是
在当今……时代
随着……不断发展
从……到……
不仅……更……
这不仅仅是……而是……
赋能
助力
深度融合
多维度
全方位
底层逻辑
重要抓手
新的篇章
综上所述
未来可期
```

Do not ban a phrase mechanically. Ask whether it names a specific relation. Replace abstractions with actor, action, mechanism, evidence, and consequence.

Watch for:

- paragraph after paragraph beginning with a summary sentence;
- too many four-character abstractions;
- balanced lists of three or four;
- universal "一方面/另一方面";
- repeated "首先、其次、最后";
- false emotional elevation;
- section endings that restate the section.

## Two-pass process

### Pass A — audit

Mark each issue with:

```text
AI-PATTERN
LOCATION
WHY IT SOUNDS GENERIC
FACTUAL RISK
PROPOSED OPERATION
```

### Pass B — rewrite

Rewrite while preserving:

- claim strength;
- source attribution;
- chronology;
- data definitions;
- quotation text;
- section job;
- author's actual stance.

Then compare sentence by sentence against the fact-check copy.

## Final question

The right standard is not "Could an AI have written this?"

Use:

```text
Does this sound like a specific writer observed, checked, selected, and meant every sentence?
```

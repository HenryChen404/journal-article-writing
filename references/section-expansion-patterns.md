# Section Expansion Tool Cards

Choose one primary pattern for each major section. Combine patterns only when the section's job genuinely requires it.

Every tool card has:

```text
Use when
Required inputs
Sequence
Output
Failure modes
Exit move
```

## EXP-01 Mechanism

**Use when:** The reader needs to understand how a policy, technology, institution, market, or behavior produces an outcome.

**Required inputs:**

- a defined process or causal chain;
- at least one primary record or direct observation;
- a concrete example;
- known limits or competing mechanisms.

**Sequence:**

```text
visible change
→ process steps
→ decisive document/data
→ concrete example
→ limit or alternative explanation
```

**Output:** The reader can explain the mechanism without repeating jargon.

**Failure modes:**

- confusing sequence with causality;
- relying only on expert explanation;
- introducing unnecessary technical history;
- hiding uncertainty.

**Exit move:** Move from mechanism to a person or institution experiencing its effect.

## EXP-02 Scale

**Use when:** The reader needs to know how large, common, concentrated, unusual, or uneven the phenomenon is.

**Required inputs:**

- numerator and denominator;
- time window;
- geography or population;
- comparison baseline;
- variation or exception.

**Sequence:**

```text
representative case or number
→ denominator and time window
→ comparison
→ distribution or variation
→ boundary of the estimate
```

**Output:** Scale becomes meaningful rather than merely large.

**Failure modes:**

- impressive totals without denominator;
- mixing incomparable periods;
- false precision;
- treating one vivid case as prevalence.

**Exit move:** Move from aggregate scale to the human consequence or mechanism.

## EXP-03 Impact

**Use when:** The section must make an effect concrete.

**Required inputs:**

- aggregate evidence;
- direct participant;
- observable action or consequence;
- mechanism;
- response or adaptation.

**Sequence:**

```text
aggregate change
→ participant scene/action
→ cost, benefit, or constraint
→ mechanism
→ participant response
```

**Output:** The reader sees both pattern and lived consequence.

**Failure modes:**

- one anecdote standing in for the whole trend;
- emotion without verifiable change;
- data without person;
- person without context.

**Exit move:** Move from impact to reaction or complication.

## EXP-04 Character Reveal

**Use when:** A person, team, organization, or community is the article's human center.

**Required inputs:**

- a revealing action;
- a relevant trait or tension;
- history that explains but does not excuse;
- contradiction;
- consequential choice.

**Sequence:**

```text
revealing action
→ inferred trait
→ prior evidence/history
→ contradictory behavior
→ consequential decision
```

**Output:** Character emerges through action rather than adjective.

**Failure modes:**

- résumé chronology;
- appearance as substitute for character;
- speculative motive;
- a single trait with no contradiction.

**Exit move:** Move from character to the system or conflict the person encounters.

## EXP-05 Conflict Braid

**Use when:** Two actors, goals, values, or systems push against each other through action.

**Required inputs:**

- two clearly different goals;
- action from both sides;
- shared object or decision;
- changing stakes;
- evidence beyond statements.

**Sequence:**

```text
side A acts
→ consequence for side B
→ side B responds
→ new constraint for side A
→ escalation, compromise, or stalemate
```

**Output:** Conflict moves instead of becoming paired opinion quotes.

**Failure modes:**

- false balance;
- alternating quotations with no action;
- assigning moral symmetry where evidence is asymmetric;
- hiding power differences.

**Exit move:** Move to the result, cost, or next decision.

## EXP-06 Complication / Counterevidence

**Use when:** The easy version of the story is incomplete, overstated, or wrong in some cases.

**Required inputs:**

- the simple claim;
- credible counterexample or contrary data;
- reason for the difference;
- revised claim;
- remaining uncertainty.

**Sequence:**

```text
simple version
→ counterevidence
→ why it differs
→ revised, narrower claim
→ unresolved question
```

**Output:** The article becomes more accurate without collapsing into "both sides."

**Failure modes:**

- token objection;
- weak source used to manufacture balance;
- counterexample that does not address the claim;
- refusing to revise the hypothesis.

**Exit move:** Move to reaction, conditional conclusion, or targeted future question.

## EXP-07 Reaction

**Use when:** The story has matured beyond impact and actors are responding.

**Required inputs:**

- prior impact;
- actor and goal;
- concrete action;
- obstacle;
- early result or next step.

**Sequence:**

```text
impact
→ actor goal
→ action
→ obstacle or opposition
→ result / next move
```

**Output:** The story regains motion and points toward the future.

**Failure modes:**

- announced plans presented as completed action;
- public relations statements without implementation;
- no obstacle;
- prediction presented as result.

**Exit move:** Move to the next committed action, deadline, or earned ending.

## EXP-08 Historical Backfill

**Use when:** A past decision or condition is necessary to understand the present.

**Required inputs:**

- present trigger;
- only the causal historical steps;
- primary records;
- clear return point.

**Sequence:**

```text
present question
→ necessary past condition
→ causal turning point
→ consequence that persists
→ return to present action
```

**Output:** History explains the present without becoming a separate essay.

**Failure modes:**

- chronology dump;
- biography or institutional history unrelated to the current mechanism;
- failing to return to the live story.

**Exit move:** Return through a current action, decision, or consequence.

## EXP-09 Future Conditional

**Use when:** The article must show what happens next without pretending to know the future.

**Required inputs:**

- committed action or deadline;
- conditional branches;
- indicators to watch;
- evidence that would invalidate the forecast;
- actor responsible.

**Sequence:**

```text
committed next step
→ condition A / condition B
→ indicators
→ actor decision
→ what would disprove the forecast
```

**Output:** A bounded, testable future rather than a generic outlook.

**Failure modes:**

- trend extrapolation without mechanism;
- "the future remains uncertain";
- unattributed prediction;
- treating aspiration as commitment.

**Exit move:** Use forward-motion ending or widen only to significance already established.

## EXP-10 Case-Led Explanation

**Use when:** One case can open and carry an explanatory article but must not stand alone as proof.

**Required inputs:**

- representative case;
- nut graf;
- mechanism;
- aggregate evidence;
- countercase;
- institutional reaction.

**Sequence:**

```text
case scene
→ story promise
→ mechanism
→ scale
→ countercase
→ reaction
```

**Output:** The case supplies continuity while broader evidence supplies validity.

**Failure modes:**

- case chosen only because it is vivid;
- no evidence of representativeness;
- returning to the case without new development.

**Exit move:** Return to the case only when the action or meaning has changed.

## Pattern selection matrix

| Section job | Default pattern | Common secondary pattern |
|---|---|---|
| explain why/how | Mechanism | Historical backfill |
| show how big | Scale | Complication |
| show consequence | Impact | Character reveal |
| deepen protagonist | Character reveal | Conflict braid |
| show opposition | Conflict braid | Reaction |
| revise easy claim | Complication | Scale |
| show what actors do | Reaction | Future conditional |
| explain origins | Historical backfill | Mechanism |
| show what comes next | Future conditional | Reaction |

## Human approval format

Before G4, present:

```text
SEC-001 [job] — EXP-##
Sequence: ...
Why this fits: ...
Risk: ...
```

Ask the user to accept all or override selected sections.

# Product Quality Baseline

This is the default Definition of Done for a new Hao app. It is deliberately short.

## 1. Product

- A new user can identify what the product does from the primary surface.
- The user can complete the core action and receive a complete result.
- The result is useful without requiring future planned features.

## 2. UX

- First use does not require a separate manual.
- The primary action is visually obvious.
- Empty and error states tell the user what happened and what action is available next.
- Loading UI exists only for real waiting states.
- No internal engineering/editorial terminology leaks into user-facing copy.

## 3. Mobile

- The same core action can be completed at 390px width.
- No horizontal overflow hides primary content or controls.
- Touch targets, text size and reading order remain usable.

## 4. State

- Refresh behavior is intentional.
- Direct URL entry is intentional.
- Persisted state has one canonical owner.
- Derived state can be rebuilt and is not a second source of truth.

## 5. Trust

- No fake metrics, readiness percentages, statuses, claims, precision or badges.
- Estimates are labeled as estimates.
- Evidence and source boundaries are explicit where the product makes factual or professional claims.

## 6. Technical

- Syntax/type checks pass when the stack supports them.
- Production build passes when the stack has a build step.
- Small contract/unit tests cover important domain invariants.
- One browser smoke covers the durable core user loop.
- Browser tests avoid brittle assertions on incidental labels, sample rows or temporary content.

## 7. Operations

For a public product, it should be possible to answer:

- Did anyone open it?
- Did users start/complete the core action?
- Did a material runtime failure occur?

Do not add an analytics event for every click.

## Ship rule

If these seven sections pass for the applicable product surface, ship. Do not delay release to add unrelated features.

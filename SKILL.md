---
name: hao-app-starter
description: Turn a product idea into the smallest complete, shippable web app by fixing repeated engineering decisions while keeping the user problem, core loop, domain model, and visual identity product-specific.
---

# Hao App Starter

This repository is the authority for starting a new Hao app. It is a skill, not a framework.

The objective is not to generate the most architecture. The objective is to reach a **small, complete product** with the shortest durable path.

## 1. Start from the idea, not the stack

Before creating application code, write `PRODUCT.md` from `common/PRODUCT.md`.

Resolve these six fields:

1. **Promise** — who gets what useful outcome.
2. **Core Action** — the single most important action the user performs.
3. **Core Loop** — entry → action → result → reason to return.
4. **Canonical State** — what facts must persist and the single write authority for each.
5. **Success** — one observable behavior showing the user received value.
6. **Non-goals** — what v0.1 explicitly does not do.

If the idea is clear enough, infer reasonable answers and proceed. Do not block on speculative questions.

If the project already exists, read its current code, dependencies, product docs and canonical data paths before changing architecture. Reuse maintained dependencies already present when they solve the problem.

## 2. Choose exactly one starter

Use the lightest starter that can support the core loop.

### `minimal`

Use HTML + CSS + JavaScript when the product can remain a focused single-page tool, editorial experience, small game, experiment, or content utility without a component framework.

### `interactive`

Use React + TypeScript + Vite when the core loop has meaningful client state, reusable interactive components, or several connected product states.

### `content-data`

Use Astro + TypeScript + Tailwind when structured content/data is the product and most pages can render at build time.

Do not switch to a heavier starter because the product might need it later.

## 3. Build one vertical slice first

Before adding secondary features, make this path real:

```text
one user → one core action → one complete result
```

The first implementation must be usable end to end. Do not begin with account systems, admin panels, generic settings, dashboards, abstract plugin systems, or future-oriented configuration.

For UI-heavy products, define the product's own visual direction before polishing implementation. The starter's neutral appearance is disposable. Do not turn every product into the same card grid, SaaS dashboard, or marketing landing page.

The primary screen should expose the real product, not a marketing wrapper around a future product.

## 4. Keep one authority for every fact

Write the canonical owner in `PRODUCT.md`.

The default direction is:

```text
canonical state → derived projection → UI
```

Never create two writable representations of the same fact. Search indexes, dashboard JSON, statistics, compiled pages, caches and operations views are projections when they can be rebuilt.

Do not add bidirectional synchronization between equivalent stores.

## 5. Add productization only after the core loop works

Then cover the applicable durable states:

- ready;
- loading, only when real asynchronous work exists;
- empty;
- error;
- completed/result;
- refresh;
- direct URL entry;
- mobile at 390px;
- share, when the result is meaningfully shareable.

If identity exists, also cover signed-out, signed-in and entitlement states.

Do not invent states the product does not have.

## 6. Shared capabilities are referenced, not copied

Read `references/shared-services.md` before adding identity, billing, analytics, persistence or backend capabilities.

`liuh886/admin` is the canonical Hao Apps identity/membership/billing control plane. Product repositories must not copy its checkout, portal, webhook, entitlement or account backend.

Add an account only when the core loop needs identity, cross-device state, paid entitlement, or an explicitly user-owned cloud record.

Add a database only when the canonical state cannot remain static, local, or repository-backed.

## 7. Testing protects invariants and the durable user loop

Do not build a large validation maze.

For v0.1:

- add small contract/unit tests for domain invariants that can silently become wrong;
- add **one browser smoke** for the actual durable user loop once that loop is known;
- prefer Playwright when the project has no existing browser-test library;
- keep browser assertions on user-observable behavior, not incidental labels, sample content, row counts, or implementation structure;
- run type/syntax checks and a production build.

A generic starter must not ship a fake E2E tied to placeholder UI. The agent generating the real product writes the real smoke.

## 8. Default things not to build

Unless the core loop proves they are required, v0.1 does **not** add:

- account/authentication;
- database;
- backend API;
- admin console;
- PWA/service worker;
- AI/model calls;
- realtime sync;
- email system;
- multi-role permissions;
- generalized plugin/config framework;
- speculative abstractions.

## 9. Delete superseded paths

There is no backwards-compatibility layer in this product-building method.

When a path, state model, component, wrapper, transport, configuration or workflow is superseded, delete it. Do not add migration shims, aliases, fallback readers, dual writes or hidden legacy routes.

Keep the loop short and the authority obvious.

## 10. Definition of Done

A v0.1 is shippable when all applicable items in `common/docs/QUALITY_BASELINE.md` pass.

At minimum:

- the user can complete the core action;
- first use does not require a manual;
- the same core action works at 390px;
- refresh/direct entry/error behavior is intentional;
- no fake precision, status or claims are shown;
- checks + build + one durable browser smoke pass;
- deployed behavior can be observed with the agreed analytics surface.

Do not continue adding features merely to make the project look larger.

## 11. Scaffold mechanics

For a new local project, use:

```bash
python3 scripts/new_app.py --type <minimal|interactive|content-data> --name <repo-name> --title "<Product name>" --output <path>
```

The script only copies `common/` and the selected `starters/<type>/` and replaces tokens. After scaffolding:

1. complete `PRODUCT.md`;
2. replace the neutral placeholder with the actual vertical slice;
3. remove unused starter code rather than preserving it;
4. install dependencies only for the chosen starter and commit its lockfile;
5. write the real browser smoke for the core loop;
6. run the quality baseline;
7. deploy.

## 12. Final review question

Before calling the project done, answer:

> If every secondary feature disappeared, would a new user still understand what this product is for, complete its core action, receive a useful result, and have a reason to use or share it again?

If not, improve the core loop before expanding scope.

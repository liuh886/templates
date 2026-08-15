# Hao App Templates

Turn an idea into the smallest complete, shippable product.

This repository is a **product-building skill**, not a framework and not a design system. It freezes the decisions that should not be re-made for every app, while keeping the user problem, core loop, domain model, and visual identity product-specific.

## Use it with an AI agent

Give the agent this repository and an idea:

```text
Use https://github.com/liuh886/templates as the product-build skill.
Idea: <your idea>
Ship the smallest complete v0.1. Do not add speculative features.
```

The authority for how the agent should work is [`SKILL.md`](./SKILL.md).

## What is fixed

- define the product before architecture;
- one core user action and one complete vertical slice first;
- choose the lightest of three starter types;
- one canonical write authority for every fact;
- derived state is rebuilt, not promoted into another source of truth;
- mobile, empty, error, refresh, direct-entry and completion states are part of product quality;
- domain invariants get contract tests; browser E2E protects only the durable user loop;
- shared account and billing capabilities stay owned by `liuh886/admin` rather than being copied into product repositories;
- ship when the product is complete enough to use, not when every possible feature exists.

## What is deliberately not fixed

- the user problem;
- the domain model;
- the product's visual personality;
- the information architecture;
- whether the product needs accounts, a database, AI, a backend, PWA support, realtime sync, or multi-role permissions.

Those are added only when the core loop requires them.

## Starter types

| Type | Default | Use when |
| --- | --- | --- |
| `minimal` | HTML + CSS + JavaScript | A focused single-page tool, editorial product, experiment, small game, or content utility does not need a component framework. |
| `interactive` | React + TypeScript + Vite | The core experience has meaningful client state, reusable interaction components, or several connected product states. |
| `content-data` | Astro + TypeScript + Tailwind | Structured content/data is the product and most surfaces can be rendered at build time. |

Use the lighter starter whenever two choices would both work.

## Workflow

```text
Define
  Promise · Core action · Core loop · Canonical state · Success · Non-goals
    ↓
Vertical slice
  One user · one core action · one complete result
    ↓
Productize
  Mobile · empty/error · persistence if required · share · analytics · account if required
    ↓
Ship
  Contract checks · one durable browser smoke · build · deploy · observe
```

## Local scaffold

```bash
python3 scripts/new_app.py \
  --type interactive \
  --name my-app \
  --title "My App" \
  --output ../my-app
```

The script only performs deterministic copying and token replacement. Product decisions remain the job of `SKILL.md` and the agent using it.

## Repository layout

```text
SKILL.md                 Agent-facing product build contract
AGENTS.md                Entry point for coding agents
common/                  Files every generated project receives
starters/minimal/        No-framework starter
starters/interactive/    React + TypeScript + Vite starter
starters/content-data/   Astro + TypeScript + Tailwind starter
references/              Durable product/architecture guidance
scripts/new_app.py       Deterministic scaffold copier
```

## Core rule

> Fix repeated decisions. Do not template the product itself.

A new app should spend its time on four things: **the user problem, the core loop, the domain model, and the visual personality**. Everything else in this repository exists to shorten the path from idea to a product that is actually usable.

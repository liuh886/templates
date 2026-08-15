# Architecture defaults

## Choose the lightest runtime

1. `minimal` if browser-native HTML/CSS/JS is sufficient.
2. `interactive` if meaningful client state/component composition warrants React.
3. `content-data` if structured content/data is the product and build-time rendering is dominant.

Do not introduce a heavier runtime to prepare for hypothetical future needs.

## State authority

For each persisted fact, name one writer.

```text
canonical state
    ↓
derived projection
    ↓
UI
```

Caches, indexes, compiled content, dashboards, summary JSON and analytics are not canonical when they can be rebuilt.

## Persistence decision

Prefer, in order:

1. no persistence if the task does not need it;
2. browser-local persistence for user-local state;
3. repository/static canonical data for curated public content when suitable;
4. Supabase when authenticated, cross-device, multi-user, server-trusted or operational persistence is genuinely required.

Do not create two writable stores for convenience.

## Module boundary

Separate:

- domain rules and canonical data semantics;
- application/session state;
- UI components/rendering;
- external service adapters.

Do not split tiny products into layers that contain no real responsibility.

## Dependency rule

Before adding a dependency:

1. inspect the current repo's dependencies;
2. use an existing maintained dependency if it already solves the problem;
3. otherwise prefer a mature maintained library;
4. write a custom implementation only when the dependency cost or semantics are clearly worse.

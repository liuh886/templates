# Product engineering rules

Read `PRODUCT.md` before changing architecture or adding features.

- Build and protect the core user loop first.
- Use the simplest implementation that satisfies the current product contract.
- Inspect existing dependencies before adding a package or rewriting a capability.
- Keep components/modules focused and separate domain rules from UI rendering.
- Give every persisted fact one canonical write authority; rebuild projections.
- Do not add speculative configuration, abstractions, roles, services or infrastructure.
- Delete superseded code and paths. Do not add compatibility layers, migration shims, aliases or fallback readers.
- Prefer mature maintained libraries when a dependency is genuinely needed.
- Tests protect domain invariants and the durable user loop, not sample content or implementation details.
- Judge completion from the user's ability to finish the task, not from feature count.

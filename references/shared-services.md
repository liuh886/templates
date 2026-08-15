# Shared services

Shared services centralize capability, not every product lifecycle.

## Hao Account / membership / billing

Canonical owner: `liuh886/admin`.

That repository owns the shared customer account shell, checkout, Stripe Customer Portal, Stripe webhook, entitlement synchronization, invitations and administrative operations.

A product repo owns only:

- its product code;
- its entitlement/product identifier;
- product-specific account placement;
- product-specific Pro copy and locked/unlocked behavior.

Do not copy shared checkout, portal, webhook or entitlement backends into a product repo.

Do not add an account merely because the capability exists. Add identity only when the core loop needs it.

## Analytics

Use Cloudflare Web Analytics for lightweight traffic/performance visibility where already available.

Keep GA4 product events small and consistent. Start with only the events that answer product questions:

```text
product_open
core_action_start
core_action_complete
share
install
sign_in
upgrade_view
purchase
```

A product may add a few domain events when they represent real product outcomes. Do not mirror every UI click into analytics and do not send private user content as event payloads.

## Persistence / backend

Do not add a backend by default.

When server persistence is required, follow the existing Supabase boundary used by Hao Apps: browser-safe credentials in the client, privileged operations in server-side functions, and one canonical table/path for each business fact.

## Deployment

Static GitHub Pages is the default when the product can be built and served statically. Introduce another hosting/runtime only when the core product requires it.

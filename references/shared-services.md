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

### Cloudflare Web Analytics is the default public-web baseline

Every public web app should have Cloudflare Web Analytics enabled before release unless the product explicitly opts out.

Choose exactly one installation path:

1. **Cloudflare automatic injection — preferred for proxied domains and Cloudflare Pages.** Enable Web Analytics in Cloudflare and leave the repository variable `CLOUDFLARE_WEB_ANALYTICS_TOKEN` unset.
2. **Manual deployment injection — default for GitHub Pages or DNS-only sites.** Register the deployed hostname in Cloudflare Web Analytics, then set the GitHub Actions repository variable `CLOUDFLARE_WEB_ANALYTICS_TOKEN` to that site's token. The generated deploy workflow injects the beacon into built HTML immediately before upload.

Never enable both paths. Cloudflare supports only one Web Analytics beacon per page, and a site token is tied to the configured hostname/apex domain; do not bake one global token into this template repository.

The manual path is implemented by `scripts/inject-cloudflare-web-analytics.mjs`. It is deliberately build-output-only: application source stays framework-neutral, the script is idempotent, and analytics does not become a runtime dependency or a second product state.

Cloudflare Web Analytics is for page traffic and real-user performance. Its SPA measurement follows History API route changes automatically; hash-based routers are not supported. It does not provide custom product events.

If a site uses a Content Security Policy, allow the Cloudflare beacon script and its reporting endpoint according to the active automatic/manual setup.

Do not store the Cloudflare Web Analytics token or traffic data in Supabase. No database table, RLS policy, Edge Function, or synchronization path is needed for this baseline.

### Product events

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

Cloudflare Web Analytics and GA4 have different jobs: Cloudflare answers traffic/performance questions; product events answer whether the core loop is being used.

## Persistence / backend

Do not add a backend by default.

When server persistence is required, follow the existing Supabase boundary used by Hao Apps: browser-safe credentials in the client, privileged operations in server-side functions, and one canonical table/path for each business fact.

Analytics alone is never a reason to add Supabase.

## Deployment

Static GitHub Pages is the default when the product can be built and served statically. Introduce another hosting/runtime only when the core product requires it.

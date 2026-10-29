# nmn.fyi

Read `SPEC.md` in full before any work in this repo. It is the only source of truth for what gets built, the gate process, and the report format at the end of every gate.

State: Gates 0-2 merged to main and live on nmn.fyi. Gate 3 (theses collection) is next, only on Naman's go.

Ops:
- Vercel project `nmn-fyi`, id `prj_dAs19OyKVnAVeT6ZxTc1xS7tM92v`, API token at `~/.vercel/token`. Prefer quiet one-line output when calling the API; never print the token.
- Before reporting a gate: `npm run build` with zero errors and zero warnings, and confirm "N page(s) built" matches expectations (an Astro build with no src/pages file produces an empty site with only a WARN).
- Relative component imports need explicit `.astro` extensions.
- Never write Naman's prose: use TODO placeholders. No em dashes in site copy or commit messages.

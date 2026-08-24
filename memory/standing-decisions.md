## Current standing decisions — do not change without explicit user instruction

These are settled. Don't re-derive, re-litigate, or "helpfully" revisit any of
them from first principles — if one seems wrong, ask the user before acting.
Full reasoning and history for each: `reference/history/zenodo-and-exposure-posture.md`.

- **No GitHub Release, no Zenodo deposit, ever, unless the user says
  otherwise** (replaced 2026-08-08; the earlier policy that tied a release to
  "all four tables final" no longer applies — all four *are* final, and that
  does not make a release due). **A doi reappearing anywhere in this repo is a
  regression, not a restoration.** The Zenodo record itself was deleted by the
  user 2026-08-08 (within Zenodo's 30-day owner-delete window); what survives
  is a public HTTP-410 tombstone, not an archived copy.
- **The edition is not promoted, and indexing is not a goal either way**
  (set 2026-08-08). No inbound link — Wikidata, Wikipedia, AMNH, anywhere — is
  seeded without asking first. `GOOGLE_SITE_VERIFICATION` must never be
  blanked (Search Console ownership is the only mechanism for a future
  takedown request, independent of the exposure decision).
- **De-indexing is closed — not important, nothing to be done.** Do not
  re-raise it as an obvious follow-on to "low exposure"; those are different
  requests and only one was made. `robots.txt`, `sitemap.xml`, JSON-LD, and the
  absence of `noindex` all stay exactly as the build emits them.
  (`Disallow:` in `robots.txt` forbids crawling, it does not de-index; `<meta
  name="robots" content="noindex">` is the tool that would, and it requires
  crawling to stay allowed — neither is deployed, and the two must never be
  combined.)
- **Wikidata is removed, permanently — no item is to be created.** The old
  payload is gone from the working tree (survives in git history only). **Do
  not offer a Wikidata item as an "easy win"** — it was the highest-return
  inbound link on the old outreach plan, which is exactly why a future
  session will be tempted to propose it again.
- **The `/search/` provenance line stays exactly where it is — closed
  2026-08-21, offered four times before that; do not offer to move it again.**
  `/search/`'s own footer note already **is** that page's provenance block;
  the landing page stays silent on identity joins by decision, not by
  oversight.
- **The edition stays on `pueblogenealogy.github.io` — no custom domain,
  ever (closed 2026-07-31).** This was decided on durability, not SEO
  (`github.io` is a public suffix; no authority gained or lost either way): a
  domain you own is portable but only survives as long as someone pays for it,
  and a lapsed one gets re-registered under every citation that pointed at it.
  `SITE` in `make_chart.py` never changes; no `CNAME` file is ever added.
- **All four plates are published and fully read** — placement on all four,
  orthography on Genealogy I, III and IV. Genealogy II has had placement only;
  its orthography (248/249's medial marks) is the one open reading question on
  any plate. See `SESSION-NOTES.md` for current status, not this file.

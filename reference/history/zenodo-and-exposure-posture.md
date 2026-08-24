# Zenodo, releases, and exposure posture — full history

Not auto-loaded. The binding conclusions live in `memory/standing-decisions.md`
(always loaded) — do not act against those without asking the user first, even
after reading the reasoning here. This file exists so the reasoning isn't
lost, not to reopen anything.

## Release policy — replaced 2026-08-08

The original policy (set 2026-07-30): cut no releases *during active
development*, cut one when all four tables, the design, the transcriptions,
the text and the citations were final. By 2026-08-08 all four were final —
under the old policy, that reads as "the release is due." **It was replaced,
not satisfied.** (A v1.1.0 release had already been prepared and cancelled in
2026-07, before the policy itself changed.) The current policy: no GitHub Release, no Zenodo deposit,
ever, unless the user says otherwise. The site keeps deploying from `main` as
it always has; publishing the site and cutting a release are different acts,
and only the second one ever touched Zenodo.

## Withdrawing Zenodo from the edition's public face (2026-08-08)

What was removed, so nobody has to re-derive it:

- `.zenodo.json` — deleted.
- `DOI`/`DOI_URL` in `make_chart.py` — deleted, along with the footer
  citation's "Archived at" line and the `identifier` field in both JSON-LD
  blocks (`Dataset` on table pages, `CollectionPage` on the landing page).
- `CITATION.cff` — the `doi:` field and the whole `identifiers:` block gone
  (this is the repo's "Cite this repository" widget — the most visible place a
  doi could reappear).
- `README.md` — the DOI badge and archiving paragraph gone.
- The Zenodo deposit webhook on the repo — removed. Two things learned
  deleting it: the hook id is **not stable** (Zenodo replaced it mid-session,
  so a stale id returns `Not Found` exactly as an unscoped token would — this
  is a false negative, not a symptom of anything broken); and GitHub's side is
  not the durable switch — Zenodo can recreate the hook while the repo is
  still enabled at `zenodo.org/account/settings/github`. The user has since
  severed the GitHub↔Zenodo link, which settles it for good.
- The webhook's access token was never findable under GitHub settings or
  Zenodo → Applications, and that's expected, not a symptom: the URL carried
  `?access_token=...` pointing at Zenodo, so it was a Zenodo credential minted
  internally for the webhook receiver, not a hand-created token. Severing the
  linked account invalidates it regardless.

## The record deletion, and the rule most people repeat about it is wrong

The record itself was deleted by the user the same day (2026-08-08), 11 days
after v1.0.0 published (2026-07-28). **Zenodo lets a record's OWNER delete it
within 30 days of publishing** — the widely-repeated claim that "published
Zenodo records are permanent, only support can withdraw them" is false for
those first 30 days; it's only true afterward, which is why it's the version
everyone knows. What survives is a **tombstone, not the deposit**: both dois
(`...21637900` concept, `...21637901` v1.0.0) now return HTTP 410 Gone. The
metadata is kept and **publicly visible** — title, author, year, doi, and the
removal reason, which reads "Personal data issue." A tombstone cannot be
removed; that part really is permanent. **A doi reappearing anywhere in this
repo would be a regression, not a restoration.**

## Exposure posture — set by the user, 2026-08-08

The user does not want the edition promoted, and does not care whether the
site is indexed — a reversal of the outreach programme that ran from launch
through 2026-08-07. Wikidata was removed (item deleted, payload gone from the
working tree, survives only in git history). No inbound link is seeded
without asking — this closed the gate the custom-domain decision (below) had
briefly opened.

**De-indexing was carried as an open thread for two sessions, awaiting a
choice of level, until the user struck it entirely on 2026-08-08: not
important, nothing to be done.** Don't conflate "don't promote it" with "take
it out of Google" — they're different requests and only the first was made.
The mechanism is kept in place because it's what makes the closure cheap to
hold, and because the intuitive move is the wrong tool: `Disallow:` in
`robots.txt` forbids crawling but doesn't de-index an already-indexed URL (it
can persist as a bare, un-re-crawlable link); `<meta name="robots"
content="noindex">` is what actually removes a page, and it requires crawling
to stay *allowed* — the two must never be combined. Neither is deployed.
`GOOGLE_SITE_VERIFICATION` must never be blanked regardless of exposure
posture, since Search Console ownership is the only mechanism a future
takedown request would run through.

The AMNH handle (`2246/158`, `https://digitallibrary.amnh.org/handle/2246/158`,
found 2026-07-30) is kept as a **fact about the source**, not an outreach
step — it's a route to a better scan, though it's no longer the only route or
the first one to try: a photograph of the page settled persons 156 and 157 on
2026-08-08 after the scan couldn't, so ask for a photograph first. Note
`digitallibrary.amnh.org` 403s automated fetches —
use a real browser, not `WebFetch`.

## Custom domain — closed 2026-07-31, and the argument that settled it is not the obvious one

The edition stays on `pueblogenealogy.github.io` permanently. This was
carried as "deferred, not closed" through several sessions (and went missing
from a `resume` list once) before the user closed it outright — a future
session re-deriving this from scratch would likely reach the wrong answer, so
the reasoning is kept in full here.

**It is not an SEO question.** Google treats `github.io` as a public suffix,
so no authority is inherited from it and none is lost by leaving — the old
framing of a custom domain as "the strongest SEO upgrade" was simply wrong.
**The real trade is durability against portability, and durability won.** A
domain you own is portable (can change hosts without breaking a doi-adjacent
link) but survives only as long as someone keeps paying for it — a lapsed
domain doesn't degrade gracefully, it gets re-registered, and every citation
seeded from Zenodo, Wikidata and AMNH then points at whoever bought it.
`pueblogenealogy.github.io` needs no renewal, can't lapse, can't be squatted.
For an edition meant to outlive the attention of its editor, GitHub's
institutional durability beats the editor's own — that's the whole argument.
Consequences: `SITE` in `make_chart.py` never changes; no `CNAME` file is ever
added; Search Console and Bing stay verified (now for a second, independent
reason — see *Exposure posture* above).

This closure had briefly lifted the gate on seeding inbound links — that
sentence was withdrawn 2026-08-08 once the user asked for low exposure. The
domain decision itself is untouched by that; only the inbound-link
consequence of it was.

# Gud apps site: agent instructions

The public website for the owner's four iPhone apps (Vocable, CycleSync,
Rungud, Met), served by GitHub Pages from this repo's `main` branch at
`https://angadb.github.io/vocable-site/`. Read `~/design-guide/AGENTS.md`
first for the brand and how the owner works.

## How it is built

- `build.py` writes every page. App names, copy, status and contact
  addresses are the `APPS` table at its top. Run `python3 build.py` and
  commit the generated HTML with it. No dependencies.
- `content/` holds the hand-written legal and support text as HTML
  fragments: `<app>-privacy.html`, `<app>-support.html`,
  `vocable-terms.html`. The first line is a comment that becomes the date
  line. `{{EMAIL}}` is replaced with the app's contact address.
- `assets/site.css` is the one stylesheet. No web fonts, no scripts, no
  analytics: the site keeps the promise the apps make.
- `assets/icons/` are the brand icons, drawn by
  `swift ~/design-guide/scripts/make-icons.swift <app> <dir>` and scaled
  to 360 px with `sips`.
- All links are relative, so the site works under any base path. Only
  the social-sharing tags use the absolute `BASE` in `build.py`.

## Rules

- Pushing to `main` publishes. Ask the owner before pushing.
- Vocable is in the App Store and its listing links to `privacy.html` and
  `terms.html` at the site root. Those two addresses must keep working;
  they redirect to `vocable/`.
- Vocable's legal text describes the shipped app. Do not change what it
  says without the owner. The other three policies describe unreleased
  apps and must be checked against each app before its release.
- A policy may only claim what the app's code does. Check before
  writing "no network requests" or similar.
- No em dashes. No emoji. Dry, kind voice; plain in policies.
- CycleSync: nothing here says "period".

## State (2026-10-08)

Branch `gud-apps` holds the rebuild as a multi-app site in the Gud apps
brand. It is not merged and not pushed. Checked by rendering in headless
Chrome: the home page, the Met page, the Vocable page at a narrow width,
and two policy pages. Dark mode was written but not looked at.

Open decisions for the owner:
- Where the site lives. Other apps' pages currently sit under a
  `vocable-site` address. A custom domain would fix that and GitHub
  redirects the old addresses to it.
- A contact address for CycleSync, Rungud and Met. They use Vocable's
  for now.
- The App Store link for Vocable (none is on the site yet).
- The Vocable page shows the new book icon, which is not in the App
  Store build yet.

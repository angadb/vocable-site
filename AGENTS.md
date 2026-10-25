# Gud apps site: agent instructions

The public website for the owner's seven iPhone apps (Talkgud (was Vocable), Lovegud (was CycleSync),
Rungud, Minglegud (was Met), Gymgud, Bolgud, Eatgud), served by GitHub Pages from this repo's `main` branch at
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
- Talkgud is in the App Store and its listing links to `privacy.html` and
  `terms.html` at the site root. Those two addresses must keep working;
  they redirect to `vocable/`.
- Talkgud's legal text describes the shipped app. Do not change what it
  says without the owner. The other policies describe unreleased
  apps and must be checked against each app before its release.
- A policy may only claim what the app's code does. Check before
  writing "no network requests" or similar.
- No em dashes. No emoji. Dry, kind voice; plain in policies.
- Lovegud: nothing here says "period".
- Names: Lovegud is the visible name, but the `APPS` key, folder `cyclesync/`, fragments
  `content/cyclesync-*` and `assets/icons/cyclesync.png` keep the old name so every address works
  (same for `vocable` and `met`).
- A page's date (the first-line comment of its fragment) changes only when that page's text changes.

## State (2026-10-25)

Seven apps, three pages each (landing, privacy, support; Talkgud also terms), all built by
`build.py`. New this session: Gymgud, Bolgud, Eatgud; Lovegud renamed; Lovegud, Rungud and
Minglegud policies rewritten from their code. Talkgud's pages and the root `privacy.html`
and `terms.html` redirects are unchanged. Local commits only, nothing pushed.

Policies were checked by reading the code of each app (Lovegud, Rungud, Minglegud, Gymgud,
Bolgud, Eatgud) on 2026-10-25, not by running them. Gymgud policy follows a build that is
"compiled and engine-tested only". Seen rendered in headless Chrome: home (narrow and wide),
the Lovegud, Gymgud, Bolgud and Eatgud pages (narrow; Lovegud and Gymgud also wide), the
Gymgud and Lovegud privacy pages. Not looked at: dark mode (written, not seen), the support
pages and the Rungud, Minglegud, Talkgud pages after the change.

Open decisions for the owner:
- Contact address: all seven apps still use `GudApps@icloud.com`.
- Lovegud status pill stays "Coming soon" (is 1.0 live?). Lovegud's site colour is still cobalt
  while the app now uses ink chrome.
- Where the site lives (custom domain or the `vocable-site` address).
- Talkgud App Store link and icon (see earlier note: site shows the new book icon).
- App issues found while reading code, not fixed here: Lovegud setup and Calendar say
  "period" in app text; Minglegud's counts screen and "Include my numbers" switch are
  DEBUG only while the feedback email includes the counts by default; Gymgud has no in-app
  erase and leaves its iCloud copy after delete; Bolgud content is unreviewed and no audio
  ships; Eatgud "Erase everything" keeps settings.

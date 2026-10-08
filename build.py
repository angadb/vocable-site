#!/usr/bin/env python3
"""Builds the Gud apps site: plain static HTML, written next to this file.

Run `python3 build.py` after changing anything here or in `content/`, then
commit the generated pages too (GitHub Pages serves them as they are).
All links are relative, so the site works under any base path.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
# Only used for social-sharing tags, which need absolute URLs.
BASE = "https://angadb.github.io/vocable-site/"
MAKER = "Angad Bedi"
LEGAL_NAME = "Angad Singh Bedi"
YEAR = "2026"
UPDATED = "8 October 2026"

APPS = {
    "vocable": {
        "name": "Vocable",
        "kicker": "A word a day",
        "line": "One good word each morning, and the means to keep it.",
        "lede": "One curated word a day with its definition, an example and a quiz for the ones that got away. Every feature is free.",
        "status": "On the App Store",
        "live": True,
        "email": "VocableSupport@icloud.com",
        "lead": ("Today's word", "serendipity", "The occurrence of events by chance in a happy or beneficial way."),
        "features": [
            ("A word every morning", "Hand-picked, with phonetics, examples, synonyms and antonyms."),
            ("Quizzes for the ones you missed", "Flashcards built from the words you got wrong, and a recall of yesterday's word."),
            ("Streaks that forgive", "A daily streak with a weekly freeze, because life happens."),
            ("Your library", "Every word you have seen, liked or looked up. Searchable and exportable."),
            ("Works offline", "Definitions you have seen before are kept on the phone."),
            ("Reminders you choose", "The word in the morning and a nudge in the evening, at the times you pick."),
        ],
        "data": "No account, no ads, no tracking. Your words stay on your phone, or in your own iCloud if you turn sync on. Definitions come from the Free Dictionary API, which is sent the word and nothing else.",
        "extra": ("Free, with a tip jar", "There is no subscription and nothing to unlock. An optional tip inside the app helps cover the developer account fee."),
        "has_terms": True,
    },
    "cyclesync": {
        "name": "CycleSync",
        "kicker": "A daily cue for partners",
        "line": "One quiet cue a day for the partner of someone with a cycle.",
        "lede": "A discreet helper for partners. It tells you what to offer today, shows roughly where the month is going, and keeps a short playbook written from evidence.",
        "status": "Coming soon",
        "live": False,
        "email": "VocableSupport@icloud.com",
        "lead": ("Today", "Comfort", "A warm drink and an early night are on offer. No questions asked."),
        "features": [
            ("One cue a day", "A single suggestion for what to offer today. It never tells you how anyone feels."),
            ("A calendar that admits doubt", "The next start is shown as a window, estimated from the dates you have logged."),
            ("A playbook from evidence", "Short, practical and sourced. It includes what you need too."),
            ("Discreet by design", "Lock it with Face ID. Widgets and notifications never show dates or counts."),
        ],
        "data": "No account and no network connection at all. The dates and settings you enter stay on your phone. A backup is a file you export yourself and keep wherever you like.",
        "extra": None,
        "has_terms": False,
    },
    "rungud": {
        "name": "Rungud",
        "kicker": "Running, from Apple Health",
        "line": "A training plan built on the phone from the runs you already do.",
        "lede": "Rungud reads your runs from Apple Health, builds a plan from plain rules, and adjusts the weeks ahead to what you actually ran. No coach in the cloud.",
        "status": "Coming soon",
        "live": False,
        "email": "VocableSupport@icloud.com",
        "lead": ("Today's run", "8 km easy", "Conversational pace. If you can't chat, you're racing."),
        "features": [
            ("Reads, never writes", "Your running workouts come from Apple Health. Rungud only reads them."),
            ("A plan from rules", "Phases, weekly distance and paces worked out on the phone. No AI and no server."),
            ("It adjusts to you", "Missed a run or ran long? The weeks ahead change to fit."),
            ("Your data, out", "Export your runs as CSV or JSON, or as a summary you can hand to whoever coaches you."),
        ],
        "data": "No account and no network connection. Health data is read on your phone and stays there. Nothing is used for advertising, and nothing is shared unless you export a file yourself.",
        "extra": None,
        "has_terms": False,
    },
    "met": {
        "name": "Met",
        "kicker": "Remember the people you meet",
        "line": "Say who you met. Met keeps the name, the face and how you know them.",
        "lede": "Tell it who you met, the way you'd tell a friend. Met sorts that into a card, gives it a face you'll recognise, and quizzes you before the name slips.",
        "status": "Coming soon",
        "live": False,
        "email": "VocableSupport@icloud.com",
        "lead": ("Due today", "4 people", "Start with Sneh, then 3 more."),
        "features": [
            ("Say it, don't file it", "Speak or type a few lines. Apple Intelligence sorts them into a card on your iPhone."),
            ("A face you'll recognise", "Describe someone and your iPhone draws them. Or use their initials."),
            ("How you know them", "Every person has a trail: through Alex, through work. Circles hold the rest."),
            ("Review before it fades", "Short spaced reviews for names, faces and the facts worth keeping."),
        ],
        "data": "No account and no network connection. What you note about people stays on your iPhone. The microphone is used only when you tap it, and what you say is transcribed on the phone and not kept.",
        "extra": None,
        "has_terms": False,
    },
}
ORDER = ["vocable", "cyclesync", "rungud", "met"]


def dotted(text):
    """A hero word or line ending in the brand dot as its full stop."""
    return f'{escape(text)}<span class="dot" aria-hidden="true">.</span>'


def page(path, title, description, body, app=None, nav=()):
    depth = len(Path(path).parts) - 1
    up = "../" * depth
    icon = f"{up}assets/icons/{app}.png" if app else f"{up}assets/dot.svg"
    social = BASE + (f"assets/icons/{app}.png" if app else "assets/icons/vocable.png")
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if current else ""}>{escape(label)}</a>'
        for label, href, current in nav
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{icon}">
<link rel="apple-touch-icon" href="{icon}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}{'' if path == 'index.html' else path.replace('index.html', '')}">
<meta property="og:image" content="{social}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{up}assets/site.css">
</head>
<body{f' data-app="{app}"' if app else ''}>
<div class="wrap">
<nav class="nav" aria-label="Site">
<a class="mark" href="{up}index.html">Gud apps<span class="dot" aria-hidden="true">.</span></a>
<div class="links">{links}</div>
</nav>
{body}
<footer>
<div>
<div class="maker">{MAKER}<span class="dot" aria-hidden="true">.</span></div>
<div class="family">Gud apps. &copy; {YEAR} {LEGAL_NAME}</div>
</div>
<div class="links">{footer_links(app, up)}</div>
</footer>
</div>
</body>
</html>
"""
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)


def footer_links(app, up):
    if not app:
        return "".join(f'<a href="{key}/index.html">{APPS[key]["name"]}</a>' for key in ORDER)
    info = APPS[app]
    links = [("Privacy", "privacy.html")]
    if info["has_terms"]:
        links.append(("Terms", "terms.html"))
    links.append(("Support", "support.html"))
    links.append(("All apps", f"{up}index.html"))
    return "".join(f'<a href="{href}">{label}</a>' for label, href in links)


def app_nav(app, current):
    info = APPS[app]
    items = [(info["name"], "index.html"), ("Privacy", "privacy.html")]
    if info["has_terms"]:
        items.append(("Terms", "terms.html"))
    items.append(("Support", "support.html"))
    return [(label, href, href == current) for label, href in items]


def home():
    tiles = ""
    for key in ORDER:
        info = APPS[key]
        tiles += f"""<a class="app" data-app="{key}" href="{key}/index.html">
<img src="assets/icons/{key}.png" alt="" width="72" height="72">
<div>
<div class="name">{dotted(info["name"])}</div>
<div class="line">{escape(info["line"])}</div>
<div class="where">{escape(info["status"])}</div>
</div>
</a>
"""
    body = f"""<main>
<header class="hero">
<div class="kicker">Four small apps for iPhone</div>
<h1 class="display">Apps that mind their own business<span class="dot" aria-hidden="true">.</span></h1>
<p class="lede">Each one does a single job, keeps what you tell it on your phone, and then gets out of the way.</p>
</header>
<section aria-label="The apps">
<div class="tiles">
{tiles}</div>
</section>
<section>
<h2 class="display">House rules</h2>
<div class="tiles">
<div class="tile"><h3>Your data stays yours</h3><p>No accounts and no servers. What you put in an app stays on your phone, or in your own iCloud where an app offers sync.</p></div>
<div class="tile"><h3>No ads, no tracking</h3><p>None of the apps contain analytics, advertising or anything that follows you around.</p></div>
<div class="tile"><h3>One look, done properly</h3><p>The apps follow your iPhone's text size, appearance and accessibility settings instead of inventing their own.</p></div>
<div class="tile"><h3>Made by one person</h3><p>{MAKER} designs and builds all four. No team, no investors, nobody to sell you to.</p></div>
</div>
</section>
</main>"""
    page("index.html", "Gud apps", "Four small iPhone apps by Angad Bedi: Vocable, CycleSync, Rungud and Met. No accounts, no ads, no tracking.",
         body, nav=[(APPS[k]["name"], f"{k}/index.html", False) for k in ORDER])


def app_home(key):
    info = APPS[key]
    kicker, big, small = info["lead"]
    features = "".join(f'<div class="tile"><h3>{escape(t)}</h3><p>{escape(p)}</p></div>\n' for t, p in info["features"])
    extra = ""
    if info["extra"]:
        extra = f'<section><h2 class="display">{escape(info["extra"][0])}</h2><p>{escape(info["extra"][1])}</p></section>'
    body = f"""<main>
<header class="hero">
<img class="icon" src="../assets/icons/{key}.png" alt="{escape(info["name"])} app icon" width="96" height="96">
<div class="kicker">{escape(info["kicker"])}</div>
<h1 class="display">{dotted(info["name"])}</h1>
<p class="lede">{escape(info["lede"])}</p>
<div class="status{' live' if info['live'] else ''}">{escape(info["status"])}</div>
<div class="lead" role="img" aria-label="How the app looks: {escape(kicker)}, {escape(big)}. {escape(small)}">
<div class="kicker">{escape(kicker)}</div>
<div class="big display">{dotted(big)}</div>
<p>{escape(small)}</p>
</div>
</header>
<section>
<h2 class="display">What it does</h2>
<div class="tiles">
{features}</div>
</section>
{extra}
<section>
<h2 class="display">Your data</h2>
<p>{escape(info["data"])} The full version is in the <a href="privacy.html">privacy policy</a>.</p>
</section>
</main>"""
    page(f"{key}/index.html", f'{info["name"]}: {info["kicker"]}', info["lede"], body, app=key, nav=app_nav(key, "index.html"))


def doc(key, file, heading, date_line, inner, description):
    info = APPS[key]
    body = f"""<main class="doc">
<div class="kicker">{escape(info["name"])}</div>
<h1 class="display">{escape(heading)}</h1>
<p class="date">{escape(date_line)}</p>
{inner}
</main>"""
    page(f"{key}/{file}", f'{info["name"]}: {heading}', description, body, app=key, nav=app_nav(key, file))


def fragment(name):
    """A hand-written HTML fragment from content/. First line is a comment holding the date line."""
    text = (ROOT / "content" / name).read_text()
    first, rest = text.split("\n", 1)
    return first.replace("<!--", "").replace("-->", "").strip(), rest


def support(key):
    info = APPS[key]
    inner, _ = None, None
    date, inner = fragment(f"{key}-support.html")
    mail = info["email"]
    inner = inner.replace("{{EMAIL}}", f'<a href="mailto:{mail}">{mail}</a>')
    doc(key, "support.html", "Support", date, inner, f'Help and contact for {info["name"]}.')


def redirect(path, target, label):
    (ROOT / path).write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{label}</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<div class="wrap"><main class="doc" style="padding-top:48px">
<p>This page has moved: <a href="{target}">{label}</a>.</p>
</main></div>
</body>
</html>
""")


def main():
    home()
    for key in ORDER:
        info = APPS[key]
        app_home(key)
        date, inner = fragment(f"{key}-privacy.html")
        mail = info["email"]
        inner = inner.replace("{{EMAIL}}", f'<a href="mailto:{mail}">{mail}</a>')
        doc(key, "privacy.html", "Privacy Policy", date, inner, f'What {info["name"]} does with your data: it stays on your device.')
        if info["has_terms"]:
            date, inner = fragment(f"{key}-terms.html")
            doc(key, "terms.html", "Terms & Conditions", date, inner, f'Terms for using {info["name"]}.')
        support(key)
    # The shipped Vocable listing links to these two addresses. Keep them working.
    redirect("privacy.html", "vocable/privacy.html", "Vocable privacy policy")
    redirect("terms.html", "vocable/terms.html", "Vocable terms")
    print("built", sum(1 for _ in ROOT.rglob("*.html")), "pages")


if __name__ == "__main__":
    main()

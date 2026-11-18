#!/usr/bin/env python3
"""
Build the LollieVox static site.

    python3 build.py   -> writes index.html, about.html, contact.html

Edit the text here, rebuild, commit, push. GitHub Pages serves the result.
"""
import html

# Contact form: Web3Forms access key (public by design). Leave "" until the key exists;
# the form then tells visitors to use email instead.
WEB3FORMS_KEY = ""

VOCAL_PACK_URL = "https://mailchi.mp/28d496237324/lollievox-bronze-vocal-pack"
MUSIC_URL = "https://music.lollievox.com"
YOUTUBE_URL = "https://www.youtube.com/user/Lollievox"
FACEBOOK_URL = "https://www.facebook.com/Lollievox"
BANDCAMP_EMBED = ("https://bandcamp.com/EmbeddedPlayer/album=2828031416/size=large/"
                  "bgcol=333333/linkcol=9a64ff/minimal=true/transparent=true/")
YOUTUBE_EMBED = "https://www.youtube-nocookie.com/embed/6J58nEsRAwQ?rel=0"

# Email addresses are assembled in the browser so scrapers don't harvest them from the page source.
EMAILS = {"booking": ("lollievox", "lollievox.com"), "general": ("laurie", "lollievox.com")}


def esc(s):
    return html.escape(s, quote=True)


NAV = [("index.html", "Home"), (MUSIC_URL, "Music"), (YOUTUBE_URL, "YouTube"),
       ("about.html", "About"), ("shop.html", "Shop"), ("contact.html", "Contact")]


def page(filename, title, description, body):
    items = []
    for href, label in NAV:
        ext = href.startswith("http")
        cur = ' aria-current="page"' if href == filename else ""
        rel = ' target="_blank" rel="noopener"' if ext else ""
        items.append(f'<li><a href="{href}"{cur}{rel}>{label}</a></li>')
    nav = "".join(items)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="top">
  <a class="logo" href="index.html"><img src="img/lollievox-logo.png" alt="LollieVox" width="1800" height="450"></a>
  <nav aria-label="Main"><ul>{nav}</ul></nav>
</header>
<main id="content">
{body}
</main>
<footer class="foot">
  <p>&copy; LollieVox &mdash; ART Webb Design</p>
</footer>
<script src="js/site.js"></script>
</body>
</html>
"""


def listen_block():
    return f"""
<section class="listen">
  <div class="embed">
    <h2>Listen now</h2>
    <iframe title="LollieVox on Bandcamp" src="{BANDCAMP_EMBED}" seamless loading="lazy"
      style="border:0;width:100%;max-width:520px;aspect-ratio:1/1;height:auto"></iframe>
  </div>
  <div class="embed">
    <h2>FL Studio 20 Official Demo Song</h2>
    <div class="video"><iframe title="FL Studio 20 Official Demo Song" src="{YOUTUBE_EMBED}" loading="lazy"
      allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
    <p class="follow"><a href="{FACEBOOK_URL}" target="_blank" rel="noopener">Follow LollieVox on Facebook</a></p>
  </div>
</section>
"""


def build_home():
    return f"""
<section class="hero" style="background-image:url('img/Lollievox-cover-web.jpg')" aria-label="LollieVox">
  <div class="hero-bar">
    <p class="promo">Get a free download of LollieVox&rsquo;s latest vocal sample pack, available for a limited time!</p>
    <a class="btn" href="{VOCAL_PACK_URL}" target="_blank" rel="noopener">Yes! I want my free vocal pack!</a>
  </div>
</section>
{listen_block()}
"""


ABOUT_PARAS = [
    "LollieVox aka Laurie Webb is a singer, songwriter hailing from Nashville, Tennessee. She wrote for LeAnne Rimes while at Curb Music Publishing (1997–2001) placing several songs in major films including “Angel Eyes” starring Jennifer Lopez, “Driven” starring Sylvester Stallone, “View from the Top Soundtrack” & more.",
    "2005 saw global success with single “Aren’t You Clever” released on world-renowned music program FL Studio, which led to a run of songs released in their program for their users to take apart & remix. They also released 3 vocal packs, LollieVox Harmor & the latest release of her single “I’ll Be Your Madonna” to be released on their 20.9 program in 2021.",
    "With 3 albums under her belt and a plethora of songs remixed by 1000’s of producers who post their remixes on YouTube, Bob Babbitt (The Shadows of Motown) as well as Ed Green (Marvin Gaye drummer) & The Memphis Horns contribution on her debut album “Dance with Me” 2005 is one of her favorite milestones.",
    "LollieVox is continually reinventing, adding skills and interests to her arsenal taking great interest in working with up and comers that excite her sensibilities. Currently working with talented South African producer Lezina J. Also writing with other artists & in an effort to empower young woman she has begun working on a soundtrack to an ‘eco-fantasy’ book that is to be produced as a movie.",
    "LollieVox continues to inspire and to be inspired looking forward to hearing new remixes from up & coming producers!",
]
INFO = [
    ("Genre", "Singer/Songwriter / Pop / Jazz / Remix"),
    ("Members", "Laurie Webb, Singer/Songwriter, Vocalist, Acoustic/Electric Guitar"),
    ("Hometown", "Nashville, TN"),
    ("Record Label", "LollieVox Productions, Inc."),
    ("Influences", "Joni Mitchell, Cheap Trick, Fleetwood Mac, Smokey Robinson, Marvin Gaye, Etta James, Shawn Colvin, The Innocence Mission, Jefferson Airplane"),
    ("Current Location", "Nashville, TN"),
]


def build_about():
    paras = "".join(f"<p>{esc(p)}</p>" for p in ABOUT_PARAS)
    info = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in INFO)
    u, d = EMAILS["general"]
    return f"""
<article class="prose">
  <h1>Laurie Webb of LollieVox</h1>
  <div class="two-col">
    <div>{paras}
      <h2>Band interests</h2>
      <p>We love to collaborate! We are constantly working with producers in all genres, ranging from Dance/Electronica to Pop to Americana</p>
      <h2>Artists we also like</h2>
      <p>The Sundays, Radiohead, PJ Harvey, Imogen Heap, Nirvana, Yeah Yeah Yeahs, Jeff Buckley, This is ART</p>
    </div>
    <div class="side">
      <img src="img/lollievox-slideshow-01.jpg" alt="Laurie Webb of LollieVox" width="1024" height="575">
      <h2>Basic info</h2>
      <dl class="info">{info}</dl>
      <h2>Contact info</h2>
      <p>Press contact: <a class="mail" data-u="{u}" data-d="{d}" href="contact.html">use the contact page</a></p>
    </div>
  </div>
</article>
{listen_block()}
"""


def build_contact():
    bu, bd = EMAILS["booking"]
    gu, gd = EMAILS["general"]
    return f"""
<article class="prose">
  <h1>Contact</h1>
  <dl class="info contact-list">
    <dt>Booking/Management</dt><dd><a class="mail" data-u="{bu}" data-d="{bd}" href="#">email</a></dd>
    <dt>Remix/Vocal Inquiries</dt><dd><a class="mail" data-u="{bu}" data-d="{bd}" href="#">email</a></dd>
    <dt>General Inquiries</dt><dd><a class="mail" data-u="{gu}" data-d="{gd}" href="#">email</a></dd>
  </dl>
  <form id="contact-form" class="form" action="https://api.web3forms.com/submit" method="POST" data-key="{WEB3FORMS_KEY}">
    <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
    <input type="hidden" name="subject" value="New message from the LollieVox website">
    <input type="hidden" name="from_name" value="LollieVox website">
    <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <label>Your name (required)<input name="name" required autocomplete="name"></label>
    <label>Your email (required)<input type="email" name="email" required autocomplete="email"></label>
    <label>Subject<input name="subject_line"></label>
    <label>Your message<textarea name="message" rows="6" required></textarea></label>
    <button class="btn" type="submit">Send</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form>
</article>
{listen_block()}
"""


def build_shop():
    return """
<article class="prose">
  <h1>Shop</h1>
  <p>LollieVox merch is on its way: shirts and other gear, printed and shipped on demand. Check back soon, or <a href="contact.html">send a note</a> and we&rsquo;ll tell you when it opens.</p>
  <div class="placeholder-grid" aria-hidden="true">
    <div class="ph">T-shirt<br><small>coming soon</small></div>
    <div class="ph">Hoodie<br><small>coming soon</small></div>
    <div class="ph">Stickers<br><small>coming soon</small></div>
  </div>
  <p><a class="btn" href="%s" target="_blank" rel="noopener">Get the free vocal pack</a></p>
</article>
""" % VOCAL_PACK_URL

PAGES = [
    ("index.html", "LollieVox – Official website for Laurie Webb of LollieVox",
     "Official website for Laurie Webb of LollieVox. Acclaimed singer/songwriter known for her hits from FL Studio Demo Songs.", build_home),
    ("about.html", "About LollieVox (Laurie Webb)",
     "About Laurie Webb of LollieVox: Nashville singer/songwriter, FL Studio vocal packs, and collaborations with producers worldwide.", build_about),
    ("shop.html", "Shop \u2013 LollieVox", "LollieVox merch: shirts and gear, coming soon.", build_shop),
    ("contact.html", "Contact LollieVox",
     "Contact LollieVox for booking, management, remix and vocal inquiries.", build_contact),
]

if __name__ == "__main__":
    for fname, title, desc, fn in PAGES:
        with open(fname, "w", encoding="utf-8") as f:
            f.write(page(fname, title, desc, fn()))
        print("wrote", fname)

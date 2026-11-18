# LollieVox website

Static rebuild of lollievox.com (Laurie Webb of LollieVox). No build tools needed to view; edit `build.py`
(text and links), run `python3 build.py`, commit and push. GitHub Pages serves the result.

- `build.py` generates `index.html`, `about.html`, `contact.html`
- `css/style.css`, `js/site.js`, `img/`
- Contact form uses Web3Forms: set `WEB3FORMS_KEY` in `build.py` (the form shows an email fallback until then)
- Not yet done: DNS cutover (keep MX/email records and `music.lollievox.com` as they are)

from html.parser import HTMLParser
from urllib.request import urlopen

class _SectionParser(HTMLParser):
    def __init__(self, start_heading=None):
        super().__init__()
        self.start_heading = start_heading.lower() if start_heading else None
        self.start_level = None
        self.collecting = start_heading is None
        self.skip = False
        self.buf = []
        self._last_tag = None

    def handle_starttag(self, tag, attrs):
        self._last_tag = tag
        if tag in ("script", "style", "noscript", "nav", "footer", "aside"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "nav", "footer", "aside"):
            self.skip = False

    def handle_data(self, data):
        if self.skip:
            return

        text = data.strip()
        if not text:
            return

        # detect heading
        if self._last_tag in ("h1","h2","h3","h4","h5","h6"):
            level = int(self._last_tag[1])

            # starting anchor
            if self.start_heading and text.lower() == self.start_heading:
                self.collecting = True
                self.start_level = level
                return

            # stop when new section begins
            if self.collecting and self.start_level is not None:
                if level <= self.start_level:
                    self.collecting = False
                    return

        if self.collecting:
            self.buf.append(text)

def scan_web_text(url: str, start_heading: str | None = None) -> str:
    with urlopen(url) as r:
        html = r.read().decode("utf-8", errors="ignore")

    parser = _SectionParser(start_heading)
    parser.feed(html)

    return _normalize(parser.buf)

def _normalize(lines):
    out = []
    last = None
    for l in lines:
        if l != last:
            out.append(l)
        last = l
    return "\n".join(out)
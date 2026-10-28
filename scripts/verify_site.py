#!/usr/bin/env python3
"""Stdlib-only assertions for the already-published project GitHub Pages design."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree as ET
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
PREFIX = "/Satzzxzxx-Labs/"
ORIGIN = "https://s2zxx0zxx.github.io"
CANONICAL = ORIGIN + PREFIX

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.h1 = 0
        self.links = []
        self.meta = {}
        self.canonical = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1 += 1
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a.get("href", ""))
        if tag == "meta":
            key = a.get("name", "")
            if key:
                self.meta[key] = a.get("content", "")
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.title += data

def fail(msg):
    raise AssertionError(msg)

def local_exists(href, source):
    if href.startswith(("#", "mailto:", "tel:", "javascript:")):
        if href.startswith("javascript:"):
            fail(f"Forbidden javascript link: {source}")
        return
    parsed = urlsplit(href)
    if parsed.scheme in ("https", "http") and parsed.netloc not in ("", "s2zxx0zxx.github.io"):
        return
    if parsed.scheme and parsed.scheme not in ("http", "https"):
        fail(f"Unexpected link scheme at {source}: {href}")
    path = unquote(parsed.path)
    if not path.startswith(PREFIX):
        # relative links are relative to the current page, not the project origin.
        if not path.startswith("/"):
            path = PREFIX + path
        else:
            fail(f"Internal link outside Pages project prefix at {source}: {href}")
    local = ROOT / path[len(PREFIX):]
    if local.is_dir() or path.endswith("/"):
        local = local / "index.html"
    if not local.is_file():
        fail(f"Broken local href in {source}: {href} (expected {local})")

def main():
    data = json.loads((ROOT / "data/catalog.json").read_text())
    if data["canonical_site"] != CANONICAL:
        fail("Unexpected canonical site")
    routes = data["public_routes"]
    if len(routes) != len(set(routes)) or "" not in routes:
        fail("Duplicate public paths or missing homepage")
    if "assets/style.css" not in [p.as_posix().split(ROOT.as_posix()+"/",1)[-1] for p in ROOT.rglob("*.css")]:
        fail("Original website stylesheet missing")
    for project in data["projects"]:
        if not (ROOT / project["detail_path"] / "index.html").is_file():
            fail("Project detail page missing: " + project["id"])
        if not project.get("source_url","").startswith("https://github.com/"):
            fail("Source link missing for " + project["id"])
        if not project.get("attribution"):
            fail("Attribution missing for " + project["id"])
    indexed = {}
    for file in ROOT.rglob("*.html"):
        rel = file.relative_to(ROOT).as_posix()
        page = Page()
        page.feed(file.read_text(encoding="utf-8"))
        if not page.title.strip() or not page.meta.get("description"):
            fail("Missing title or description in " + rel)
        if page.h1 != 1 and rel != "blog/index.html":
            # The original journal uses h2 for its visual headline; layout preserved.
            fail("Exactly one h1 required: " + rel)
        for href in page.links:
            local_exists(href, rel)
        route = rel[:-len("index.html")]
        if route in routes:
            if "noindex" in page.meta.get("robots", "").lower():
                fail("Indexed public route marked noindex: " + rel)
            expected = CANONICAL + route
            if page.canonical != [expected]:
                fail("Missing/incorrect canonical " + rel + ": " + str(page.canonical))
            if page.title in indexed:
                fail("Duplicate public title " + page.title)
            indexed[page.title] = rel
        elif rel.startswith("blog/"):
            if "noindex" not in page.meta.get("robots", "").lower():
                fail("Draft article leaked as indexable: " + rel)
        else:
            fail("Unregistered HTML path: " + rel)
    for route in routes:
        if not (ROOT / route / "index.html").is_file():
            fail("Listed route has no index.html: " + route)
    for article in data["articles"]:
        route = article["path"]
        if article["status"] == "published":
            if route not in routes or not article.get("sources"):
                fail("Published content missing sitemap route or sources: " + route)
        elif article["status"] == "draft":
            if route in routes:
                fail("Draft is in sitemap: " + route)
        else:
            fail("Unrecognized publication state")
    root = ET.fromstring((ROOT / "sitemap.xml").read_text())
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    urls = [node.text for node in root.findall(f"{namespace}url/{namespace}loc")]
    expected_urls = [CANONICAL + route for route in routes]
    if urls != expected_urls:
        fail("Sitemap does not match published catalog routes")
    robots = (ROOT / "robots.txt").read_text()
    if "Sitemap: " + CANONICAL + "sitemap.xml" not in robots:
        fail("robots.txt missing sitemap discovery")
    feed = (ROOT / "feed.xml").read_text()
    for article in data["articles"]:
        address = CANONICAL + article["path"]
        if article["status"] == "published" and address not in feed:
            fail("Published article missing feed entry")
        if article["status"] != "published" and address in feed:
            fail("Draft leaked to feed")
    print(f"PASS: {len(routes)} canonical public routes, {len(data['projects'])} attributed projects, {sum(a['status']=='published' for a in data['articles'])} published article, {sum(a['status']=='draft' for a in data['articles'])} noindex drafts, local links and sitemap consistent")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, KeyError, ValueError, ET.ParseError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)

import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_attrs = {}
        self.meta = []
        self.title_parts = []
        self.in_title = False
        self.references = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.html_attrs = attrs
        if tag == "meta":
            self.meta.append(attrs)
        if tag == "title":
            self.in_title = True
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for key in ("src", "href"):
            value = attrs.get(key)
            if value:
                self.references.append((tag, key, value))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)


class StaticSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.inspector = PageInspector()
        cls.inspector.feed(cls.page)
        cls.inspector.close()

    def test_page_has_arabic_rtl_document_contract(self):
        self.assertEqual(self.inspector.html_attrs.get("lang"), "ar")
        self.assertEqual(self.inspector.html_attrs.get("dir"), "rtl")
        self.assertTrue("NexaPay" in "".join(self.inspector.title_parts))

    def test_mobile_viewport_is_declared(self):
        viewport = [m.get("content", "") for m in self.inspector.meta if m.get("name") == "viewport"]
        self.assertTrue(viewport)
        self.assertIn("width=device-width", viewport[0])

    def test_all_local_asset_references_exist(self):
        missing = []
        for tag, attribute, value in self.inspector.references:
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or value.startswith(("#", "data:")):
                continue
            target = (ROOT / parsed.path).resolve()
            if parsed.path and not target.is_file():
                missing.append((tag, attribute, value))
        self.assertEqual(missing, [], f"Missing local assets: {missing}")

    def test_all_local_fragment_targets_exist(self):
        missing = []
        for _, attribute, value in self.inspector.references:
            if attribute == "href" and value.startswith("#") and len(value) > 1:
                if value[1:] not in self.inspector.ids:
                    missing.append(value)
        self.assertEqual(missing, [], f"Missing fragment targets: {missing}")

    def test_demo_video_source_and_builder_exist(self):
        self.assertTrue((ROOT / "media/insta-freelancer-demo.mp4").is_file())
        self.assertTrue((ROOT / "render_demo.py").is_file())
        self.assertTrue((ROOT / "build_video.sh").is_file())


if __name__ == "__main__":
    unittest.main()

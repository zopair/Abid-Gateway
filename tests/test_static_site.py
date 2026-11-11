import unittest
from pathlib import Path

from scripts.validate_site import validate_site


class StaticSiteValidationTests(unittest.TestCase):
    def test_site_has_arabic_rtl_document_and_main_content(self):
        root = Path(__file__).resolve().parents[1]
        result = validate_site(root)
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["language"], "ar")
        self.assertTrue(result["has_main"])


if __name__ == "__main__":
    unittest.main()

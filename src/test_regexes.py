import unittest
from regexes import extract_markdown_images, extract_markdown_links

class TestRegex(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_links_dont_include_images(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_images_dont_include_links(self):
        matches = extract_markdown_images(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "![one](https://example.com/1.png) and ![two](https://example.com/2.png)"
        )
        self.assertListEqual(
            [
                ("one", "https://example.com/1.png"),
                ("two", "https://example.com/2.png"),
            ],
            matches,
        )

    def test_images_empty_string(self):
        matches = extract_markdown_images("")
        self.assertEqual([],matches)

    def test_links_empty_string(self):
        matches = extract_markdown_links("")
        self.assertEqual([],matches)

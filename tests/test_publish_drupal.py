import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.publish_drupal import normalize_markdown_links, render_markdown


class PublishDrupalTest(unittest.TestCase):
    def test_render_markdown_creates_html(self):
        rendered = render_markdown("## 标题\n\n> 引用\n\n```python\nprint(1)\n```")
        self.assertIn("<h2>标题</h2>", rendered)
        self.assertIn("<blockquote>", rendered)
        self.assertIn("<pre><code class=\"language-python\">", rendered)
        self.assertNotIn("```", rendered)

    def test_local_file_links_become_public_urls(self):
        source = (
            "[上一章](file:///home/ben/projects/gitea/kunpengzhi-podcast/"
            "docs/spinoff_%E5%8D%8E%E4%B8%A5%E8%92%B2%E7%89%A2/EP01.md)"
        )
        normalized = normalize_markdown_links(source)
        self.assertNotIn("file:///", normalized)
        self.assertIn(
            "https://gitea.capitaltrain.cn/seekkey/kunpengzhi-podcast/"
            "raw/branch/main/docs/spinoff_%E5%8D%8E%E4%B8%A5%E8%92%B2%E7%89%A2/EP01.md",
            normalized,
        )


if __name__ == "__main__":
    unittest.main()

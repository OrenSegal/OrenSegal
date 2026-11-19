import unittest

import update_readme as u


class RenderTest(unittest.TestCase):
    def test_replaces_only_the_recent_block(self):
        text = f"top\n{u.START}\nold\n{u.END}\nbottom\n"
        out = u.render(text, [("2026-11-02", "[sous v0.4.0](https://example.test/r)")])
        self.assertEqual(
            out,
            f"top\n{u.START}\n**Releases**\n\n- [sous v0.4.0](https://example.test/r) (2026-11-02)\n{u.END}\nbottom\n",
        )

    def test_missing_markers_fail_instead_of_silently_doing_nothing(self):
        with self.assertRaises(SystemExit):
            u.render("a README whose markers were edited away\n", [])


if __name__ == "__main__":
    unittest.main()

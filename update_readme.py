"""Fill the Recent block in README.md with the latest releases.

Runs in a GitHub Action with `gh` authenticated by the workflow token.
"""

import json
import pathlib
import re
import subprocess

USER = "OrenSegal"
README = pathlib.Path(__file__).parent / "README.md"
START, END = "<!-- recent starts -->", "<!-- recent ends -->"


def gh(*args: str):
    return json.loads(subprocess.run(["gh", "api", *args], check=True, capture_output=True, text=True).stdout)


def releases(limit: int = 5):
    found = []
    for repo in gh(f"users/{USER}/repos?type=owner&sort=pushed&per_page=50"):
        if repo["fork"] or repo["private"] or repo["archived"]:
            continue
        for rel in gh(f"repos/{USER}/{repo['name']}/releases?per_page=3"):
            if rel["draft"] or not rel["published_at"]:
                continue
            found.append((rel["published_at"][:10], f"[{repo['name']} {rel['tag_name']}]({rel['html_url']})"))
    return sorted(found, reverse=True)[:limit]


def render(text: str, items) -> str:
    """Return README text with the Recent block replaced by `items` (date, link) pairs."""
    lines = ["**Releases**", ""] + [f"- {link} ({date})" for date, link in items]
    block = START + "\n" + "\n".join(lines) + "\n" + END
    # A function replacement, so nothing in a release name is read as a regex escape.
    out, count = re.subn(re.escape(START) + ".*" + re.escape(END), lambda _: block, text, flags=re.S)
    if count != 1:
        raise SystemExit(f"README.md must contain exactly one {START} ... {END} block, found {count}")
    return out


def main() -> None:
    README.write_text(render(README.read_text(encoding="utf-8"), releases()), encoding="utf-8")


if __name__ == "__main__":
    main()

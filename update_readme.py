"""Fill the Recent block in README.md with the latest releases and TIL notes.

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
        if repo["fork"] or repo["private"]:
            continue
        for rel in gh(f"repos/{USER}/{repo['name']}/releases?per_page=3"):
            if rel["draft"] or not rel["published_at"]:
                continue
            found.append((rel["published_at"][:10], f"[{repo['name']} {rel['tag_name']}]({rel['html_url']})"))
    return sorted(found, reverse=True)[:limit]


def tils(limit: int = 5):
    raw = subprocess.run(
        ["gh", "api", f"repos/{USER}/til/contents/README.md", "-H", "Accept: application/vnd.github.raw"],
        check=True, capture_output=True, text=True,
    ).stdout
    found = []
    for title, path, date in re.findall(r"^- \[(.+?)\]\((.+?)\) - (\d{4}-\d{2}-\d{2})$", raw, re.M):
        found.append((date, f"[{title}](https://github.com/{USER}/til/blob/main/{path})"))
    return sorted(found, reverse=True)[:limit]


def main() -> None:
    lines = ["**Releases**", ""] + [f"- {link} ({date})" for date, link in releases()]
    lines += ["", "**TIL**", ""] + [f"- {link} ({date})" for date, link in tils()]
    block = START + "\n" + "\n".join(lines) + "\n" + END
    text = README.read_text(encoding="utf-8")
    README.write_text(re.sub(re.escape(START) + ".*" + re.escape(END), block, text, flags=re.S), encoding="utf-8")


if __name__ == "__main__":
    main()

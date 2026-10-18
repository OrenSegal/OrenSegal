## Oren Segal

Applied AI engineer. I build agents, and the evals and CI checks that show whether they work.

**Latest: [`rootcause`](https://github.com/OrenSegal/rootcause)**, an incident and CI root-cause agent with a hand-written loop, tools over MCP and an approval gate. I measured it over 525 runs on 25 incidents with known causes. Across seven model and effort settings, accuracy stayed at 77-84% with overlapping intervals, while cost per solved incident varied 25x. In a separate 300-run comparison, an orchestrator with workers tripled the cost for no measurable gain. Mutation-testing its brief with [`litmus`](https://github.com/OrenSegal/litmus) showed the suite couldn't catch a regression in any single instruction, which is what the next scenarios are built to fix. [Results](https://github.com/OrenSegal/rootcause#results).

**Also building: [Shelfie](https://shelfie.food)**, an iOS app that keeps track of what's in your kitchen and when it expires, then suggests what to cook from it. Scan your groceries and it identifies them on the phone first, only asking a cloud model when it has to. Swift 6 / SwiftUI with Watch, widget and iMessage extensions, on Supabase with about 60 TypeScript edge functions. Most of the code is written by Claude Code agents; I review what they produce and build the checks that decide what gets merged. The harness they work in treats an agent's "done" as a claim to verify, and holds a merge for me when a review asks for a person. The public part of it is [`sous`](https://github.com/OrenSegal/sous).

Shelfie is in a closed TestFlight beta, so the architecture diagram stays private for now. Ask me if you want the real version.

**Before this:** five years as a senior data analyst at a major TV network, building the pipelines and forecasting models the business actually ran on. One pricing analysis changed how primetime ad slots were priced. A viewership forecast became the standard input for content and greenlight decisions.

**Stack I live in:** Swift/SwiftUI, TypeScript, Python, Supabase and Postgres, Claude Code and multi-model routing, GitHub Actions, Docker.

**Public proof, since most of the real work is still private:**

- [`rootcause`](https://github.com/OrenSegal/rootcause): the incident agent above. It runs as a CLI with exit codes for CI, as an MCP server, and as a GitHub Action.
- [`litmus`](https://github.com/OrenSegal/litmus): mutation testing for eval suites. It breaks the thing under test on purpose and lists the broken copies your evals missed.
- [`sous`](https://github.com/OrenSegal/sous): a Claude Code plugin marketplace and harness checker. A guard hook blocks destructive commands and secret reads; `sous gate` says whether a branch is safe to merge (tests really ran and were not weakened, no unreviewed blocks, plugins unchanged since you last reviewed them); `sous doctor` checks the harness still holds. Installs `cited`, `scoped` and `deuce` from the same marketplace.
- [`cited`](https://github.com/OrenSegal/cited): re-fetches every source an LLM cites and flags any claim whose words, numbers or names aren't on the cited page, before a person ships it.
- [`scoped`](https://github.com/OrenSegal/scoped): stops parallel Claude Code sessions from editing the same file, enforced in a `PreToolUse` hook and tested with real racing processes.
- [`deuce`](https://github.com/OrenSegal/deuce): post-merge cleanup. It finds merged branches (squash merges too, through `gh`), shows a dry run, then removes worktrees and local and remote branches on approval, with an audit log and undo.
- [`architecture-lint`](https://github.com/OrenSegal/architecture-lint): a module-boundary linter with a ratchet baseline, so existing violations don't block adoption but new ones fail CI.

**Pull requests where a check proved less than it claimed:**

- [scoped#1](https://github.com/OrenSegal/scoped/pull/1): the README promised safe claims under concurrent sessions, but the only test ran on one connection. Racing real OS processes let two sessions claim the same file; the PR fixes both causes.
- [cited#1](https://github.com/OrenSegal/cited/pull/1): a made-up funding round scored as a near match on a page that only named the company. Numbers and names in a claim now have to appear on the page.
- [signal-scout#3](https://github.com/OrenSegal/signal-scout/pull/3): the eval job graded hand-written outputs, so no change to the skill could fail it. It now runs the pipeline code on fixtures, and each of three planted bugs turns it red.
- [signal-skills#1](https://github.com/OrenSegal/signal-skills/pull/1): removed a CI job that was grading a different skill from the one in the repo.

## Recent

<!-- recent starts -->
**Releases**

- [sous v0.3.1](https://github.com/OrenSegal/sous/releases/tag/v0.3.1) (2026-10-14)
- [sous v0.3.0](https://github.com/OrenSegal/sous/releases/tag/v0.3.0) (2026-10-02)
- [litmus v0.2.0](https://github.com/OrenSegal/litmus/releases/tag/v0.2.0) (2026-10-02)
- [deuce v0.1.1](https://github.com/OrenSegal/deuce/releases/tag/v0.1.1) (2026-10-02)
- [deuce v0.1.0](https://github.com/OrenSegal/deuce/releases/tag/v0.1.0) (2026-10-02)

**TIL**

- [A concurrency test on one connection can't find a race](https://github.com/OrenSegal/til/blob/main/sqlite/one-connection-cannot-test-a-race.md) (2026-09-28)
<!-- recent ends -->

<details>
<summary>A fact that has nothing to do with any of this</summary>
<br>
Moved to the US in 2023 and spent until 2025 deliberately retraining in AI/ML before writing a line of Shelfie's code. Would make that trade again. Some of that retraining is public, like <a href="https://github.com/OrenSegal/rag-generation">a RAG lab</a>: embeddings, an in-memory Qdrant index, and real semantic search over a wine dataset.
</details>

Brooklyn, NY. Always up for a conversation on LLM systems, agentic architecture, or anything food and inventory tech.

[LinkedIn](https://www.linkedin.com/in/oren-segal) · [orenssegal@gmail.com](mailto:orenssegal@gmail.com)

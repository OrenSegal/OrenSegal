## Oren Segal

Founder and engineer. I build AI products, and the tests and CI checks that catch what coding agents get wrong.

**Currently building: [Shelfie](https://shelfie.food)**, an iOS app that keeps track of what's in your kitchen and when it expires, then suggests what to cook from it. Scan your groceries and it identifies them on the phone first, only asking a cloud model when it has to. Swift 6 / SwiftUI with Watch, widget and iMessage extensions, on Supabase with about 60 TypeScript edge functions. Most of the code is written by Claude Code agents; I review what they produce and build the checks that decide what gets merged.

Shelfie is in TestFlight beta, so the architecture diagram stays private for now. Ask me if you want the real version.

**Before this:** five years as a senior data analyst at a major TV network, building the pipelines and forecasting models the business actually ran on. One pricing analysis changed how primetime ad slots were priced. A viewership forecast became the standard input for content and greenlight decisions.

**Stack I live in:** Swift/SwiftUI, TypeScript, Python, Supabase and Postgres, Claude Code and multi-model routing, GitHub Actions, Docker.

**Public proof, since most of the real work is still private:**

- [`verify-before-ship`](https://github.com/OrenSegal/verify-before-ship): re-fetches every source an LLM cites and flags any claim whose words aren't on the cited page, before a person ships it.
- [`scoped`](https://github.com/OrenSegal/scoped): stops parallel Claude Code sessions from editing the same file, enforced in a `PreToolUse` hook and tested with real racing processes.
- [`litmus`](https://github.com/OrenSegal/litmus): tests for prompt-based skills. Deterministic checks where possible; a model judge only counts once it has agreed with known pass and fail examples.
- [`architecture-lint`](https://github.com/OrenSegal/architecture-lint): a module-boundary linter with a ratchet baseline, so existing violations don't block adoption but new ones fail CI.
- [`llm-gateway-kit`](https://github.com/OrenSegal/llm-gateway-kit): the budget, caching and circuit-breaker patterns from Shelfie's AI gateway, extracted.
- [`signal-scout`](https://github.com/OrenSegal/signal-scout): a Claude Code skill that turns a startup URL into a prospect shortlist and checks every cited source before handing it over.
- [`til`](https://github.com/OrenSegal/til): short notes on testing and verifying agent-written code.
- [`metropulse-nyc`](https://github.com/OrenSegal/metropulse-nyc): a Dagster/DuckDB pipeline that groups 344 NYC subway stations by how riders actually use them.

## Recent

<!-- recent starts -->
**Releases**

- [verify-before-ship v0.1.0](https://github.com/OrenSegal/verify-before-ship/releases/tag/v0.1.0) (2026-09-09)
- [signal-scout v1.6.1](https://github.com/OrenSegal/signal-scout/releases/tag/v1.6.1) (2026-09-09)
- [scoped v0.2.1](https://github.com/OrenSegal/scoped/releases/tag/v0.2.1) (2026-09-09)
- [metropulse-nyc v1.1.0](https://github.com/OrenSegal/metropulse-nyc/releases/tag/v1.1.0) (2026-09-09)
- [architecture-lint v1.1.0](https://github.com/OrenSegal/architecture-lint/releases/tag/v1.1.0) (2026-09-09)

**TIL**

- [A concurrency test on one connection can't find a race](https://github.com/OrenSegal/til/blob/main/sqlite/one-connection-cannot-test-a-race.md) (2026-09-28)
<!-- recent ends -->

<details>
<summary>A fact that has nothing to do with any of this</summary>
<br>
Moved to the US in 2023, spent a year deliberately retraining in AI/ML before writing a line of Shelfie's code. Would make that trade again. Some of that retraining is public: <a href="https://github.com/OrenSegal/coursera-deep-learning-specialization">deeplearning.ai's Deep Learning Specialization</a> (notes and assignments across all five courses), and <a href="https://github.com/OrenSegal/rag-generation">a RAG lab</a>: embeddings, an in-memory Qdrant index, and real semantic search over a wine dataset.
</details>

Brooklyn, NY. Always up for a conversation on LLM systems, agentic architecture, or anything food and inventory tech.

[LinkedIn](https://www.linkedin.com/in/oren-segal) · [orenssegal@gmail.com](mailto:orenssegal@gmail.com)

## Oren Segal

![Status](https://img.shields.io/badge/status-shipping-black) ![Focus](https://img.shields.io/badge/focus-applied%20AI-black) ![Location](https://img.shields.io/badge/based%20in-Brooklyn%2C%20NY-black)

Founder and engineer. I take AI systems from "cool demo" to something that survives production traffic, edge cases, and real users who don't read the happy path.

**Currently building: [Shelfie](https://shelfie.food)** - an AI-native Kitchen OS. Point your camera at your fridge or pantry, it identifies what you actually have, and turns that into recipes, a grocery list, and a plan - no manual entry. Native Swift 6 / SwiftUI on the front end, a fleet of agentic services underneath handling computer vision, retrieval, and recipe intelligence, on infrastructure I designed and run end to end.

Pre-launch, so the architecture diagram stays private for now - ask me if you want the real version.

**Before this:** five years as a senior data analyst at a major TV network, building the pipelines and forecasting models the business actually ran on. One pricing model paid for itself several times over. One forecasting model earned enough trust to inform real greenlight decisions.

**Stack I live in:** Swift/SwiftUI, TypeScript, Python, agentic systems and multi-model orchestration, RAG and vector search, Postgres, Docker, and whatever cloud is having a good day.

**Public proof, since most of the real work is still private:** [`signal-scout`](https://github.com/OrenSegal/signal-scout) — a Claude Code agent skill that turns a startup URL into an evidence-backed prospect shortlist, and re-fetches every cited source to catch fabricated claims before they ship, instead of trusting the same model's self-graded confidence. [`verify-before-ship`](https://github.com/OrenSegal/verify-before-ship) — that same containment-checking verifier, generalized to any claim/source pair. [`scoped`](https://github.com/OrenSegal/scoped) — an MCP coordination layer that stops concurrent Claude Code sessions from stomping the same file, with real `PreToolUse` enforcement, not just an advisory API. [`architecture-lint`](https://github.com/OrenSegal/architecture-lint) — a config-driven module-boundary linter with a ratchet baseline, tested and CI-gated. [`metropulse-nyc`](https://github.com/OrenSegal/metropulse-nyc) — a Dagster/DuckDB pipeline segmenting 344 NYC subway stations by behavior across 106,810 ridership rows, ~6ms DuckDB query execution (p50 5.82ms/p95 6.83ms).

<details>
<summary>A fact that has nothing to do with any of this</summary>
<br>
Moved to the US in 2023, spent a year deliberately retraining in AI/ML before writing a line of Shelfie's code. Would make that trade again in a heartbeat. Some of that retraining is public: <a href="https://github.com/OrenSegal/coursera-deep-learning-specialization">deeplearning.ai's Deep Learning Specialization</a> (notes + assignments across all five courses), and <a href="https://github.com/OrenSegal/rag-generation">a completed RAG lab</a> — embeddings, an in-memory Qdrant index, and real semantic search over a wine dataset.
</details>

Most of the real work lives in private repos right now. The commit graph is real — the code just isn't public yet.

Brooklyn, NY. Always up for a conversation on production LLM systems, agentic architecture, or anything food and inventory tech.

[LinkedIn](https://www.linkedin.com/in/oren-segal) · [orenssegal@gmail.com](mailto:orenssegal@gmail.com)

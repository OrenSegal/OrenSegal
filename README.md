## Oren Segal

Applied AI engineer. I build agents, the evals that show whether they work, and the checks that show whether the evals can fail.

> **Across 525 graded runs, switching models changed cost per solved incident 25x, and no accuracy gap could be detected.** [rootcause](https://github.com/OrenSegal/rootcause) · [write-up](https://orensegal.github.io/writing/rootcause-benchmark/)

| Project | What it does | Result |
|---|---|---|
| [**rootcause**](https://github.com/OrenSegal/rootcause) | Incident and CI root-cause agent: hand-written tool loop over MCP, approval gate, crash-recovery log, OpenTelemetry. CLI, MCP server, GitHub Action | 25x cost spread, 77-84% pass rate across 7 model settings |
| [**litmus**](https://github.com/OrenSegal/litmus) | Mutation testing for eval suites: breaks a prompt on purpose and finds graders that can't fail | rootcause's suite killed 0 of 12 mutants |
| [**cited**](https://github.com/OrenSegal/cited) | Re-fetches every source an LLM cites and flags claims the page doesn't support | 10 of 15 unsupported claims caught |
| [**sous**](https://github.com/OrenSegal/sous) | The harness my coding agents run in: guard hooks, fails green runs that ran no tests, merge gate. Also ships scoped, deuce, blast-shield, architecture-lint | Every rule has a block and an allow test |
| [**codebase-audit**](https://github.com/OrenSegal/codebase-audit) | Adversarial audit skill: a separate refuter challenges every serious finding, and fixes come back as tickets | |
| [**rag-generation**](https://github.com/OrenSegal/rag-generation) | BM25 vs local embeddings vs hybrid on 55 labelled queries, with bootstrap intervals | BM25 won on exact labels and lost on paraphrases |
| [**ny-noise**](https://github.com/OrenSegal/ny-noise) ([live](https://ny-noise.vercel.app)) | 1.6M NYC 311 noise reports mapped block by block, with next week's forecast for 177 ZIPs | 78% deviance explained on held-out areas |
| [**llm-gateway-kit**](https://github.com/OrenSegal/llm-gateway-kit) | Caching, circuit breakers and daily spend caps for Swift apps that call LLMs | |
| [**signal-scout**](https://github.com/OrenSegal/signal-scout) · [**signal-skills**](https://github.com/OrenSegal/signal-skills) · [**visibility**](https://github.com/OrenSegal/visibility) | Agent skills: find a startup's first customers, turn podcasts and reviews into cited build proposals, get a product listed on agent marketplaces | |

Intervals, sample sizes and limitations are in each repo's README.

**Building [Shelfie](https://shelfie.food)**, an iOS kitchen-inventory app in closed beta, written by coding agents inside sous.

**Before:** since 2025, the data side of a consumer transactions business (an unattended BigQuery warehouse and anomaly-flagging sales forecasts). Before that, five years as a senior data analyst at Reshet 13, building pricing and forecasting models.

**Writing:** [The benchmark that didn't pick a winner](https://orensegal.github.io/writing/rootcause-benchmark/) · [Three checks that passed when they shouldn't have](https://orensegal.github.io/writing/checks-that-could-not-fail/) · [Getting a pricing model adopted at Reshet 13](https://orensegal.github.io/writing/reshet-pricing-model/)

## Recent

<!-- recent starts -->
**Releases**

- [sous v0.4.0](https://github.com/OrenSegal/sous/releases/tag/v0.4.0) (2026-11-02)
- [signal-skills v1.0.2](https://github.com/OrenSegal/signal-skills/releases/tag/v1.0.2) (2026-11-02)
- [signal-scout v1.7.0](https://github.com/OrenSegal/signal-scout/releases/tag/v1.7.0) (2026-11-02)
- [rootcause v0.2.0](https://github.com/OrenSegal/rootcause/releases/tag/v0.2.0) (2026-11-02)
- [llm-gateway-kit v0.2.0](https://github.com/OrenSegal/llm-gateway-kit/releases/tag/v0.2.0) (2026-11-02)
<!-- recent ends -->

Brooklyn, NY · Open to applied AI engineering roles · [Portfolio](https://orensegal.github.io) · [LinkedIn](https://www.linkedin.com/in/oren-segal) · [orenssegal@gmail.com](mailto:orenssegal@gmail.com)

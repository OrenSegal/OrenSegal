## Oren Segal

Applied AI engineer. I build agents, and the evals and CI checks that show whether they work.

**[`rootcause`](https://github.com/OrenSegal/rootcause)** is an incident and CI root-cause agent: a hand-written tool loop over MCP, an approval gate for anything that touches production, crash-safe resume from an append-only log, and OpenTelemetry traces. It runs as a CLI, an MCP server and a GitHub Action. Its eval suite has 25 incidents with known causes and planted decoys. Across 525 graded runs on seven model, effort and retrieval settings (Claude Code as the agent, over rootcause's tools and grader), accuracy stayed at 77-84% with overlapping intervals, while cost per solved incident varied 25x. In a 300-run comparison, my hand-written loop and a LangGraph version of the same agent were indistinguishable, and an orchestrator with workers cost about three times as much for no measurable gain. [Results](https://github.com/OrenSegal/rootcause#results).

**Tools for checking what agents actually do:**

- [`litmus`](https://github.com/OrenSegal/litmus): mutation testing for eval suites. It breaks a prompt or skill on purpose and lists the broken copies your evals missed, and it finds graders that cannot fail. Run against rootcause's brief, it killed none of 11 mutants, which told me the suite needed scenarios that hinge on a single rule.
- [`cited`](https://github.com/OrenSegal/cited): re-fetches every source an LLM cites and flags claims whose words, numbers or names aren't on the page.
- [`sous`](https://github.com/OrenSegal/sous): the harness my coding agents run in. A guard hook with a block and an allow test for every rule, `tests-ran` and `tests-weakened` for green runs that proved nothing, a merge gate, and a doctor that re-checks it all. The same marketplace installs [`scoped`](https://github.com/OrenSegal/scoped) (file locks between parallel sessions, over MCP) and [`deuce`](https://github.com/OrenSegal/deuce) (post-merge cleanup with dry run and undo).
- [`llm-gateway-kit`](https://github.com/OrenSegal/llm-gateway-kit): caching, circuit breakers and hard spending limits for Swift apps that call LLMs, extracted from the gateway in my iOS app.

**Pull requests where a check proved less than it claimed:**

- [scoped#1](https://github.com/OrenSegal/scoped/pull/1): the only concurrency test ran on one connection. Racing real processes let two sessions claim the same file; the PR fixes both causes.
- [cited#1](https://github.com/OrenSegal/cited/pull/1): a made-up funding round scored as a near match. Numbers and names in a claim now have to be on the page.
- [signal-scout#3](https://github.com/OrenSegal/signal-scout/pull/3): the eval job graded hand-written outputs, so no change could fail it. It now runs the pipeline on fixtures, and three planted bugs each turn it red.

**Building: [Shelfie](https://shelfie.food)**, an iOS kitchen-inventory app in closed TestFlight beta, written mostly by Claude Code agents inside the sous harness, with every model call going through one gateway.

Before this: five years as a senior data analyst at an Israeli TV network, building pricing and forecasting models.

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

Brooklyn, NY · [Portfolio](https://orensegal.github.io) · [LinkedIn](https://www.linkedin.com/in/oren-segal) · [orenssegal@gmail.com](mailto:orenssegal@gmail.com)

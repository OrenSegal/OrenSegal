## Oren Segal

Applied AI engineer. I build agents, and the evals and CI checks that show whether they work.

**[`rootcause`](https://github.com/OrenSegal/rootcause)** is an incident and CI root-cause agent: a hand-written tool loop over MCP, an approval gate on production actions, an append-only log for crash recovery, and OpenTelemetry traces. It runs as a CLI, an MCP server and a GitHub Action. Its eval suite has 25 incidents with known causes and planted decoys. Across 525 graded runs on seven model, effort and retrieval settings (Claude Code as the agent, over rootcause's tools and grader), pass rates stayed at 77-84% with overlapping intervals, while cost per solved incident varied 25x. Without one strict service check, Opus pulls ahead of Sonnet (93% against 83%), so that flat result depends on the grader. In a 300-run comparison, I found no detectable difference between my hand-written loop and a LangGraph version of the same agent, and an orchestrator with workers cost about three times as much for no measurable gain. [Results](https://github.com/OrenSegal/rootcause#results).

**Tools for checking what agents actually do:**

- [`litmus`](https://github.com/OrenSegal/litmus): mutation testing for eval suites. It breaks a prompt or skill on purpose and lists the broken copies your evals missed, and it finds graders that cannot fail. Its operators made 12 mutants of rootcause's investigator brief, and the suite killed 0 of 12 (11 survived, 1 inconclusive). Two could not fail because the harness enforces the output format; the rest told me the suite needs scenarios that hinge on a single rule.
- [`cited`](https://github.com/OrenSegal/cited): re-fetches every source an LLM cites and flags claims whose words, numbers or names aren't on the page.
- [`sous`](https://github.com/OrenSegal/sous): the harness my coding agents run in. A guard hook with a block and an allow test for every rule, `tests-ran` and `tests-weakened` for green runs that proved nothing, a merge gate, and a doctor that re-checks it all. The same marketplace installs [`scoped`](https://github.com/OrenSegal/scoped) (file locks between parallel sessions, over MCP) and [`deuce`](https://github.com/OrenSegal/deuce) (post-merge cleanup with dry run and undo).
- [`llm-gateway-kit`](https://github.com/OrenSegal/llm-gateway-kit): caching, circuit breakers and daily spending limits for Swift apps that call LLMs, based on the patterns in my iOS app's gateway.
- [`blast-shield`](https://github.com/OrenSegal/blast-shield): holds a risky shell command and shows what it would change before you press Proceed. A fork of the Blast Radius mod from Anthropic's DevRel team, with wider coverage and explanations.

**Retrieval and agent skills:**

- [`rag-generation`](https://github.com/OrenSegal/rag-generation): BM25, a local embedding model and a hybrid scored on 55 labelled queries, with bootstrap intervals. BM25 led when a query named the label and mostly failed on paraphrases, so the right pick depends on your query mix.
- [`signal-scout`](https://github.com/OrenSegal/signal-scout): a skill that takes a startup's URL and returns likely first customers, dropping any whose cited evidence is clearly missing from the page and flagging partial matches for review.
- [`signal-skills`](https://github.com/OrenSegal/signal-skills): six skills for Claude Code and Codex that mine podcasts and app reviews into cited build proposals.

**Pull requests where a check proved less than it claimed:**

- [scoped#1](https://github.com/OrenSegal/scoped/pull/1): the only concurrency test ran on one connection. Racing real processes let two sessions claim the same file; the PR fixes both causes.
- [cited#1](https://github.com/OrenSegal/cited/pull/1): a made-up funding round scored as a near match. Numbers and names in a claim now have to be on the page.
- [signal-scout#3](https://github.com/OrenSegal/signal-scout/pull/3): the eval job graded hand-written outputs, so no change could fail it. It now runs the pipeline on fixtures, and three planted bugs each turn it red.

**Building: [Shelfie](https://shelfie.food)**, an iOS kitchen-inventory app in closed TestFlight beta, with much of the code written by Claude Code agents inside the sous harness. Every cloud model call from the app goes through one gateway.

Before this: five years as a senior data analyst at an Israeli TV network, building pricing and forecasting models. [How I got the pricing model adopted](https://orensegal.github.io/writing/reshet-pricing-model/).

## Recent

<!-- recent starts -->
**Releases**

- [sous v0.4.0](https://github.com/OrenSegal/sous/releases/tag/v0.4.0) (2026-11-02)
- [signal-skills v1.0.2](https://github.com/OrenSegal/signal-skills/releases/tag/v1.0.2) (2026-11-02)
- [signal-scout v1.7.0](https://github.com/OrenSegal/signal-scout/releases/tag/v1.7.0) (2026-11-02)
- [scoped v0.4.2](https://github.com/OrenSegal/scoped/releases/tag/v0.4.2) (2026-11-02)
- [rootcause v0.2.0](https://github.com/OrenSegal/rootcause/releases/tag/v0.2.0) (2026-11-02)

**TIL**

- [A concurrency test on one connection can't find a race](https://github.com/OrenSegal/til/blob/main/sqlite/one-connection-cannot-test-a-race.md) (2026-09-28)
<!-- recent ends -->

Brooklyn, NY · [Portfolio](https://orensegal.github.io) · [LinkedIn](https://www.linkedin.com/in/oren-segal) · [orenssegal@gmail.com](mailto:orenssegal@gmail.com)

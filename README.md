## Oren Segal

Applied AI engineer. I build agents, and the evals and CI checks that show whether they work.

**[`rootcause`](https://github.com/OrenSegal/rootcause)** is an incident and CI root-cause agent: a hand-written tool loop over MCP, an approval gate on production actions, an append-only log for crash recovery, and OpenTelemetry traces. It runs as a CLI, an MCP server and a GitHub Action. The 525-run sweep used 25 incidents with known causes, several with planted decoys (the suite has 33 now). Across those 525 graded runs on seven model, effort and retrieval settings (Claude Code as the agent, over rootcause's tools and grader), cost per solved incident varied 25x, and in a separate 300-run comparison an orchestrator with workers cost about three times as much as a single agent. On accuracy, 77-84% of runs passed and no pair of settings differed detectably, but runs repeat the same 25 incidents, and paired by incident the design detects only gaps above about 13-19 points between model tiers, so model accuracy differences are unresolved, not a tie. The result also depends on the grader: without one strict service check, the point gap between Opus and Sonnet widens to 93% against 83%, a comparison chosen after the fact and not corrected for the others, so a hint rather than a finding. I found no detectable difference between my hand-written loop and a LangGraph version of the same agent either: -2.7 points (-8.0 to +2.7) paired, with gaps under about 8 points out of reach. On eight incidents adapted from public postmortems, with the answers committed before any run, Haiku passed 50% (21-79%) against 77% on my own suite: a rough range from eight cases, not a test. [Results](https://github.com/OrenSegal/rootcause#results), [limitations](https://github.com/OrenSegal/rootcause#limitations).

**Tools for checking what agents actually do:**

- [`litmus`](https://github.com/OrenSegal/litmus): mutation testing for eval suites. It breaks a prompt or skill on purpose and lists the broken copies your evals missed, and it finds graders that cannot fail. Its operators made 12 mutants of rootcause's investigator brief, and the suite killed 0 of 12 (11 survived, 1 inconclusive). Eight scenarios built around single rules then killed 2 of 14, both through the search requirement; cited's suite killed 5 of 14. One run per mutant throughout, so run-to-run variance is not measured.
- [`cited`](https://github.com/OrenSegal/cited): re-fetches every source an LLM cites and flags claims whose words, numbers or names it can't find on the page. On its own 29-claim benchmark it caught 10 of 15 unsupported claims (recall 0.67, 95% interval 0.41-0.90); swapped words get through.
- [`sous`](https://github.com/OrenSegal/sous): the harness my coding agents run in. A guard hook with a block and an allow test for every rule, `tests-ran` and `tests-weakened` for green runs that proved nothing, a merge gate, and a doctor that re-checks it all. The same marketplace installs [`scoped`](https://github.com/OrenSegal/sous/tree/main/plugins/scoped) (file locks between parallel sessions, over MCP) and [`deuce`](https://github.com/OrenSegal/sous/tree/main/plugins/deuce) (post-merge cleanup with dry run and undo).
- [`llm-gateway-kit`](https://github.com/OrenSegal/llm-gateway-kit): caching, circuit breakers and daily spending limits for Swift apps that call LLMs, based on the patterns in my iOS app's gateway.
- [`blast-shield`](https://github.com/OrenSegal/sous/tree/main/plugins/blast-shield): holds a risky shell command and shows what it would change before you press Proceed. A fork of the Blast Radius mod from Anthropic's DevRel team, with wider coverage and explanations.

**Retrieval and agent skills:**

- [`rag-generation`](https://github.com/OrenSegal/rag-generation): BM25, a local embedding model and a hybrid scored on 55 labelled queries, with bootstrap intervals. BM25 led when a query named the label and mostly failed on paraphrases, so the right pick depends on your query mix.
- [`signal-scout`](https://github.com/OrenSegal/signal-scout): a skill that takes a startup's URL and returns likely first customers, dropping any whose cited evidence is clearly missing from the page and flagging partial matches for review.
- [`signal-skills`](https://github.com/OrenSegal/signal-skills): six skills for Claude Code and Codex that mine podcasts and app reviews into cited build proposals.
- [`architecture-lint`](https://github.com/OrenSegal/sous/tree/main/plugins/architecture-lint): a module-boundary linter with a per-rule count baseline, so CI fails only when a rule's violation count rises.

**How I build.** My coding agents run inside sous, which blocks destructive commands and fails a green run that executed no tests. Before I trust a check, I make sure it can fail: litmus mutates the prompt under test, and planted bugs have to turn CI red. The pull requests below are the times a check proved less than it claimed.

**Pull requests where a check proved less than it claimed:**

- [scoped#1](https://github.com/OrenSegal/scoped/pull/1): the only concurrency test ran on one connection. Racing real processes let two sessions edit the same file; the PR fixes both causes.
- [cited#1](https://github.com/OrenSegal/cited/pull/1): a made-up funding round scored as a near match. Numbers and names in a claim now have to be on the page.
- [signal-scout#3](https://github.com/OrenSegal/signal-scout/pull/3): the eval job graded hand-written outputs, so no change could fail it. It now runs the pipeline on fixtures, and three planted bugs each turn it red.

Design decisions, with the alternatives I rejected where they were written down (each file says "not recorded" where they were not): [rootcause](https://github.com/OrenSegal/rootcause/blob/main/docs/decisions.md), [sous](https://github.com/OrenSegal/sous/blob/main/docs/decisions.md), [litmus](https://github.com/OrenSegal/litmus/blob/main/docs/decisions.md), [cited](https://github.com/OrenSegal/cited/blob/main/docs/decisions.md).

**Building: [Shelfie](https://shelfie.food)**, an iOS kitchen-inventory app, pre-launch. Every cloud model call from the app goes through one gateway.

Before this: five years as a senior data analyst at an Israeli TV network, building pricing and forecasting models. [How I got the pricing model adopted](https://orensegal.github.io/writing/reshet-pricing-model/).

## Recent

<!-- recent starts -->
**Releases**

- [sous v0.4.0](https://github.com/OrenSegal/sous/releases/tag/v0.4.0) (2026-11-02)
- [signal-skills v1.0.2](https://github.com/OrenSegal/signal-skills/releases/tag/v1.0.2) (2026-11-02)
- [signal-scout v1.7.0](https://github.com/OrenSegal/signal-scout/releases/tag/v1.7.0) (2026-11-02)
- [scoped v0.4.2](https://github.com/OrenSegal/scoped/releases/tag/v0.4.2) (2026-11-02)
- [rootcause v0.2.0](https://github.com/OrenSegal/rootcause/releases/tag/v0.2.0) (2026-11-02)
<!-- recent ends -->

Brooklyn, NY · [Portfolio](https://orensegal.github.io) · [LinkedIn](https://www.linkedin.com/in/oren-segal) · [orenssegal@gmail.com](mailto:orenssegal@gmail.com)

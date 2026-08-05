# mastery-ai Framework — Issue & Project Register

**This is the single source of truth for what is open in this repo.** One row per
issue/project. Detail lives in the linked doc; this file is the index the Mission
Control reconcile (`repo-reconcile.py`) reads and mirrors to the cockpit.

## ID convention (collision-safe)

Mission Control owns the bare `ISS-`/`PRJ-`/`T-` namespaces. **Every mastery-ai Framework ID
carries the `MAI-` prefix** so it can never collide with a Mission-Control-native
ID or another repo's. Raise issues here with `python3 ~/shared/scripts/repo-issue.py`.

---

## Open

| ID | Title | Status | Severity | Detail | MC-SYNC |
|----|-------|--------|----------|--------|---------|
| MAI-ISS-1 | CLAUDE.md working copy has been overwritten with AGENT-11 boilerplate — describes this repo as 'AGENT-11, a framework for deploying specialized AI agents' instead of the MASTERY-AI Framework. Uncommitted since 2025-08-20 (391 added / 90 deleted vs commit 6d3e6dd). Same contamination class as the DevProjects tree file fixed under PRJ-9/T-348. Decide: restore from git, or rewrite as real MASTERY-AI product context. Do NOT just commit the working copy. | ✅ Resolved 2026-08-03 — CLAUDE.md rewritten from the repo as real MASTERY-AI product context and committed in d3d07c3. AGENT-11 boilerplate discarded; only the .claude/CLAUDE.md pair-declaration line salvaged. 132 lines, zero AGENT-11 mentions, registry two-layer, consistency-check clean, fact-checked by independent reader agents. | high | — | pending |

## Recently closed

| ID | Title | Status | Commit | Detail |
|----|-------|--------|--------|--------|

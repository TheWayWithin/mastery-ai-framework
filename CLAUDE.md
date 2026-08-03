# CLAUDE.md

Framework rules (Karpathy constitution, mission routing, tracking-file protocols, MCP, hooks, security) live in `.claude/CLAUDE.md`. Read both. This file is the product layer.

## What this repo is

The **MASTERY-AI Framework**: an assessment framework for AI Search Optimization (AISO), scoring a
site or piece of content out of 100 against **8 weighted pillars** spelling MASTERY. Shipped as the
Python package `mastery-ai` (import name `mastery_ai`), public at
`github.com/TheWayWithin/mastery-ai-framework`, MIT, Python 3.8+.

It is a scoring library, not an agent framework and not a crawler. It takes structured input you
supply (`url`, `content`, `technical_data`) and returns pillar scores, an overall score and
recommendations. Nothing in it fetches a page for you.

Much of the tree is **not** the product. `.claude/`, `missions/`, `templates/`, `field-manual/`,
`gates/`, `schemas/`, `stack-profiles/` and all of `docs/` (MCP guides and an upgrade note, no
product documentation) are a vendored deployment of the agent tooling used to work on this repo,
described in `.claude/CLAUDE.md`. They are how the work happens, never what it is about. Do not
describe this project in terms of them, and do not hand-edit them: the next deployment overwrites
the lot.

## The pillars

`FrameworkSchema.get_default_schema` in `mastery_ai/core/schema.py` is canonical for pillar names,
weights and factor *counts* only. It defines no factors: all eight pillars are built with
`sub_pillars=[]`. The only factor definitions in the codebase are in `mastery_ai/pillars/ai_response.py`.

The prose specification is `Ideation/`: eight pillar appendices at v3.2.0, plus the main framework
document, which exists there in both v3.2 and superseded v3.1.1 copies alongside a validation
script per version. Check the version in the filename before quoting one; superseded material
belongs in `Ideation/archive/` and some has not been moved yet. Where code and appendix disagree,
the code is what runs and the appendix is what was intended: fix whichever is wrong rather than
papering over it. The appendices are the real asset here, so never edit them to match buggy code.

Weights are not decorative. The eight pillar weights must total exactly 100% and factor weights
within a sub-pillar must total 100%. Never adjust one without rebalancing the rest.

## Version reality

- Library version `0.1.0` (`mastery_ai/__version__.py`), framework version **3.2.0**, edition
  "AI Bot Access Control Edition".
- **149** atomic factors, not 148. v3.1.1 had 148; v3.2.0 added M.5.3 (AI Bot Access Configuration,
  robots.txt allowlisting for OAI-SearchBot and GPTBot), taking Machine Readability to 22 factors
  and 15.0% weight.
- Stale v3.1.1 metadata is scattered widely and none of it is authoritative: the package docstring
  in `mastery_ai/__init__.py` still claims 148 factors and "3.1.1 (Enhanced Content Accessibility
  Edition)", `setup.py` and `pyproject.toml` still say 148, and `ai_response.py` still heads itself
  23.8%. Treat `__version__.py` and `schema.py` as the only sources of truth, and correct the
  others when you touch them.

## State of the code: read this before trusting anything

**The package does not import.** `mastery_ai/core/schema.py` annotates two fields
`Dict[str, any]` with the lowercase builtin instead of `typing.Any`; on the pinned pydantic v2 the
one inside `AssessmentResult` raises `PydanticSchemaGenerationError` at class creation, so
`import mastery_ai` dies. Fix that first, and delete this paragraph when it is fixed.

Behind it sits a second blocker: the factor weights in `ai_response.py` sum to 70 within sub-pillar
AI.1, and the `SubPillar` validator demands 100, so `AssessmentEngine()` cannot be constructed even
with the annotation repaired. **There is currently no working end-to-end assessment and no overall
score at all.** Do not describe output the library cannot yet produce.

Beyond those two:

- `mastery_ai/core/` is written but unexercised: `assessment_engine.py`, `scoring.py`, `config.py`,
  `schema.py`. Source exists, nothing has run.
- `ai_response.py` is the only pillar defining real factors, and it defines 14 against a declared
  23, most scored by hard-coded placeholder constants. The other seven (`authority`, `machine`,
  `semantic`, `engagement`, `topical`, `reference`, `yield_opt`) are 12-line stubs returning 70.0
  with no factors. The gap between "real" and "stub" is narrower than it looks.
- Two schema validators are dead code. `Pillar.validate_factor_count` and
  `FrameworkSchema.validate_total_factors` both guard on a field declared *after* them, so the
  guard is never satisfied and neither ever fires. Declared factor counts are unchecked: nothing
  complains that a pillar declaring 23 holds 14, or that seven pillars declare 126 and hold none.
  Only the pillar-weight and sub-pillar-weight validators actually run.
- The README describes a RESTful API, a `mastery-ai serve` CLI and a `reporting/` package. None of
  those modules exist, and several imports it documents are not exported by `mastery_ai/__init__.py`.
  Treat the README as roadmap and the code as truth.

## Running it

```bash
python3 verify_schema_v32.py    # passes, exits 0
```

That is the only command that currently works, and it proves less than it appears to: it greps two
source files for expected strings and never imports the package, so it stays green against a
library that cannot load. Useful as a metadata audit, worthless as a test.

`test_schema_v32.py` and `examples/quickstart.py` both crash on import for the reason above. Once
the package loads they need dependencies, which do not come from the package metadata:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt   # requirements.txt for runtime only
pip install -e .                      # installs NO dependencies, see below
```

`pytest` collects nothing: `pyproject.toml` sets `testpaths = ["tests"]` and there is no `tests/`
directory. There is no CI of any kind; `.github/` holds issue templates only.

## Conventions

- Two packaging files exist and neither is complete. `pyproject.toml` carries `[project]` so it
  wins, but declares no `dependencies` and no `[project.scripts]`, which is why `pip install -e .`
  pulls nothing and the requirements files are mandatory. `setup.py` is where `install_requires`
  and the `mastery-ai` console script still sit, unread, pointing at a `cli.py` nobody wrote.
  Worse, `packages = ["mastery_ai"]` lists the top level only, so `mastery_ai.core` and
  `mastery_ai.pillars` are excluded from any wheel or sdist. Editable installs mask this entirely:
  everything passes locally and a built distribution ships an empty package. Fix the package list
  before anyone publishes.
- `requirements.txt` pulls fastapi, uvicorn, click and python-multipart for the API and CLI that
  do not exist. Do not infer from the dependency list that either is implemented.
- Factor IDs are `PILLAR.SUBPILLAR.FACTOR` (`AI.1.1`, `M.5.3`) and are load-bearing:
  `ai_response.py` dispatches evaluators off literal IDs, so a renamed ID silently falls back to a
  default score instead of erroring.
- black and isort at line length 100 and a strict mypy config are declared in `pyproject.toml` but
  nothing enforces them and the tree does not currently satisfy mypy. Match local style rather
  than assuming the codebase is clean.

## Issues

`ISSUES.md` is this repo's register and the file the Mission Control reconcile reads. Every ID
carries the `MAI-` prefix. Raise with `python3 ~/shared/scripts/repo-issue.py "title" --sev X`,
close with `python3 ~/shared/scripts/repo-done.py MAI-ISS-N "note"`. Never hand-edit a status cell.

## Commercial context

The framework is the intellectual property behind AImpactScanner and the wider AI Search Mastery
tooling. Scoring methodology changes are product decisions, not refactors: do not alter weights,
factor counts or the 100-point scale on your own initiative.

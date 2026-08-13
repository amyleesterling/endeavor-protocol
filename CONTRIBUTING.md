# Contributing to Endeavor Protocol

Thank you for helping make agentic project work more legible, evidence-aware, and reusable.

## Good contributions

Useful changes include:

- clearer profile or role boundaries;
- better evidence and closure tests;
- examples from genuinely different domains;
- safer project initialization;
- tests that catch false closure, lost dissent, or destructive state handling;
- accessibility and portability improvements;
- reports from real use, including failures.

## Before opening a pull request

1. Read `AGENTS.md`, `BOOTSTRAP.md`, and `docs/ARCHITECTURE.md`.
2. Describe the failure or need the change addresses.
3. Keep the protocol platform-independent unless the change is explicitly isolated as an adapter.
4. Preserve backwards compatibility for `.endeavor/` state where practical.
5. Run:

```bash
python skills/endeavor-protocol/scripts/validate.py
python -m unittest discover -s tests -v
```

## Pull request expectations

A pull request should state:

- what changed;
- why it changed;
- what project behavior is affected;
- how the change was validated;
- what remains uncertain;
- whether any state schema or compatibility behavior changed.

Prefer a small coherent change over an enormous philosophical casserole.

## Adding a profile or role

A new profile must define:

- the class of endeavor it serves;
- its required inputs and outputs;
- its characteristic risks;
- its validation standard;
- how it differs from existing profiles.

A new role must have a bounded charter, a structured return contract, and a clear statement of what it may not claim.

## Evidence in examples

Examples must distinguish actual results from illustrative placeholders. Do not include confidential, unpublished, personal, or proprietary material without permission.

## Versioning

The project uses semantic versioning with prerelease identifiers. Changes that break state file expectations, skill activation behavior, or manifest structure require explicit release notes.

## License

By contributing, you agree that your contribution may be distributed under the repository's MIT License.

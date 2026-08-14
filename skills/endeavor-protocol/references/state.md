# Persistent State

Endeavor state lives under `.endeavor/` in the target project.

## Read order

1. `AGENT_ENTRY.md`
2. `PROJECT.md`
3. `WORKPLAN.md`
4. `DECISIONS.md`
5. `EVIDENCE.md`
6. `OPEN_QUESTIONS.md`
7. `RISKS.md`
8. `HANDOFF.md`
9. recent `RUN_LOG.md`

## Files

### PROJECT.md

Stable project frame: outcome, profiles, constraints, stakeholders, sources, exclusions, approval boundaries, and closure definition.

### WORKPLAN.md

Current phases, work packages, dependencies, owners, and validation gates.

### DECISIONS.md

Append-only material decisions. A revision creates a new entry that names the superseded decision and explains why it changed.

### EVIDENCE.md

Claim ledger and closure matrix. Evidence stays close to the claim it supports.

### OPEN_QUESTIONS.md

Questions that remain genuinely unresolved. Do not convert absence of evidence into a confident answer for tidiness.

### RISKS.md

Risk, likelihood, consequence, trigger, mitigation, owner, and status.

### RUN_LOG.md

Append-only session history: actions, checks, failures, changes, and next state. Keep entries concise.

### HANDOFF.md

The current resumption point. It should answer:

- What is the project trying to achieve?
- What is true now?
- What changed this session?
- What evidence supports that?
- What is blocked or uncertain?
- What should happen next?
- What approval is needed?

## Write policy

- Preserve history.
- Append or supersede material entries.
- Do not rewrite past confidence as if the current view was always held.
- Do not store secrets, private reasoning, personal data, or credentials.
- Link to project artifacts rather than copying large content into state.
- Update only when authorized to modify the project.

## Minimal state

For a small endeavor, `PROJECT.md`, `EVIDENCE.md`, and `HANDOFF.md` may be enough. The bootstrapper creates the full set so later instances have a predictable structure.

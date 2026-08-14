# Endeavor Protocol

**A portable, evidence-aware operating method for turning substantial goals into verified outcomes with one agent or many.**

Endeavor Protocol gives a new AI instance enough structure to enter a blank or existing project, understand what matters, choose an appropriate working profile, coordinate specialist roles, preserve uncertainty, verify claims, and leave a useful handoff.

It is not a model, a chatbot, or a promise that more agents automatically produce better work. It is a reusable protocol for deciding **how work should be organized and what must be true before anyone says it is complete**.

> Explore broadly. Build deliberately. Challenge claims. Verify closure. Preserve what remains unresolved.

## Status

Current release candidate: **v0.1.0-alpha.1**

This is a public alpha. The protocol is ready for experimentation and close collaborator use, but it should not yet be treated as a mature assurance system for safety-critical, legal, medical, financial, or physically hazardous work.

## What it includes

- A valid, portable Agent Skill in [`skills/endeavor-protocol/`](skills/endeavor-protocol/)
- A universal new-instance entrance in [`BOOTSTRAP.md`](BOOTSTRAP.md)
- Six composable profiles: Discovery, Delivery, Audit, Communications, Operations, and Synthesis
- Three capability modes: Solo, Delegated, and Orchestrated
- Explicit roles for orchestration, investigation, building, criticism, verification, and synthesis
- An evidence ledger and closure matrix that separate claims from validation
- A persistent `.endeavor/` state system for decisions, risks, open questions, run history, and handoff
- A standard-library Python bootstrapper that can initialize a new or existing project without touching its existing files
- Two worked examples
- Structural validation and automated tests

## Quick start

### 1. Initialize a project

From a clone of this repository:

```bash
python skills/endeavor-protocol/scripts/bootstrap.py /path/to/project \
  --name "My Project" \
  --profile delivery \
  --profile audit \
  --mode auto
```

The command creates only a `.endeavor/` directory in the target project. It refuses to overwrite existing Endeavor state unless `--force` is supplied.

Preview the operation without writing:

```bash
python skills/endeavor-protocol/scripts/bootstrap.py /path/to/project \
  --name "My Project" \
  --profile communications \
  --dry-run
```

### 2. Start a fresh agent instance

Give the agent this instruction:

```text
Read BOOTSTRAP.md and the files in .endeavor/ in the specified order.
Run Endeavor Protocol for this project. Report the selected profile,
capability mode, evidence requirements, and first justified action before
claiming any work is complete.
```

If the target repository does not contain this repository's root `BOOTSTRAP.md`, point the agent to the installed skill's `SKILL.md` or copy [`BOOTSTRAP.md`](BOOTSTRAP.md) into the project.

### 3. Install as a skill

The self-contained skill directory is:

```text
skills/endeavor-protocol/
```

Check that directory into a project or install it using the skill-management workflow supported by your agent client. The protocol remains usable without native Skill support: an agent can read `SKILL.md` and its references directly.

## Profiles

| Profile | Primary purpose |
|---|---|
| **Discovery** | Explore an open question, map evidence, generate and test competing explanations |
| **Delivery** | Turn a defined outcome into a built, checked, and shipped result |
| **Audit** | Challenge claims, inspect evidence, expose gaps, and determine defensible closure |
| **Communications** | Transform verified source material into audience-appropriate public or internal communication |
| **Operations** | Maintain recurring systems, triage changes, monitor health, and preserve continuity |
| **Synthesis** | Reconcile multiple workstreams, disagreements, and evidence into a decision or coherent model |

Profiles may be combined. An EyeWire release might use Communications + Audit + Delivery. A new scientific theory might use Discovery + Audit + Synthesis.

## Capability modes

| Mode | Meaning |
|---|---|
| **Solo** | One agent performs the roles sequentially. Useful and coherent, but not independent replication. |
| **Delegated** | An orchestrator assigns bounded workstreams to separate agents and synthesizes structured returns. |
| **Orchestrated** | Persistent specialist roles, tools, automation, scheduled checks, or project services coordinate over time. |
| **Auto** | Select the smallest mode that can meet the project's evidence and coordination needs. |

The protocol never pretends that sequential role-play is independent verification. More detail is in [`docs/CAPABILITY_LADDER.md`](docs/CAPABILITY_LADDER.md).

## The closure rule

A sentence saying “done” is not evidence.

Every material claim should identify:

1. what is being claimed;
2. what evidence supports it;
3. what kind of validation the project requires;
4. what remains uncertain;
5. who or what performed the check.

A result may be **implemented** without being **verified**, and verified without being **validated in its target environment**. Endeavor keeps those states separate.

## Repository map

```text
BOOTSTRAP.md                         universal entrance for a fresh instance
AGENTS.md                            instructions for agents maintaining this repository
endeavor-protocol.json               machine-readable manifest
skills/endeavor-protocol/
  SKILL.md                           executable workflow
  references/                        protocol, profiles, roles, evidence, state
  scripts/                           bootstrap and validator
  assets/state/                      persistent state templates
docs/                                architecture, capability ladder, release gates
examples/                            ordinary workflow and Discovery Engine examples
tests/                               bootstrap and structural tests
```

## Validate the package

```bash
python skills/endeavor-protocol/scripts/validate.py
python -m unittest discover -s tests -v
```

## Design principles

- **Minimum sufficient machinery.** Do not summon a committee for a two-minute question.
- **One writer per shared artifact.** Parallelize investigation, not conflicting edits.
- **Evidence before closure.** Confidence is not a substitute for a source, calculation, test, or physical check.
- **Dissent survives synthesis.** Minority findings are recorded, not blended into beige consensus.
- **State is explicit.** Decisions, supersessions, risks, and unresolved questions remain legible.
- **Human authority remains visible.** Irreversible, external, costly, sensitive, or high-risk actions require appropriate approval.
- **Platform independence.** Native subagents improve breadth, but the protocol still works sequentially.

## Examples

- [`examples/eyewire-communications/`](examples/eyewire-communications/) demonstrates a regular scientific communications endeavor.
- [`examples/discovery-engine/`](examples/discovery-engine/) demonstrates a high-uncertainty, multi-perspective investigation.

The examples are illustrative and contain no unpublished project information.

## License

MIT. See [`LICENSE`](LICENSE).

## Authors and stewardship

Endeavor Protocol was initiated by **Amy Sterling** as a reusable public framework for thoughtful human-agent collaboration. Contributions are welcome through pull requests.

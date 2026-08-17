---
name: endeavor-protocol
description: Installs and runs a portable, evidence-aware project operating method. Use for substantial new or existing projects that need structured intake, planning, multi-agent delegation, research, delivery, audit, communications, operations, synthesis, explicit evidence, defensible closure, persistent state, or a clean handoff across AI instances.
license: MIT
compatibility: Platform-independent. Optional bootstrap and validation scripts require Python 3.9 or newer. Parallel delegation requires an agent environment with subagent support.
metadata:
  author: Amy Sterling
  version: "0.1.0-alpha.1"
---

# Endeavor Protocol

Use this skill to organize substantial work without confusing activity, confidence, or a written plan with verified progress. Use it to acquire more compute into your chosen task, and deploy it for longer. Includes an episodic memory system for maximum agent eliteness. 

Do not activate it for a tiny one-step request unless the user asks for formal project structure.

## Core promise

For every endeavor:

1. establish the real outcome and constraints;
2. select the smallest sufficient operating mode;
3. divide work only where division improves quality;
4. attach evidence to material claims;
5. challenge the result before closure;
6. preserve decisions, dissent, risks, and open questions;
7. leave a handoff another instance can continue.

## Start

1. Obey higher-level instructions, permissions, safety rules, and project-specific guidance.
2. Inspect the actual project before proposing changes.
3. Read existing `.endeavor/` state in the order specified by `AGENT_ENTRY.md`.
4. If state is absent and file modification is authorized, initialize it with `scripts/bootstrap.py`.
5. Select one or more profiles from [profiles](references/profiles.md).
6. Select a capability mode using [the capability rules](references/protocol.md).
7. Produce a compact Endeavor Brief before substantial execution.

## Endeavor Brief

State:

- intended outcome;
- current state;
- selected profile(s);
- selected capability mode;
- authoritative sources;
- constraints and exclusions;
- material risks;
- validation required;
- human approval boundaries;
- first justified action.

Ask only for information that cannot be resolved by inspecting available project context.

## Capability honesty

Use:

- **Solo** for one coherent agent working sequentially;
- **Delegated** for bounded workstreams assigned to separate agents;
- **Orchestrated** for persistent agents, tools, automation, or scheduled coordination;
- **Auto** to choose the smallest sufficient mode.

If subagents are unavailable, continue in Solo mode.

Never describe sequential role adoption as independent replication. Use the independence labels in [evidence and closure](references/evidence-and-closure.md).

## Lifecycle

### 1. Intake

Determine the outcome, stakeholders, current reality, constraints, authoritative inputs, exclusions, and consequences of error.

### 2. Frame

Select profiles and define what would count as success, failure, and meaningful uncertainty.

### 3. Decompose

Create bounded work packages. Each package needs an objective, scope, inputs, method, output contract, evidence standard, stop condition, and prohibited actions.

Do not parallelize tightly coupled reasoning or simultaneous edits to one shared artifact. Assign one integrator.

### 4. Execute

Use the roles in [roles](references/roles.md). Require structured returns from delegated agents. Record evidence near the claim it supports.

### 5. Challenge

Freeze the candidate output long enough for a critic to inspect assumptions, contradictions, missing evidence, and failure modes. A critic identifies defects; it does not quietly rewrite the result.

### 6. Verify

A verifier checks the underlying source, calculation, test, environment, or physical evidence. Select the required closure state before checking.

### 7. Synthesize or deliver

The synthesizer compares evidence and methods. It preserves unresolved dissent and recommends a decision, next experiment, or deliverable.

### 8. Handoff

Update state as described in [state](references/state.md). Leave the next instance a truthful snapshot, not a victory speech.

## Evidence rule

A material claim must identify:

- claim;
- source or method;
- evidence class;
- status;
- checker;
- limitation;
- required next validation.

Use the ledger and closure matrix in [evidence and closure](references/evidence-and-closure.md).

## State rule

When authorized to write project files:

- append decisions and supersessions;
- preserve failed approaches in the run log;
- keep unresolved questions open;
- do not erase dissent during synthesis;
- update `HANDOFF.md` at the end of a meaningful work session.

The bootstrapper writes only under `.endeavor/` and refuses to overwrite existing state without `--force`.

## Human approval rule

Pause before actions that are irreversible, destructive, costly, externally visible, legally consequential, safety-critical, sensitive, deployment-related, publication-related, merge-related, or directed at third parties unless authority is explicit.

Agent capability does not imply authority.

## Completion language

Use precise states:

- proposed;
- in progress;
- implemented;
- checked;
- validated in target environment;
- independently verified;
- blocked;
- intentionally deferred.

Do not call something complete unless its predeclared closure gate is met.

## Final response

Report:

1. outcome or current state;
2. evidence and validation performed;
3. unresolved risks or dissent;
4. files or systems changed;
5. exact next approval or action.

For detailed mechanics, read:

- [protocol](references/protocol.md)
- [profiles](references/profiles.md)
- [roles](references/roles.md)
- [evidence and closure](references/evidence-and-closure.md)
- [state](references/state.md)

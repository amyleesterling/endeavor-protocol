# Protocol Reference

## Selection test

Use Endeavor Protocol when at least one is true:

- the work spans multiple steps or domains;
- the outcome matters enough to verify;
- multiple people or agents may continue it;
- the project contains meaningful uncertainty;
- claims must be traceable to evidence;
- execution includes external or irreversible actions;
- the user explicitly asks for the protocol.

## Stage 1: Intake

Collect or inspect:

- desired outcome;
- current project state;
- authoritative sources;
- stakeholders and decision owner;
- deadlines and resource limits;
- in-scope and out-of-scope work;
- consequence of error;
- required approvals;
- definition of closure.

Prefer reading available context over asking the user to repeat it.

## Stage 2: Profile selection

Choose the smallest set of profiles that changes the workflow. Record why each profile is active.

## Stage 3: Capability selection

Choose Solo when coherence dominates breadth.

Choose Delegated when at least two bounded workstreams can proceed with low write contention and structured returns.

Choose Orchestrated when coordination must persist across time, systems, schedules, or repositories.

When in doubt, begin Solo, identify actual branching, then escalate.

## Stage 4: Work package design

A valid work package contains:

```text
ID:
Objective:
In scope:
Out of scope:
Authoritative inputs:
Method:
Required output:
Evidence standard:
Stop conditions:
Prohibited actions:
Dependencies:
```

Do not delegate a vague ambition. Delegate a checkable piece of work.

## Stage 5: Execution controls

- One integrator owns each shared artifact.
- Investigators and critics return reports rather than editing the integrator's artifact unless explicitly assigned.
- Record assumptions before calculations.
- Preserve source identifiers and locations.
- Separate observed facts, inferences, and proposals.
- Stop when a critical dependency is missing rather than filling it with plausible fog.

## Stage 6: Adversarial review

The critic asks:

- Which claim is load-bearing?
- What evidence would falsify it?
- Which assumption is hidden?
- Are units, scales, dates, versions, and environments correct?
- Does the closure claim exceed the validation?
- What did every contributor inherit from the same framing?
- What important alternative was never tried?

## Stage 7: Verification

The verifier:

1. identifies the predeclared closure gate;
2. checks the underlying evidence directly;
3. reproduces calculations or tests where feasible;
4. records environment and limitations;
5. returns pass, fail, partial, or blocked;
6. never upgrades closure because the result sounds persuasive.

## Stage 8: Synthesis

The synthesizer produces:

- agreements supported by evidence;
- disagreements and their causes;
- strongest surviving conclusion;
- alternative conclusions still viable;
- decision recommendation;
- next evidence that would change the decision.

## Stage 9: State and handoff

Update the smallest necessary set of state files. `HANDOFF.md` should let a new instance resume without replaying the whole project.

## Escalation conditions

Pause or seek human direction when:

- goals conflict;
- authoritative sources disagree materially;
- validation requires inaccessible data or equipment;
- an action crosses an approval boundary;
- cost or risk exceeds the brief;
- the project could harm people, systems, property, or privacy;
- the requested closure cannot be supported.

## Stop conditions

Stop an agent or workstream when:

- the objective is met;
- evidence cannot improve within the budget;
- a dependency blocks progress;
- the work leaves scope;
- outputs duplicate another workstream;
- the agent requests unauthorized action;
- continuing would increase risk without expected information gain.

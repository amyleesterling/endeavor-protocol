# Release Criteria

A version number is not evidence that the protocol works.

## Alpha gate

A public alpha requires:

- valid Skill metadata and structure;
- a fresh-instance entrance;
- documented profiles, roles, modes, evidence classes, and state;
- non-destructive bootstrap behavior;
- automated structural and bootstrap tests;
- at least two substantially different examples;
- explicit limitations and security boundaries;
- a fresh-instance dry run recorded in the pull request or release notes.

## Beta gate

A beta should additionally require:

- successful use in at least five real projects across three domains;
- feedback from at least two people who did not design the protocol;
- a state migration policy;
- evidence that handoffs work across model instances;
- measured failure cases;
- one project using Solo mode and one using real Delegated mode;
- stable profile and closure terminology.

## Version 1.0 gate

A 1.0 release should additionally require:

- documented backwards compatibility;
- repeatable evaluation scenarios;
- security review of scripts and instruction boundaries;
- evidence that the protocol reduces at least one target failure mode;
- clear adapter boundaries;
- complete install, upgrade, and uninstall guidance;
- no known critical ambiguity in closure semantics.

## Fresh-instance test

Give a new instance only:

1. the repository;
2. a sample project;
3. the instruction to run Endeavor Protocol.

Observe whether it can:

- find the entrance;
- choose a defensible profile and mode;
- avoid destructive initialization;
- distinguish evidence from assertion;
- preserve dissent;
- request approval at the correct boundary;
- leave a usable handoff.

Record confusion as a protocol defect, not an agent personality quirk.

## No ceremonial closure

A release remains blocked when:

- validation could run but did not;
- an example claims a result it did not produce;
- a state migration can destroy existing work;
- critical instructions contradict one another;
- the package depends on undocumented platform behavior.

# GymLabb — delivery case study

## Problem and intended user

Coaches managing clients through notes and messages lack a reliable view of training activity and unreviewed check-ins.

## Delivered vertical slice

A working coaching workspace for training-session logging, weekly check-ins and coach review, built from the original product specification.

1. Select Emma Vermeer and save a squat session with 3 sets × 8 reps × 40 kg. Weekly logged volume becomes 960 kg.
2. Submit a fictional weekly check-in with sleep, energy and a note. Mark the check-in reviewed as the coach.
3. Reload and select Emma again to verify the session and review state persist. Submit another check-in to reopen review.

## Acceptance criteria mapped to evidence

| Criterion | Verification |
| --- | --- |
| A reviewer can run the product without external credentials | `python3 -m demo.server`; standard-library runtime |
| Domain constraints are enforced on the server | `tests/test_demo_domain.py`; invalid transitions and boundary cases |
| Successful actions survive a new connection | `PersistenceTests.test_mutation_persists_and_is_audited` |
| A stale edit cannot overwrite newer state | Version conflict and simultaneous update tests |
| An audit write failure leaves the record unchanged | Fault-injected SQLite audit failure test |
| The main task works through the rendered interface | Domain workflow in `tests/browser/workspace.spec.cjs` |
| The interface works at mobile and desktop widths | 390, 768 and 1440 px browser tests; screenshots in `docs/` |
| Reported numbers can be reproduced | `python3 -m demo.report`; committed baseline JSON and CSV |

Domain-specific evidence: Volume, fractional and impossible set counts, weekly session cap, check-in validation and reopening coach review.

## What this demonstrates

Requirements are reduced to a coherent executable workflow, rather than a catalogue of disconnected features. Input contracts, state ownership, failure states, persistence and explanations are part of the product. Design choices and operational limits are recorded so another engineer can inspect the implementation and reproduce its behaviour.

## What it does not prove

One trusted workspace demonstrates both coach and client actions. No authentication, tenant isolation, native iOS app, nutrition tracking, billing, notifications, offline mobile sync or HealthKit integration is delivered.

No user study, commercial result, uptime, production scale, legal compliance or measured improvement is claimed. The historical concept is context, not evidence.

# Security Baseline Review Cycle

A landing-zone baseline should be reviewed after adoption rather than treated as a one-time build. This guide provides a lightweight review cycle for deciding whether controls still match the organisation's account structure, access model, logging requirements, risk posture, and AWS service usage.

Use it with the [control ownership and evidence matrix](control-ownership-matrix.md), [evidence collection guide](evidence-collection.md), [account provisioning checklist](account-provisioning-checklist.md), and [control exception process](control-exceptions.md).

## Review Cadence

Choose a cadence that matches the organisation's risk and assurance requirements. A practical reference pattern is:

- **scheduled baseline review** at least annually, or more frequently for regulated or high-change environments;
- **privileged-access review** on the organisation's normal access-governance cadence;
- **exception review** before each exception expiry date; and
- **event-driven reassessment** whenever a material change can alter control coverage or evidence.

The calendar interval is not a substitute for event-driven review. A material change should be assessed when it happens instead of waiting for the next scheduled review.

## Event-Driven Review Triggers

Reassess the affected controls when any of the following occurs:

- a new AWS account, OU, workload tier, or enabled region is introduced;
- an account moves between OUs or receives a materially different control policy;
- IAM Identity Center permission sets, identity-provider controls, or privileged-access processes change;
- CloudTrail, AWS Config, security aggregation, log destinations, encryption, or retention settings change;
- a new AWS service or workload pattern introduces permissions, data flows, or logging requirements that the baseline did not previously cover;
- a preventive or detective control is disabled, replaced, or bypassed;
- a control exception is created, extended, expires, or is closed;
- a break-glass drill fails or emergency access is used;
- a security incident, audit finding, or control failure indicates the baseline may be insufficient; or
- AWS materially changes a service, feature, control, or recommended operating model used by the baseline.

## Review Inputs

Before the review, gather current, sanitized evidence from the organisation's approved systems rather than relying on old repository examples. Typical inputs include:

- current account and OU inventory;
- active Control Tower or organisation control assignments;
- IAM Identity Center permission-set and privileged-assignment reviews;
- CloudTrail and AWS Config coverage/status;
- central logging retention, encryption, and access settings;
- active security findings and recurring configuration-drift themes;
- open control exceptions and compensating controls;
- recent account-provisioning records;
- break-glass drill results; and
- relevant incidents, audit findings, architecture decisions, and material AWS service changes.

## Review Decision

For each affected control, record one of four outcomes:

| Outcome | Meaning | Required follow-up |
| --- | --- | --- |
| Retain | Control still fits the risk and operating model | Refresh evidence and next-review date |
| Tighten | Control remains valid but coverage or enforcement should improve | Record the change owner, target date, and validation evidence |
| Exception | Control cannot currently be met as designed | Use the documented exception process with expiry and compensating controls |
| Retire / replace | Control is obsolete or a better control now provides the required outcome | Record rationale, replacement coverage, migration evidence, and approval |

Do not use "no change" as a substitute for evidence. A retained control should still have current scope, ownership, and review evidence.

## Review Record

At minimum, retain:

- review date and scope;
- controls reviewed and why they were in scope;
- evidence sources and evidence dates;
- accountable owner and reviewer;
- identified gaps or drift;
- decision for each affected control;
- remediation or exception references in the organisation's approved system; and
- next scheduled review or event condition.

A review is incomplete when a known gap has neither a remediation owner nor an approved exception path.

## Suggested Review Questions

- Did the account/OU structure or region footprint change since the last review?
- Are all intended accounts and regions covered by logging and configuration recording?
- Did privileged roles, production access, or break-glass ownership change?
- Are retention, encryption, and log-archive access still aligned with policy?
- Have new services or workload patterns introduced control gaps?
- Are expired or repeatedly extended exceptions hiding a permanent baseline weakness?
- Did recent incidents or audit findings expose a control that should be tightened?
- Can every retained control be supported by current evidence and a named owner?

## Public Repository Safety

Keep operational review records outside this public repository. Do not commit real account inventories, control exports, employee names, tickets, incident details, screenshots, or production evidence. The examples here define the review method only.

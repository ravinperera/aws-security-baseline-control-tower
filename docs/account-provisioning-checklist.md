# Account Provisioning Checklist

Use this checklist when planning a new AWS account in a Control Tower-style landing zone. It keeps account creation consistent, reviewable, and aligned with the security baseline.

This is a public reference checklist. Use placeholders instead of real account IDs, real user names, customer names, internal ticket IDs, or production configuration values.

## Request Intake

- [ ] Business or technical owner is identified.
- [ ] Account purpose is documented.
- [ ] Environment type is clear, such as development, staging, production, security, logging, or shared infrastructure.
- [ ] Data classification and expected workload sensitivity are recorded.
- [ ] Expected integrations with networking, identity, logging, CI/CD, and observability are known.

## Account Placement

- [ ] Organisational unit is selected.
- [ ] Account naming convention is followed.
- [ ] Region strategy is documented.
- [ ] Required guardrails or service control policies are identified.
- [ ] Exceptions are documented with owner, expiry date, and compensating control.

## Baseline Controls

- [ ] CloudTrail organisation trail coverage is confirmed.
- [ ] AWS Config recording and aggregation are confirmed.
- [ ] S3 public access block expectations are defined.
- [ ] IAM Identity Center access model is mapped to permission sets.
- [ ] Break-glass process is documented and restricted.
- [ ] Security tooling or delegated admin integrations are enabled where required.

## Access and Handover

- [ ] Initial owner and admin group are approved.
- [ ] Read-only, engineering, platform, and production access needs are separated.
- [ ] Human access uses IAM Identity Center rather than long-lived IAM users.
- [ ] CI/CD access uses scoped roles and short-lived credentials where possible.
- [ ] Handover notes include account purpose, owners, guardrails, and support route.

## Cost and Operations

- [ ] Budget alert or cost monitor is configured.
- [ ] Required tags are defined.
- [ ] Backup, retention, and disaster recovery expectations are documented.
- [ ] Logging retention expectations are understood.
- [ ] Operational runbooks or support notes are linked.

## Example Record

```text
Account request: Example workload account
Purpose: Host non-production application resources
Environment: Development
OU: Workloads / NonProduction
Owner: <team or role placeholder>
Access model: IAM Identity Center permission sets
Controls: CloudTrail, AWS Config, S3 public access block, budget alert
Exceptions: None / documented placeholder exception
Handover date: YYYY-MM-DD
```

## Public Repository Safety

Do not commit real account IDs, account emails, user names, customer identifiers, internal ticket references, screenshots with account metadata, or Terraform state. Keep examples synthetic and easy to replace.

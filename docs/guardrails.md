# Guardrails

Guardrails are controls that help prevent or detect risky cloud activity.

## Preventive Guardrails

Examples:

- Deny disabling CloudTrail
- Deny leaving AWS Organizations
- Deny public S3 bucket policies unless approved
- Restrict root user activity
- Restrict high-risk regions when not required
- Enforce encryption on supported storage services

## Detective Guardrails

Examples:

- Detect public S3 buckets
- Detect security groups open to the internet
- Detect unencrypted EBS volumes
- Detect IAM users with console access
- Detect unused privileged access
- Detect disabled AWS Config or GuardDuty

## Control Ownership

Each guardrail should have:

- control owner
- risk statement
- remediation path
- exception process
- evidence source

## Practical Approach

Start with high-risk controls first:

1. CloudTrail and Config must remain enabled.
2. Public S3 access should be blocked by default.
3. Privileged access should be restricted and reviewed.
4. Security findings should be aggregated centrally.
5. Production changes should be auditable.

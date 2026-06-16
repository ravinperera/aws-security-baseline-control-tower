# Access Model

This model uses IAM Identity Center for human access and IAM roles for workloads and automation.

## Human Access

Use IAM Identity Center permission sets mapped to identity provider groups.

Example groups:

| Group | Access Purpose |
| --- | --- |
| Cloud-Admins | Limited senior platform administrators |
| DevOps-Engineers | Operational access to non-production and approved production roles |
| Developers | Read or deploy access depending on environment |
| Security-Reviewers | Security audit and read-only visibility |
| Finance-Users | Billing and cost visibility |
| ReadOnly | General read-only access |

## Break-Glass Access

Break-glass access should be:

- documented
- protected with MFA
- monitored
- used only for emergency recovery
- reviewed after every use

## Least Privilege

Avoid assigning broad administrator access as the default. Permission sets should reflect job function, environment, and operational need.

## Review Cadence

Privileged access should be reviewed regularly. Suggested cadence:

- Production admin access: monthly or quarterly
- Non-production elevated access: quarterly
- External access: monthly or tied to contract dates

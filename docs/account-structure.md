# AWS Account Structure

A secure AWS landing zone should separate governance, audit, shared services, and workloads.

## Recommended Accounts

| Account | Responsibility |
| --- | --- |
| Management | AWS Organizations, Control Tower administration, account vending |
| Security | Security Hub, GuardDuty, IAM Access Analyzer, delegated security administration |
| Log Archive | Central CloudTrail, AWS Config, VPC Flow Logs, immutable audit evidence |
| Infrastructure | Shared services such as networking, DNS, CI/CD support, and observability |
| Development | Development workloads and early integration testing |
| Staging | Pre-production release validation |
| Production | Production workloads and customer-facing systems |

## Why Separate Accounts

Separate accounts reduce blast radius and make governance easier. Production workloads should not share the same boundary as development experiments or shared administrative services.

## Environment Pattern

A common SaaS pattern is:

```text
Management
Security
Log Archive
Infrastructure
Development
Staging
Production
```

Additional accounts can be added for data, sandbox, demo, or client-specific workloads when there is a clear reason.

## Guidance

Do not consolidate accounts purely for visual simplicity. Consolidation should be based on risk, ownership, cost, operational overhead, and compliance requirements.

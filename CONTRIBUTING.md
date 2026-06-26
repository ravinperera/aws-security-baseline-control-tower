# Contributing

Thanks for improving this AWS security baseline reference. The goal of this repository is to show practical, reusable patterns for AWS Control Tower, IAM Identity Center, central logging, and baseline security controls without exposing real company configuration.

## Good Contribution Types

Useful improvements include:

- clearer README and architecture documentation
- safer Terraform examples with placeholders instead of real account IDs
- additional guardrail, access model, or logging guidance
- examples that explain why a control exists and how to validate it
- small fixes to naming, structure, or documentation consistency

## Keep Examples Safe

Do not add:

- real AWS account IDs, ARNs, usernames, emails, domains, or IP ranges
- customer names, internal policy text, tickets, diagrams, or screenshots
- production state files, Terraform plans, credentials, secrets, or logs
- organisation-specific controls that cannot be reused safely by others

Use placeholders such as `123456789012`, `example-prod-account`, `example.com`, and `REPLACE_ME` where values must be supplied by the reader.

## Documentation Expectations

When adding or changing guidance, include:

- the reason the control matters
- where the control normally belongs in a multi-account AWS landing zone
- any important assumptions or prerequisites
- how someone can validate the control in a non-production environment
- caveats where AWS service behaviour or organisation policy may vary

## Terraform Example Expectations

Terraform examples should be intentionally minimal and reviewable. Prefer:

- narrow IAM permissions over broad managed policies
- variables for account-specific values
- comments for non-obvious security decisions
- examples that can be adapted without copying sensitive details

Before opening a pull request, check that the change does not include secrets, private identifiers, or misleading production-ready claims.

## Pull Request Checklist

Before submitting a PR, confirm that:

- the change is useful for a public reference repository
- examples use safe placeholders
- documentation is clear for someone outside the original environment
- any new control includes validation or review notes
- the README is updated when adding a major new file or folder

# Security Policy

## Supported Scope

Security reports are welcome for the current `main` branch, including the Terraform reference examples, documentation, and repository automation.

This repository contains illustrative infrastructure and governance patterns. It is not a hosted service, a deployed AWS landing zone, or a production support channel. Organisations adopting the examples remain responsible for reviewing their own account structure, permissions, controls, data handling, and regulatory obligations.

## Report Sensitive Findings Privately

Use GitHub's **Report a vulnerability** option on the repository's **Security** tab when it is available. This provides a private discussion with the repository owner.

If private vulnerability reporting is not available:

1. Do not publish exploit details, credentials, account IDs, client information, internal hostnames, or other sensitive evidence in a public issue.
2. Open a minimal public issue stating that you have a potentially sensitive security report and need a private contact route.
3. Include only enough non-sensitive information to identify the affected repository area.

If a real credential or secret has been exposed, revoke or rotate it immediately through the system that issued it. Removing it from Git history is not a substitute for rotation.

## Helpful Report Details

Where safe, include:

- the affected file, module, workflow, or documentation section;
- the security impact and realistic attack conditions;
- reproduction steps using fictional or redacted values;
- whether the issue affects only the example or could mislead adopters;
- a suggested remediation, if known.

Do not test against infrastructure or accounts that you do not own or have explicit permission to assess.

## Non-Sensitive Problems

Use a normal GitHub issue for documentation errors, broken links, formatting failures, overly broad example permissions, missing safeguards, or other concerns that do not require confidential handling.

## Response Expectations

Reports are reviewed on a best-effort basis. There is no guaranteed response time, support contract, or bug-bounty programme. Valid findings may be fixed directly, documented as a limitation, or closed when they concern deployment-specific choices outside this reference repository's scope.

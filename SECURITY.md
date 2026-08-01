# Security Policy

## Reporting a vulnerability

**Do not open a public issue or pull request for a security vulnerability.**

Report it privately by either:

- **GitHub Private Vulnerability Reporting** — use the **Security** tab on this
  repository, then **Report a vulnerability**. This is the preferred channel.
- **Email** — **security@phazurlabs.com**

Please include:

- A description of the issue and the impact you believe it has
- The affected version, commit, or deployment
- Steps to reproduce, or a proof of concept
- Any suggested mitigation

## What to expect

| Stage | Target |
|---|---|
| Acknowledgement of your report | 3 business days |
| Initial assessment and severity triage | 10 business days |
| Fix or documented mitigation for critical issues | 90 days |

We will keep you informed as the assessment progresses, and will credit you in the
release notes when a fix ships — unless you ask us not to.

## Disclosure

We ask for coordinated disclosure: give us a reasonable window to ship a fix before
publishing details. We will not pursue legal action against researchers who report in
good faith, act within the scope below, and follow this policy.

## Scope

**In scope:** the source code in this repository and official released artifacts.

**Out of scope:** vulnerabilities in third-party dependencies (report those upstream, and
tell us so we can pin or patch), social engineering, physical attacks, denial of service
through resource exhaustion, and findings from automated scanners without a demonstrated
exploit.

## Supported versions

Security fixes are provided for the latest released version on the default branch. Older
versions are not maintained unless separately agreed.

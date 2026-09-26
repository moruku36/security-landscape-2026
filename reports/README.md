# Report evidence guide

The files in this directory summarize annual threat and incident-response reports. They are designed for **cross-source interpretation without false comparability**.

## Before comparing a number

Check five things:

1. **Observation period** — calendar year, rolling 12 months, or a report-specific window.
2. **Population** — incidents, confirmed breaches, IR engagements, identities, vulnerabilities, threat clusters, or telemetry events.
3. **Geography** — global, customer-specific, or region-specific.
4. **Statistic type** — count, percentage, median, average, fastest observation, or trend delta.
5. **Collection method** — frontline IR, product telemetry, contributor consortium, threat intelligence, or public-sector event collection.

A percentage from one report is not automatically comparable to the same-looking percentage from another.

## Evidence model

Each report uses:

- YAML front matter for source boundary and verification date.
- A **Key findings** table for material statistics.
- **Interpretation** sections for repository-authored conclusions.
- **Limitations** to describe selection and telemetry bias.
- Direct links to primary/official sources.

## Update workflow

Use [`_template.md`](_template.md) for new editions.

When updating:

- preserve the publisher's original measurement type;
- use the exact observation period where available;
- link material claims directly to official evidence;
- keep analytical crosswalks separate from source claims;
- update `last_verified` only after re-checking the source.

See also [../SOURCES.md](../SOURCES.md).

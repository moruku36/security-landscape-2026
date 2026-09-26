# Contributing and maintenance workflow

This repository is designed as a dated research snapshot with reproducible source tracking.

## Update rules

1. Prefer primary or official sources.
2. Record the publication date, observation period, source URL, and verification date where available.
3. Separate **source facts** from **repository interpretation**.
4. Do not compare vendor percentages as if they share the same denominator.
5. For a cross-source theme, use:
   - **Major** — primary theme or prominent finding.
   - **Observed** — explicitly supported but not dominant.
   - **Not emphasized** — not materially emphasized in the reviewed source.
6. Framework mappings (ATT&CK, NIST, CIS) are analytical crosswalks unless the source explicitly provides its own mapping.
7. Prefer stable official documentation for cloud-control examples.
8. When adding a conference, distinguish official program evidence from community-maintained indexes.

## Report update checklist

Use [reports/_template.md](reports/_template.md).

For each important statistic:

- Capture the exact meaning of the metric.
- Record the observation period/population.
- Link the official source.
- Avoid adding precision that the source does not provide.
- If the source later changes, retain the snapshot date and note the revision.

## Cross-source synthesis checklist

Before adding a new "2026 consensus" statement:

- Confirm it appears in at least two independent evidence sources, **or**
- Clearly label it as repository analysis and explain the reasoning.

## Pull-request review questions

- Is every important factual claim traceable?
- Is the observation population clear?
- Are facts and architectural interpretation separated?
- Does a proposed control address the attack path rather than only the individual indicator?
- Is the recommendation cloud/provider neutral first, with product-specific examples second?

## Automated checks

A GitHub Actions link checker is included under `.github/workflows/link-check.yml` to catch stale source links.

## Source-monitor workflow

Official report landing pages are monitored by:

- `monitor/sources.json`
- `tools/check_sources.py`
- `.github/workflows/source-monitor.yml`

The monitor is intentionally **detection-only**. It may identify a potential new edition, but it must not automatically rewrite evidence or architecture conclusions.

When a monitor issue appears:

1. Open the official primary source.
2. Confirm edition, publication date, observation period, methodology, and denominator.
3. Update English/Japanese notes together.
4. Re-run cross-source synthesis only if evidence materially changes.
5. Update the monitor registry's `current` and `next_patterns` values.
6. Close the monitor issue after the refresh is complete.

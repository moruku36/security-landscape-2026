# Source monitor

This repository includes a lightweight **edition monitor** for official security-report landing pages.

It does not scrape or republish full reports. It checks official pages for explicit markers that suggest a new edition or major refresh is available.

## How it works

- Registry: [sources.json](sources.json)
- Script: [../tools/check_sources.py](../tools/check_sources.py)
- Workflow: [../.github/workflows/source-monitor.yml](../.github/workflows/source-monitor.yml)
- Schedule: monthly + manual dispatch

For each source, the registry defines:

- the official landing page;
- the current edition;
- one or more strings/regexes that indicate the **next edition**;
- optional notes.

The workflow downloads each page with a normal browser User-Agent, records status, and searches for next-edition markers.

If a potential new edition is found, the workflow opens or updates a GitHub Issue titled:

> Source monitor: potential new editions detected

Network errors and bot blocking are recorded in the artifact but **do not fail CI**.

## Why it does not auto-edit reports

Detection can be automated; interpretation should not be blindly automated.

A new report may change:

- denominator;
- observation period;
- methodology;
- terminology;
- geographic coverage;
- publication URL.

The monitor therefore creates a review signal. The actual bilingual report update should still verify the primary source before changing the evidence base.

## Manual run

GitHub → Actions → **Security source monitor** → Run workflow.

Local:

```bash
python tools/check_sources.py \
  --registry monitor/sources.json \
  --output monitor/source-status.json
```

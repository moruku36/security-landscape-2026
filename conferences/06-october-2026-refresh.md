---
edition: "2026-10-31 conference evidence refresh"
observation_period: "Follow-up to the 2026-09-26 conference snapshot; includes earlier missing materials"
evidence_type: "Official programs, organizer recaps, public abstracts, and material availability"
last_verified: "2026-10-31"
language: "en"
---

# October 2026 conference evidence refresh

[日本語](06-october-2026-refresh.ja.md)

## Scope and evidence rules

Checked **2026-10-31 (UTC)**. This is a bounded refresh, not a worldwide conference census or a claim that all linked recordings were watched. Earlier publications are included to fill gaps in the September snapshot; their discovery now does **not** make them October releases. Publication dates below are supplied by the source; unknown means not established.

**Program** describes planned content; **organizer recap** supports event completion, not every research claim; **public abstract** is an author's claim, not independent replication. A linked file is not the same as an inspected file. Retrieval failure is not proof that material is unpublished. Community indexes are discovery aids only. No private/member content was accessed.

## Existing conference follow-up

| Event and dates | Evidence / publication date | Availability checked 2026-10-31 |
|---|---|---|
| RSAC, March 23–26 | [Official post-event page](https://www.rsaconference.com/events/2026-usa); page publication date unknown | Held; recorded sessions are routed to RSAC Membership. This refresh does not claim to have watched those recordings. |
| Black Hat USA, August 1–6 | [Official completion release](https://blackhat.com/html/press/2026-08-11.html), August 11 | Held. [Briefings page](https://blackhat.com/us-26/briefings.html) describes speaker-supplied materials and restricted recording access. The [retrieved session listing](https://blackhat.com/us-26/briefings/schedule/) returned no sessions; individual research files were not verified. |
| DEF CON 34, August 6–9 | [AI Village organizer recap](https://aivillage.org/blog/defcon34-bruce-schneier-fireside-chat/), August 22 | Held. Organizer links one recorded fireside chat and an author-permission-based poster archive, not complete recordings of all village activity. |
| FIRST CTI, April 21–23 | [Official completion release](https://www.first.org/newsroom/releases/20260423), April 23; [program/material register](https://www.first.org/conference/firstcti26/program) | Held. Sigma workshop slides show last update April 24; scenario-planning slides May 19. These are file-update dates, not proven original publication dates. |
| FIRSTCON26, June 14–19 | [Official program/material register](https://www.first.org/conference/2026/program); page publication date unknown | Past event dates; public program links the Chaos Stack exercise template, last update June 9. Program/material evidence is not attendance verification for each session. |

The FIRST [Sigma slides](https://www.first.org/resources/papers/cti26/Detection-Engineering-with-Sigma.pdf) and [Chaos Stack template](https://www.first.org/resources/papers/firstcon26/FIRSTCON26-Chaos-Stack-Templates-John-Hollenberger.pdf) were linked by the official register but direct retrieval failed in this check. Their full contents are not summarized. Only public TLP:CLEAR entries were selected; no restricted session material was used.

### Evidence correction: Black Hat

The September note described compiler, GPU, and Unicode research as demonstrated results while citing a [June 2 announcement](https://blackhat.com/html/press/2026-06-02.html). That source announces intended presentations. The note now explicitly labels these as announcement claims. The August recap establishes that the event occurred, but does not validate each announced demonstration.

### A concrete additional DEF CON research lead

The AI Village organizer-hosted [SOC telemetry poster abstract](https://aivillage.org/posters/poisoning-the-soc-prompt-injection-via-ingested-telemetry/) describes testing whether attacker-controlled log fields can influence SOC agents after SIEM ingestion. The page links a poster; its publication date is unstated and this refresh reviewed the abstract, not the linked poster or an evaluation dataset. Do not infer a success rate or affected-product list. [The archive](https://aivillage.org/events/defcon-34/) also explicitly marks some posters unavailable online.

**Repository interpretation:** Treat collected telemetry as untrusted input even inside a trusted SIEM. Separate evidence extraction from tool authorization, preserve provenance, and test agent response boundaries using representative malicious log content. This is a validation backlog item, not evidence of attack prevalence.

## Expanded coverage: academic conferences and CCC

| Event | Event dates / status at check | Official material and publication evidence |
|---|---|---|
| USENIX Security 2026 | August 12–14; held | [Organizer](https://www.usenix.org/conference/usenixsecurity26) and [technical sessions](https://www.usenix.org/conference/usenixsecurity26/technical-sessions): open proceedings; selected paper dated August 2026, exact upload date unknown. |
| IEEE S&P 2026 | May 18–20; workshops May 21; dates elapsed | [Official site](https://sp2026.ieee-security.org/) and [agenda](https://sp2026.ieee-security.org/program.html): program evidence only here; opening-slides retrieval timed out and proceedings rendering was empty. Publication date unknown. |
| NDSS 2026 | February 23–27; held | [Official archive](https://www.ndss-symposium.org/ndss2026/) confirms completion. February 2026 proceedings; selected landing pages link papers, slides, and video. Exact upload dates unknown. |
| ACM CCS 2026 | November 15–19; **planned**, The Hague | [Official site](https://www.sigsac.org/ccs/CCS2026/): schedule announced September 27, after the prior check. This is not evidence of delivered talks or complete public proceedings. |
| CCC 40C3 | December 27–30; **planned**, Hamburg | [Official announcement](https://events.ccc.de/en/2026/09/12/40c3-model-citizens/), September 12. Announcement/CFP only; no talk outcomes inferred. |
| CCC 39C3 context | December 27–30, **2025**; held | [Official archive](https://events.ccc.de/en/category/39c3/) includes a January 13, 2026 follow-up. A 2026 follow-up does not change the event year. No talk reviewed here. |

### Selected research: facts versus implications

1. **USENIX — Download More RAM.** [Paper page](https://www.usenix.org/conference/usenixsecurity26/presentation/collins), [paper](https://www.usenix.org/system/files/usenixsecurity26-collins.pdf), August 2026. **Fact:** the authors describe a Windows VBS/HVCI attack assuming local administrator privileges and DIMMs lacking SPD write protection; disclosure reports a partial April 2026 mitigation. Paper reviewed, not video. **Analysis:** check hardware/configuration preconditions and vendor mitigation status; this does not establish fleet-wide vulnerability.
2. **NDSS — ACE.** [Paper and media index](https://www.ndss-symposium.org/ndss-paper/ace-a-security-architecture-for-llm-integrated-app-systems/), [paper](https://www.ndss-symposium.org/wp-content/uploads/2026-s352-paper.pdf), February 2026. **Fact:** separates abstract planning from app selection/execution, using information-flow checks and capability boundaries. Abstract/introduction reviewed; linked slides/video not reviewed. **Analysis:** a concrete reference for isolating untrusted tool descriptions/results from authority-bearing plans, not universal prompt-injection immunity.
3. **NDSS — One Email, Many Faces.** [Paper and media index](https://www.ndss-symposium.org/ndss-paper/one-email-many-faces-a-deep-dive-into-identity-confusion-in-email-aliases/), [paper](https://www.ndss-symposium.org/wp-content/uploads/2026-s148-paper.pdf), February 2026. **Fact:** studies email-alias identity mismatches across 28 providers and 18 platforms. Abstract/introduction reviewed; video not watched. **Analysis:** account linking and recovery need provider-aware identity semantics; this sample does not justify universal alias normalization.

## What changes, and what does not

The useful delta is stronger provenance, missing academic coverage, and a post-September CCS schedule announcement—not proof of a new worldwide attack trend. The five-plane model and annual-report consensus remain unchanged. This refresh neither modifies nor runs the source-monitor workflow.

Next evidence gates: actual CCS proceedings and completed-event records after November; 40C3 delivered material after December; recover individual Black Hat and FIRST files before treating their detailed claims as reviewed results. Availability checks are selective and do not replace the repository link-check CI.

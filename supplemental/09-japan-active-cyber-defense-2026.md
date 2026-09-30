---
publisher: "Repository synthesis of Japanese government primary sources"
edition: "2026-09-30 policy snapshot"
publication_date: "2026-09-30"
observation_period: "Sources verified through 2026-09-30"
dataset_or_scope: "Japanese active cyber defense legislation and implementation; not incident statistics"
geography: "Japan"
language: "en"
primary_source: "https://www.cao.go.jp/cybersecurity/"
last_verified: "2026-09-30"
---

# Japan active cyber defense: October 2026 commencement and operational implications

[日本語の詳細解説](09-japan-active-cyber-defense-2026.ja.md)

This English companion summarizes the Japanese research note. It is a dated policy and implementation supplement, not legal advice or additional incident-frequency evidence for the repository's annual-report consensus matrix. Statutory facts and repository analysis are distinguished below.

## Executive summary

**1 October 2026 is an important commencement date, but not the simultaneous start of every component of Japan's active cyber defense framework.** Cabinet Order No. 46 specifies that date for commencement under the main clause of the strengthening act's supplementary Article 1. Other provisions follow separate commencement arrangements. Public-private cooperation and police/Self-Defense Forces access and neutralization measures are the central October milestone; the new communications-information acquisition and handling regime belongs to a later stage. [Commencement order](https://www.cao.go.jp/cybersecurity/pdf/sekoukijitsu.pdf), [Prime Minister's Office, 31 July 2026](https://www.kantei.go.jp/jp/105/actions/202607/31security.html)

The government's 28 April 2026 parliamentary response also distinguishes the October milestone from preparations to commence communications-information use by autumn of the following year. This review did not establish a separately promulgated exact commencement date for the latter regime. A version date embedded in a legal-database URL is not treated as proof of that date. [House of Representatives proceedings](https://www.shugiin.go.jp/internet/itdb_kaigiroku.nsf/html/kaigiroku/000122120260428016.htm)

## Evidence profile

| Dimension | Scope |
|---|---|
| Verification date | 2026-09-30 |
| Jurisdiction | Japan |
| Evidence | Statutes, commencement order, government explanations, parliamentary proceedings and official consultation responses |
| Population | Legal institutions and covered operators; no incident dataset or comparable vendor denominator |
| Limitations | Some official pages were available only through indexed text; current reporting-order details were not fully retrievable |

## 1. Legal framework and timeline

The two central statutes, both promulgated on 23 May 2025, are Act No. 42 (重要電子計算機に対する不正な行為による被害の防止に関する法律) and related amendment Act No. 43. The former establishes reporting, information sharing and communications-information arrangements; the latter amends legislation including the Police Duties Execution Act and Self-Defense Forces Act. [Cabinet Office legislation index](https://www.cao.go.jp/cybersecurity/index.html)

| Date or stage | What it concerns | Important distinction |
|---|---|---|
| 1 July 2025 | Early commencement of general/basic-policy provisions | Preparations began before October 2026 |
| July 2025 | National Cybersecurity Office (NCO) established | Not a new organization created on 1 October 2026 |
| 1 April 2026 | Cyber Communications Information Oversight Commission establishment stage | Establishing an oversight body does not activate every regime it will oversee |
| **1 October 2026** | **Public-private cooperation, covered-operator notifications/reporting, access and neutralization measures** | **Do not describe this as commencement of all communications-information provisions** |
| Subsequent stage | Communications-information acquisition and handling | Supplementary Article 1 provides for a Cabinet-Order date within two years and six months of promulgation; exact date not established by this review |

Sources: [20 June 2025 ministerial briefing](https://www.digital.go.jp/speech/minister-250620-01), [NCO overview](https://www.cyber.go.jp/about/overview/index.html), [23 December 2025 ministerial briefing](https://www.digital.go.jp/speech/minister-251223-01), [Act No. 42 and supplementary provisions](https://www.shugiin.go.jp/internet/itdb_housei.nsf/html/housei/21720250523042.htm).

Separately, NCO describes 1 October 2026 commencement for cross-sector critical-infrastructure standards and associated guidelines. Those policy frameworks should not be substituted for the statutory definitions determining whether an operator or computer is covered by the new reporting duties. [NCO critical-infrastructure policy](https://www.cyber.go.jp/policy/group/infra/policy.html)

## 2. Covered businesses and reporting

### Established legal provisions

The relevant statutory category is **特別社会基盤事業者**, a defined subset of designated operators under the Economic Security Promotion Act that use specified important computers. This is not equivalent to all Japanese companies or every company serving critical infrastructure.

The framework includes notifications concerning covered computers and changes, reporting of specified compromising events or prescribed precursor events, corrective orders, and requests for reports or supporting material. See Articles 2(3) and 4–10. The fine of up to JPY 2 million in Article 83 relates to violating an Article 6 order; it should not be presented as an automatic uniform fine for every missed report. [Act No. 42](https://www.shugiin.go.jp/internet/itdb_housei.nsf/html/housei/21720250523042.htm)

**Existing covered assets have a six-month notification transition period, explained by the government as ending on 31 March 2027.** Government consultation response No. 81 states this explicitly. It is a transition for existing-asset notifications, not a general six-month exemption from incident reporting. [Official consultation responses](https://public-comment.e-gov.go.jp/pcm/download?seqNo=0000315045)

The framework also supports a public-private council, government analysis and vulnerability information, and requests to suppliers. Council participation, communications-information agreements and mandatory incident reporting are distinct mechanisms. [Government explanation, pp. 9–17](https://www.cao.go.jp/cybersecurity/pdf/setsumei.pdf)

### Repository analysis: operational preparation

- Confirm covered business activities and assets with legal counsel and the responsible ministry
- Assign decision ownership across CSIRT, SOC, infrastructure operations, suppliers and legal teams
- Separate incident recognition, reportability decisions, approval and submission responsibilities
- Check overlapping personal-data and sectoral reporting duties; a report under this framework does not automatically discharge other obligations
- Verify current reporting orders, forms and ministry guidance before production use

No universal 24-hour or 72-hour deadline is asserted here: the latest reporting-order text was not fully retrievable. [Current orders/forms](https://www.cao.go.jp/cybersecurity/index.html), [NCO legal Q&A](https://security-portal.cyber.go.jp/guidance/law-handbook/v2-03.html)

## 3. Access and neutralization

### Established legal provisions

Designated police officials may, subject to conditions including a risk of serious harm and urgent necessity, order relevant administrators to act or take measures themselves within the scope ordinarily necessary to prevent harm. This does not grant private companies a general right to hack back. [National Police Agency explanation](https://www.npa.go.jp/hakusyo/r07/honbun/html/bb3321000.html)

The amended Police Duties Execution Act generally requires prior approval by the oversight commission. An exceptional inability to wait for approval entails prompt subsequent notification and commission review, including recommendations where necessary. Measures against computers not reasonably believed to be located in Japan are restricted to National Police Agency officials and require prior consultation with the foreign minister.

The Self-Defense Forces' new communications-protection measures have additional conditions, including highly organized and planned conduct by overseas actors, risk of serious disruption, indispensability of their capabilities, and a request or consent from the National Public Safety Commission. They operate under a prime-ministerial order jointly with the police. [Related amendment Act No. 43, Articles 2 and 4](https://www.shugiin.go.jp/internet/itdb_housei.nsf/html/housei/21720250523043.htm)

### Repository analysis

Legal authority and safe operational capability require separate evaluation. Apparent attack infrastructure may be a compromised third-party service. Relevant evidence includes attribution accuracy, collateral service effects, overseas coordination and use of exceptional retrospective review. Commencement alone proves neither successful operations nor deterrence.

## 4. Communications information and safeguards

The later regime includes acquisition under agreements and approved acquisition of specified foreign-related communications. The categories and conditions differ for foreign-to-foreign traffic traversing Japan, inbound and outbound communications.

Acquisition is not identical to human analysis. The framework uses automated selection of attack-related machine information, without humans learning the unselected content, and immediate deletion of other information. Both “only metadata can ever be acquired” and “officials may freely read email contents” mischaracterize this design. [House of Representatives research](https://www.shugiin.go.jp/internet/itdb_rchome.nsf/html/rchome/shiryo/2025ron22-all.pdf/%24File/2025ron22-all.pdf)

The oversight commission independently examines and inspects relevant activities, including acquisition approvals, ongoing handling, responses to violations and access/neutralization review. [Commission website](https://www.aoc.go.jp/)

**Analysis:** This review found no basis for asserting a blanket new registration or device-configuration duty for ordinary individual users. Domestic users' communications with overseas services may nevertheless be relevant. Statutory safeguards should be evaluated separately from their demonstrated effectiveness: selection accuracy, deletion and retention, access logs, onward disclosure, inspection findings and reporting to the Diet remain important research questions. This note does not adjudicate constitutionality.

## 5. Architecture implications and follow-up evidence

The following are **repository recommendations, not asserted statutory technical controls**:

| Security plane | Practical preparation |
|---|---|
| Identity / control | Clear authority to assess reportability, approve disclosures and coordinate response |
| Data | Controlled handling of sensitive asset and incident information; minimum necessary disclosure |
| Telemetry | Traceable recognition, escalation and reporting decisions, with usable incident evidence |
| Recovery | Coordinate containment and service restoration with reporting and government interaction |

Track subsequent commencement orders, reporting guidance, council operations, commission findings, collateral-impact explanations and defensible evidence of faster detection or containment. This policy note does not change the repository's ATT&CK mappings or consensus matrix merely because a law has commenced.

## 6. Evidence limitations

- The [Livedoor article that prompted this review](https://news.livedoor.com/article/detail/32451445/) could not be retrieved. Its exact headline, time, speakers and claims were not verified or summarized as if read
- The October milestone was checked independently against official sources
- The 31 July Prime Minister's Office text was available through the search service's indexed official content, but direct retrieval returned 404; re-check against the statute and parliamentary record if the page remains inaccessible
- The absolute date meant by “tomorrow” in the original research context is **1 October 2026**
- Operational counts, staffing sufficiency, specific operations and error rates were not established
- No unverified current count of covered companies or sectors is supplied
- Current reporting-order details need further confirmation before individual deadlines, exceptions or asset classifications are used operationally
- Published enacted statutes contain provisions that may not yet be in force. Read them together with commencement and transitional provisions

For the complete claim-level primary-source index and Japanese legal terminology, see the [Japanese companion](09-japan-active-cyber-defense-2026.ja.md).

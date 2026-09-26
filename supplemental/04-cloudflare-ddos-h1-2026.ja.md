---
publisher: "Cloudflare / Cloudforce One"
edition: "DDoS Threat Report H1 2026"
publication_date: "2026-08-12"
observation_period: "2026-01-01 to 2026-06-30"
language: "ja"
translation_of: "04-cloudflare-ddos-h1-2026.md"
primary_source: "https://blog.cloudflare.com/ja-jp/ddos-threat-report-2026-h1/"
last_verified: "2026-09-27"
---

# Cloudflare DDoS Threat Report H1 2026 — 日本語解説

[English](04-cloudflare-ddos-h1-2026.md)

## 追加する価値

Cloudflare Annual ReportがStrategic Viewなのに対し、こちらは**2026年上半期のAvailability Attackの実データ**です。

## 主要データ

Cloudflareは2026年上半期に、**1 Tbpsを超えるNetwork-layer DDoSを935件**Mitigateしました。Q1→Q2では、この規模のAttackが**519%増加**しています。

DNS FloodやGeopolitical Tensionも主要論点です。

## Architecture上の意味

DDoS Defenseは次を前提にします。

- 秒単位のRamp-up
- On-prem Link Capacityを超えるBotnet
- L3/L4とL7の同時圧力
- Event/GeopoliticsでTargetingが変化
- DNS Dependency

したがってLocal ApplianceだけでなくUpstream/Anycast Mitigationが基本になります。

## 優先アクション

- Upstream / Anycast Scrubbing
- Authoritative DNSの冗長化・Failover Test
- L3/L4とL7を別々に可視化
- Rate Limit / Degraded Modeを事前定義
- 大型Event時のReadiness Level
- Peak Load込みのDDoS Exercise

## Primary Sources

- https://blog.cloudflare.com/ja-jp/ddos-threat-report-2026-h1/
- https://blog.cloudflare.com/ddos-threat-report-2026-h1/

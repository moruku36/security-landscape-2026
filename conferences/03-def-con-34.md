# DEF CON 34

Sources:
- Official date announcement: https://forum.defcon.org/node/253965
- AI Village: https://aivillage.org/events/defcon-34/
- Cloud Village: https://www.cloud-village.org/dc34
- Recon Village: https://reconvillage.org/reconvillage-2026-defcon-34/talks
- Community program index: https://defcon.outel.org/dcwp/dc34/activities/dctalkslist/

Las Vegas Convention Center, 2026-08-06〜09.

## Positioning

Black Hatよりcommunity / hacker / hands-on寄り。製品戦略よりも、実際に何を壊せるか、既存技術のassumptionがどこで破れるかを見るのに向く。

## 2026 signals

### AI infrastructure becomes a target

AI Villageでは12 stage sessions、34 poster presentations、6 fireside chats、2 competitionsを実施。HalCTFでは、人間がtargetを直接操作せず、autonomous agent自身にsandbox targetを攻略させる形式が採用された。

Recon Villageでは、exposed inference endpointやleaked AI API keyを悪用し、他者のinference resourceを攻撃活動に転用する研究が紹介された。

### Cloud is still a hacking surface

Cloud Villageではoffensive/defensive cloud securityを中心にtalk/workshop/CTFを展開。2026年の年次レポート群が指摘するcloud-conscious intrusionときれいにつながる。

### OT / ICS and edge remain important

ICS VillageではOT protocol exploitation、threat hunting、AI-driven attack tooling、electric-sector incidentなどが扱われた。

### Trusted technology can be weaponized

DEF CONの技術研究では、AI runtime、WMI、EDR、AD/Kerberos、WAF、IoT cloudなど「防御側が当然信頼している仕組み」そのものを攻撃面として捉える流れが強い。

## Interpretation

DEF CONからEnterprise側が持ち帰るべきなのは「そのexploitを明日使われるか」ではなく、**trust assumptionを定期的にred-teamする文化**。

特に2026年はAI Agent / Local AI Runtime / Cloud / Identity / EDR bypassの境界が重なってきた。

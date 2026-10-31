---
edition: "2026-10-31 conference evidence refresh"
observation_period: "2026-09-26版の追補。以前の未収録資料も対象"
evidence_type: "公式プログラム・主催者報告・公開要旨・資料公開状況"
last_verified: "2026-10-31"
language: "ja"
---

# 2026年10月：カンファレンス資料の確認と対象拡張

[English](06-october-2026-refresh.md)

## 範囲と証拠の区分

確認日：**2026-10-31（UTC）**。限定した対象の追補であり、世界の全会議の網羅や全動画の視聴を意味しない。9月版の不足を補うため以前の資料も含む。今回発見した資料を「10月公開」と読み替えない。公開日不明は未確認を意味する。

プログラムは予定、主催者の開催後報告は開催の証拠、公開要旨は著者の主張であり、個別研究の独立検証とは異なる。リンクの存在とファイル本文の確認も区別する。取得失敗は未公開の証明ではない。コミュニティ索引は探索用に限定し、会員限定・非公開資料にはアクセスしていない。

## 既存対象の追補

| 会議・開催日 | 証拠・公開日 | 2026-10-31の確認結果 |
|---|---|---|
| RSAC：3月23–26日 | [公式開催後ページ](https://www.rsaconference.com/events/2026-usa)。ページ公開日不明 | 開催済み。録画はMembershipへ誘導される。今回、録画内容は視聴していない。 |
| Black Hat USA：8月1–6日 | [公式終了報告](https://blackhat.com/html/press/2026-08-11.html)：8月11日 | 開催済み。[Briefings案内](https://blackhat.com/us-26/briefings.html)は登壇者提供資料とアクセス制限のある録画を区別。[セッション一覧](https://blackhat.com/us-26/briefings/schedule/)は取得結果にセッションがなく、個別研究資料は未検証。 |
| DEF CON 34：8月6–9日 | [AI Village主催者報告](https://aivillage.org/blog/defcon34-bruce-schneier-fireside-chat/)：8月22日 | 開催済み。録画できたfireside chat 1件と、著者の許諾を得たポスターの公開を案内。全活動の録画公開ではない。 |
| FIRST CTI：4月21–23日 | [公式終了報告](https://www.first.org/newsroom/releases/20260423)：4月23日。[プログラム・資料一覧](https://www.first.org/conference/firstcti26/program) | 開催済み。Sigma資料の最終更新は4月24日、シナリオプランニング資料は5月19日。初公開日とは断定しない。 |
| FIRSTCON26：6月14–19日 | [公式プログラム・資料一覧](https://www.first.org/conference/2026/program)。ページ公開日不明 | 日程は経過。Chaos Stack演習テンプレートの最終更新は6月9日。プログラムと資料だけで各セッションの実施を証明しない。 |

FIRSTの[Sigma資料](https://www.first.org/resources/papers/cti26/Detection-Engineering-with-Sigma.pdf)と[Chaos Stackテンプレート](https://www.first.org/resources/papers/firstcon26/FIRSTCON26-Chaos-Stack-Templates-John-Hollenberger.pdf)は公式一覧にリンクがあるが、直接取得に失敗したため本文を要約していない。選んだのは公開TLP:CLEAR項目のみであり、制限付き資料は使用していない。

### Black Hatの証拠区分を訂正

9月版は[6月2日の告知](https://blackhat.com/html/press/2026-06-02.html)を根拠に、コンパイラ・GPU・Unicode研究を実証済みの結果のように説明していた。この出典は発表予定の告知であるため、元ノートを「告知の主張」と明示する形に修正した。8月の終了報告は開催を裏付けるが、予定された個々の実演結果まで検証するものではない。

### DEF CONで追加した具体的な研究候補

AI Villageが掲載する[SOCテレメトリのポスター要旨](https://aivillage.org/posters/poisoning-the-soc-prompt-injection-via-ingested-telemetry/)は、攻撃者が制御するログ項目がSIEM取り込み後にSOCエージェントへ影響するかを評価する研究を説明する。公開日は不明。今回は要旨を確認し、リンク先ポスターや評価データは未検証。成功率や影響製品の一覧を推測しない。[主催者アーカイブ](https://aivillage.org/events/defcon-34/)にはオンライン非公開と明記されたポスターもある。

**リポジトリ側の解釈：** 信頼するSIEM内でも収集ログを非信頼入力として扱う。証拠抽出とツール実行権限を分離し、来歴を保持し、悪意あるログを用いてエージェントの応答境界を検証する。これは検証課題であって、被害の普及率の根拠ではない。

## 学術会議・CCCへ対象を拡張

| 会議 | 確認日時点の日程・状態 | 公式資料・公開日の根拠 |
|---|---|---|
| USENIX Security 2026 | 8月12–14日、開催済み | [主催者](https://www.usenix.org/conference/usenixsecurity26)・[技術セッション](https://www.usenix.org/conference/usenixsecurity26/technical-sessions)：公開論文集。選定論文は2026年8月刊、アップロード日は不明。 |
| IEEE S&P 2026 | 5月18–20日、workshopは21日。日程経過 | [公式サイト](https://sp2026.ieee-security.org/)・[議事日程](https://sp2026.ieee-security.org/program.html)。今回はプログラムの確認に限定。opening slidesはタイムアウト、論文集は空の表示となり、内容未検証。公開日不明。 |
| NDSS 2026 | 2月23–27日、開催済み | [公式アーカイブ](https://www.ndss-symposium.org/ndss2026/)で開催を確認。2026年2月の論文集。選定論文のページには論文・スライド・動画のリンクがある。アップロード日は不明。 |
| ACM CCS 2026 | 11月15–19日、ハーグ、**開催予定** | [公式サイト](https://www.sigsac.org/ccs/CCS2026/)が9月27日に日程公開を告知。前回確認後の更新だが、発表実施や論文集全体の公開を示す証拠ではない。 |
| CCC 40C3 | 12月27–30日、ハンブルク、**開催予定** | [公式告知](https://events.ccc.de/en/2026/09/12/40c3-model-citizens/)は9月12日公開。告知・CFPを根拠に発表成果を推測しない。 |
| CCC 39C3（文脈） | **2025年**12月27–30日、開催済み | [公式アーカイブ](https://events.ccc.de/en/category/39c3/)には2026年1月13日の追補がある。追補年を会議開催年に置き換えない。個別講演は未確認。 |

### 選定研究：事実と解釈

1. **USENIX — Download More RAM：** [論文ページ](https://www.usenix.org/conference/usenixsecurity26/presentation/collins)、[論文](https://www.usenix.org/system/files/usenixsecurity26-collins.pdf)、2026年8月。**事実：** Windows VBS/HVCIへの攻撃はローカル管理者権限とSPD書き込み保護のないDIMMを前提とする。開示欄には2026年4月の部分的緩和策が記載される。論文を確認し、動画は未視聴。**解釈：** 構成上の前提とベンダー対策を個別評価する。全端末が脆弱とは主張しない。
2. **NDSS — ACE：** [論文・資料一覧](https://www.ndss-symposium.org/ndss-paper/ace-a-security-architecture-for-llm-integrated-app-systems/)、[論文](https://www.ndss-symposium.org/wp-content/uploads/2026-s352-paper.pdf)、2026年2月。**事実：** 抽象的計画とアプリ選択・実行を分け、情報フロー検査とcapability境界を使う。要旨・導入を確認し、リンク先スライド・動画は未確認。**解釈：** 非信頼のツール説明・結果から権限を伴う計画を隔離する設計参考であり、万能なprompt injection耐性ではない。
3. **NDSS — One Email, Many Faces：** [論文・資料一覧](https://www.ndss-symposium.org/ndss-paper/one-email-many-faces-a-deep-dive-into-identity-confusion-in-email-aliases/)、[論文](https://www.ndss-symposium.org/wp-content/uploads/2026-s148-paper.pdf)、2026年2月。**事実：** 28のメールプロバイダーと18のプラットフォームを対象にエイリアスの識別不整合を調べる。要旨・導入を確認、動画は未視聴。**解釈：** アカウント連携・復旧は提供者ごとの識別規則を考慮する。この標本から普遍的なエイリアス正規化を推奨しない。

## 変更した点・維持した点

今回の差分は出典精度、未収録の学術研究、前回確認後のCCS日程告知である。世界的な攻撃傾向の変化を示すものではない。5-planeモデルと年次レポートのConsensusは維持し、source-monitorの変更・実行は行わない。

次の確認対象は11月のCCS論文集・開催後記録、12月の40C3公開成果、Black HatとFIRSTの個別資料取得である。資料本文を確認するまでは詳細な実証結果として扱わない。今回の限定的な公開状況確認はリポジトリ全体のlink-check CIを代替しない。

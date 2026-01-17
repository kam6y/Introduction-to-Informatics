<!-- .slide: class="layout-section" -->
## Intro / Goals
<p class="subtitle">到達点・評価軸・90枚のロードマップ</p>

---

<!-- .slide: class="layout-section" -->
## Foundations
<p class="subtitle">要件定義・設計・テストの種類</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Foundationsの学習目標</h2>
  <ul>
    <li>Vモデルで開発工程の全体像を説明できる</li>
    <li>品質・納期・コストのトレードオフを意識する</li>
    <li>要件→設計→テストの対応関係を説明できる</li>
  </ul>
</div>

---

<!-- .slide: class="layout-full-bleed dev-flow-slide" data-background-color="#f4f5f7" -->
<div class="overlay overlay-solid">
  <h2>開発の流れ（Vモデル）</h2>
  <p class="subtle">定義・設計とテストの対応関係</p>
  <ul class="subtle">
    <li><strong>要件定義</strong> : 2割、<strong>開発（設計＋実装）</strong> : 6.5割、<strong>テスト</strong> : 1.5割  ←割合はIPAより</li>
  </ul>
</div>
<img class="dev-flow-image" src="assets/dev-flow.svg" alt="開発の流れ（Vモデル）の全体像" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>要件定義で合意を作る</h2>
  <ul>
    <li>目的とスコープ（作る/作らない）</li>
    <li>成果物・評価基準（受入条件）</li>
    <li>ステークホルダーと決裁者を明確化</li>
  </ul>
</div>
<div class="callout">
  <p><strong>成果物例</strong></p>
  <ul>
    <li>目的・課題の整理</li>
    <li>主要ユースケース</li>
    <li>制約・前提条件</li>
    <li>機能要件・非機能要件</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>機能要件をユーザー行動で書く</h2>
  <ul>
    <li>ユースケース/ユーザーストーリーで整理</li>
    <li>入力・出力・例外を明確化</li>
    <li>受入条件をテスト可能にする</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>「利用者は予約を変更できる」</p>
  <p class="subtle">期限・通知・制約を追記</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>非機能要件は数値で固定する</h2>
  <ul>
    <li>性能: 応答時間・同時接続</li>
    <li>可用性: 可用性SLO(稼働率) / RTO(目標復旧時間) / RPO(目標復旧時点)</li>
    <li>セキュリティ・法規制・運用要件</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>主要画面の応答目標: 3秒</p>
  <p>SLO: 99.9%</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>粒度を合わせて手戻りを減らす</h2>
  <ul>
    <li>MVPとフェーズ分割で優先度を決める</li>
    <li>ワイヤー/プロトタイプで認識合わせ</li>
    <li>変更は影響範囲とコストを可視化</li>
  </ul>
</div>
<div class="callout">
  <p><strong>合意の道具</strong></p>
  <ul>
    <li>ワイヤーフレーム</li>
    <li>プロトタイプ</li>
    <li>優先度表</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>外部設計と内部設計を分ける</h2>
  <ul>
    <li>外部設計: 画面 / API / 入出力</li>
    <li>内部設計: データ / ロジック / 構成</li>
    <li>要件↔設計のトレーサビリティを維持</li>
  </ul>
</div>
<div class="callout">
  <p><strong>成果物例</strong></p>
  <ul>
    <li>画面遷移図・API仕様</li>
    <li>ER図・シーケンス図</li>
    <li>構成図・運用設計</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-3col corner-image" -->
<h2>設計の意思決定を残す</h2>
<div>
  <h3>構成</h3>
  <ul>
    <li>モノリス: 速く作れるが、変更影響が大きい</li>
    <li>マイクロサービス: 独立性が高いが、運用コスト増</li>
  </ul>
</div>
<div>
  <h3>Build vs Buy</h3>
  <ul>
    <li>自社開発: 柔軟に改善できるが、時間/保守負担</li>
    <li>SaaS: 立ち上げが速いが制約/コストがかかる</li>
  </ul>
</div>
<div>
  <h3>品質軸</h3>
  <ul>
    <li>性能重視? コスト重視?</li>
    <li>非機能がどれだけ重視されるかによる</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>テストの種類と対応関係</h2>
  <ul>
    <li>単体テスト: 関数/モジュール</li>
    <li>結合テスト: 境界/連携</li>
    <li>システムテスト: 外部仕様</li>
    <li>受入テスト: 要件/受入条件</li>
  </ul>
</div>
<div class="callout">
  <p><strong>対応関係</strong></p>
  <ul>
    <li>要件 → 受入テスト</li>
    <li>外部設計 → システムテスト</li>
    <li>内部設計 → 結合テスト</li>
    <li>実装 → 単体テスト</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>テスト計画は観点から作る</h2>
  <ul>
    <li>正常/異常/境界の観点で網羅</li>
    <li>テストデータと環境を先に準備</li>
    <li>自動化は「変更頻度×影響度」から</li>
  </ul>
</div>
<div class="callout">
  <p><strong>テスト実装の優先度の式</strong></p>
  <p class="subtle">変更頻度 × 影響度</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col corner-image" -->
<div>
  <h2>ミニケース：予約アプリ</h2>
  <ul>
    <li>要件: 変更/キャンセル/通知/在庫反映</li>
    <li>設計: 予約API + 通知キュー + 在庫ロック</li>
    <li>テスト: 期限/通知遅延/二重予約/同時操作</li>
  </ul>
</div>
<div class="callout">
  <p><strong>受入条件（例）</strong></p>
  <ul>
    <li>変更は前日23:59まで</li>
    <li>キャンセル後は在庫が即時復活</li>
  </ul>
  <p class="subtle">通知は30秒以内に送信</p>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Foundations自己チェック</h2>
  <ul>
    <li>Vモデルの対応関係を図で説明できる</li>
    <li>要件定義の成果物を3つ言える</li>
    <li>非機能要件を数値で書ける（SLO/RTO/RPO）</li>
    <li>テスト観点（正常/異常/境界）を挙げられる</li>
    <li>ミニケースの受入条件を2つ作れる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Git / GitHubに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Git / GitHub
<p class="subtitle">ブランチ/PR/レビューと履歴の読み方</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Git / GitHubの学習目標</h2>
  <ul>
    <li>GitとGitHubの役割の違いを説明できる</li>
    <li>ローカル/リモートの関係と同期の流れを説明できる</li>
    <li>pull→add→commit→pushの最小フローを使える</li>
    <li>ブランチ/PR/レビューの目的を言語化できる</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>共有フォルダの課題を解決する</h2>
  <ul>
    <li>最新版が分からない/上書きが起きる</li>
    <li>差分が追えず品質が落ちる</li>
  </ul>
  <p>だからGitで履歴を追い、GitHubで共有する</p>
</div>
<div class="callout">
  <p><strong>現場の困りごと</strong></p>
  <ul>
    <li>誰がいつ修正したか分からない</li>
    <li>ロールバックの手段がない</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>メリット① 効率と品質が上がる</h2>
  <ul>
    <li><strong>Git</strong> : 最新版と履歴が追える</li>
    <li><strong>Git</strong> : 上書きトラブルを減らす</li>
    <li><strong>GitHub</strong> : 共同開発機能が豊富</li>
  </ul>
</div>
<div class="callout">
  <p><strong>効果</strong></p>
  <ul>
    <li>属人化が減る</li>
    <li>レビューし合うことで品質が上がる</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>GitHubのメリット② 無料でプライベート</h2>
  <ul>
    <li><strong>GitHub</strong> : 無料で基本機能が使える</li>
    <li><strong>GitHub</strong> : プライベートリポジトリも無料</li>
    <li><strong>GitHub</strong> : 学習/小規模チームでも始めやすい</li>
  </ul>
</div>
<div class="callout">
  <p><strong>使い分け</strong></p>
  <ul>
    <li>学習用は公開でOK</li>
    <li>業務は非公開で運用</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>GitとGitHubの違い</h2>
  <ul>
    <li><strong>Git</strong> : 変更履歴を管理する仕組み</li>
    <li><strong>GitHub</strong> : Gitのリポジトリを共有するサービス</li>
    <li>履歴とレビューでコードの変遷を追跡し、チーム開発を支える</li>
  </ul>
</div>
<div class="callout">
  <p><strong>押さえる視点</strong></p>
  <ul>
    <li>Gitはローカルでも完結できる</li>
    <li>GitHubは共同作業を加速させる</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>リポジトリの基本</h2>
  <ul>
    <li>コードと履歴を保存する場所</li>
    <li><strong>ローカル</strong>と<strong>リモート</strong>を分けて持つ</li>
    <li>同期して履歴を揃える</li>
  </ul>
</div>
<div class="diagram" data-diagram="repo-map" aria-label="ローカルとリモートの関係図"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>コミットとプッシュの意味</h2>
  <ul>
    <li>コミット = 変更点を履歴として固定</li>
    <li>プッシュ = ローカル履歴をリモートに送る</li>
    <li>小さく頻繁に残すと追跡しやすい</li>
  </ul>
</div>
<div class="callout">
  <p><strong>コツ</strong></p>
  <ul>
    <li>「理由」が分かるメッセージを付ける</li>
    <li>変更の単位を揃える</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Gitの最小フローを覚える</h2>
  <ul>
    <li>1作業 = 1コミットが目安</li>
    <li><strong>作業前</strong>にpull、<strong>作業後</strong>にadd→commit→push</li>
    <li>PRでレビュー→マージ</li>
  </ul>
</div>
<div class="diagram" data-diagram="git-flow" aria-label="Gitの最小フロー"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ブランチで並行作業する</h2>
  <ul>
    <li>目的ごとに作業の枝を分ける</li>
    <li>mainは安定、featureは試行</li>
    <li>まとまったらPR→マージ</li>
  </ul>
</div>
<div class="diagram" data-diagram="branch-merge" aria-label="ブランチとマージの流れ"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>プルリクエストで提案する</h2>
  <ul>
    <li>変更内容をレビューへ届ける</li>
    <li>議論・修正・合意の場になる</li>
    <li>「誰が何を変えたか」が残る</li>
  </ul>
</div>
<div class="callout">
  <p><strong>チェック観点</strong></p>
  <ul>
    <li>仕様に合っているか</li>
    <li>読みやすいか/壊していないか</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>マージで取り込む</h2>
  <ul>
    <li>レビュー後に変更を取り込む</li>
    <li>競合があれば解消してから統合</li>
    <li>履歴は一本に集約される</li>
  </ul>
</div>
<div class="callout">
  <p><strong>実務の習慣</strong></p>
  <ul>
    <li>マージ前に最新を取り込む</li>
    <li>小さく頻繁にPRを出す</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>コンフリクトの基本対応</h2>
  <ul>
    <li>同じ行を別々に変更すると競合</li>
    <li><strong>pull/merge/rebase/PR取り込み</strong>時に発覚→差分を確認</li>
    <li>片方を残して修正→再commit</li>
  </ul>
</div>
<div class="diagram" data-diagram="git-conflict" aria-label="コンフリクト解決の流れ"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>スタッシュで一時退避</h2>
  <ul>
    <li>作業中の変更を一時退避</li>
    <li>pull/切り替えの前に整理</li>
    <li><strong>apply</strong> = 取り出すがスタッシュは残る</li>
    <li><strong>pop</strong> = 取り出してスタッシュを削除</li>
    <li>再利用ならapply、1回きりならpop</li>
  </ul>
</div>
<div class="diagram" data-diagram="git-stash" aria-label="スタッシュの流れ"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>リバートで取り消す</h2>
  <ul>
    <li>変更を打ち消す「新しいコミット」</li>
    <li>履歴を消さずに戻せる</li>
    <li>共有ブランチで安全に使える</li>
  </ul>
</div>
<div class="diagram" data-diagram="git-revert" aria-label="リバートの考え方"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Git / GitHub自己チェック</h2>
  <ul>
    <li>GitとGitHubの違いを一言で説明できる</li>
    <li>pull/add/commit/pushの順番を図で言える</li>
    <li>ブランチとPRが必要な理由を説明できる</li>
    <li>コンフリクト時の基本手順を言える</li>
    <li>リバートとスタッシュの使い分けを説明できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Networking Basicsに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Networking Basics
<p class="subtitle">TCP/IP・DNS・HTTP/HTTPS・ポートと通信の基礎</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Networking Basicsの学習目標</h2>
  <ul>
    <li>TCP/IPの4層を列挙できる</li>
    <li>IPアドレスとポートの役割を説明できる</li>
    <li>DNSの名前解決の流れを説明できる</li>
    <li>HTTP/HTTPSの違いを言語化できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>今日のキーワード</strong></p>
  <ul>
    <li>層で分ける</li>
    <li>宛先を特定する</li>
    <li>安全に届ける</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>通信の課題を解決する</h2>
  <ul>
    <li>異なる機器・ソフト間でどう繋がるか</li>
    <li>宛先をどう特定するか</li>
    <li>安全にデータを届けるには</li>
  </ul>
</div>
<div class="callout">
  <p><strong>答え</strong></p>
  <p>標準化されたプロトコルで解決</p>
  <p class="subtle">共通ルールが相互接続性を生む</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>TCP/IPで通信を階層化する</h2>
  <ul>
    <li>4層モデル（アプリ/トランスポート/インターネット/リンク）</li>
    <li>役割を分けて責務を明確にする</li>
    <li>例: HTTPはアプリ層、TCPはトランスポート層</li>
  </ul>
</div>
<div class="diagram" data-diagram="tcpip-layers" aria-label="TCP/IPの4層モデル"></div>


---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>IPアドレスで宛先を決める（インターネット層）</h2>
  <ul>
    <li>IPv4 / IPv6の形式を知る</li>
    <li>グローバルIPはインターネットで到達可能</li>
    <li>プライベートIPは社内/家庭の内部用</li>
    <li>NATが内部IPをグローバルIPに変換</li>
  </ul>
</div>
<div class="callout">
  <p><strong>見分けるコツ</strong></p>
  <ul>
    <li>10.x.x.x / 172.16-31.x.x / 192.168.x.x はプライベート</li>
    <li>それ以外は基本的にグローバル</li>
  </ul>
  <p class="subtle">NAT = 1つのグローバルIPを内部で共有</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>TCP/UDPを使い分ける（トランスポート層）</h2>
  <ul>
    <li>TCP: 接続してから送る、順序と再送で信頼性を担保</li>
    <li>UDP: 接続不要で軽量、多少の欠損は許容</li>
    <li>正確さ重視か、速さ重視かで選ぶ</li>
  </ul>
</div>
<div class="callout">
  <p><strong>よくある例</strong></p>
  <ul>
    <li>TCP: HTTPS / SSH / メール</li>
    <li>UDP: DNS / 音声・動画のリアルタイム配信</li>
  </ul>
  <p class="subtle">同じポート番号でもTCPとUDPは別扱い</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ポートでアプリを区別する（トランスポート層）</h2>
  <ul>
    <li>1台に複数サービスが動く</li>
    <li>ポート番号（80/443/22など）でアプリを分ける</li>
    <li>IPアドレス=住所、ポート=部屋番号</li>
  </ul>
</div>
<div class="callout">
  <p><strong>よく使うポート</strong></p>
  <ul>
    <li>80: HTTP</li>
    <li>443: HTTPS</li>
    <li>8000: 開発用サーバー</li>
    <li>22: SSH</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>DNSで名前を解決する（アプリ層）</h2>
  <ul>
    <li>ドメイン名 → IPアドレスに変換する仕組み</li>
    <li>「住所はどこ?」をDNSが代わりに調べる</li>
    <li>一度調べた結果はキャッシュで早く返す</li>
  </ul>
</div>
<div class="diagram">
  <img
    src="assets/dns-2-2048x1102.png"
    alt="DNSの名前解決フロー"
    style="width: 100%; height: 100%; object-fit: contain;"
  />
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>HTTPでWebを取得する（アプリ層）</h2>
  <ul>
    <li>リクエスト（GET/POST）とレスポンス</li>
    <li>ステータスコードで結果を伝える</li>
    <li>ヘッダーとボディで情報を分離</li>
  </ul>
</div>
<div class="callout">
  <p><strong>代表的なコード</strong></p>
  <ul>
    <li>200: OK</li>
    <li>404: Not Found</li>
    <li>500: Server Error</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>HTTPSで通信を守る（アプリ層）</h2>
  <ul>
    <li>TLSで暗号化・改ざん検知</li>
    <li>証明書で相手を確認する</li>
    <li>HTTPだけでは盗聴・改ざんリスク</li>
  </ul>
</div>
<div class="callout">
  <p><strong>TLSが守る3つ</strong></p>
  <ul>
    <li>機密性（暗号化）</li>
    <li>完全性（改ざん検知）</li>
    <li>認証（なりすまし防止）</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ミニケース：Webページ表示の流れ</h2>
  <ul>
    <li>ブラウザ → DNS → TCP接続 → HTTPリクエスト → 表示</li>
    <li>各層が連携して1つの体験を作る</li>
    <li>開発者ツールで流れを確認できる</li>
  </ul>
</div>
<div class="diagram" data-diagram="web-flow" aria-label="Webページ表示の流れ"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Networking Basics自己チェック</h2>
  <ul>
    <li>TCP/IPの4層を列挙できる</li>
    <li>IPアドレスとポートの違いを説明できる</li>
    <li>DNSの役割を一言で言える</li>
    <li>HTTP/HTTPSの違いを説明できる</li>
    <li>Webページ表示の流れを追える</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Web Apps &amp; Cloudに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Web Apps & Cloud
<p class="subtitle">HTTP/API・3層構成・クラウド責務分界</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Web Apps &amp; Cloudの学習目標</h2>
  <ul>
    <li>3層構成（プレゼンテーション/アプリケーション/データ）を説明できる</li>
    <li>REST APIの基本（HTTPメソッド・エンドポイント）を理解できる</li>
    <li>クラウドの責任共有モデル（IaaS/PaaS/SaaS）を区別できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>キーワード</strong></p>
  <ul>
    <li>3層構成</li>
    <li>API設計</li>
    <li>クラウド運用</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Webアプリ開発の課題を整理する</h2>
  <ul>
    <li>ユーザーにどう画面を届けるか</li>
    <li>ビジネスロジックをどこで処理するか</li>
    <li>データをどう永続化・保護するか</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p>責務を分けることでスケール・保守性が上がる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>クライアント/サーバーモデル</h2>
  <ul>
    <li>ブラウザ（クライアント）がリクエストを送る</li>
    <li>サーバーが処理してレスポンスを返す</li>
    <li>役割を分けることで並行開発が可能に</li>
  </ul>
</div>
<div class="diagram" data-diagram="client-server" aria-label="クライアントとサーバーの関係図"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>3層構成で責務を分ける</h2>
  <ul>
    <li>プレゼンテーション層（UI/UX）</li>
    <li>アプリケーション層（ビジネスロジック）</li>
    <li>データ層（永続化・DB）</li>
  </ul>
</div>
<div class="diagram" data-diagram="three-tier" aria-label="3層アーキテクチャ図"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>フロントエンドの役割</h2>
  <ul>
    <li>ユーザーが触れる部分を担当</li>
    <li>HTML/CSS/JavaScriptで構築</li>
    <li>状態管理・バリデーション・表示最適化</li>
  </ul>
</div>
<div class="callout">
  <p><strong>代表的技術</strong></p>
  <p>React / Vue / Next.js</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>バックエンドの役割</h2>
  <ul>
    <li>ビジネスロジックを実行</li>
    <li>DBアクセス・外部API連携</li>
    <li>認証・認可のゲートキーパー</li>
  </ul>
</div>
<div class="callout">
  <p><strong>代表的技術</strong></p>
  <p>Node.js / Python / Go / Java</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>APIでフロントとバックを繋ぐ</h2>
  <ul>
    <li>API = アプリケーション間の「契約」</li>
    <li>フロントエンドがバックエンドを呼び出す窓口</li>
    <li>疎結合で独立した開発・デプロイが可能</li>
  </ul>
</div>
<div class="diagram" data-diagram="api-flow" aria-label="フロントとバックの接続図"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>REST APIの基本</h2>
  <ul>
    <li>HTTPメソッドで操作を表現（GET/POST/PUT/DELETE）</li>
    <li>エンドポイント = リソースのURL</li>
    <li>JSONでデータをやりとり</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <ul>
    <li>GET /users/123 → ユーザー取得</li>
    <li>POST /users → 新規作成</li>
    <li>PUT /users/123 → ユーザー更新</li>
    <li>DELETE /users/123 → ユーザー削除</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>REST APIとHTTP APIの違い</h2>
  <ul>
    <li>HTTP API: HTTPを使うAPI全般（設計は自由）</li>
    <li>REST API: RESTの原則に従ったAPI（リソース指向・ステートレス）</li>
    <li>同じHTTPでもURL設計の思想が違う</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>REST: /users/123 に GET/PUT/DELETE を割り当てる</p>
  <p>HTTP API: /getUser /updateUser などアクション名で呼ぶ</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ステートレスとセッション管理</h2>
  <ul>
    <li>サーバーは「状態を持たない」が原則</li>
    <li>リクエストごとに認証情報を送る</li>
    <li>JWT（トークン）やCookieで認証を継続</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p>ステートレス → スケールしやすい</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>オンプレミスからクラウドへ</h2>
  <ul>
    <li>オンプレミス: 自社で全て管理（HW/OS/ミドルウェア/アプリ）</li>
    <li>クラウド: 必要な部分だけ借りる</li>
    <li>初期投資を抑え、スケールが容易に</li>
  </ul>
</div>
<div class="callout">
  <p><strong>現場の変化</strong></p>
  <p>所有 → 利用へ</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>クラウドの責任共有モデル</h2>
  <ul>
    <li>IaaS: インフラだけ借りる（OS以上は自己管理）</li>
    <li>PaaS: ランタイムまで提供（アプリに集中）</li>
    <li>SaaS: 全て提供（設定だけで利用）</li>
  </ul>
</div>
<div class="diagram">
  <img
    src="assets/SaaS_dictionary01_@CON.png"
    alt="IaaS/PaaS/SaaSの責任共有モデル"
    style="width: 100%; height: 100%; object-fit: contain;"
  />
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>マネージドサービスで運用負荷を下げる</h2>
  <ul>
    <li>DBやキュー、ストレージをクラウドに任せる</li>
    <li>パッチ適用・スケール・バックアップが自動</li>
    <li>開発者はアプリ開発に集中できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>RDS / Cloud SQL / S3 / Cloud Storage</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ミニケース：ECサイトの構成例</h2>
  <ul>
    <li>フロント: Next.js（Vercel / AWS Amplify）</li>
    <li>API: Node.js（Cloud Run / App Runner / AWS Lambda + API Gateway）</li>
    <li>DB: PostgreSQL（Cloud SQL / RDS / Aurora）</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p>責任分界を意識して選定する</p>
</div>

---

<div class="layout-2col layout-2col-wide">
  <div>
    <h2>実際のECサイト例</h2>
    <ul>
      <li>CloudFrontで静的配信を高速化</li>
      <li>Application Load Balancerが入口のルーティング</li>
      <li>AWS Fargateでアプリを実行</li>
      <li>Amazon Auroraで受注・会員データを保管</li>
      <li>ElastiCacheでキャッシュを高速化</li>
      <li>S3で画像・静的アセットを保存</li>
      <li>SQSで非同期処理、CloudWatch Logsで監視</li>
    </ul>
    <p class="subtle">
      参考: <a href="https://aws.amazon.com/jp/solutions/case-studies/basefood-case-study/">Basefood Case Study</a>
    </p>
  </div>
  <img
    class="media-box"
    src="assets/c2baa9090a0892dce64e27f040df49cf-basefood-aws-architecture-diagram-japanese-1500x1297.d678afcf532d0956016a0ec8f56b24cff32ed602.jpg"
    alt="ECサイトのAWSアーキテクチャ例"
    style="width: 100%; height: 100%; object-fit: contain;"
  />
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>理解度チェック</h2>
  <ul>
    <li>3層構成の各層の役割を説明できる</li>
    <li>REST APIのHTTPメソッド4つを挙げられる</li>
    <li>IaaS/PaaS/SaaSの違いを一言で言える</li>
    <li>ステートレスのメリットを説明できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Database Basicsに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Database Basics
<p class="subtitle">RDB/NoSQL・スキーマ設計・インデックス/トランザクション</p>

---

<!-- .slide: class="layout-section" -->
## Security Basics
<p class="subtitle">認証/認可・OWASP Top 10・セキュアコーディング</p>

---

<!-- .slide: class="layout-section" -->
## Docker
<p class="subtitle">イメージ/コンテナ/レジストリと基本コマンド</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Dockerの学習目標</h2>
  <ul>
    <li>コンテナ化のメリットを説明できる</li>
    <li>イメージとコンテナの違いを区別できる</li>
    <li>Dockerfileの基本構造を読める</li>
    <li>基本コマンド（build/run/push）の役割を言える</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>環境差異の課題を解決する</h2>
  <ul>
    <li>「自分の環境では動く」問題が起きる</li>
    <li>開発/本番の差異でバグが出る</li>
    <li>セットアップが重く属人化しやすい</li>
  </ul>
</div>
<div class="callout">
  <p><strong>現場の困りごと</strong></p>
  <ul>
    <li>OS・ライブラリ・設定が揃わない</li>
    <li>新メンバーの環境構築に時間がかかる</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>コンテナで環境をパッケージ化する</h2>
  <ul>
    <li>アプリと依存をまとめて「箱」にする</li>
    <li>どこでも同じ動作を再現できる</li>
    <li>VMより軽く、起動が速い</li>
  </ul>
</div>
<div class="diagram">
  <img src="assets/vm-docker.png" alt="VMとDockerコンテナの比較" style="width: 100%; height: 100%; object-fit: contain;" />
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>イメージとコンテナを区別する</h2>
  <ul>
    <li>イメージ = 設計図（テンプレート・読み取り専用）</li>
    <li>コンテナ = 実行中のインスタンス</li>
    <li>1つのイメージから複数のコンテナを起動できる</li>
  </ul>
</div>
<div class="diagram" data-diagram="image-container" aria-label="イメージとコンテナの関係図"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>レジストリでイメージを共有する</h2>
  <ul>
    <li>Docker Hub / ECR / GCR などに保存</li>
    <li>pull で取得、push で公開</li>
    <li>タグでバージョン管理（例: app:v1.2）</li>
  </ul>
</div>
<div class="callout">
  <p><strong>GitHubとの対比</strong></p>
  <ul>
    <li>コード → GitHub</li>
    <li>イメージ → レジストリ</li>
  </ul>
</div>

---

<!-- .slide: class="layout-code" -->
<h2>Dockerfileでイメージを定義する</h2>
<pre><code class="language-docker">FROM python:3.11
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]</code></pre>
<div class="callout">
  <p><strong>命令の意味</strong></p>
  <ul>
    <li>FROM: ベースイメージを指定</li>
    <li>COPY: ファイルをイメージ内へ配置</li>
    <li>RUN: ビルド時にコマンド実行</li>
    <li>CMD: 起動時に実行する処理</li>
  </ul>
  <p class="subtle">上から順にレイヤーが積まれる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>build / run でコンテナを動かす</h2>
  <ul>
    <li>docker build -t myapp . → イメージ作成</li>
    <li>docker run myapp → コンテナ起動</li>
    <li>-p 8080:80 で公開、-d でバックグラウンド</li>
  </ul>
</div>
<div class="callout">
  <p><strong>覚えるコマンド</strong></p>
  <ul>
    <li>build: イメージを作る</li>
    <li>run: コンテナを起動する</li>
    <li>down: コンテナの出力を見る</li>
    <li>ps: 起動中の一覧を見る</li>
    <li>stop: コンテナを停止する</li>
    <li>logs: コンテナの出力を見る</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>push / pull でチームと共有する</h2>
  <ul>
    <li>docker push myapp:v1 → レジストリへ送信</li>
    <li>docker pull myapp:v1 → レジストリから取得</li>
    <li>CI/CDでビルド→push→本番でpullが基本形</li>
  </ul>
</div>
<div class="diagram" data-diagram="registry-flow" aria-label="ローカルとレジストリと本番の流れ"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Composeで複数サービスをまとめる</h2>
  <ul>
    <li>アプリ + DB + キャッシュを1ファイルで定義</li>
    <li>docker compose up で一括起動</li>
    <li>開発環境の再現性が上がる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>覚えて欲しいコマンド</strong></p>
  <ul>
    <li>docker compose up -d: バックグラウンドで起動</li>
    <li>docker compose build --no-cache: キャッシュなしで再ビルド</li>
    <li>docker compose down: 停止して関連リソースを削除</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Docker自己チェック</h2>
  <ul>
    <li>イメージとコンテナの違いを説明できる</li>
    <li>Dockerfileの主要命令（FROM/COPY/RUN/CMD）の意味を言える</li>
    <li>build/run/push/pullの役割を説明できる</li>
    <li>レジストリの目的を言語化できる</li>
    <li>覚えて欲しいコマンドを言える</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Testing &amp; Observabilityに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Testing & Observability
<p class="subtitle">unit/integration/e2e・ログ/アラート</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Testing & Observabilityの学習目標</h2>
  <ul>
    <li>unit/integration/e2eの違いを説明できる</li>
    <li>テストの役割と優先度の考え方を言語化できる</li>
    <li>ログとアラートの基本を説明できる</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>テストは変更を安全にする</h2>
  <ul>
    <li>「壊れていない」を素早く確認する</li>
    <li>後から直すコストを下げる</li>
    <li>安心して改善を続けるための土台</li>
  </ul>
</div>
<div class="callout">
  <p><strong>現場のメリット</strong></p>
  <ul>
    <li>リリースが速くなる</li>
    <li>手戻りが減る</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>テストピラミッドの考え方</h2>
  <ul>
    <li>unitを多く、e2eは少なく</li>
    <li>速い/安いテストを中心にする</li>
    <li>重要フローだけe2eで守る</li>
  </ul>
</div>
<div class="diagram">
  <img src="assets/image_2ca15acecf.png" alt="テストピラミッドの図" style="width: 100%; height: 100%; object-fit: contain;" />
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Unit Testで小さく守る</h2>
  <ul>
    <li>関数/モジュールの動きを確認</li>
    <li>失敗原因が特定しやすい</li>
    <li>依存はモック/スタブで切り分け</li>
    <li>スタブ: 返り値を固定 / モック: 呼び出し検証</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>料金計算・割引ロジック</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Integration Testで境界を守る</h2>
  <ul>
    <li>API・DB・外部サービスの連携</li>
    <li>データ形式や例外の扱いを確認</li>
    <li>テスト用データ/環境が重要</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>予約API → 在庫更新</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>E2E Testで重要フローを守る</h2>
  <ul>
    <li>ユーザー操作の流れを通す</li>
    <li>数は絞って重要フローに集中</li>
    <li>遅い/壊れやすいので最小限</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p>ログイン → 購入完了</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ログとアラートの基本</h2>
  <ul>
    <li>ログ: 何が起きたかを記録</li>
    <li>アラート: 「いつもと違う」を通知</li>
    <li>運用の早期気づきを助ける</li>
  </ul>
</div>
<div class="callout">
  <p><strong>最低限入れる</strong></p>
  <ul>
    <li>時刻・レベル・ID</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ログ設計のコツ</h2>
  <ul>
    <li>構造化（JSON）で検索しやすく</li>
    <li>INFO/WARN/ERRORで分ける</li>
    <li>user_id / request_id を必ず残す</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p class="subtle">level=ERROR request_id=... action=checkout</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Testing & Observability自己チェック</h2>
  <ul>
    <li>unit/integration/e2eの違いを言える</li>
    <li>テストピラミッドの意図を説明できる</li>
    <li>ログに入れるべき情報を挙げられる</li>
    <li>アラートの役割を説明できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">CI/CDに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## CI/CD
<p class="subtitle">ワークフロー設計・Secrets・自動デプロイ</p>

---

<!-- .slide: class="layout-section" -->
## Streamlit
<p class="subtitle">社内ツール/ダッシュボードの最短プロトタイプ</p>

---

<!-- .slide: class="layout-section" -->
## Generative AI Fundamentals
<p class="subtitle">LLMの仕組み・トークン/Attentionまで</p>

---

<!-- .slide: class="layout-section" -->
## Generative AI in Practice
<p class="subtitle">性能ベンチ比較・ユースケース・ガードレール</p>

---

<!-- .slide: class="layout-section" -->
## Wrap-up / Next Steps
<p class="subtitle">今日の要点・次に学ぶ順番・実務への接続</p>

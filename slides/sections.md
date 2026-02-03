<!-- .slide: class="layout-section" -->
## Intro / Goals
<p class="subtitle">到達点・評価軸・90枚のロードマップ</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>この講座で到達する地点</h2>
  <ul>
    <li>開発プロセスの全体像を説明できる</li>
    <li>Git/GitHubでチーム開発に参加できる</li>
    <li>Web/Cloud/DBの仕組みを理解し活用できる</li>
    <li>AIツールを使った開発ワークフローを実践できる</li>
    <li><strong>これら知識をベースとしてQiitaやZennの記事が読める←エンジニアにとって自走力は非常に非常に非常に大切</strong></li>
  </ul>
</div>
<div class="callout">
  <p><strong>究極的な目標</strong></p>
  <p class="subtle">生成AIによって細かい部分をあまり覚えなくても良い時代になりつつあります。</p>
  <p class="subtle">だけど、生成AIの言っていることや変なことを言っていたら指摘できるくらいの知識はやっぱり必要です。</p>
  <p class="subtle">また、要件定義やそれに基づく技術選定・スケジュール調整はまだまだ人がやらないといけません。</p>
  <p class="subtle">なのでこのセッションでは、要件定義や開発で人と関わるときに、技術職としてこれらを導けるような人になれることを目標にします。</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>自己評価のポイント</h2>
  <ul>
    <li>各セクション末の「自己チェック」で理解を確認</li>
    <li>概念を自分の言葉で説明できるか</li>
    <li>これらをベースにした議論が実装時にできるか</li>
  </ul>
<div class="callout" style="display: flex; justify-content: center;">
  <img src="assets/image.png" alt="目標の写真" style="height: 50vh;" />
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>180枚のロードマップ（前半）</h2>
  <ul>
    <li><strong>Foundations</strong>: 要件定義・設計・テストの基礎</li>
    <li><strong>Git / GitHub</strong>: 履歴管理と共同開発</li>
    <li><strong>Networking</strong>: TCP/IP・DNS・HTTPの仕組み</li>
    <li><strong>Web & Cloud</strong>: 3層構造とクラウドサービス</li>
    <li><strong>Database</strong>: SQL・正規化・トランザクション</li>
    <li><strong>Security</strong>: 認証・暗号・脆弱性対策</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>180枚のロードマップ（後半）</h2>
  <ul>
    <li><strong>Docker</strong>: コンテナ仮想化の基本</li>
    <li><strong>Testing & Observability</strong>: テスト戦略とログ/メトリクス</li>
    <li><strong>CI/CD</strong>: 自動化パイプライン</li>
    <li><strong>Streamlit</strong>: Pythonで素早くUI構築</li>
    <li><strong>Generative AI</strong>: LLMの活用と限界</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>学習のために</h2>
  <ul>
    <li>スライドはGitHubやURL（セッション時間のみ）で共有しています。</li>
    <li>分からないことはいつでも質問してください！（でも自分に聞くよりAIの方が詳しいです泣）</li>
    <li>このスライドは急造品なのでスライドに書いていないことをしゃべります！適宜メモを！</li>
    <li>後半はある程度手を動かすコンテンツを入れています</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ルーティーン</strong></p>
  <p class="subtle">50分に一回を目安に10分の休憩をとります。</p>
  <p class="subtle">チェックポイントを振り返るなどの時間にしてください！</p>
</div>

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
  <p>それぞれの作業時間割合↓</p>
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
    <li>変更/キャンセル/通知/在庫反映ができている</li>
    <li>変更・キャンセルは前日23:59まで</li>
    <li>キャンセル後は在庫が即時復活</li>
    <li>通知は30秒以内に送信</li>
  </ul>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>コラム：図で企業の種類を分けてみる</h2>
  <p class="subtle">ビジネス起点 vs 技術起点</p>
  <p><strong>ITコンサル・独立系</strong>（NRI/アクセンチュアなど）</p>
  <ul>
    <li>顧客の課題から構想→企画→要件→設計→開発→テスト→運用まで一気通貫</li>
    <li>ベンダーフリーで最適構成</li>
  </ul>
</div>
<div>
  <p><strong>メーカー系SIer</strong>（富士通/NECなど）</p>
  <ul>
    <li>技術資産・インフラ起点で提案</li>
    <li>R&Dや社会基盤に強い</li>
  </ul>
  <div class="callout">
    <p><strong>使い分けの軸</strong></p>
    <p class="subtle">ビジネス変革の設計か、社会インフラの最適化か</p>
  </div>
</div>
<img class="corner-image-badge" src="assets/dev-flow.svg" alt="開発の流れの要約" />

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>コラム：開発・ステージング・本番環境</h2>
  <p class="subtle">同じアプリでも「役割」を分ける</p>
  <ul>
    <li><strong>開発</strong>: 変更が多い / デバッグ重視 / ダミーデータ</li>
    <li><strong>ステージング</strong>: 本番に近い構成で最終確認</li>
    <li><strong>本番</strong>: 安定性最優先 / 実データ / 監視・バックアップ</li>
  </ul>
</div>
<div>
  <p><strong>分ける理由</strong></p>
  <ul>
    <li>障害や性能劣化を本番から隔離</li>
    <li>本番相当の検証でリリース判断</li>
    <li>データ・権限・APIキーを分離</li>
  </ul>
  <div class="callout">
    <p><strong>典型的な流れ</strong></p>
    <p class="subtle">Dev → Staging → Prod</p>
  </div>
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
    <li>ミニケースの受入条件を新たに2つ作れる</li>
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
  <h2>コラム：2026年の主要言語を実行方式で整理</h2>
  <p class="subtle"><a href="https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/">主要指標</a>で上位の言語を対象。</p>
  <p><strong>インタープリター系</strong></p>
  <ul>
    <li><strong>Python</strong>: AI/データの標準、学習容易、試作が速い。実行速度・配布・フロント用途は不向き。</li>
    <li><strong>JavaScript/TypeScript</strong>: Web独占、フルスタック、型安全で大規模に強い。ツールチェーンが複雑で流行変化が激しい。</li>
  </ul>
</div>
<div>
  <p><strong>コンパイラ系</strong></p>
  <ul>
    <li><strong>Go</strong>: 並行処理に強く、単一バイナリでクラウド運用が楽。表現力が控えめ、GUI/モバイルは不得意。</li>
    <li><strong>Rust</strong>: メモリ安全＋高速、Wasmなど高性能領域に強い。学習難度が高く、ビルド時間が長め。</li>
    <li><strong>Java/C#</strong>: 企業基盤と資産が厚い（弱み: 起動/メモリ/冗長）</li>
  </ul>
  <div class="callout">
    <p><strong>2026年の選び方（要点）</strong></p>
    <p>AI/データ: Python、Webのフロントエンド: TypeScript、高速サーバー: Go、基盤/高性能: Rust、企業の基盤システム: Java or C#</p>
  </div>
</div>

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
  <h2>コラム：IPv4 / IPv6の違いと歴史</h2>
  <ul>
    <li>IPv4は32bit、IPv6は128bitで、アドレス空間が大きく拡張</li>
    <li>表現できる数: IPv4は2^32（約43億）、IPv6は2^128（約3.4×10^38）</li>
    <li>IPv4の普及が先行し、枯渇・NAT利用が一般化</li>
    <li>IPv6は後発で標準化され、段階的に移行が進む</li>
    <li>現場ではIPv4/IPv6のデュアルスタック運用が多い</li>
  </ul>
</div>
<div class="callout">
  <p><strong>実務の視点</strong></p>
  <ul>
    <li>IPv6でもDNS・TCP/UDP・HTTPは同じ層構造</li>
    <li>移行はコストと互換性を見ながら段階的に</li>
  </ul>
</div>

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
    <li>IaaS: インフラだけ借りる（OS以上は自己管理） e.g. Compute Engine</li>
    <li>PaaS: ランタイムまで提供（アプリに集中） e.g. Cloud Run</li>
    <li>SaaS: 全て提供（設定だけで利用） e.g. sansan</li>
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

<div class="layout-2col layout-2col-wide">
  <div>
    <h2>コラム：BtoB SaaSのテナント分離</h2>
    <ul>
      <li>顧客ごとにデータを論理/物理で分離する設計</li>
      <li>分離レベル: DB別 / スキーマ別 / 行レベル（tenant_id）</li>
      <li>要件: 監査・越境防止・性能の公平性</li>
      <li>実務では<strong>コストと運用負荷</strong>のバランスが鍵</li>
    </ul>
    <p class="subtle">
      引用: <a href="https://speakerdeck.com/yaggy/tenantofen-li-shi-noshi-ifen-ketobaransu-saas-engineering-meetup-kitukuohuibento?slide=12">Speaker Deck（テナント分離方式の使い分けとバランス, slide 12）</a>
    </p>
  </div>
  <img
    class="media-box"
    src="assets/SaaS_isolation_model.png"
    alt="SaaSのテナント分離モデル"
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
    <li><strong>テスト</strong>：：今から出すアプリのテナント分離を考えてください</li>
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

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Database Basicsの学習目標</h2>
  <ul>
    <li>RDBとNoSQLの違いを説明できる</li>
    <li>テーブル設計の基本（正規化・主キー・外部キー）を理解できる</li>
    <li>インデックスの役割を説明できる</li>
    <li>トランザクション（ACID）の意味を言語化できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>キーワード</strong></p>
  <ul>
    <li>構造化と柔軟性</li>
    <li>検索の高速化</li>
    <li>整合性の担保</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>データ管理の課題を整理する</h2>
  <ul>
    <li>大量データをどう整理・保存するか</li>
    <li>検索・更新を速くするには</li>
    <li>データの整合性をどう保つか</li>
  </ul>
</div>
<div class="callout">
  <p><strong>答え</strong></p>
  <p>データベースで解決</p>
  <p class="subtle">用途に応じてRDB/NoSQLを選ぶ</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>RDBで構造化データを扱う</h2>
  <ul>
    <li>テーブル（表）/行/列でデータを整理</li>
    <li>スキーマ（構造）を先に定義する</li>
    <li>SQLで操作する</li>
  </ul>
</div>
<div class="callout">
  <p><strong>代表的なRDB</strong></p>
  <ul>
    <li>PostgreSQL</li>
    <li>MySQL</li>
    <li>Oracle / SQL Server</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>テーブル設計の基本</h2>
  <ul>
    <li><strong>主キー</strong>: 行を一意に識別（例: user_id）</li>
    <li><strong>外部キー</strong>: 他テーブルとの関連付け</li>
    <li><strong>正規化</strong>: 重複を減らし更新異常を防ぐ</li>
  </ul>
</div>
<div class="callout">
  <p><strong>設計のコツ</strong></p>
  <ul>
    <li>1テーブル1責務</li>
    <li>NULLを減らす</li>
    <li>命名規則を統一</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>SQLで操作する（CRUD）</h2>
  <ul>
    <li><strong>SELECT</strong>: データ取得</li>
    <li><strong>INSERT</strong>: データ追加</li>
    <li><strong>UPDATE</strong>: データ更新</li>
    <li><strong>DELETE</strong>: データ削除</li>
  </ul>
</div>
<div class="callout">
  <p><strong>よく使う句</strong></p>
  <ul>
    <li>WHERE: 条件指定</li>
    <li>JOIN: テーブル結合</li>
    <li>ORDER BY / LIMIT</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>インデックスで検索を速くする</h2>
  <p>インデックス = <strong>本の索引</strong>のようなもの</p>
  <ul>
    <li>本で「API」を探すとき<br/>
      1ページ目から順に探す → 遅い<br/>
      巻末の索引で「A」を引く → 速い</li>
    <li>DBも同じ！特定の列に索引を作ると検索が爆速に</li>
  </ul>
  <p class="subtle">索引を増やすと本が厚くなるように、データ追加時の負荷は増える</p>
</div>
<div class="callout">
  <p><strong>インデックスを作るべき列</strong></p>
  <ul>
    <li>WHERE句で頻繁に使う列<br/>
      <span class="subtle">例: メールアドレスでユーザー検索</span></li>
    <li>JOINのキー列<br/>
      <span class="subtle">例: 注文テーブルのuser_id</span></li>
    <li>ORDER BYの対象列<br/>
      <span class="subtle">例: 作成日時で並び替え</span></li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>トランザクションで整合性を守る</h2>
  <ul>
    <li>複数操作を1つの塊として扱う</li>
    <li><strong>COMMIT</strong>: 確定 / <strong>ROLLBACK</strong>: 取消</li>
    <li>途中で失敗したら全て戻る</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例: 銀行振込</strong></p>
  <p>A口座から引き落とし → B口座へ入金</p>
  <p class="subtle">片方だけ成功は許されない</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ACIDで信頼性を担保する</h2>
  <ul>
    <li><strong>Atomicity（原子性）</strong>: 全て成功 or 全て失敗</li>
    <li><strong>Consistency（一貫性）</strong>: 制約を常に満たす</li>
    <li><strong>Isolation（分離性）</strong>: 同時実行が干渉しない</li>
    <li><strong>Durability（持続性）</strong>: 確定したら消えない</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p>RDBはACIDを標準で保証</p>
  <p class="subtle">NoSQLは一部緩和することも</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>NoSQLで柔軟性を得る</h2>
  <ul>
    <li>スキーマレスで柔軟に保存</li>
    <li>水平スケール（台数増加）がしやすい</li>
    <li>用途に特化した種類がある</li>
  </ul>
</div>
<div class="callout">
  <p><strong>NoSQLの種類</strong></p>
  <ul>
    <li>ドキュメント型: MongoDB</li>
    <li>Key-Value: Redis / DynamoDB</li>
    <li>カラム指向: Cassandra</li>
    <li>グラフ: Neo4j</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>RDBとNoSQLを使い分ける</h2>
  <ul>
    <li><strong>RDB</strong>: 整合性重視・複雑なクエリ・関係データ</li>
    <li><strong>NoSQL</strong>: 柔軟性・大量データ・高速読み書き</li>
    <li>要件に応じて選択、併用も一般的</li>
  </ul>
</div>
<div class="callout">
  <p><strong>選定の観点</strong></p>
  <ul>
    <li>データ構造の安定性</li>
    <li>スケール要件</li>
    <li>整合性 vs 可用性</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ミニケース：ECサイトのDB設計</h2>
  <ul>
    <li>ユーザー/商品/注文 → RDBで管理</li>
    <li>商品検索ログ/閲覧履歴 → NoSQLで蓄積</li>
    <li>セッション/カート → Redisでキャッシュ</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p>決済は整合性重視 → RDB</p>
  <p>ログは速度重視 → NoSQL</p>
  <p class="subtle">適材適所で組み合わせる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Database Basics理解度チェック</h2>
  <ul>
    <li>RDBとNoSQLの違いを説明できる</li>
    <li>主キー/外部キー/正規化の役割を言える</li>
    <li>インデックスのメリット/デメリットを挙げられる</li>
    <li>ACIDの4要素を説明できる</li>
    <li>用途に応じたDB選択の観点を言える</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Security Basicsに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Security Basics
<p class="subtitle">認証/認可・OWASP Top 10・セキュアコーディング</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Security Basicsの学習目標</h2>
  <ul>
    <li>認証と認可の違いを説明できる</li>
    <li>OWASP Top 10の代表的な脆弱性を挙げられる</li>
    <li>セキュアコーディングの基本原則を言語化できる</li>
    <li>機密情報の安全な取り扱い方を理解できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>キーワード</strong></p>
  <ul>
    <li>誰か・何ができるか</li>
    <li>脆弱性を知る</li>
    <li>安全に作る</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>セキュリティの課題を整理する</h2>
  <ul>
    <li>不正アクセス・情報漏洩のリスク</li>
    <li>攻撃者視点で「穴」を探される現実</li>
    <li>被害は金銭・信用・法的責任に及ぶ</li>
  </ul>
</div>
<div class="callout">
  <p><strong>なぜ学ぶか</strong></p>
  <p>作る人が知らないと守れない</p>
  <p class="subtle">セキュリティは後付けが難しい</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>認証と認可を区別する</h2>
  <ul>
    <li><strong>認証（Authentication）</strong>: 「誰か」を確認する</li>
    <li><strong>認可（Authorization）</strong>: 「何ができるか」を制御する</li>
    <li>両方揃って初めてアクセス制御が成立</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例え</strong></p>
  <p>認証 = 社員証で本人確認</p>
  <p>認可 = 入れる部屋が決まる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>認証の実現方法</h2>
  <ul>
    <li>パスワード認証の限界（漏洩・使い回し）</li>
    <li>多要素認証（MFA）で強化</li>
    <li>OAuth/OIDCで外部委託（Google/GitHub等）</li>
  </ul>
</div>
<div class="callout">
  <p><strong>MFAの3要素</strong></p>
  <ul>
    <li>知識: パスワード</li>
    <li>所持: スマホ・トークン</li>
    <li>生体: 指紋・顔</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>トークンベース認証（JWT）とは</h2>
  <ul>
    <li><strong>JWT</strong> = JSON Web Token（ジョット）</li>
    <li>ログイン後にサーバーが発行する「通行証」</li>
    <li>以降のリクエストにこのトークンを添付して「自分」を証明</li>
  </ul>
</div>
<div class="callout">
  <p><strong>イメージ</strong></p>
  <p>遊園地で入場時にリストバンドをもらい、アトラクションごとに見せる感じ</p>
  <p class="subtle">毎回入口で身分証を見せなくてOK</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>JWTの構造</h2>
  <p>3つのパートをドット(.)で連結</p>
  <pre style="font-size: 0.7em; background: #f5f5f5; padding: 8px; border-radius: 4px;">
xxxxx.yyyyy.zzzzz
  ↓      ↓      ↓
Header.Payload.Signature</pre>
  <ul style="font-size: 0.9em;">
    <li><strong>Header</strong>: 種類と署名アルゴリズム</li>
    <li><strong>Payload</strong>: ユーザーID・有効期限など</li>
    <li><strong>Signature</strong>: 改ざん検知用の署名</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p>PayloadはBase64エンコード（暗号化ではない）</p>
  <p class="subtle">→ 誰でも中身を読める！</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>JWT認証の流れ</h2>
  <ol style="font-size: 0.9em;">
    <li>ユーザーがID/パスワードでログイン</li>
    <li>サーバーが認証し、JWTを発行</li>
    <li>クライアントがJWTを保存（localStorage等）</li>
    <li>APIリクエスト時に <code>Authorization: Bearer &lt;JWT&gt;</code> を付与</li>
    <li>サーバーは署名を検証してユーザーを特定</li>
  </ol>
</div>
<div class="callout">
  <p><strong>Bearerとは？</strong></p>
  <p>「持参人」の意味</p>
  <p class="subtle">このトークンを持っている人 = 認証済み</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>JWTの注意点</h2>
  <ul>
    <li><strong>署名検証は必須</strong>: 検証しないと偽造トークンを受け入れてしまう</li>
    <li><strong>有効期限は短めに</strong>: 漏洩時の被害を限定（15分〜1時間程度）</li>
    <li><strong>機密情報はPayloadに入れない</strong>: パスワードやクレカ番号はNG</li>
    <li><strong>HTTPS必須</strong>: 通信経路での盗聴を防ぐ</li>
  </ul>
</div>
<div class="callout">
  <p><strong>よくある失敗</strong></p>
  <p>「alg: none」攻撃 → 署名なしを許可してしまう</p>
  <p class="subtle">ライブラリの設定を確認しよう</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>認可の設計</h2>
  <ul>
    <li>RBAC（ロールベースアクセス制御）</li>
    <li>最小権限の原則: 必要最小限だけ許可</li>
    <li>認可チェックはサーバー側で必ず行う</li>
  </ul>
</div>
<div class="callout">
  <p><strong>よくある失敗</strong></p>
  <p>フロントで非表示 → APIは叩ける</p>
  <p class="subtle">UIで隠すだけでは守れない</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>OWASP Top 10を知る</h2>
  <ul>
    <li>Webアプリの代表的な脆弱性リスト</li>
    <li>業界標準のチェックポイント</li>
    <li>定期的に更新される（最新動向を追う）</li>
  </ul>
  <p class="subtle">参考: <a href="https://www.proactivedefense.jp/blog/blog-training/post-7210">OWASP Top 10 解説</a></p>
</div>
<div class="callout">
  <p><strong>代表的な項目</strong></p>
  <ul>
    <li>インジェクション</li>
    <li>認証の不備</li>
    <li>機密データの露出</li>
    <li>XSS / CSRF</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>インジェクション攻撃を防ぐ</h2>
  <ul>
    <li>SQLインジェクション: 入力からSQL文を改変</li>
    <li>コマンドインジェクション: OSコマンドを実行</li>
    <li>対策: プリペアドステートメント、パラメータ化</li>
  </ul>
</div>
<div class="callout">
  <p><strong>悪い例</strong></p>
  <p class="subtle">SELECT * FROM users WHERE id = '$input'</p>
  <p class="subtle">→ 入力がそのままSQL文に結合される</p>
  <p class="subtle">→ ' OR '1'='1 で全件取得される</p>
  <p><strong>良い例</strong></p>
  <p class="subtle">SELECT * FROM users WHERE id = ?</p>
  <p class="subtle">→ ?はプレースホルダ（値として扱われる）</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>XSS（クロスサイトスクリプティング）を防ぐ</h2>
  <ul>
    <li>悪意あるスクリプトを埋め込まれる攻撃</li>
    <li>反射型 / 保存型 / DOMベースの3種類</li>
    <li>対策: 出力エスケープ、CSP</li>
  </ul>
</div>
<div class="callout">
  <p><strong>CSP（Content Security Policy）</strong></p>
  <p>許可するスクリプトの出所を制限</p>
  <p class="subtle">インラインスクリプトを禁止</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>CSRF（クロスサイトリクエストフォージェリ）を防ぐ</h2>
  <ul>
    <li>ユーザーの意図しない操作を実行させる</li>
    <li>ログイン中のセッションを悪用</li>
    <li>対策: CSRFトークン、SameSite Cookie</li>
  </ul>
</div>
<div class="callout">
  <p><strong>攻撃の流れ</strong></p>
  <p>罠サイト訪問 → 勝手にリクエスト送信</p>
  <p class="subtle">ユーザーは気づかない</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>セキュアコーディングの原則</h2>
  <ul>
    <li>入力は全て検証する（信頼しない）</li>
    <li>出力は必ずエスケープする</li>
    <li>フェイルセーフ: 失敗時は安全側に倒す</li>
  </ul>
</div>
<div class="callout">
  <p><strong>心構え</strong></p>
  <p>外部からの入力は全て「攻撃」かもしれない</p>
  <p class="subtle">性善説では守れない</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>機密情報の取り扱い</h2>
  <ul>
    <li>パスワードは必ずハッシュ化（bcrypt等）</li>
    <li>APIキー・秘密鍵はコードに書かない</li>
    <li>環境変数（.envファイル）やシークレットマネージャで管理</li>
  </ul>
</div>
<div class="callout">
  <p><strong>絶対NG</strong></p>
  <ul>
    <li>パスワードの平文保存</li>
    <li>GitHubにAPIキーをpush</li>
    <li>ログに機密情報を出力</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ミニケース：ログイン機能のセキュリティ</h2>
  <ul>
    <li>パスワードハッシュ + ソルト</li>
    <li>ログイン試行回数制限（ブルートフォース対策）</li>
    <li>セッション固定攻撃への対応（ログイン後に再発行）</li>
  </ul>
</div>
<div class="callout">
  <p><strong>追加で検討</strong></p>
  <ul>
    <li>アカウントロック</li>
    <li>パスワード強度チェック</li>
    <li>ログイン通知</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Security Basics理解度チェック</h2>
  <ul>
    <li>認証と認可の違いを一言で説明できる</li>
    <li>OWASP Top 10の脆弱性を3つ挙げられる</li>
    <li>SQLインジェクションの対策を言える</li>
    <li>パスワードの安全な保存方法を説明できる</li>
    <li>最小権限の原則を言語化できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Dockerに進む</p>
</div>

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
    <li>down: イメージを削除</li>
    <li>run: コンテナを起動する</li>
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

<!-- .slide: class="layout-2col" -->
<div>
  <h2>CI/CDの学習目標</h2>
  <ul>
    <li>CIとCD（Delivery/Deploy）の違いを説明できる</li>
    <li>ワークフローの基本構成（トリガー/ジョブ/ステップ）を理解できる</li>
    <li>Secretsの安全な管理方法を言語化できる</li>
    <li>自動デプロイのメリットと代表的パターンを挙げられる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ゴール</strong></p>
  <p class="subtle">「安全に早く出す」仕組みを説明できる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>手動デプロイの課題を整理する</h2>
  <ul>
    <li>手作業でビルド・デプロイすると時間がかかる</li>
    <li>ヒューマンエラー（手順漏れ・設定ミス）が起きやすい</li>
    <li>「誰が・いつ・何を」反映したか追えない</li>
  </ul>
</div>
<div class="callout">
  <p><strong>結論</strong></p>
  <p class="subtle">自動化で解決 → 速く・安全に・再現可能に</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>CI/CDとは何か</h2>
  <ul>
    <li>CI（継続的インテグレーション）: 変更を頻繁に統合し自動ビルド/テスト</li>
    <li>CD（継続的デリバリー）: いつでもリリースできる状態を維持</li>
    <li>CD（継続的デプロイ）: テスト通過後に自動で本番反映</li>
  </ul>
</div>
<div class="callout">
  <p><strong>まとめ</strong></p>
  <p class="subtle">CI → ビルド/テスト自動化 / CD → リリース自動化</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>CIで品質を守る</h2>
  <ul>
    <li>push/PRのたびに自動でビルド・テストを実行</li>
    <li>壊れたコードがmainに入るのを防ぐ</li>
    <li>問題を早期発見し、修正コストを下げる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p class="subtle">小さく頻繁に統合 → コンフリクトも小さく</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>CDでリリースを速くする</h2>
  <ul>
    <li>テスト通過後、ステージング/本番へ自動反映</li>
    <li>手作業を減らし、リリース頻度を上げる</li>
    <li>ロールバックも自動化で素早く対応</li>
  </ul>
</div>
<div class="callout">
  <p><strong>効果</strong></p>
  <p class="subtle">デプロイが怖くなくなる → 改善サイクルが速くなる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>GitHub Actionsの基本</h2>
  <ul>
    <li><code>.github/workflows/</code>にYAMLで定義</li>
    <li>イベント（push/PR/schedule）で自動実行</li>
    <li>GitHub上でログと結果を確認できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>代表的なCI/CDツール</strong></p>
  <ul>
    <li>GitHub Actions</li>
    <li>GitLab CI</li>
    <li>CircleCI / Jenkins</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ワークフローの構成要素</h2>
  <ul>
    <li>トリガー（on）: いつ実行するか（push / pull_request / schedule）</li>
    <li>ジョブ（jobs）: 並列/直列で動く処理単位</li>
    <li>ステップ（steps）: ジョブ内の個々のコマンド</li>
  </ul>
</div>
<div class="diagram" data-diagram="workflow-structure" aria-label="ワークフロー構成図"></div>

---

<!-- .slide: class="layout-code" -->
<h2>YAMLの基本例</h2>
<pre><code class="language-yaml">on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm test</code></pre>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p class="subtle">uses = 再利用可能なAction / run = シェルコマンド</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Secretsで機密情報を守る</h2>
  <ul>
    <li>APIキー・トークンをコードに書かない</li>
    <li>GitHubのSecrets設定で暗号化保存</li>
    <li><code>${{ secrets.MY_KEY }}</code>で参照</li>
  </ul>
</div>
<div class="callout">
  <p><strong>絶対NG</strong></p>
  <p class="subtle">シークレットをログに出力 / コードにハードコード</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>自動デプロイのパターンを選ぶ</h2>
  <ul>
    <li><strong>ローリング</strong>: 順次入れ替え（ダウンタイムなし）</li>
    <li><strong>ブルーグリーン</strong>: 新旧環境を切り替え（即時ロールバック可能）</li>
    <li><strong>カナリア</strong>: 一部ユーザーに先行リリース</li>
  </ul>
</div>
<div class="callout">
  <p><strong>判断軸</strong></p>
  <p class="subtle">リスクを下げながら本番反映</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ミニケース：PRからデプロイまでの流れ</h2>
  <ul>
    <li>開発者がPRを作成</li>
    <li>CI（ビルド・テスト）が自動実行</li>
    <li>レビュー・承認後にマージ</li>
    <li>CD（ステージング→本番）が自動実行</li>
  </ul>
</div>
<div class="diagram" data-diagram="cicd-pipeline" aria-label="PRから本番までの流れ"></div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>CI/CD理解度チェック</h2>
  <ul>
    <li>CIとCDの違いを一言で説明できる</li>
    <li>ワークフローの3要素（トリガー/ジョブ/ステップ）を言える</li>
    <li>Secretsを安全に扱う方法を説明できる</li>
    <li>自動デプロイのメリットを挙げられる</li>
    <li>ブルーグリーン/カナリアの違いを説明できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Streamlitに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Streamlit
<p class="subtitle">社内ツール/ダッシュボードの最短プロトタイプ</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Streamlitの学習目標</h2>
  <ul>
    <li>Streamlitが解決する課題を説明できる</li>
    <li>基本的なUIコンポーネントを使える</li>
    <li>簡易ダッシュボードを構築できる</li>
    <li>Streamlit Cloudへのデプロイ方法を言語化できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ゴール</strong></p>
  <p class="subtle">Pythonだけで動くUIを作れるようになる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>社内ツール開発の課題を解決する</h2>
  <ul>
    <li>データ可視化やダッシュボードに専門スキルが必要</li>
    <li>フロントエンド/バックエンドの分離が手間</li>
    <li>プロトタイプに時間がかかる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>結論</strong></p>
  <p class="subtle">Streamlitなら「Pythonだけ」で即UI構築</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Streamlitとは</h2>
  <ul>
    <li>PythonだけでWebアプリが作れるフレームワーク</li>
    <li>データサイエンス・社内ツール向け</li>
    <li>HTML/CSS/JS不要で即プロトタイプ</li>
  </ul>
</div>
<div class="callout">
  <p><strong>特徴</strong></p>
  <ul>
    <li>スクリプト感覚で書ける</li>
    <li>変更すると自動リロード</li>
    <li>デプロイも簡単</li>
  </ul>
</div>

---

<!-- .slide: class="layout-code" -->
<h2>基本構造を理解する</h2>
<pre><code class="language-python">import streamlit as st

st.title("売上ダッシュボード")
st.write("データを可視化します")

name = st.text_input("名前を入力")
st.write(f"こんにちは、{name}さん")</code></pre>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <ul>
    <li>上から下へ順に実行・描画</li>
    <li>ウィジェットの戻り値をそのまま使える</li>
    <li>保存すると自動でリロード（Hot reload）</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ウィジェットで入力を受け取る</h2>
  <ul>
    <li><code>st.button()</code>: ボタン</li>
    <li><code>st.text_input()</code>: テキスト入力</li>
    <li><code>st.selectbox()</code>: プルダウン選択</li>
    <li><code>st.slider()</code>: スライダー</li>
    <li><code>st.date_input()</code>: 日付選択</li>
  </ul>
</div>
<div class="callout">
  <p><strong>使い方</strong></p>
  <p class="subtle">戻り値を変数に受けて処理に使う</p>
  <pre><code class="language-python">age = st.slider("年齢", 0, 100)
st.write(f"あなたは{age}歳")</code></pre>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>データを表示・可視化する</h2>
  <ul>
    <li><code>st.dataframe()</code>: インタラクティブな表</li>
    <li><code>st.table()</code>: 静的な表</li>
    <li><code>st.line_chart()</code>: 折れ線グラフ</li>
    <li><code>st.bar_chart()</code>: 棒グラフ</li>
    <li><code>st.plotly_chart()</code>: Plotly連携</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <pre><code class="language-python">import pandas as pd
df = pd.read_csv("sales.csv")
st.dataframe(df)
st.line_chart(df["売上"])</code></pre>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>レイアウトを整える</h2>
  <ul>
    <li><code>st.columns()</code>: カラム分割</li>
    <li><code>st.sidebar</code>: サイドバー</li>
    <li><code>st.expander()</code>: 折りたたみ</li>
    <li><code>st.tabs()</code>: タブ切り替え</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例: 2カラム</strong></p>
  <pre><code class="language-python">col1, col2 = st.columns(2)
col1.metric("売上", "100万円")
col2.metric("利益", "20万円")</code></pre>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>状態管理（Session State）</h2>
  <ul>
    <li>Streamlitは毎回スクリプトを再実行する</li>
    <li><code>st.session_state</code>でリロード間のデータ保持</li>
    <li>ボタンクリック回数やフォーム入力の維持に使う</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例: カウンター</strong></p>
  <pre><code class="language-python">if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("カウント"):
    st.session_state.count += 1
st.write(st.session_state.count)</code></pre>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>デプロイする</h2>
  <ul>
    <li><strong>Streamlit Cloud</strong>: GitHub連携で無料デプロイ</li>
    <li><strong>Docker</strong>: コンテナ化してCloud Run等へ</li>
    <li><strong>secrets管理</strong>: <code>st.secrets</code>でAPIキー等を安全に参照</li>
  </ul>
</div>
<div class="callout">
  <p><strong>Streamlit Cloudの手順</strong></p>
  <ol>
    <li>GitHubにpush</li>
    <li>Streamlit Cloudで連携</li>
    <li>自動でデプロイ完了</li>
  </ol>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ミニケース：売上ダッシュボード</h2>
  <ul>
    <li>CSVアップロード → データ表示</li>
    <li>サイドバーで日付フィルタ</li>
    <li>グラフで売上推移を可視化</li>
    <li>KPIをメトリクスで表示</li>
  </ul>
</div>
<div class="callout">
  <p><strong>構成イメージ</strong></p>
  <ul>
    <li>サイドバー: フィルタ設定</li>
    <li>メイン上部: KPIカード</li>
    <li>メイン下部: グラフ + 表</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Streamlit理解度チェック</h2>
  <ul>
    <li>Streamlitが解決する課題を説明できる</li>
    <li>基本コンポーネント5つを挙げられる</li>
    <li>Session Stateの役割を言える</li>
    <li>レイアウト用コンポーネントを2つ挙げられる</li>
    <li>デプロイ方法を2つ挙げられる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Generative AI Fundamentalsに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Generative AI Fundamentals
<p class="subtitle">LLMの仕組み・トークン/Attentionまで</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>学習目標を確認する</h2>
  <ul>
    <li>LLMの基本的な仕組みを理解できる</li>
    <li>トークンとトークナイズの流れを説明できる</li>
    <li>Attentionがなぜ重要かを言語化できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ゴール</strong></p>
  <p class="subtle">「LLMが文章を生成する仕組み」を概念レベルで説明できる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>AI入門には3Blue1Brownの動画がおすすめ</h2>
  <ul>
    <li>LLMの全体像と学習/推論の流れ</li>
    <li>AttentionとTransformerの要点</li>
    <li>Temperatureの理解</li>
  </ul>
</div>
<div class="callout">
  <p><strong>視聴リンク</strong></p>
  <p class="subtle"><a href="https://www.youtube.com/watch?v=y7NQiNER6r4">LLMの仕組み（簡単バージョン）</a></p>
  <p class="subtle">視聴後、用語を自分の言葉で説明できるか確認する</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>コラム:言葉のベクトルで遊んでみる</h2>
  <ul>
  <li class="subtle"><a href="https://colab.research.google.com/drive/1EHjVX8U6a7jN8h-DgBQVOfQTfyMdtlZY?usp=sharing">言葉のベクトルのColab</a></li>
  </ul>
</div>
  <div class="diagram" style="height: 70%; align-self: stretch;">
    <img
      src="assets/newplot2.png"
      alt="プロット"
      style="width: 100%; height: 100%; object-fit: contain;"
    />
  </div>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>理解度チェック</h2>
  <ul>
    <li>トークンとは何かを説明できる</li>
    <li>Attentionが解決する課題を言える</li>
    <li>Transformerの基本構造（Attention + Feedforward）を図示できる</li>
    <li><strong>クイズ</strong>：何かのテキストを使ってAIと会話するときにテキストの代名詞として適切なのはどれ？</li>
    <li>①これ　②以下　③以上</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Generative AI in Practiceに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Generative AI in Practice
<p class="subtitle">性能ベンチ比較・ユースケース・ガードレール</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Generative AI in Practiceの学習目標</h2>
  <ul>
    <li>用途に応じたモデル選定の考え方を説明できる</li>
    <li>LLMの性能ベンチマークの読み方を理解できる</li>
    <li>主要なユースケースとその実装パターンを言語化できる</li>
    <li>Codexの使い方を理解できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ゴール</strong></p>
  <p class="subtle">実務でLLMを使い分け、効果的に活用できる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>LLMの限界と課題</h2>
  <ul>
    <li><strong>ハルシネーション</strong>: 事実と異なる出力を自信満々に生成</li>
    <li><strong>知識のカットオフ</strong>: 学習データ時点の情報で止まる</li>
    <li><strong>コンテキスト長の制限</strong>: 長い入力は処理しきれない</li>
    <li><strong>推論コストの高さ</strong>: 高性能モデルは遅く・高価</li>
  </ul>
</div>
<div class="callout">
  <p><strong>心構え</strong></p>
  <p class="subtle">「限界を知った上で使う」が実務の基本</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>主要プロバイダーとモデルの特徴</h2>
  <ul>
    <li><strong>OpenAI</strong>: GPT-5.2（Instant/Thinking/Pro）/ GPT-5.2-Codex → 現状最も優れている・実装能力が高い・リミットが長い・教えるのは下手</li>
    <li><strong>Google</strong>: Gemini 3 Pro / Gemini 3 Flash → 画像認識が強い・コンテキストが非常に長い・リミットが長い・エコシステムが強力</li>
    <li><strong>Anthropic</strong>: Claude Opus 4.5 / Sonnet 4.5 / Haiku 4.5 → コーディング特化型AI・コードを教えるのが上手い・リミットが短い</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p class="subtle">各社の強み・弱みを把握して選定する</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>モデル選定の考え方</h2>
  <ul>
    <li><strong>コーディング・分析</strong>: 各社の最上位モデル（Extra high）を使う（精度が重要）</li>
    <li>コードレビューはhighでもOK</li>
    <li><strong>大量処理・要約</strong>: 軽量モデル（Flash系）でコスト抑制</li>
    <li><strong>判断軸</strong>: コスト × 速度 × 品質のトレードオフ</li>
  </ul>
</div>
<div class="callout">
  <p><strong>使い分け</strong></p>
  <ul>
    <li>高品質必須 → 最上位モデル</li>
    <li>大量・低コスト → 軽量モデル</li>
  </ul>
</div>

---

<div class="layout-2col" style="height: 100%; align-items: stretch;">
  <div>
    <h2>各社モデルのベンチマーク比較</h2>
    <ul>
      <li><strong>SWE-Bench Pro</strong>: 実務的なソフトウェア修正</li>
      <li><strong>GPQA Diamond / CharXiv Reasoning</strong>: 専門推論・科学論文読解</li>
      <li><strong>FrontierMath / AIME 2025</strong>: 数学推論・競技数学</li>
      <li><strong>ARC-AGI 1/2 / GDPval</strong>: 抽象推論・知識労働タスク</li>
      <li><strong>注意</strong>: 最大推論設定など条件差で結果が変わる</li>
    </ul>
  </div>
  <div class="diagram" style="height: 70%; align-self: stretch;">
    <img
      src="assets/1765546235-9mDYPGaS7woElBRMF0Htgpjy.webp"
      alt="各社モデルのベンチマーク比較"
      style="width: 100%; height: 100%; object-fit: contain;"
    />
  </div>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>最近のプロンプトエンジニアリング①</h2>
  <h3>思考型モデル（Thinking）への最適化</h3>
  <ul>
    <li>従来のCoT（「Step-by-stepで考えて」）は<strong>不要・逆効果</strong></li>
    <li>ペルソナ設定（「あなたは専門家です」）も精度を下げる可能性</li>
    <li><strong>推奨</strong>: シンプルに「目的」と「制約事項」だけを伝える</li>
  </ul>
</div>
<div class="callout">
  <p><strong>理由</strong></p>
  <p class="subtle">思考型モデルは自律的に最適な思考を行う</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>最近のプロンプトエンジニアリング②</h2>
  <h3>会話継続による「精度の劣化」</h3>
  <ul>
    <li>最初の入力が最も高精度</li>
    <li>2ターン以上続くと、過去の出力（誤りを含む）に引っ張られる</li>
    <li><strong>対策</strong>: 可能な限り1回の入力で完結させる</li>
    <li>長引いたら「要約→新しいチャットで再開」</li>
  </ul>
</div>
<div class="callout">
  <p><strong>参考</strong></p>
  <p class="subtle"><a href="https://arxiv.org/abs/2505.06120">LLMs Get Lost In Multi-Turn Conversation</a></p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>最近のプロンプトエンジニアリング③</h2>
  <h3>LLMが一度に処理できる「指示の数」</h3>
  <ul>
    <li>高性能モデル（o3, Gemini 2.0 Pro）: 100個近い指示でも精度維持</li>
    <li>軽量モデル: 指示が増えると急激に精度低下</li>
    <li><strong>対策</strong>: 軽量モデル→指示を分割、高性能モデル→まとめてOK</li>
  </ul>
</div>
<div class="callout">
  <p><strong>参考</strong></p>
  <p class="subtle"><a href="https://arxiv.org/abs/2507.11538">How Many Instructions Can LLMs Follow at Once?</a></p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>最近のプロンプトエンジニアリング④</h2>
  <h3>プロンプト繰り返し手法（非思考型モデル向け）</h3>
  <ul>
    <li>プロンプトを2回繰り返すだけで精度向上</li>
    <li>理由: 1回目がコンテキストとして機能し、2回目で質問意図を理解した状態で処理</li>
    <li><strong>注意</strong>: 思考型モデル（o1等）では効果薄い</li>
  </ul>
</div>
<div class="callout">
  <p><strong>参考</strong></p>
  <p class="subtle"><a href="https://transformer-explainer.dataviz.cnn.io/">TRANSFORMER EXPLAINER</a>でAttentionの仕組みを学べる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>最近のプロンプトエンジニアリング⑤</h2>
  <h3>AIの忖度（Sycophancy）</h3>
  <ul>
    <li>学習データの性質上、<strong>正解より同調</strong>を優先しがち</li>
    <li>「Aが好き」→Aを支持、「Bが好き」→Bを支持</li>
    <li>確証バイアスや誤判断が強化される</li>
  </ul>
</div>
<div class="callout">
  <p><strong>注意</strong></p>
  <p class="subtle">特に難しい分野などで顕著になる。数理最適化モデルのコード生成など</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>忖度を防ぐ5つのTips</h2>
  <ul>
    <li>意見・所有権を示さない（「私が書いた」等）</li>
    <li><strong>第三者成果物</strong>として評価させる</li>
    <li>指摘は断定するか、根拠を貼って検証させる</li>
    <li>メモリ機能/履歴はオフ、<strong>一時チャット</strong>を使う</li>
    <li>「機嫌を取るな」など批判的プロンプトを設定</li>
  </ul>
</div>
<div class="callout">
  <p><strong>例</strong></p>
  <p class="subtle">「外注先のコードです。5点満点で厳しく評価して」</p>
  <p class="subtle">重要判断は外部ソースと突き合わせる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Codexの使い方のおすすめ</h2>
  <ul>
    <li><strong>OpenAI Codex</strong>: コード生成に特化したAIツール（ChatGPT内で利用可能）</li>
    <li>タスクを明確に指示する</li>
    <li>既存コードのコンテキストを与える</li>
    <li>生成コードは必ずレビュー・テストする</li>
  </ul>
</div>
<div class="callout">
  <p><strong>鉄則</strong></p>
  <p class="subtle">生成コードを鵜呑みにしない</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>CodexでSKILLを使ってみる</h2>
  <ul>
    <li><strong>SKILL</strong>: Codexのカスタム機能（特定タスクのテンプレート）</li>
    <li>活用例: コードレビュー、テスト生成、リファクタリング提案</li>
    <li>定型作業を効率化できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>実践</strong></p>
  <p class="subtle">実際に試してみよう</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>ケース：このスライド資料の作り方</h2>
  <ul>
    <li>最初はスライドを書かせずに、各章の構成案を生成させる</li>
    <li>構成案を元に、各章の草案を作成</li>
    <li>生成AIにスライドをほとんど書かせたかったのでHTML形式で出力できるプラグイン（CDN）を探す</li>
    <li>各章の草案を踏まえつつスライドのテンプレート（右半分写真、下半分写真用のスライドなど）を書かせる。</li>
    <li>テンプレの使い方は別途SKILLでまとめる</li>
    <li>各章は生成AIで「目的→要点→例→理解度チェック」の草案を作成</li>
    <li>仕上げは人手で整形（3〜5点の箇条書き、図の差し替え、レイアウト調整）</li>
    <li>AI出力は必ず<strong>出典確認</strong>と<strong>レビュー</strong>で確定</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>コラム：RAGについて</h2>
  <ul>
    <li>RAG（Retrieval-Augmented Generation）とは、AIが持っていない知識をデータベースから引っ張ってくることでAI自体は知らない知識をあたかも知っているかのように振る舞わさせる技術のこと</li>
  </ul>
</div>
  <div class="diagram" style="height: 60vh;  align-self: stretch;">
    <img
      src="assets/Careerport プレゼンテーション資料.png"
      alt="プロット"
      style="width: 100%; height: 100%; object-fit: contain;"
    />
  </div>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>Generative AI in Practice 理解度チェック</h2>
  <ul>
    <li>モデル選定で考慮する3軸（コスト・速度・品質）を説明できる</li>
    <li>思考型モデルで「不要になったテクニック」を2つ挙げられる</li>
    <li>会話が長引いた時の対策を言える</li>
    <li>LLMの限界（ハルシネーション等）を3つ挙げられる</li>
    <li>Codexの適切な使い方を説明できる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>次の章へ</strong></p>
  <p class="subtle">Wrap-upに進む</p>
</div>

---

<!-- .slide: class="layout-section" -->
## Wrap-up
<p class="subtitle">今日の要点・次に学ぶべきもの</p>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>今回のセッションで学んだこと</h2>
  <ul>
    <li><strong>基盤</strong>: 要件定義・設計・テストの流れ（Vモデル）</li>
    <li><strong>バージョン管理</strong>: Git/GitHubでチーム開発</li>
    <li><strong>インフラ</strong>: ネットワーク・Web・クラウド・DB</li>
    <li><strong>品質・安全</strong>: セキュリティ・テスト・CI/CD</li>
    <li><strong>最新技術</strong>: Docker・Streamlit・生成AI</li>
  </ul>
</div>
<div class="callout">
  <p><strong>全体像</strong></p>
  <p class="subtle">「作る→守る→届ける」のサイクルを一周した</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>知識はつながっている</h2>
  <ul>
    <li><strong>要件定義</strong>でゴールを決める</li>
    <li><strong>Git/GitHub</strong>でコードを共有</li>
    <li><strong>Web/Cloud/DB</strong>でシステムを構築</li>
    <li><strong>Security/Testing</strong>で品質を担保</li>
    <li><strong>CI/CD</strong>で自動化・高速化</li>
    <li><strong>AI</strong>で開発を加速</li>
  </ul>
</div>
<div class="callout">
  <p><strong>ポイント</strong></p>
  <p>各技術は単独ではなく、開発フロー全体で連携する</p>
  <p class="subtle">1つを深く学ぶと、他の理解も深まる</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>今日から実践できること</h2>
  <ul>
    <li>個人プロジェクトでGit/GitHubを使う</li>
    <li>Dockerで開発環境を作ってみる</li>
    <li>Streamlitでミニダッシュボードをデプロイ</li>
    <li>AIを使ってコードレビュー・学習を加速</li>
    <li>Qiita/Zennの記事を1つ読んで理解度を確認</li>
  </ul>
</div>
<div class="callout">
  <p><strong>鉄則</strong></p>
  <p>インプットだけでなく、手を動かして定着させる</p>
  <p class="subtle">「分かる」と「できる」は違う</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>次に学ぶべきもの</h2>
  <ul>
    <li><strong>深掘り</strong>: 興味を持ったセクションの公式ドキュメント</li>
    <li><strong>実践</strong>: 小さなアプリを1つ作って公開する</li>
    <li><strong>チーム開発</strong>: チームプロジェクトに参加</li>
    <li><strong>継続学習</strong>: 技術ブログ・ポッドキャスト・勉強会</li>
  </ul>
</div>
<div class="callout">
  <p><strong>おすすめリソース</strong></p>
  <ul>
    <li>公式ドキュメント（最も正確）</li>
    <li>Zenn / Qiita（日本語の実践例）</li>
    <li>YouTube（ビジュアルで学ぶ）</li>
  </ul>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>最終チェック：自分の言葉で説明できる？</h2>
  <ul>
    <li>Vモデルの対応関係を図示できる</li>
    <li>Git/GitHubの基本フローを説明できる</li>
    <li>3層構成とREST APIを説明できる</li>
    <li>認証と認可の違いを一言で言える</li>
    <li>CI/CDのメリットを説明できる</li>
    <li>LLMの限界を3つ挙げられる</li>
  </ul>
</div>
<div class="callout">
  <p><strong>目安</strong></p>
  <p>7割以上できれば合格</p>
  <p class="subtle">分からない部分は復習ポイント</p>
</div>

---

<!-- .slide: class="layout-2col" -->
<div>
  <h2>質問タイム</h2>
  <ul>
    <li>今日の内容で分からなかったこと</li>
    <li>実務でどう使うか具体例が欲しい部分</li>
    <li>次に何を学べばいいか迷っていること</li>
  </ul>
</div>
<div class="callout">
  <p><strong>最後に</strong></p>
  <p>技術は「知る→試す→使う→教える」で身につく</p>
  <p class="subtle">今日がスタート地点。継続が力になる。</p>
  <p><strong>お疲れ様でした！</strong></p>
</div>
